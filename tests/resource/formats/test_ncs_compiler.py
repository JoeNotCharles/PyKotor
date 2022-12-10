from typing import Dict
from unittest import TestCase

from pykotor.resource.formats.ncs import NCS
from pykotor.resource.formats.ncs.compiler.classes import CompileException
from pykotor.resource.formats.ncs.compiler.interpreter import Interpreter, ActionSnapshot
from pykotor.resource.formats.ncs.compiler.lexer import NssLexer
from pykotor.resource.formats.ncs.compiler.parser import NssParser


class TestNSSCompiler(TestCase):

    def compile(self, script: str, library: Dict[str, str] = None) -> NCS:
        nssLexer = NssLexer()
        nssParser = NssParser()
        nssParser.library = library
        parser = nssParser.parser

        t = parser.parse(script, tracking=True)

        ncs = NCS()
        t.compile(ncs)
        return ncs

    # region Engine Call
    def test_enginecall(self):
        ncs = self.compile("""
            void main()
            {
                object oExisting = GetExitingObject();
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, len(interpreter.action_snapshots))

        self.assertEqual("GetExitingObject", interpreter.action_snapshots[0].function_name)
        self.assertEqual([], interpreter.action_snapshots[0].arg_values)

    def test_enginecall_return_value(self):
        ncs = self.compile("""
            void main()
            {
                int inescapable = GetAreaUnescapable();
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.set_mock("GetAreaUnescapable", lambda: 10)
        interpreter.run()

        self.assertEqual(10, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_enginecall_with_params(self):
        ncs = self.compile("""
            void main()
            {
                string tag = "something";
                int n = 15;
                object oSomething = GetObjectByTag(tag, n);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, len(interpreter.action_snapshots))

        self.assertEqual("GetObjectByTag", interpreter.action_snapshots[0].function_name)
        self.assertEqual(["something", 15], interpreter.action_snapshots[0].arg_values)

    def test_enginecall_with_default_params(self):
        ncs = self.compile("""
            void main()
            {
                string tag = "something";
                object oSomething = GetObjectByTag(tag);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

    def test_enginecall_with_missing_params(self):
        script = """
            void main()
            {
                string tag = "something";
                object oSomething = GetObjectByTag();
            }
        """

        self.assertRaises(CompileException, self.compile, script)

    def test_enginecall_with_too_many_params(self):
        script = """
            void main()
            {
                string tag = "something";
                object oSomething = GetObjectByTag("", 0, "shouldnotbehere");
            }
        """

        self.assertRaises(CompileException, self.compile, script)
    # endregion

    # region Arithmetic Operator
    def test_addop_int_int(self):
        ncs = self.compile("""
            void main()
            {
                int value = 10 + 5;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(15, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_addop_float_float(self):
        ncs = self.compile("""
            void main()
            {
                float value = 10.0 + 5.0;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(15.0, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_addop_string_string(self):
        ncs = self.compile("""
            void main()
            {
                string value = "abc" + "def";
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual("abcdef", interpreter.stack_snapshots[-4].stack[-1].value)

    def test_subop_int_int(self):
        ncs = self.compile("""
            void main()
            {
                int value = 10 - 5;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(5, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_subop_float_float(self):
        ncs = self.compile("""
            void main()
            {
                float value = 10.0 - 5.0;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(5.0, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_mulop_int_int(self):
        ncs = self.compile("""
            void main()
            {
                int a = 10 * 5;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(50, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_mulop_float_float(self):
        ncs = self.compile("""
            void main()
            {
                float a = 10.0 * 5.0;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(50.0, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_divop_int_int(self):
        ncs = self.compile("""
            void main()
            {
                int a = 10 / 5;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(2, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_divop_float_float(self):
        ncs = self.compile("""
            void main()
            {
                float a = 10.0 / 5.0;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(2.0, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_modop_int_int(self):
        ncs = self.compile("""
            void main()
            {
                int a = 10 % 3;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_negop_int(self):
        ncs = self.compile("""
            void main()
            {
                int a = -10;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(-10, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_negop_float(self):
        ncs = self.compile("""
            void main()
            {
                float a = -10.0;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(-10.0, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_op_with_variables(self):
        ncs = self.compile("""
            void main()
            {
                int a = 10;
                int b = 5;
                int c = a * b * a;
                int d = 10 * 5 * 10;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(500, interpreter.stack_snapshots[-4].stack[-1].value)
        self.assertEqual(500, interpreter.stack_snapshots[-4].stack[-2].value)

    # test_addop_vector_vector
    # test_addop_int_float
    # test_addop_float_int
    # test_subop_int_float
    # test_subop_float_int
    # test_subop_vector_vector
    # test_mulop_int_float
    # test_mulop_float_int
    # test_mulop_float_vector
    # test_mulop_vector_float
    # test_divop_int_float
    # test_divop_float_int
    # test_divop_vector_float

    # endregion

    # region Logical Operator
    def test_not_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = !1;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(0, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_logical_and_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 0 && 0;
                int b = 1 && 0;
                int c = 1 && 1;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(0, interpreter.stack_snapshots[-4].stack[-3].value)
        self.assertEqual(0, interpreter.stack_snapshots[-4].stack[-2].value)
        self.assertEqual(1, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_logical_or_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 0 || 0;
                int b = 1 || 0;
                int c = 1 || 1;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(0, interpreter.stack_snapshots[-4].stack[-3].value)
        self.assertEqual(1, interpreter.stack_snapshots[-4].stack[-2].value)
        self.assertEqual(1, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_logical_equals_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 1 == 1;
                int b = 1 == 2;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, interpreter.stack_snapshots[-4].stack[-2].value)
        self.assertEqual(0, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_logical_notequals_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 1 != 1;
                int b = 1 != 2;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(0, interpreter.stack_snapshots[-4].stack[-2].value)
        self.assertEqual(1, interpreter.stack_snapshots[-4].stack[-1].value)
    # endregion

    # region Comparision Operator
    def test_compare_greaterthan_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 10 > 1;
                int b = 10 > 10;
                int c = 10 > 20;
                
                PrintInteger(a);
                PrintInteger(b);
                PrintInteger(c);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, interpreter.action_snapshots[-3].arg_values[0])
        self.assertEqual(0, interpreter.action_snapshots[-2].arg_values[0])
        self.assertEqual(0, interpreter.action_snapshots[-1].arg_values[0])

    def test_compare_greaterthanorequal_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 10 >= 1;
                int b = 10 >= 10;
                int c = 10 >= 20;
                
                PrintInteger(a);
                PrintInteger(b);
                PrintInteger(c);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, interpreter.action_snapshots[-3].arg_values[0])
        self.assertEqual(1, interpreter.action_snapshots[-2].arg_values[0])
        self.assertEqual(0, interpreter.action_snapshots[-1].arg_values[0])

    def test_compare_lessthan_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 10 < 1;
                int b = 10 < 10;
                int c = 10 < 20;
                
                PrintInteger(a);
                PrintInteger(b);
                PrintInteger(c);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(0, interpreter.action_snapshots[-3].arg_values[0])
        self.assertEqual(0, interpreter.action_snapshots[-2].arg_values[0])
        self.assertEqual(1, interpreter.action_snapshots[-1].arg_values[0])

    def test_compare_lessthanorequal_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 10 <= 1;
                int b = 10 <= 10;
                int c = 10 <= 20;
                
                PrintInteger(a);
                PrintInteger(b);
                PrintInteger(c);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(0, interpreter.action_snapshots[-3].arg_values[0])
        self.assertEqual(1, interpreter.action_snapshots[-2].arg_values[0])
        self.assertEqual(1, interpreter.action_snapshots[-1].arg_values[0])

    # endregion

    # region Bitwise Operator
    def test_bitwise_or_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 5 | 2;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(7, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_bitwise_xor_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 7 ^ 2;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(5, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_bitwise_not_float(self):
        ncs = self.compile("""
            void main()
            {
                int a = ~1;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(-2, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_bitwise_and_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 7 & 2;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()
        
        self.assertEqual(2, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_bitwise_shiftleft_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 7 << 2;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(28, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_bitwise_shiftright_op(self):
        ncs = self.compile("""
            void main()
            {
                int a = 7 >> 2;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, interpreter.stack_snapshots[-4].stack[-1].value)
    # endregion

    # region Assignment
    def test_assignment(self):
        ncs = self.compile("""
            void main()
            {
                int a = 1;
                a = 2 * 2;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(4, interpreter.stack_snapshots[-4].stack[-1].value)

    def test_addition_assignment_int_int(self):
        ncs = self.compile("""
            void main()
            {
                int value = 1;
                value += 2;
                
                PrintInteger(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        snap = interpreter.action_snapshots[-1]
        self.assertEqual("PrintInteger", snap.function_name)
        self.assertEqual(3, snap.arg_values[0])

    def test_addition_assignment_int_float(self):
        ncs = self.compile("""
            void main()
            {
                int value = 1;
                value += 2.0;
                
                PrintInteger(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        snap = interpreter.action_snapshots[-1]
        self.assertEqual("PrintInteger", snap.function_name)
        self.assertEqual(3, snap.arg_values[0])

    def test_addition_assignment_float_float(self):
        ncs = self.compile("""
            void main()
            {
                float value = 1.0;
                value += 2.0;
                
                PrintFloat(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        snap = interpreter.action_snapshots[-1]
        self.assertEqual("PrintFloat", snap.function_name)
        self.assertEqual(3.0, snap.arg_values[0])

    def test_addition_assignment_float_int(self):
        ncs = self.compile("""
            void main()
            {
                float value = 1.0;
                value += 2;
                
                PrintFloat(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        snap = interpreter.action_snapshots[-1]
        self.assertEqual("PrintFloat", snap.function_name)
        self.assertEqual(3.0, snap.arg_values[0])

    def test_addition_assignment_string_string(self):
        ncs = self.compile("""
            void main()
            {
                string value = "a";
                value += "b";
                
                PrintString(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        snap = interpreter.action_snapshots[-1]
        self.assertEqual("PrintString", snap.function_name)
        self.assertEqual("ab", snap.arg_values[0])

    def test_subtraction_assignment_int_int(self):
        ncs = self.compile("""
            void main()
            {
                int value = 10;
                value -= 2 * 2;
                
                PrintInteger(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        snap = interpreter.action_snapshots[-1]
        self.assertEqual("PrintInteger", snap.function_name)
        self.assertEqual([6], snap.arg_values)

    def test_subtraction_assignment_int_float(self):
        ncs = self.compile("""
            void main()
            {
                int value = 10;
                value -= 2.0;
                
                PrintInteger(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        snap = interpreter.action_snapshots[-1]
        self.assertEqual("PrintInteger", snap.function_name)
        self.assertEqual(8.0, snap.arg_values[0])

    def test_subtraction_assignment_float_float(self):
        ncs = self.compile("""
            void main()
            {
                float value = 10.0;
                value -= 2.0;
                
                PrintFloat(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        snap = interpreter.action_snapshots[-1]
        self.assertEqual("PrintFloat", snap.function_name)
        self.assertEqual(8.0, snap.arg_values[0])

    def test_subtraction_assignment_float_int(self):
        ncs = self.compile("""
            void main()
            {
                float value = 10.0;
                value -= 2;
                
                PrintFloat(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        snap = interpreter.action_snapshots[-1]
        self.assertEqual("PrintFloat", snap.function_name)
        self.assertEqual(8.0, snap.arg_values[0])

    def test_multiplication_assignment(self):
        ncs = self.compile("""
            void main()
            {
                int value = 10;
                value *= 2 * 2;
                
                PrintInteger(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        snap = interpreter.action_snapshots[-1]
        self.assertEqual("PrintInteger", snap.function_name)
        self.assertEqual([40], snap.arg_values)

    def test_division_assignment(self):
        ncs = self.compile("""
            void main()
            {
                int value = 12;
                value /= 2 * 2;
                
                PrintInteger(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        snap = interpreter.action_snapshots[-1]
        self.assertEqual("PrintInteger", snap.function_name)
        self.assertEqual([3], snap.arg_values)
    # endregion

    # region Simple Expressions

    # endregion

    def test_scope(self):
        ncs = self.compile("""
            void main()
            {
                int value = 1;
                
                if (value == 1)
                {
                    value = 2;
                }
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

    def test_if(self):
        ncs = self.compile("""
            void main()
            {
                if(0)
                {
                    PrintInteger(0);
                }
            
                if(1)
                {
                    PrintInteger(1);
                }
                
                if(0)
                {
                    PrintInteger(2);
                }
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, len(interpreter.action_snapshots))
        self.assertEqual(1, interpreter.action_snapshots[0].arg_values[0])

    def test_while_loop(self):
        ncs = self.compile("""
            void main()
            {
                int value = 3;
                while (value)
                {
                    PrintInteger(value);
                    value -= 1;
                }
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(3, len(interpreter.action_snapshots))
        self.assertEqual(3, interpreter.action_snapshots[0].arg_values[0])
        self.assertEqual(2, interpreter.action_snapshots[1].arg_values[0])
        self.assertEqual(1, interpreter.action_snapshots[2].arg_values[0])

    def test_do_while_loop(self):
        ncs = self.compile("""
            void main()
            {
                int value = 3;
                do
                {
                    PrintInteger(value);
                    value -= 1;
                } while (value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(3, len(interpreter.action_snapshots))
        self.assertEqual(3, interpreter.action_snapshots[0].arg_values[0])
        self.assertEqual(2, interpreter.action_snapshots[1].arg_values[0])
        self.assertEqual(1, interpreter.action_snapshots[2].arg_values[0])

    def test_for_loop(self):
        ncs = self.compile("""
            void main()
            {
                int i = 99;
                for (i = 1; i <= 3; i += 1)
                {
                    PrintInteger(i);
                }
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(3, len(interpreter.action_snapshots))
        self.assertEqual(1, interpreter.action_snapshots[0].arg_values[0])
        self.assertEqual(2, interpreter.action_snapshots[1].arg_values[0])
        self.assertEqual(3, interpreter.action_snapshots[2].arg_values[0])

    def test_comment(self):
        ncs = self.compile("""
            void main()
            {
                // int a = "abc"; // [] /*
                int a = 0;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

    def test_multiline_comment(self):
        ncs = self.compile("""
            void main()
            {
                /* int 
                abc = 
                ;; 123
                */
                
                string aaa = "";
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

    def test_include(self):
        ncs = self.compile("""
            #include "k_inc_debug"
            
            void main()
            {
            
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

    def test_return(self):
        ncs = self.compile("""
            void main()
            {
                int a = 1;
            
                if (a == 1)
                {
                    PrintInteger(a);
                    return;
                }
                
                PrintInteger(0);
                return;
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, len(interpreter.action_snapshots))
        self.assertEqual(1, interpreter.action_snapshots[0].arg_values[0])

    def test_import(self):
        otherscript = """
            void TestFunc()
            {
                PrintInteger(123);
            }
        """

        ncs = self.compile("""
            #include "otherscript"
        
            void main()
            {
                TestFunc();
            }
        """, library={"otherscript": otherscript})

        interpreter = Interpreter(ncs)
        interpreter.run()
        ncs.print()

    # region User-defined Functions
    def test_forward_declaration_no_args(self):
        ncs = self.compile("""
            void test();

            void main()
            {
                test();
            }

            void test()
            {
                PrintInteger(56);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, len(interpreter.action_snapshots))
        self.assertEqual(56, interpreter.action_snapshots[0].arg_values[0])

    def test_forward_declaration_with_args(self):
        ncs = self.compile("""
            void test();

            void main()
            {
                test(57);
            }

            void test(int value)
            {
                PrintInteger(value);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, len(interpreter.action_snapshots))
        self.assertEqual(57, interpreter.action_snapshots[0].arg_values[0])

    def test_redefine_function(self):
        script = """
            void test()
            {
                
            }
        
            void test()
            {
                
            }
        """
        self.assertRaises(CompileException, self.compile, script)

    def test_call_undefined(self):
        script = """
            void main()
            {
                test(0);
            }
        """

        self.assertRaises(CompileException, self.compile, script)

    def test_call_void_with_no_args(self):
        ncs = self.compile("""
            void test()
            {
                PrintInteger(123);
            }
        
            void main()
            {
                test();
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, len(interpreter.action_snapshots))
        self.assertEqual(123, interpreter.action_snapshots[0].arg_values[0])

    def test_call_void_with_one_arg(self):
        ncs = self.compile("""
            void test(int value)
            {
                PrintInteger(value);
            }

            void main()
            {
                test(123);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, len(interpreter.action_snapshots))
        self.assertEqual(123, interpreter.action_snapshots[0].arg_values[0])

    def test_call_void_with_two_args(self):
        ncs = self.compile("""
            void test(int value1, int value2)
            {
                PrintInteger(value1);
                PrintInteger(value2);
            }

            void main()
            {
                test(1, 2);
            }
        """)

        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(2, len(interpreter.action_snapshots))
        self.assertEqual(1, interpreter.action_snapshots[0].arg_values[0])
        self.assertEqual(2, interpreter.action_snapshots[1].arg_values[0])

    def test_call_int_with_no_args(self):
        ncs = self.compile("""
            int test()
            {
                return 5;
            }

            void main()
            {
                int x = test();
                PrintInteger(x);
            }
        """)

        ncs.print()
        interpreter = Interpreter(ncs)
        interpreter.run()

        self.assertEqual(1, len(interpreter.action_snapshots))
        self.assertEqual(5, interpreter.action_snapshots[0].arg_values[0])
    # endregion
