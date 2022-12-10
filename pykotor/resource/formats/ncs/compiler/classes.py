from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional, Tuple, Dict, NamedTuple, Union
from pykotor.common.script import DataType, ScriptFunction
from pykotor.common.stream import BinaryReader
from pykotor.resource.formats.ncs import NCS, NCSInstruction, NCSInstructionType


class CompileException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Identifier:
    def __init__(self, label: str):
        self.label: str = label

    def __eq__(self, other):
        if isinstance(other, Identifier):
            return self.label == other.label
        elif isinstance(other, str):
            return self.label == other
        else:
            return NotImplemented

    def __str__(self):
        return self.label

    def __hash__(self):
        return hash(self.label)


class ControlKeyword(Enum):
    BREAK = "break"
    CASE = "control"
    DEFAULT = "default"
    DO = "do"
    ELSE = "else"
    SWITCH = "switch"
    WHILE = "while"
    FOR = "for"
    IF = "if"
    RETURN = "return"


class Operator(Enum):
    ADDITION = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    MODULUS = "%"
    NOT = "!"
    EQUAL = "=="
    NOT_EQUAL = "!="
    GREATER_THAN = ">"
    LESS_THAN = "<"
    GREATER_THAN_OR_EQUAL = ">="
    LESS_THAN_OR_EQUAL = "<="
    AND = "&&"
    OR = "||"
    BITWISE_AND = "&"
    BITWISE_OR = "|"
    BITWISE_XOR = "^"
    BITWISE_LEFT = "<<"
    BITWISE_RIGHT = ">>"
    ONES_COMPLEMENT = "~"


class FunctionReference(NamedTuple):
    instruction: NCSInstruction
    definition: Union[FunctionForwardDeclaration, FunctionDefinition]


class CodeRoot:
    def __init__(self):
        # TODO: merge these three into one list extending common class
        self.includes: List[IncludeScript] = []
        self.function_decs: List[FunctionForwardDeclaration] = []
        self.function_defs: List[FunctionDefinition] = []

        self.function_map: Dict[str, FunctionReference] = {}

    def compile(self, ncs: NCS):
        for include in self.includes:
            include.compile(ncs, self)

        for foward_dec in self.function_decs:
            self.function_map[foward_dec.identifier.label] = FunctionReference(ncs.add(NCSInstructionType.NOP, args=[]), foward_dec)

        for function in self.function_defs:
            name = function.identifier.label

            # TODO: throw error when signature does not match forward declaration
            if name in self.function_map:
                if isinstance(self.function_map[name].definition, FunctionDefinition):
                    raise CompileException(f"Function '{name}' has already been defined.")

                # Function has forward declaration, insert the compiled definition after the stub
                temp = NCS()
                function.compile(temp, self)
                stub_index = ncs.instructions.index(self.function_map[name].instruction)
                ncs.instructions[stub_index+1:stub_index+1] = temp.instructions
            else:
                start_index = len(ncs.instructions)
                function.compile(ncs, self)
                self.function_map[function.identifier.label] = FunctionReference(ncs.instructions[start_index], function)

        if "main" in self.function_map:
            ncs.add(NCSInstructionType.RETN, args=[], prepend=True)
            ncs.add(NCSInstructionType.JSR, jump=self.function_map["main"][0], prepend=True)

    def compile_jsr(self, ncs: NCS, block: CodeBlock, name: str, *args: Expression) -> DataType:
        if name not in self.function_map:
            raise CompileException(f"Function '{name}' has not been defined.")

        start_instruction, definition = self.function_map[name]

        if definition.return_type == DataType.INT:
            ncs.add(NCSInstructionType.RSADDI, args=[])
        elif definition.return_type == DataType.FLOAT:
            ncs.add(NCSInstructionType.RSADDF, args=[])
        elif definition.return_type == DataType.STRING:
            ncs.add(NCSInstructionType.RSADDS, args=[])
        elif definition.return_type == DataType.VECTOR:
            raise NotImplementedError("Cannot define a function that returns Vector yet")  # TODO
        elif definition.return_type == DataType.OBJECT:
            ncs.add(NCSInstructionType.RSADDO, args=[])
        elif definition.return_type == DataType.VOID:
            ...
        else:
            raise NotImplementedError("Trying to return unsuppoted type?")  # TODO

        for arg in args:
            arg.compile(ncs, self, block)
        ncs.add(NCSInstructionType.JSR, jump=start_instruction)

        return definition.return_type


