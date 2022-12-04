import operator

from pykotor.common.script import DataType
from pykotor.resource.formats.ncs.compiler.classes import IntExpression, ControlKeyword, StringExpression, \
    FloatExpression, Identifier, Operator

from abc import ABC
from enum import Enum
from typing import Any

import ply.lex as lex


class NssLexer:
    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.lexer.begin("INITIAL")

    tokens = [
        "STRING_VALUE", "INT_VALUE", "FLOAT_VALUE", "IDENTIFIER", "INT_TYPE", "FLOAT_TYPE", "OBJECT_TYPE",
        "VOID_TYPE",  "EVENT_TYPE", "EFFECT_TYPE", "ITEMPROPERTY_TYPE", "LOCATION_TYPE", "STRING_TYPE", "TALENT_TYPE",
        "VECTOR_TYPE", "ACTION_TYPE", "BREAK_CONTROL", "CASE_CONTROL", "DEFAULT_CONTROL", "DO_CONTROL", "ELSE_CONTROL",
        "SWITCH_CONTROL", "WHILE_CONTROL", "FOR_CONTROL", "IF_CONTROL", "TRUE_VALUE", "FALSE_VALUE", "OBJECTSELF_VALUE",
        "OBJECTINVALID_VALUE", "ADDITION_OPERATOR", "SUBTRACTION_OPERATOR", "MULTIPLY_OPERATOR", "DIVIDE_OPERATOR",
        "MODULUS_OPERATOR", "EQUAL_OPERATOR", "NOT_EQUAL_OPERATOR", "GREATER_THAN_OPERATOR", "LESS_THAN_OPERATOR",
        "LESS_THAN_OR_EQUAL_OPERATOR", "GREATER_THAN_OR_EQUAL_OPERATOR", "AND_OPERATOR", "OR_OPERATOR",
        "NOT_OPERATOR", "BITWISE_AND_OPERATOR", "BITWISE_OR_OPERATOR", "BITWISE_LEFT_OPERATOR",
        "BITWISE_RIGHT_OPERATOR", "BITWISE_XOR_OPERATOR", "ONES_COMPLEMENT_OPERATOR", "COMMENT"
    ]

    literals = [
        '{', '}', '(', ')', ';', '=', ','
    ]

    t_ignore = " \t\n\r"

    def t_COMMENT(self, t):
        r'//[^\n]*\n'
        pass

    # region Control Tokens
    def t_BREAK_CONTROL(self, t):
        r'break'
        t.value = ControlKeyword.BREAK
        return t

    def t_CASE_CONTROL(self, t):
        r'case'
        t.value = ControlKeyword.CASE
        return t

    def t_DEFAULT_CONTROL(self, t):
        r'default'
        t.value = ControlKeyword.DEFAULT
        return t

    def t_DO_CONTROL(self, t):
        r'do'
        t.value = ControlKeyword.DO
        return t

    def t_ELSE_CONTROL(self, t):
        r'else'
        t.value = ControlKeyword.ELSE
        return t

    def t_SWITCH_CONTROL(self, t):
        r'switch'
        t.value = ControlKeyword.SWITCH
        return t

    def t_WHILE_CONTROL(self, t):
        r'while'
        t.value = ControlKeyword.WHILE
        return t

    def t_FOR_CONTROL(self, t):
        r'for'
        t.value = ControlKeyword.FOR
        return t

    def t_IF_CONTROL(self, t):
        r'if'
        t.value = ControlKeyword.IF
        return t
    # endregion

    # region Type Tokens
    def t_INT_TYPE(self, t):
        r'int'
        t.value = DataType.INT
        return t

    def t_FLOAT_TYPE(self, t):
        r'float'
        t.value = DataType.FLOAT
        return t

    def t_OBJECT_TYPE(self, t):
        r'object'
        t.value = DataType.OBJECT
        return t

    def t_VOID_TYPE(self, t):
        r'void'
        t.value = DataType.VOID
        return t

    def t_EVENT_TYPE(self, t):
        r'event'
        t.value = DataType.EVENT
        return t

    def t_EFFECT_TYPE(self, t):
        r'effect'
        t.value = DataType.EFFECT
        return t

    def t_ITEMPROPERTY_TYPE(self, t):
        r'itemproperty'
        t.value = DataType.ITEMPROPERTY
        return t

    def t_LOCATION_TYPE(self, t):
        r'location'
        t.value = DataType.LOCATION
        return t

    def t_STRING_TYPE(self, t):
        r'string'
        t.value = DataType.STRING
        return t

    def t_TALENT_TYPE(self, t):
        r'talent'
        t.value = DataType.TALENT
        return t

    def t_ACTION_TYPE(self, t):
        r'action'
        t.value = DataType.ACTION
        return t

    def t_VECTOR_TYPE(self, t):
        r'vector'
        t.value = DataType.VECTOR
        return t
    # endregion

    # region Value Tokens
    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_]+[a-zA-Z0-9_]*'
        t.value = Identifier(t.value)
        return t

    def t_STRING_VALUE(self, t):
        r'\"[^\"]*\"'
        t.value = StringExpression(t.value[1:-1])
        return t

    def t_FLOAT_VALUE(self, t):
        r'[0-9]+\.[0-9]+'
        t.value = FloatExpression(float(t.value))
        return t

    def t_INT_VALUE(self, t):
        r'[0-9]+'
        t.value = IntExpression(int(t.value))
        return t

    def t_TRUE_VALUE(self, t):
        r'TRUE'
        t.value = IntExpression(1)
        return t

    def t_FALSE_VALUE(self, t):
        r'FALSE'
        t.value = IntExpression(0)
        return t

    def t_OBJECTSELF_VALUE(self, t):
        r'OBJECT_SELF'
        t.value = IntExpression(0)
        return t

    def t_OBJECTINVALID_VALUE(self, t):
        r'OBJECT_INVALID'
        t.value = IntExpression(-1)
        return t
    # endregion

    # region Operators
    def t_BITWISE_LEFT_OPERATOR(self, t):
        '<<'
        t.value = Operator.ADDITION
        return t

    def t_BITWISE_RIGHT_OPERATOR(self, t):
        '>>'
        t.value = Operator.ADDITION
        return t

    def t_ADDITION_OPERATOR(self, t):
        '\+'
        t.value = Operator.ADDITION
        return t

    def t_SUBTRACTION_OPERATOR(self, t):
        '-'
        t.value = Operator.SUBTRACT
        return t

    def t_MULTIPLY_OPERATOR(self, t):
        '\*'
        t.value = Operator.MULTIPLY
        return t

    def t_DIVIDE_OPERATOR(self, t):
        '/'
        t.value = Operator.DIVIDE
        return t

    def t_MODULUS_OPERATOR(self, t):
        '\%'
        t.value = Operator.MODULUS
        return t

    def t_EQUAL_OPERATOR(self, t):
        '\=\='
        t.value = Operator.EQUAL
        return t

    def t_NOT_EQUAL_OPERATOR(self, t):
        '\!='
        t.value = Operator.NOT_EQUAL
        return t

    def t_GREATER_THAN_OR_EQUAL_OPERATOR(self, t):
        '>\='
        t.value = Operator.GREATER_THAN_OR_EQUAL
        return t

    def t_GREATER_THAN_OPERATOR(self, t):
        '>'
        t.value = Operator.GREATER_THAN
        return t

    def t_LESS_THAN_OR_EQUAL_OPERATOR(self, t):
        '\<='
        t.value = Operator.ADDITION
        return t

    def t_LESS_THAN_OPERATOR(self, t):
        '\<'
        t.value = Operator.ADDITION
        return t

    def t_GREATER_OR_EQUAL_OPERATOR(self, t):
        '<\='
        t.value = Operator.ADDITION
        return t

    def t_AND_OPERATOR(self, t):
        '&&'
        t.value = Operator.ADDITION
        return t

    def t_OR_OPERATOR(self, t):
        '\|\|'
        t.value = Operator.ADDITION
        return t

    def t_NOT_OPERATOR(self, t):
        '\!'
        t.value = Operator.ADDITION
        return t

    def t_BITWISE_AND_OPERATOR(self, t):
        '&'
        t.value = Operator.ADDITION
        return t

    def t_BITWISE_OR_OPERATOR(self, t):
        '\|'
        t.value = Operator.ADDITION
        return t

    def t_BITWISE_XOR_OPERATOR(self, t):
        '\^'
        t.value = Operator.ADDITION
        return t

    def t_ONES_COMPLEMENT_OPERATOR(self, t):
        '\~'
        t.value = Operator.ONES_COMPLEMENT
        return t
    # endregion