class CodeBlock:
    def __init__(self):
        self.scope: List[ScopedValue] = []
        self._parent: Optional[CodeBlock] = None
        self._statements: List[Statement] = []
        self.tempstack: int = 0

    def add(self, statement: Statement):
        self._statements.append(statement)

    def compile(self, ncs: NCS, root: CodeRoot, block: Optional[CodeBlock], return_instruction: NCSInstruction):
        self._parent = block

        for statement in self._statements:

            if isinstance(statement, ReturnStatement):
                scope_size = self.full_scope_size()

                return_type = statement.compile(ncs, root, self, return_instruction)
                if return_type != DataType.VOID:
                    ncs.add(NCSInstructionType.CPDOWNSP, args=[-scope_size-return_type.size()*2, 4])
                    ncs.add(NCSInstructionType.MOVSP, args=[-return_type.size()])

                ncs.add(NCSInstructionType.MOVSP, args=[-scope_size])
                ncs.add(NCSInstructionType.JMP, jump=return_instruction)
                return
            else:
                statement.compile(ncs, root, self, return_instruction)
        ncs.instructions.append(NCSInstruction(NCSInstructionType.MOVSP, [-self.scope_size()]))

        if self.tempstack != 0:
            # If the temp stack is 0 after the whole block has compiled there must be an logic error in the code
            # of one of the expression/statement classes
            raise ValueError

    def add_scoped(self, identifier: Identifier, data_type: DataType):
        self.scope.insert(0, ScopedValue(identifier, data_type))

    def get_scoped(self, identifier: Identifier):
        index = -self.tempstack
        for scoped in self.scope:
            index -= scoped.data_type.size()
            if scoped.identifier == identifier:
                break
        else:
            if self._parent is not None:
                return self._parent.get_scoped(identifier)
            else:
                raise CompileException(f"Could not find symbol {identifier}.")
        return scoped.data_type, index

    def scope_size(self):
        """Returns size of local scope."""
        return abs(self.get_scoped(self.scope[-1].identifier)[-1]) if self.scope else 0

    def full_scope_size(self):
        """Returns size of scope, including outer blocks."""
        size = 0
        size += self.scope_size()
        if self._parent is not None:
            size += self._parent.full_scope_size()
        return size


class ScopedValue:
    def __init__(self, identifier: Identifier, data_type: DataType):
        self.identifier: Identifier = identifier
        self.data_type: DataType = data_type


class FunctionForwardDeclaration:
    def __init__(self, return_type: DataType, identifier: Identifier, parameters: List[FunctionDefinitionParam]):
        self.return_type: DataType = return_type
        self.identifier: Identifier = identifier
        self.paramaters: List[FunctionDefinitionParam] = parameters

    def compile(self, ncs: NCS, root: CodeRoot):
        ...


class FunctionDefinition:
    # TODO: split definition into signature + block?
    def __init__(self, return_type: DataType, identifier: Identifier, parameters: List[FunctionDefinitionParam], block: CodeBlock):
        self.return_type: DataType = return_type
        self.identifier: Identifier = identifier
        self.parameters: List[FunctionDefinitionParam] = parameters
        self.block: CodeBlock = block

        for param in parameters:
            block.add_scoped(param.identifier, param.data_type)

    def compile(self, ncs: NCS, root: CodeRoot):
        retn = NCSInstruction(NCSInstructionType.RETN)
        self.block.compile(ncs, root, None, retn)
        ncs.instructions.append(retn)


class FunctionDefinitionParam:
    def __init__(self, data_type: DataType, identifier: Identifier):
        self.data_type: DataType = data_type
        self.identifier: Identifier = identifier


class IncludeScript:
    def __init__(self, file: StringExpression, library: Dict[str, str] = None):
        self.file: StringExpression = file
        self.builtin_library: Dict[str, str] = library

    def compile(self, ncs: NCS, root: CodeRoot) -> None:
        builtin_library = self.builtin_library if self.builtin_library else {}

        if self.file.value in builtin_library:
            source = self.builtin_library[self.file.value]
            # TODO try get file from drive
        else:
            raise CompileException(f"Could not find file '{self.file.value}.nss'.")

        from pykotor.resource.formats.ncs.compiler.parser import NssParser
        nssParser = NssParser()
        t = nssParser.parser.parse(source, tracking=True)

        imported = NCS()
        t.compile(imported)
        ncs.merge(imported)
        # TODO: throw error of function redefined
        root.function_map.update(t.function_map)


class Expression(ABC):
    @abstractmethod
    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        ...


class Statement(ABC):
    def __init__(self):
        self.linenum: Optional[None] = None

    @abstractmethod
    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock, return_instruction: NCSInstruction):
        ...


# region Expressions: Simple
class IdentifierExpression(Expression):
    def __init__(self, value: Identifier):
        super().__init__()
        self.identifier: Identifier = value

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        datatype, stack_index = block.get_scoped(self.identifier)
        ncs.instructions.append(NCSInstruction(NCSInstructionType.CPTOPSP, [stack_index, datatype.size()]))
        return datatype


class StringExpression(Expression):
    def __init__(self, value: str):
        super().__init__()
        self.value: str = value

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        ncs.instructions.append(NCSInstruction(NCSInstructionType.CONSTS, [self.value]))
        return DataType.STRING


class IntExpression(Expression):
    def __init__(self, value: int):
        super().__init__()
        self.value: int = value

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        ncs.instructions.append(NCSInstruction(NCSInstructionType.CONSTI, [self.value]))
        return DataType.INT


class FloatExpression(Expression):
    def __init__(self, value: float):
        super().__init__()
        self.value: float = value

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        ncs.instructions.append(NCSInstruction(NCSInstructionType.CONSTF, [self.value]))
        return DataType.FLOAT


class EngineCallExpression(Expression):
    def __init__(self, function: ScriptFunction, routine_id: int, data_type: DataType, args: List[Expression]):
        super().__init__()
        self._function: ScriptFunction = function
        self._routine_id: int = routine_id
        self._args: List[Expression] = args

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        arg_count = len(self._args)

        if arg_count > len(self._function.params):
            raise CompileException(f"Too many arguments passed to '{self._function.name}'.")

        for i, param in enumerate(self._function.params):
            if i >= arg_count:
                if param.default is None:
                    raise CompileException(f"Not enough arguments passed to '{self._function.name}'.")
                else:
                    if param.datatype == DataType.INT:
                        self._args.append(IntExpression(int(param.default)))
                    elif param.datatype == DataType.FLOAT:
                        self._args.append(FloatExpression(float(param.default)))
                    elif param.datatype == DataType.STRING:
                        self._args.append(StringExpression(param.default))
                    else:
                        raise CompileException(f"Unexpected compilation error at '{self._function.name}' call.")

        this_stack = 0
        for i, arg in enumerate(reversed(self._args)):
            added = arg.compile(ncs, root, block)
            block.tempstack += added.size()
            this_stack += added.size()

            if added != self._function.params[-i - 1].datatype:
                raise CompileException(f"Tried to pass an argument of the incorrect type to '{self._function.name}'.")

        ncs.instructions.append(NCSInstruction(NCSInstructionType.ACTION, [self._routine_id, len(self._args)]))
        block.tempstack -= this_stack
        return self._function.returntype


class FunctionCallExpression(Expression):
    def __init__(self, function: Identifier, args: List[Expression]):
        super().__init__()
        self._function: Identifier = function
        self._args: List[Expression] = args

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        return root.compile_jsr(ncs, block, self._function.label, *self._args)
# endregion


# region Expressions: Arithmetic
class AdditionExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type1 == DataType.INT:
            ncs.add(NCSInstructionType.ADDII)
        elif type1 == DataType.INT and type1 == DataType.FLOAT:
            ncs.add(NCSInstructionType.ADDIF)
        elif type1 == DataType.FLOAT and type1 == DataType.FLOAT:
            ncs.add(NCSInstructionType.ADDFF)
        elif type1 == DataType.FLOAT and type1 == DataType.INT:
            ncs.add(NCSInstructionType.ADDFI)
        elif type1 == DataType.STRING and type1 == DataType.STRING:
            ncs.add(NCSInstructionType.ADDSS)
        elif type1 == DataType.VECTOR and type1 == DataType.VECTOR:
            ncs.add(NCSInstructionType.ADDVV)
        else:
            raise CompileException(f"Cannot add {type1.name.lower()} to {type2.name.lower()}")

        block.tempstack -= 8
        return type1


class SubtractionExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type1 == DataType.INT:
            ncs.add(NCSInstructionType.SUBII)
        elif type1 == DataType.INT and type1 == DataType.FLOAT:
            ncs.add(NCSInstructionType.SUBIF)
        elif type1 == DataType.FLOAT and type1 == DataType.FLOAT:
            ncs.add(NCSInstructionType.SUBFF)
        elif type1 == DataType.FLOAT and type1 == DataType.INT:
            ncs.add(NCSInstructionType.SUBFI)
        elif type1 == DataType.VECTOR and type1 == DataType.VECTOR:
            ncs.add(NCSInstructionType.SUBVV)
        else:
            raise CompileException(f"Cannot subtract {type2.name.lower()} from {type1.name.lower()}")

        block.tempstack -= 8
        return type1


class MultiplicationExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type1 == DataType.INT:
            ncs.add(NCSInstructionType.MULII)
        elif type1 == DataType.INT and type1 == DataType.FLOAT:
            ncs.add(NCSInstructionType.MULIF)
        elif type1 == DataType.FLOAT and type1 == DataType.FLOAT:
            ncs.add(NCSInstructionType.MULFF)
        elif type1 == DataType.FLOAT and type1 == DataType.INT:
            ncs.add(NCSInstructionType.MULFI)
        elif type1 == DataType.VECTOR and type1 == DataType.FLOAT:
            ncs.add(NCSInstructionType.MULVF)
        elif type1 == DataType.FLOAT and type1 == DataType.VECTOR:
            ncs.add(NCSInstructionType.MULFV)
        else:
            raise CompileException(f"Cannot multiply {type1.name.lower()} to {type2.name.lower()}")

        block.tempstack -= 8
        return type1


class DivisionExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type1 == DataType.INT:
            ncs.add(NCSInstructionType.DIVII)
        elif type1 == DataType.INT and type1 == DataType.FLOAT:
            ncs.add(NCSInstructionType.DIVIF)
        elif type1 == DataType.FLOAT and type1 == DataType.FLOAT:
            ncs.add(NCSInstructionType.DIVFF)
        elif type1 == DataType.FLOAT and type1 == DataType.INT:
            ncs.add(NCSInstructionType.DIVFI)
        elif type1 == DataType.VECTOR and type1 == DataType.FLOAT:
            ncs.add(NCSInstructionType.DIVVF)
        else:
            raise CompileException(f"Cannot divide {type1.name.lower()} by {type2.name.lower()}")

        block.tempstack -= 8
        return type1


class ModulusExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type1 == DataType.INT:
            ncs.add(NCSInstructionType.MODII)
        else:
            raise CompileException(f"Cannot get the modulus of {type1.name.lower()} and {type2.name.lower()}")

        block.tempstack -= 8
        return type1


class NegationExpression(Expression):
    def __init__(self, expression1: Expression):
        super().__init__()
        self.expression1: Expression = expression1

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT:
            ncs.add(NCSInstructionType.NEGI)
        elif type1 == DataType.FLOAT:
            ncs.add(NCSInstructionType.NEGF)
        else:
            raise CompileException(f"Cannot negate {type1.name.lower()}")

        block.tempstack -= 4
        return type1
# endregion


# region Expressions: Logical
class LogicalNotExpression(Expression):
    def __init__(self, expression1: Expression):
        super().__init__()
        self.expression1: Expression = expression1

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT:
            ncs.add(NCSInstructionType.NOTI)
        else:
            raise CompileException(f"Cannot get the logical NOT of {type1.name.lower()}")

        block.tempstack -= 4
        return DataType.INT


class LogicalAndExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.LOGANDII)
        else:
            raise CompileException(f"Cannot get the logical AND of {type1.name.lower()} and {type2.name.lower()}")

        block.tempstack -= 8
        return DataType.INT


class LogicalOrExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.LOGORII)
        else:
            raise CompileException(f"Cannot get the logical OR of {type1.name.lower()} and {type2.name.lower()}")

        block.tempstack -= 8
        return DataType.INT
# endregion


# region Expressions: Relational
class LogicalEqualityExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.EQUALII)
        elif type1 == DataType.FLOAT and type2 == DataType.FLOAT:
            ncs.add(NCSInstructionType.EQUALFF)
        elif type1 == DataType.STRING and type2 == DataType.STRING:
            ncs.add(NCSInstructionType.EQUALSS)
        elif type1 == DataType.OBJECT and type2 == DataType.OBJECT:
            ncs.add(NCSInstructionType.EQUALOO)
        else:
            raise CompileException(f"Cannot test the equality of {type1.name.lower()} and {type2.name.lower()}")

        block.tempstack -= 8
        return DataType.INT


class LogicalInequalityExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2
        self._type = None

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.NEQUALII)
        elif type1 == DataType.FLOAT and type2 == DataType.FLOAT:
            ncs.add(NCSInstructionType.NEQUALFF)
        elif type1 == DataType.STRING and type2 == DataType.STRING:
            ncs.add(NCSInstructionType.NEQUALSS)
        elif type1 == DataType.OBJECT and type2 == DataType.OBJECT:
            ncs.add(NCSInstructionType.NEQUALOO)
        else:
            raise CompileException(f"Cannot test the equality of {type1.name.lower()} and {type2.name.lower()}")

        block.tempstack -= 8
        return DataType.INT


class GreaterThanExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.GTII)
        elif type1 == DataType.FLOAT and type2 == DataType.FLOAT:
            ncs.add(NCSInstructionType.GTFF)
        else:
            raise CompileException(f"Cannot test if {type1.name.lower()} is greater than {type2.name.lower()}")

        block.tempstack -= 8
        return DataType.INT


class GreaterThanOrEqualExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2
        self._type = None

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.GEQII)
        elif type1 == DataType.FLOAT and type2 == DataType.FLOAT:
            ncs.add(NCSInstructionType.GEQFF)
        else:
            raise CompileException(f"Cannot test if {type1.name.lower()} is greater than or equal to {type2.name.lower()}")

        block.tempstack -= 8
        return DataType.INT


class LessThanExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2
        self._type = None

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.LTII)
        elif type1 == DataType.FLOAT and type2 == DataType.FLOAT:
            ncs.add(NCSInstructionType.LTFF)
        else:
            raise CompileException(f"Cannot test if {type1.name.lower()} is less than {type2.name.lower()}")

        block.tempstack -= 8
        return DataType.INT


class LessThanOrEqualExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2
        self._type = None

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.LEQII)
        elif type1 == DataType.FLOAT and type2 == DataType.FLOAT:
            ncs.add(NCSInstructionType.LEQFF)
        else:
            raise CompileException(f"Cannot test if {type1.name.lower()} is less than {type2.name.lower()}")

        block.tempstack -= 8
        return DataType.INT
# endregion


# region Expression: Bitwise
class BitwiseOrExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.INCORII)
        else:
            raise CompileException(f"Cannot get the bitwise OR of {type1.name.lower()} and {type2.name.lower()}")

        block.tempstack -= 8
        return type1


class BitwiseXorExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.EXCORII)
        else:
            raise CompileException(f"Cannot get the bitwise XOR of {type1.name.lower()} and {type2.name.lower()}")

        block.tempstack -= 8
        return type1


class BitwiseAndExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.BOOLANDII)
        else:
            raise CompileException(f"Cannot get the bitwise AND of {type1.name.lower()} and {type2.name.lower()}")

        block.tempstack -= 8
        return type1


class BitwiseNotExpression(Expression):
    def __init__(self, expression1: Expression):
        super().__init__()
        self.expression1: Expression = expression1

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT:
            ncs.add(NCSInstructionType.COMPI)
        else:
            raise CompileException(f"Cannot get one's complement of {type1.name.lower()}")

        block.tempstack -= 4
        return type1


class BitwiseLeftShiftExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.SHLEFTII)
        else:
            raise CompileException(f"Cannot bitshift {type1.name.lower()} with {type2.name.lower()}")

        block.tempstack -= 8
        return type1


class BitwiseRightShiftExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        super().__init__()
        self.expression1: Expression = expression1
        self.expression2: Expression = expression2

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        type1 = self.expression1.compile(ncs, root, block)
        block.tempstack += 4
        type2 = self.expression2.compile(ncs, root, block)
        block.tempstack += 4

        if type1 == DataType.INT and type2 == DataType.INT:
            ncs.add(NCSInstructionType.SHRIGHTII)
        else:
            raise CompileException(f"Cannot bitshift {type1.name.lower()} with {type2.name.lower()}")

        block.tempstack -= 8
        return type1
# endregion


# region Expressions: Assignment
class Assignment(Expression):
    def __init__(self, identifier: Identifier, value: Expression):
        super().__init__()
        self.identifier: Identifier = identifier
        self.expression: Expression = value

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        variable_type = self.expression.compile(ncs, root, block)

        expression_type, stack_index = block.get_scoped(self.identifier)
        stack_index -= expression_type.size()

        if variable_type != expression_type:
            raise CompileException(f"Wrong type was assigned to symbol {self.identifier}.")

        # Copy the value that the expression has already been placed on the stack to where the identifiers position is
        ncs.instructions.append(NCSInstruction(NCSInstructionType.CPDOWNSP, [stack_index, expression_type.size()]))
        # Remove the temporary value from the stack that the expression created
        ncs.instructions.append(NCSInstruction(NCSInstructionType.MOVSP, [-expression_type.size()]))

        return variable_type


class AdditionAssignment(Expression):
    def __init__(self, identifier: Identifier, value: Expression):
        super().__init__()
        self.identifier: Identifier = identifier
        self.expression: Expression = value

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        # Copy the variable to the top of the stack
        variable_type, stack_index = block.get_scoped(self.identifier)
        ncs.add(NCSInstructionType.CPTOPSP, args=[stack_index, variable_type.size()])

        # Add the result of the expression to the stack
        expresion_type = self.expression.compile(ncs, root, block)
        block.tempstack += expresion_type.size()

        # Determine what instruction to apply to the two values
        if variable_type == DataType.INT and expresion_type == DataType.INT:
            arthimetic_instruction = NCSInstructionType.ADDII
        elif variable_type == DataType.INT and expresion_type == DataType.FLOAT:
            arthimetic_instruction = NCSInstructionType.ADDIF
        elif variable_type == DataType.FLOAT and expresion_type == DataType.FLOAT:
            arthimetic_instruction = NCSInstructionType.ADDFF
        elif variable_type == DataType.FLOAT and expresion_type == DataType.INT:
            arthimetic_instruction = NCSInstructionType.ADDFI
        elif variable_type == DataType.STRING and expresion_type == DataType.STRING:
            arthimetic_instruction = NCSInstructionType.ADDSS
        else:
            raise CompileException(f"Wrong type was assigned to symbol {self.identifier}.")

        # Add the expression and our temp variable copy together
        ncs.add(arthimetic_instruction)
        # Copy the result to the original variable in the stack
        ncs.add(NCSInstructionType.CPDOWNSP, args=[stack_index - expresion_type.size(), variable_type.size()])
        # Pop the temp variable
        ncs.add(NCSInstructionType.MOVSP, args=[-variable_type.size()])

        block.tempstack -= expresion_type.size()
        return expresion_type


class SubtractionAssignment(Expression):
    def __init__(self, identifier: Identifier, value: Expression):
        super().__init__()
        self.identifier: Identifier = identifier
        self.expression: Expression = value

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        # Copy the variable to the top of the stack
        variable_type, stack_index = block.get_scoped(self.identifier)
        ncs.add(NCSInstructionType.CPTOPSP, args=[stack_index, variable_type.size()])

        # Add the result of the expression to the stack
        expresion_type = self.expression.compile(ncs, root, block)
        block.tempstack += expresion_type.size()

        # Determine what instruction to apply to the two values
        if variable_type == DataType.INT and expresion_type == DataType.INT:
            arthimetic_instruction = NCSInstructionType.SUBII
        elif variable_type == DataType.INT and expresion_type == DataType.FLOAT:
            arthimetic_instruction = NCSInstructionType.SUBIF
        elif variable_type == DataType.FLOAT and expresion_type == DataType.FLOAT:
            arthimetic_instruction = NCSInstructionType.SUBFF
        elif variable_type == DataType.FLOAT and expresion_type == DataType.INT:
            arthimetic_instruction = NCSInstructionType.SUBFI
        else:
            raise CompileException(f"Wrong type was assigned to symbol {self.identifier}.")

        # Add the expression and our temp variable copy together
        ncs.add(arthimetic_instruction)
        # Copy the result to the original variable in the stack
        ncs.add(NCSInstructionType.CPDOWNSP, args=[stack_index - expresion_type.size(), variable_type.size()])
        # Pop the temp variable
        ncs.add(NCSInstructionType.MOVSP, args=[-variable_type.size()])

        block.tempstack -= expresion_type.size()
        return expresion_type


class MultiplicationAssignment(Expression):
    def __init__(self, identifier: Identifier, value: Expression):
        super().__init__()
        self.identifier: Identifier = identifier
        self.expression: Expression = value

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        # Copy the variable to the top of the stack
        variable_type, stack_index = block.get_scoped(self.identifier)
        ncs.add(NCSInstructionType.CPTOPSP, args=[stack_index, variable_type.size()])

        # Add the result of the expression to the stack
        expresion_type = self.expression.compile(ncs, root, block)
        block.tempstack += expresion_type.size()

        # Determine what instruction to apply to the two values
        if variable_type == DataType.INT and expresion_type == DataType.INT:
            arthimetic_instruction = NCSInstructionType.MULII
        elif variable_type == DataType.INT and expresion_type == DataType.FLOAT:
            arthimetic_instruction = NCSInstructionType.MULIF
        elif variable_type == DataType.FLOAT and expresion_type == DataType.FLOAT:
            arthimetic_instruction = NCSInstructionType.MULFF
        elif variable_type == DataType.FLOAT and expresion_type == DataType.INT:
            arthimetic_instruction = NCSInstructionType.MULFI
        else:
            raise CompileException(f"Wrong type was assigned to symbol {self.identifier}.")

        # Add the expression and our temp variable copy together
        ncs.add(arthimetic_instruction)
        # Copy the result to the original variable in the stack
        ncs.add(NCSInstructionType.CPDOWNSP, args=[stack_index - expresion_type.size(), variable_type.size()])
        # Pop the temp variable
        ncs.add(NCSInstructionType.MOVSP, args=[-variable_type.size()])

        block.tempstack -= expresion_type.size()
        return expresion_type


class DivisionAssignment(Expression):
    def __init__(self, identifier: Identifier, value: Expression):
        super().__init__()
        self.identifier: Identifier = identifier
        self.expression: Expression = value

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock) -> DataType:
        # Copy the variable to the top of the stack
        variable_type, stack_index = block.get_scoped(self.identifier)
        ncs.add(NCSInstructionType.CPTOPSP, args=[stack_index, variable_type.size()])

        # Add the result of the expression to the stack
        expresion_type = self.expression.compile(ncs, root, block)
        block.tempstack += expresion_type.size()

        # Determine what instruction to apply to the two values
        if variable_type == DataType.INT and expresion_type == DataType.INT:
            arthimetic_instruction = NCSInstructionType.DIVII
        elif variable_type == DataType.INT and expresion_type == DataType.FLOAT:
            arthimetic_instruction = NCSInstructionType.DIVIF
        elif variable_type == DataType.FLOAT and expresion_type == DataType.FLOAT:
            arthimetic_instruction = NCSInstructionType.DIVFF
        elif variable_type == DataType.FLOAT and expresion_type == DataType.INT:
            arthimetic_instruction = NCSInstructionType.DIVFI
        else:
            raise CompileException(f"Wrong type was assigned to symbol {self.identifier}.")

        # Add the expression and our temp variable copy together
        ncs.add(arthimetic_instruction)
        # Copy the result to the original variable in the stack
        ncs.add(NCSInstructionType.CPDOWNSP, args=[stack_index - expresion_type.size(), variable_type.size()])
        # Pop the temp variable
        ncs.add(NCSInstructionType.MOVSP, args=[-variable_type.size()])

        block.tempstack -= expresion_type.size()
        return expresion_type
# endregion


# region Statements
class EmptyStatement(Statement):
    def __init__(self):
        super().__init__()

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock, return_instruction: NCSInstruction):
        return DataType.VOID


class ExpressionStatement(Statement):
    def __init__(self, expression: Expression):
        super().__init__()
        self.expression: Expression = expression

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock, return_instruction: NCSInstruction):
        self.expression.compile(ncs, root, block)


class DeclarationStatement(Statement):
    def __init__(self, identifier: Identifier, data_type: DataType, value: Expression):
        super().__init__()
        self.identifier: Identifier = identifier
        self.data_type: DataType = data_type
        self.expression: Expression = value

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock, return_instruction: NCSInstruction):
        expression_type = self.expression.compile(ncs, root, block)
        if expression_type != self.data_type:
            raise CompileException(f"Tried to declare '{self.identifier}' a new variable with incorrect type '{expression_type}'.")
        block.add_scoped(self.identifier, self.data_type)


class ConditionalBlock(Statement):
    def __init__(self, condition: Expression, block: CodeBlock):
        super().__init__()
        self.condition: Expression = condition
        self.block: CodeBlock = block

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock, return_instruction: NCSInstruction):
        self.condition.compile(ncs, root, block)
        jz = ncs.add(NCSInstructionType.JZ, jump=None)
        self.block.compile(ncs, root, block, return_instruction)
        block_end = ncs.add(NCSInstructionType.NOP, args=[])

        # Set the Jump If Zero instruction to jump to the end of the block
        jz.jump = block_end


class ReturnStatement(Statement):
    def __init__(self, expression: Optional[Expression] = None):
        super().__init__()
        self.expression: Optional[Expression] = expression

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock, return_instruction: NCSInstruction):
        if self.expression is not None:
            return self.expression.compile(ncs, root, block)
        return DataType.VOID


class WhileLoopBlock(Statement):
    def __init__(self, condition: Expression, block: CodeBlock):
        super().__init__()
        self.condition: Expression = condition
        self.block: CodeBlock = block

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock, return_instruction: NCSInstruction):
        loopstart = ncs.add(NCSInstructionType.NOP, args=[])
        condition_type = self.condition.compile(ncs, root, block)

        if condition_type != DataType.INT:
            raise CompileException("Condition must be int type.")

        jz = ncs.add(NCSInstructionType.JZ, jump=None)
        self.block.compile(ncs, root, block, return_instruction)

        ncs.add(NCSInstructionType.JMP, jump=loopstart)

        loopend = ncs.add(NCSInstructionType.NOP, args=[])
        jz.jump = loopend


class DoWhileLoopBlock(Statement):
    def __init__(self, condition: Expression, block: CodeBlock):
        super().__init__()
        self.condition: Expression = condition
        self.block: CodeBlock = block

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock, return_instruction: NCSInstruction):
        loopstart = ncs.add(NCSInstructionType.NOP, args=[])

        self.block.compile(ncs, root, block, return_instruction)

        condition_type = self.condition.compile(ncs, root, block)
        if condition_type != DataType.INT:
            raise CompileException("Condition must be int type.")

        jz = ncs.add(NCSInstructionType.JZ, jump=None)
        ncs.add(NCSInstructionType.JMP, jump=loopstart)

        loopend = ncs.add(NCSInstructionType.NOP, args=[])


class ForLoopBlock(Statement):
    def __init__(self, initial: Expression, condition: Expression, iteration: Expression, block: CodeBlock):
        super().__init__()
        self.initial: Expression = initial
        self.condition: Expression = condition
        self.iteration: Expression = iteration
        self.block: CodeBlock = block

    def compile(self, ncs: NCS, root: CodeRoot, block: CodeBlock, return_instruction: NCSInstruction):
        self.initial.compile(ncs, root, block)
        loopstart = ncs.add(NCSInstructionType.NOP, args=[])

        condition_type = self.condition.compile(ncs, root, block)
        if condition_type != DataType.INT:
            raise CompileException("Condition must be int type.")

        jz = ncs.add(NCSInstructionType.JZ, jump=None)
        self.block.compile(ncs, root, block, return_instruction)

        self.iteration.compile(ncs, root, block)
        ncs.add(NCSInstructionType.JMP, jump=loopstart)

        loopend = ncs.add(NCSInstructionType.NOP, args=[])
        jz.jump = loopend
# endregion
