# import unittest
# from TestUtils import TestLexer
# class LexerSuite(unittest.TestCase):
      
#     def test1(self):
#         self.assertTrue(TestLexer.test("{ } ( ) , . ; : [ ]","{,},(,),,,.,;,:,[,],<EOF>",1))  

#     def test2(self):
#         self.assertTrue(TestLexer.test("+ - * / % ! != && || == = != < > >= <= :: $ \\ #","+,-,*,/,%,!,!=,&&,||,==,=,!=,<,>,>=,<=,::,Error Token $",2))  

#     def test3(self):
#         self.assertTrue(TestLexer.test("Hello\nHello","Hello,Hello,<EOF>",3))

#     def test4(self):
#         self.assertTrue(TestLexer.test('''##Hello\nHello##''',"<EOF>",4))

#     def test5(self):
#         self.assertTrue(TestLexer.test("_","_,<EOF>",5))
    
#     def test6(self):
#         self.assertTrue(TestLexer.test("##Hello\r\t\n\fHello##","<EOF>",6))

#     def test7(self):
#         self.assertTrue(TestLexer.test("##Hello\nHello##","<EOF>",7))

#     def test8(self):
#         self.assertTrue(TestLexer.test("##Hello\\rHello##","<EOF>",8))

#     def test9(self):
#         self.assertTrue(TestLexer.test("$0_Hello_123_","$0_Hello_123_,<EOF>",9))
   
#     def test10(self):
#         self.assertTrue(TestLexer.test("##Hello##Hello##","Hello,Error Token #",10))

#     def test11(self):
#         self.assertTrue(TestLexer.test("$0","$0,<EOF>",11))

#     def test12(self):
#         self.assertTrue(TestLexer.test('''"Hello'"''',"Unclosed String: Hello'\"",12))

#     def test13(self):
#         self.assertTrue(TestLexer.test(""" "Hello 'Hello \\t " ""","Hello 'Hello \\t ,<EOF>",13))
        
#     def test14(self):
#         self.assertTrue(TestLexer.test(""" 'Hello' ""","Error Token '",14))
    
#     def test15(self):
#         self.assertTrue(TestLexer.test(''' "Hello\\ ''',"Illegal Escape In String: Hello\ ",15))
    
#     def test16(self):
#         self.assertTrue(TestLexer.test("$0_123_4_5","$0_123_4_5,<EOF>",16))

#     def test17(self):
#         self.assertTrue(TestLexer.test(''' "Hello\\a\\b\\c" ''',"Illegal Escape In String: Hello\\a",17))

#     def test18(self):
#         self.assertTrue(TestLexer.test(''' "Hello\nHello" ''',"Unclosed String: Hello",18))

#     def test19(self):
#         self.assertTrue(TestLexer.test(''' "Hello\tHello \\n \\f \\b \\r \\t \\\\ \\' '"' " ''','''Hello	Hello \\n \\f \\b \\r \\t \\\\ \\' '"' ,<EOF>''',19))

#     def test20(self):
#         self.assertTrue(TestLexer.test(''' "Hello \\h ''',"Illegal Escape In String: Hello \h",20))
    
#     def test21(self):
#         self.assertTrue(TestLexer.test("0b111__11","0b111,__11,<EOF>",21))
    
#     ''' Check Float'''
#     def test22(self):
#         self.assertTrue(TestLexer.test("1.234","1.234,<EOF>",22))

#     def test23(self):
#         self.assertTrue(TestLexer.test("1.234e5","1.234e5,<EOF>",23))
    
#     def test24(self):
#         self.assertTrue(TestLexer.test("1.234e-5","1.234e-5,<EOF>",24))

#     def test25(self):
#         self.assertTrue(TestLexer.test("7E-10","7E-10,<EOF>",25))

#     def test26(self):
#         self.assertTrue(TestLexer.test("1_234.567","1234.567,<EOF>",26))
    
#     def test27(self):
#         self.assertTrue(TestLexer.test("0x56.567e-10","0x56,.567e-10,<EOF>",27))

#     def test28(self):
#         self.assertTrue(TestLexer.test("0x56.567e-10_","0x56,.567e-10,_,<EOF>",28))
    
#     def test29(self):
#         self.assertTrue(TestLexer.test("1.e123_56","1.e123,_56,<EOF>",29))

#     def test30(self):
#         self.assertTrue(TestLexer.test(".0123",".,0123,<EOF>",30))
    
#     def test31(self):
#         self.assertTrue(TestLexer.test(".123",".,123,<EOF>",31))

#     def test32(self):
#         self.assertTrue(TestLexer.test("e135","e135,<EOF>",32))

#     def test33(self):
#         self.assertTrue(TestLexer.test("0.12_5e-120","0.12,_5e,-,120,<EOF>",33))

#     def test34(self):
#         self.assertTrue(TestLexer.test("00.12_5e-120","00,.,125e-120,<EOF>",34))
    
#     def test35(self):
#         self.assertTrue(TestLexer.test("00123","00,123,<EOF>",35))

#     def test36(self):
#         self.assertTrue(TestLexer.test("00 0b0 1_2_33.E+123","00,0b0,1233.E+123,<EOF>",36))

#     def test37(self):
#         self.assertTrue(TestLexer.test("12.00001","12.00001,<EOF>",37))

#     def test38(self):
#         self.assertTrue(TestLexer.test("08123","0,8123,<EOF>",38))

#     def test39(self):
#         self.assertTrue(TestLexer.test("0x123n",",<EOF>",39))

#     def test39(self):
#         self.assertTrue(TestLexer.test("\"Hello\"","Hello,<EOF>",39))
    
#     def test40(self):
#         self.assertTrue(TestLexer.test("\"Hello\\n\"","Hello\\n,<EOF>",40))

#     def test41(self):
#         self.assertTrue(TestLexer.test('''"This is a string containing tab \\t"''',"This is a string containing tab \\t,<EOF>",41))
    
#     def test42(self):
#         self.assertTrue(TestLexer.test('''"This is a string containing backslash \\\\"''',"This is a string containing backslash \\\\,<EOF>",42))

#     def test43(self):
#         self.assertTrue(TestLexer.test(''' "Test case string '"" ''','''Test case string '",<EOF>''',43))

#     def test44(self):
#         self.assertTrue(TestLexer.test(''' "Test case string "" ''',",<EOF>",44)) 
    
#     def test44(self):
#         self.assertTrue(TestLexer.test(''' "Test case string '" ''',"Unclosed String: Test case string '\" ",55))

#     def test45(self):
#         self.assertTrue(TestLexer.test('''"Test case \n string "''',",<EOF>",46))
#     '''Test error'''
#     def test45(self):
#         self.assertTrue(TestLexer.test(''' "Hello\\a ''',"Illegal Escape In String: Hello\\a",45))

#     def test46(self):
#         self.assertTrue(TestLexer.test(''' "Hello\nHello new line "''',"Unclosed String: Hello",46))
    
#     def test47(self):
#         self.assertTrue(TestLexer.test(''' "abc\\h def" ''',"Illegal Escape In String: abc\\h",47))
    
#     def test48(self):
#         self.assertTrue(TestLexer.test(''' "Hello new line "" ''',"Hello new line ,Unclosed String:  ",48))

#     def test49(self):
#         self.assertTrue(TestLexer.test(''' "Hello new line ""\n"''',"Hello new line ,Unclosed String: ",49))

#     def test50(self):
#         self.assertTrue(TestLexer.test(''' "Hello new line ""abc\n''',"Hello new line ,Unclosed String: abc",50))
    
#     def test51(self):
#         self.assertTrue(TestLexer.test(''' "t'" ''',"Unclosed String: t'\" ",51))
    
#     def test52(self):
#         self.assertTrue(TestLexer.test(''' " Hello new line \\\ "''' ,''' Hello new line \\\\ ,<EOF>''',52))
    
#     def test53(self):
#         self.assertTrue(TestLexer.test(''' " Hello new line \\\\ "''' ," Hello new line \\\\ ,<EOF>",53))
    
#     def test54(self):
#         self.assertTrue(TestLexer.test(''' " Hello new line \\\"''' ,"Illegal Escape In String:  Hello new line \\\"",54))
    
#     def test55(self):
#         self.assertTrue(TestLexer.test(''' "Hello""Hello"" ''' ,"Hello,Hello,Unclosed String:  ",55))
    
#     def test56(self):
#         self.assertTrue(TestLexer.test(''' " Hello \\a\\b\\c " ''' ,"Illegal Escape In String:  Hello \\a",56))

#     def test57(self):
#         self.assertTrue(TestLexer.test('''"aaa\\pbb''',"Illegal Escape In String: aaa\p",57))
    
#     def test58(self):
#         self.assertTrue(TestLexer.test(""" "abc \\h def ""","""Illegal Escape In String: abc \h""",58))

#     def test59(self):
#         self.assertTrue(TestLexer.test(""" "abc \h def ""","""Illegal Escape In String: abc \h""",59))

#     def test60(self):
#         self.assertTrue(TestLexer.test(""" Array(1, 5, 7, 12)""","""Array,(,1,,,5,,,7,,,12,),<EOF>""",60))

#     def test61(self):
#         self.assertTrue(TestLexer.test(""" 0x000000 ""","""0x0,00,00,0,<EOF>""",61))

#     def test62(self):
#         self.assertTrue(TestLexer.test(""" 0x000000n ""","""0x0,00,00,0,n,<EOF>""",62))

#     def test63(self):
#         self.assertTrue(TestLexer.test(""" 0xafbc123 ""","""0,xafbc123,<EOF>""",63))
    
#     def test64(self):
#         self.assertTrue(TestLexer.test(""" 00123 0_00123 0_0 0_x12_34_AF 1.E_+_3  1_.E_00 ""","""00,123,0,_00123,0,_0,0,_x12_34_AF,1.,E_,+,_3,1,_,.,E_00,<EOF>""",64))

#     def test65(self):
#         self.assertTrue(TestLexer.test(""" 0.12_5e-120 0b111_111 0b0111_00 0b_00011 0b_001.11000X7E.10+3 1.e- 1.e-_ 1.e765_123""","""0.12,_5e,-,120,0b111111,0b0,11100,0,b_00011,0,b_001,.,11000,X7E,.,10,+,3,1.,e,-,1.,e,-,_,1.e765,_123,<EOF>""",65))

#     def test66(self):
#         self.assertTrue(TestLexer.test(""" 1_23__456 012378""","""123,__456,01237,8,<EOF>""",66))

#     def test67(self):
#         self.assertTrue(TestLexer.test(""" " Break Breakafb NewHello Elseifabc Value voidHello mptypeHello ProgramABC mainHello" """,""" Break Breakafb NewHello Elseifabc Value voidHello mptypeHello ProgramABC mainHello,<EOF>""",67))
    
#     def test68(self):
#         self.assertTrue(TestLexer.test(""" "......." """,""".......,<EOF>""",68))

#     def test69(self):
#         self.assertTrue(TestLexer.test(""" ":::" """,""":::,<EOF>""",69))
    
#     def test70(self):
#         self.assertTrue(TestLexer.test(""" "Hello\\0 " ""","""Illegal Escape In String: Hello\\0""",70))

#     def test71(self):
#         self.assertTrue(TestLexer.test(""" "Hello\'0'Hello " ""","""Hello'0'Hello ,<EOF>""",71))

#     def test72(self):
#         self.assertTrue(TestLexer.test(""" "Hello||Hello " ""","""Hello||Hello ,<EOF>""",72))

#     def test73(self):
#         self.assertTrue(TestLexer.test(""" Hello||Hello ""","""Hello,||,Hello,<EOF>""",73))
    
#     def test74(self):
#         self.assertTrue(TestLexer.test(""" Hi;Hi" ""","""Hi,;,Hi,Unclosed String:  """,74))
    
#     def test75(self):
#         self.assertTrue(TestLexer.test(""" ==> <== ==. ==.. ...== +... ||| !!==.. ""","""==,>,<=,=,==.,==.,.,.,.,.,==,+.,.,.,||,Error Token |""",75))
    
#     def test76(self):
#         self.assertTrue(TestLexer.test(""" "Hello \\'' " \\" " ""","""Hello \\'' ,Error Token \\""",76))
    
#     def test77(self):
#         self.assertTrue(TestLexer.test(""" "" """,""",<EOF>""",77))

#     def test78(self):
#         self.assertTrue(TestLexer.test(""" 00.12_5e-120 ""","""00,.,125e-120,<EOF>""",78))

#     def test79(self):
#         self.assertTrue(TestLexer.test("""""","""<EOF>""",79))

#     def test80(self):
#         self.assertTrue(TestLexer.test("""abc?sxny""","""abc,Error Token ?""",80))

#     def test81(self):
#         self.assertTrue(TestLexer.test("""..1E+123""",""".,.1E+123,<EOF>""",81))
    
#     def test82(self):
#         self.assertTrue(TestLexer.test("""$..3E123""","""Error Token $""",82))
    
#     def test83(self):
#         self.assertTrue(TestLexer.test("""$.3E123""","""Error Token $""",83))
    
#     def test84(self):
#         self.assertTrue(TestLexer.test("""\\\\""","""Error Token \\""",84))
    
#     def test85(self):
#         self.assertTrue(TestLexer.test("""E5678""","""E5678,<EOF>""",85))
    
#     def test86(self):
#         self.assertTrue(TestLexer.test("""00123.1_12_e+120""","""00,123.1,_12_e,+,120,<EOF>""",86))
    
#     def test87(self):
#         self.assertTrue(TestLexer.test("""::""","""::,<EOF>""",87))
    
#     def test88(self):
#         self.assertTrue(TestLexer.test("""123.0""","""123.0,<EOF>""",88))
    
#     def test89(self):
#         self.assertTrue(TestLexer.test("""123.""","""123.,<EOF>""",89))
    
#     def test90(self):
#         self.assertTrue(TestLexer.test("""E+123""","""E,+,123,<EOF>""",90))
    
#     def test91(self):
#         self.assertTrue(TestLexer.test(""".123""",""".,123,<EOF>""",91))
    
#     def test92(self):
#         self.assertTrue(TestLexer.test(""" Hello" ""","""Hello,Unclosed String:  """,92))
    
#     def test93(self):
#         self.assertTrue(TestLexer.test(""" "Hello\\0Hello " ""","""Illegal Escape In String: Hello\\0""",93))
    
#     def test94(self):
#         self.assertTrue(TestLexer.test(""" "\\" """,'''Illegal Escape In String: \\"''',94))
    
#     def test95(self):
#         self.assertTrue(TestLexer.test(""" $___ """,'$___,<EOF>',95))
    
#     def test96(self):
#         self.assertTrue(TestLexer.test(""" $$ ""","""Error Token $""",96))
    
#     def test97(self):
#         self.assertTrue(TestLexer.test('''"string\'\'\'\'\'"""""""''',"""string'''''",,,Unclosed String: """,97))
    
#     def test98(self):
#         self.assertTrue(TestLexer.test(""" \\r\\b\\n\\r\\t ""","""Error Token \\""",98))
    
#     def test99(self):
#         self.assertTrue(TestLexer.test(""" \r\f\b\t\n ""","""<EOF>""",99))
    
#     def test100(self):
#         self.assertTrue(TestLexer.test(""" "Hello ''\\'''"\\\ " ""","""Hello ''\\'''"\\\\ ,<EOF>""",100))

     

    




# import unittest
# from TestUtils import TestLexer


# class LexerSuite(unittest.TestCase):

#     def test_comment_1(self):
#         test = """ ##Khang is my name## """
#         expect = "<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 1'))

#     def test_comment_2(self):
#         test = """ ##khang \n\b\f\r\t \\## """
#         expect = "<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 2'))

#     def test_comment_3(self):
#         test = """ ######## """
#         expect = "<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 3'))

#     def test_comment_4(self):
#         test = """ ##"My name is khang \\n"## """
#         expect = "<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 4'))

#     def test_comment_5(self):
#         test = """ ##  "My name is khang \\n"
#             hello world
#             ##
#         """
#         expect = "<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 5'))

#     def test_comment_6(self):
#         test = """ ##### """
#         expect = "Error Token #"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 6'))

#     def test_comment_7(self):
#         test = """ ####khang#### """
#         expect = "khang,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 7'))

#     def test_comment_8(self):
#         test = """ ##
#          #khang#
#          k
#          h
#          \n\b#//
#          ##
#          """
#         expect = "<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 8'))

#     def test_comment_9(self):
#         test = """ 
#          ##
#          khangro\n
#          #
#          ###
#          khang
#          """
#         expect = "Error Token #"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 9'))

#     def test_comment_10(self):
#         test = """ khang ##
#         \n abcd ED
#         ## 
#         PPL
#         """
#         expect = "khang,PPL,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 10'))

#     def test_id_11(self):
#         test = """khang Ppl _dinhkout khang123"""
#         expect = "khang,Ppl,_dinhkout,khang123,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 11'))

#     def test_id_12(self):
#         test = """1khang__"""
#         expect = "1,khang__,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 12'))

#     def test_id_13(self):
#         test = """$khang $123 $__12__"""
#         expect = "$khang,$123,$__12__,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 13'))

#     def test_id_14(self):
#         test = """khang__khang _123kh__ $012___456_7"""
#         expect = "khang__khang,_123kh__,$012___456_7,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 14'))

#     def test_id_15(self):
#         test = """$$khang $ """
#         expect = "Error Token $"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 15'))

#     def test_id_16(self):
#         test = """$____ ____ """
#         expect = "$____,____,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 16'))

#     def test_id_17(self):
#         test = """$123 _$1234khang """
#         expect = "$123,_,$1234khang,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 17'))

#     def test_keyword_18(self):
#         test = """Break Continue If Elseif Else """
#         expect = "Break,Continue,If,Elseif,Else,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 18'))

#     def test_integer_19(self):
#         test = """123 456 120 0"""
#         expect = "123,456,120,0,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 19'))

#     def test_integer_20(self):
#         test = """123_456_789 1_2_3_4 567_7"""
#         expect = "123456789,1234,5677,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 20'))

#     def test_integer_21(self):
#         test = """123__45 0_123"""
#         expect = "123,__45,0,_123,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 21'))

#     def test_integer_22(self):
#         test = """0000"""
#         expect = "00,00,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 22'))

#     def test_integer_23(self):
#         test = """0x123 0XABC 0x678"""
#         expect = "0x123,0XABC,0x678,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 23'))

#     def test_integer_24(self):
#         test = """0x123_456 0X0 0xA_123_CF"""
#         expect = "0x123456,0X0,0xA123CF,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 23'))

#     def test_integer_25(self):
#         test = """0x01 0x_0"""
#         expect = "0x0,1,0,x_0,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 25'))

#     def test_integer_26(self):
#         test = """0x00 00x00"""
#         expect = "0x0,0,00,x00,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 26'))

#     def test_integer_27(self):
#         test = """000 0b0 0b100_1100"""
#         expect = "00,0,0b0,0b1001100,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 27'))

#     def test_integer_28(self):
#         test = """0123_456_7 000 0_00 00_00"""
#         expect = "01234567,00,0,0,_00,00,_00,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 28'))

#     def test_integer_29(self):
#         test = """0B11_1100 0b124 0xABC_DEF_GH """
#         expect = "0B111100,0b1,24,0xABCDEF,_GH,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 29'))

#     def test_integer_30(self):
#         test = """0b00B0 0x00X0 0567878787 """
#         expect = "0b0,0B0,0x0,0X0,0567,878787,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 30'))

#     def test_string_31(self):
#         test = """ "khang" """
#         expect = "khang,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 31'))

#     def test_string_32(self):
#         test = """ "my name is khang" """
#         expect = "my name is khang,<EOF>"
#         self.assertTrue(TestLexer.test(test, expect, 'Test 32'))

#     def test_string_33(self):
#         test = """ "khang \n" """
#         expect = """Unclosed String: khang """
#         self.assertTrue(TestLexer.test(test, expect, 'Test 33'))

#     def test_string_34(self):
#         test = """ "khang\nkhang" """
#         expect = """Unclosed String: khang"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 34'))

#     def test_string_35(self):
#         test = """ "khang"""
#         expect = """Unclosed String: khang"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 35'))

#     def test_string_36(self):
#         test = """ "aaa\\pbb """
#         expect = """Illegal Escape In String: aaa\\p"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 36'))

#     def test_string_37(self):
#         test = """ "khang \\b \\f \\r\\t" """
#         expect = """khang \\b \\f \\r\\t,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 37'))

#     def test_string_38(self):
#         test = """ "khang" " """
#         expect = """khang,Unclosed String:  """
#         self.assertTrue(TestLexer.test(test, expect, 'Test 38'))

#     def test_string_39(self):
#         test = """ "This is a string containing tab \\t" """
#         expect = """This is a string containing tab \\t,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 39'))

#     def test_string_40(self):
#         test = """ "aa\naa" """
#         expect = """Unclosed String: aa"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 40'))

#     def test_string_41(self):
#         test = """ "khang\\ " """
#         expect = """Illegal Escape In String: khang\\ """
#         self.assertTrue(TestLexer.test(test, expect, 'Test 41'))

#     def test_string_42(self):
#         test = """ "khang\\\\" """
#         expect = """khang\\\\,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 42'))

#     def test_string_43(self):
#         test = """ "khang'hana' " """
#         expect = """khang'hana' ,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 43'))

#     def test_string_44(self):
#         test = """ "My name is '"khang'"?" """
#         expect = """My name is '"khang'"?,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 44'))

#     def test_float_45(self):
#         test = """ 1.001 2.56 3.24"""
#         expect = """1.001,2.56,3.24,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 45'))

#     def test_float_46(self):
#         test = """ 1. 2. """
#         expect = """1.,2.,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 46'))

#     def test_float_47(self):
#         test = """ 123_456.01 1.00000 123_45.0000 """
#         expect = """123456.01,1.00000,12345.0000,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 47'))

#     def test_float_48(self):
#         test = """ 123e+10 145_45e-10 123.e-10"""
#         expect = """123e+10,14545e-10,123.e-10,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 48'))

#     def test_float_49(self):
#         test = """ 123.12e+15 124.1e-00012"""
#         expect = """123.12e+15,124.1e-00012,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 49'))

#     def test_float_50(self):
#         test = """ e+15 e-12"""
#         expect = """e,+,15,e,-,12,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 50'))

#     def test_float_51(self):
#         test = """ 123e 456e"""
#         expect = """123,e,456,e,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 51'))

#     def test_float_52(self):
#         test = """ 123.456_534 567.12_1_1"""
#         expect = """123.456,_534,567.12,_1_1,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 52'))

#     def test_float_53(self):
#         test = """ 01.e-12 001.2e+13"""
#         expect = """01,.e-12,00,1.2e+13,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 53'))

#     def test_float_54(self):
#         test = """ 12e-12_34_56"""
#         expect = """12e-12,_34_56,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 54'))

#     def test_float_55(self):
#         test = """ .123e-12"""
#         expect = """.123e-12,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 55'))

#     def test_string_56(self):
#         test = """ "khang\b """
#         expect = """Unclosed String: khang\b """
#         self.assertTrue(TestLexer.test(test, expect, 'Test 56'))

#     def test_string_57(self):
#         test = """ "khang\b" """
#         expect = """khang\b,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 57'))

#     def test_string_58(self):
#         test = """ "khang\b """
#         expect = """Unclosed String: khang\b """
#         self.assertTrue(TestLexer.test(test, expect, 'Test 58'))

#     def test_id_59(self):
#         test = """ Ifelse """
#         expect = """Ifelse,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 59'))

#     def test_id_60(self):
#         test = """ 12abc """
#         expect = """12,abc,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 60'))

#     def test_id_61(self):
#         test = """ aAsVN3 """
#         expect = """aAsVN3,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 61'))

#     def test_id_62(self):
#         test = """ 123a123 """
#         expect = """123,a123,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 62'))

#     def test_op_63(self):
#         test = """ & & """
#         expect = """Error Token &"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 63'))

#     def test_op_64(self):
#         test = """ && """
#         expect = """&&,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 64'))

#     def test_op_65(self):
#         test = """ && """
#         expect = """&&,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 65'))

#     def test_op_66(self):
#         test = """ != => """
#         expect = """!=,=,>,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 66'))

#     def test_op_67(self):
#         test = """ == . """
#         expect = """==,.,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 67'))

#     def test_op_68(self):
#         test = """ ==. """
#         expect = """==.,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 68'))

#     def test_op_69(self):
#         test = """ | | """
#         expect = """Error Token |"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 69'))

#     def test_op_70(self):
#         test = """ || """
#         expect = """||,<EOF>"""
#         self.assertTrue(TestLexer.test(test, expect, 'Test 70'))


# import unittest
# from TestUtils import TestLexer

# class LexerSuite(unittest.TestCase): 
#     def test_cmt_1(self):
#         self.assertTrue(TestLexer.test(""" ## Le thanh phuong##  """, """<EOF>""", 101))           
#     def test_cmt_2(self):
#         self.assertTrue(TestLexer.test(""" ######## """, """<EOF>""", 102))   
#     def test_cmt_3(self):
#         self.assertTrue(TestLexer.test(""" ##"aStrng"/an\\rd/d" ## """, """<EOF>""", 103))
#     def test_cmt_4(self):
#         self.assertTrue(TestLexer.test(""" ##### """, """Error Token #""", 104))
#     def test_cmt_5(self):
#         self.assertTrue(TestLexer.test(""" ####abcd#### """, """abcd,<EOF>""", 105))
#     def test_cmt_6(self):
#         input = r""" 
#         ## comment
#         #a
#         #b
#         ## """
#         self.assertTrue(TestLexer.test(input, """<EOF>""", 106))
#     def test_cmt_7(self):
#         input = r""" 
#         ## comment
#         #a
#         #b
#         ###
#         """
#         self.assertTrue(TestLexer.test(input, """Error Token #""", 107))
#     def test_cmt_8(self):
#         input = r""" 
#         ## comment
#         #a.\nass
#         #b.\t
#         ## """
#         self.assertTrue(TestLexer.test(input, """<EOF>""", 108))
#     def test_cmt_9(self):
#         input = r""" 
#         ## comment
#         #a.
#         #b
#         """
#         self.assertTrue(TestLexer.test(input, """Error Token #""", 109))
#     def test_id_10(self):
#         self.assertTrue(TestLexer.test(""" abc """, """abc,<EOF>""", 110))

#     def test_id_11(self):
#         self.assertTrue(TestLexer.test(""" 1eNa """, """1,eNa,<EOF>""", 111))

#     def test_id_12(self):
#         self.assertTrue(TestLexer.test(""" _ 01abc """, """_,01,abc,<EOF>""", 112))

#     def test_id_13(self):
#         self.assertTrue(TestLexer.test(""" _ 0a abc """, """_,0,a,abc,<EOF>""", 113))

#     def test_id_14(self):
#         self.assertTrue(TestLexer.test(""" a """, """a,<EOF>""", 114))

#     def test_id_15(self):
#         self.assertTrue(TestLexer.test(""" 0.11$test0.11 """, """0.11,$test0,.,11,<EOF>""", 115))

#     def test_id_16(self):
#         self.assertTrue(TestLexer.test(""" $_  """, """$_,<EOF>""", 116))

#     def test_id_17(self):
#         self.assertTrue(TestLexer.test(""" $a """, """$a,<EOF>""", 117))

#     def test_id_18(self):
#         self.assertTrue(TestLexer.test(""" $ """, """Error Token $""", 118))

#     def test_id_19(self):
#         self.assertTrue(TestLexer.test(""" $a _a 1kaw 1 """, """$a,_a,1,kaw,1,<EOF>""", 119))

#     def test_id_20(self):
#         self.assertTrue(
#             TestLexer.test(""" abcd_1234$ """, """abcd_1234,Error Token $""", 120))
#     def test_id_21(self):
#         self.assertTrue(
#             TestLexer.test(""" abcd_1234$_ """, """abcd_1234,$_,<EOF>""", 121))
#     def test_keyword_22(self):
#         self.assertTrue(
#             TestLexer.test(""" Continue Break If Elseif """, """Continue,Break,If,Elseif,<EOF>""", 122))
#     def test_decimal_23(self):
#         self.assertTrue(
#             TestLexer.test(""" 0 """, """0,<EOF>""", 123))
#     def test_decimal_24(self):
#         self.assertTrue(
#             TestLexer.test(""" 1 """, """1,<EOF>""", 124))   
#     def test_decimal_25(self):
#         self.assertTrue(
#             TestLexer.test(""" 12345 """, """12345,<EOF>""", 125))
#     def test_decimal_26(self):
#         self.assertTrue(
#             TestLexer.test(""" 123_12343_525 """, """12312343525,<EOF>""", 126))   
#     def test_decimal_27(self):
#         self.assertTrue(
#             TestLexer.test(""" 1_234_1 """, """12341,<EOF>""", 127))
#     def test_decimal_28(self):
#         self.assertTrue(
#             TestLexer.test(""" 1_234_ """, """1234,_,<EOF>""", 128))         
#     def test_decimal_29(self):
#         self.assertTrue(
#             TestLexer.test(""" 1_ """, """1,_,<EOF>""", 129))  
#     def test_oct_30(self):
#         self.assertTrue(
#             TestLexer.test(""" 00000 """, """00,00,0,<EOF>""", 130))
#     def test_oct_31(self):
#         self.assertTrue(
#             TestLexer.test(""" 02_123 """, """02123,<EOF>""", 131))
#     def test_id_32(self):
#         self.assertTrue(
#             TestLexer.test(""" True False """, """True,False,<EOF>""", 132))    
#     def test_33(self):
#         self.assertTrue(TestLexer.test(""" Int Float ""","""Int,Float,<EOF>""", 133))
#     def test34(self):
#         input = """ 0_123 """
#         output = """0,_123,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,134))
#     def test35(self):
#         input = """ 000123_313_334 """
#         output = """00,0123313334,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,135))
#     def test36(self):
#         input = """ 012_34 """
#         output = """01234,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,136))
#     def test37(self):
#         input = """ 09 """
#         output = """0,9,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,137))
#     def test38(self):
#         input = """ 07 """
#         output = """07,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,138))
#     def test39(self):
#         input = """ 000123879 """
#         output = """00,0123,879,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,139))
#     def test40(self):
#         input = """ 09_123a """
#         output = """0,9123,a,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,140))

#     def test41(self):
#         input = """ 0x """
#         output = """0,x,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,141))
#     def test42(self):
#         input = """ 0x0 """
#         output = """0x0,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,142))
#     def test43(self):
#         input = """ 0x00X0 """
#         output = """0x0,0X0,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,143))
#     def test44(self):
#         input = """ 0x00001 """
#         output = """0x0,00,01,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,144))
#     def test45(self):
#         input = """ 0xA """
#         output = """0xA,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,145))
#     def test46(self):
#         input = """ 0xAG """
#         output = """0xA,G,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,146))
#     def test47(self):
#         input = """ 0xaz """
#         output = """0,xaz,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,147))
#     def test48(self):
#         input = """ 0xAb_cd_e_123_f """
#         output = """0xA,b_cd_e_123_f,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,148))
#     def test49(self):
#         input = """ 0x1_A_F410 """
#         output = """0x1AF410,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,149))
#     def test50(self):
#         input = """ 0xAb_cd_e_123_fContinueIfIn """
#         output = """0xA,b_cd_e_123_fContinueIfIn,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,150))
#     def test51(self):
#         input = """ True False Fl """
#         output = """True,False,Fl,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,151))
#     def test52(self):
#         input = """ Constructor Destructor Self Break Continue If Elseif Foreach Array In Int Float Boolean String Return Null Class"""
#         output = """Constructor,Destructor,Self,Break,Continue,If,Elseif,Foreach,Array,In,Int,Float,Boolean,String,Return,Null,Class,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,152))
#     def test53(self):
#         input = """ Val Var New By + - * / % ! && ||"""
#         output = """Val,Var,New,By,+,-,*,/,%,!,&&,||,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,153))
#     def test54(self):
#         input = """ ===!=><>=<===.+..:::(){}[],;"""
#         output = """==,=,!=,>,<,>=,<=,==.,+.,.,::,:,(,),{,},[,],,,;,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,154))
#     def test55(self):
#         input = """...."""
#         output = """.,.,.,.,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,155))
#     def test56(self):
#         input = """ 0b00B00 """
#         output = """0b0,0B0,0,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,156))
#     def test57(self):
#         input = """ 0b012_430B1_01 """
#         output = """0b0,12430,B1_01,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,157))
#     def test58(self):
#         input = """ 0b1_234 """
#         output = """0b1,_234,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,158))
#     def test59(self):
#         input = """ 0B_123 """
#         output = """0,B_123,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,159))
#     def test60(self):
#         input = """ 0000x00X00b00B00x123_F """
#         output = """00,00,x00X00b00B00x123_F,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,160))
#     def test61(self):
#         input = """ 0b11_21341 """
#         output = """0b11,_21341,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,161))
#     def test62(self):
#         input = """ 12.e1 """
#         output = """12.e1,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,162))
#     def test63(self):
#         input = """ 12.E-1 """
#         output = """12.E-1,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,163))
#     def test64(self):
#         input = """ 12.E-00000000 """
#         output = """12.E-00000000,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,164))
#     def test65(self):
#         input = """ 12_46.23E-00000010 """
#         output = """1246.23E-00000010,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,165))

#     def test66(self):
#         input = """1.e"""
#         output = """1.,e,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 166))    
#     def test67(self):
#         input = """00.000000110"""
#         output = """00,.,00,00,00,110,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 167))   
#     def test68(self):
#         input = """1_23.01230"""
#         output = """123.01230,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 168)) 
#     def test69(self):
#         input = """0."""
#         output = """0.,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 169)) 
#     def test70(self):
#         input = """00."""
#         output = """00,.,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 170)) 
#     def test71(self):
#         input = """12_3e+001"""
#         output = """123e+001,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 171)) 
#     def test72(self):
#         input = """12_3e+000"""
#         output = """123e+000,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 172))
#     def test73(self):
#         input = """12_3e-001"""
#         output = """123e-001,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 173))
#     def test74(self):
#         input = """12_3e"""
#         output = """123,e,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 174))   
#     def test75(self):
#         input = """12_3e-"""
#         output = """123,e,-,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 175))
#     def test76(self):
#         input = """.e1"""
#         output = """.e1,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 176))      
#     def test77(self):
#         input = """.0000e0"""
#         output = """.0000e0,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 177))  
#     def test78(self):
#         input = """.0000e000"""
#         output = """.0000e000,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 178)) 
#     def test79(self):
#         input = """.0000e"""
#         output = """.,00,00,e,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 179)) 
#     def test80(self):
#         input = """-2Pad0x.^2"""
#         output = """-,2,Pad0x,.,Error Token ^"""
#         self.assertTrue(TestLexer.test(input,output, 180)) 
#     def test81(self):
#         input = """00.e12"""
#         output = """00,.e12,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 181))

#     def test82(self):
#         input = """ "Le Thanh 'Phuong" """
#         output = """Le Thanh 'Phuong,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 182))
#     def test83(self):
#         input = """ "Hello\\b\\f\\t\\r\\n\\'\\\\\'"" """
#         output = """Hello\\b\\f\\t\\r\\n\\'\\\\\'",<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 183))
#     def test84(self):
#         input = """ "Hello\n" """
#         output = """Unclosed String: Hello"""
#         self.assertTrue(TestLexer.test(input,output, 184))
#     def test85(self):
#         input = """ "Hello\n """
#         output = """Unclosed String: Hello"""
#         self.assertTrue(TestLexer.test(input,output, 185))
#     def test86(self):
#         input = """ "Hello\b" """
#         output = """Hello\b,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 186))
#     def test87(self):
#         input = """ "Hello\b\t\f" """
#         output = """Hello\b\t\f,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 187))
#     def test88(self):
#         input = """ "Hello\\h """
#         output = """Illegal Escape In String: Hello\h"""
#         self.assertTrue(TestLexer.test(input,output, 188))
#     def test89(self):
#         input = """ "Hello\h """
#         output = """Illegal Escape In String: Hello\h"""
#         self.assertTrue(TestLexer.test(input,output, 189))
#     def test90(self):
#         input = """ "Hello"""
#         output = """Unclosed String: Hello"""
#         self.assertTrue(TestLexer.test(input,output, 190))
#     def test91(self):
#         input = """ "Hello \r" """
#         output = """Unclosed String: Hello """
#         self.assertTrue(TestLexer.test(input,output, 191))
#     def test92(self):
#         input = """ "Hello \'k" """
#         output = """Hello 'k,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 192))
#     def test93(self):
#         input = """ "Hello \\a" """
#         output = """Illegal Escape In String: Hello \\a"""
#         self.assertTrue(TestLexer.test(input,output, 193))
#     def test94(self):
#         input = """ "Dai. Hoc. Bach' Khoa" """
#         output = """Dai. Hoc. Bach' Khoa,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 194))
#     def test95(self):
#         input = """ "He said:'"What's your name?'"" """
#         output = """He said:'"What's your name?'",<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 195))

#     def test96(self):
#         input = """ "Hello\\" """
#         output = """Illegal Escape In String: Hello\\\""""
#         self.assertTrue(TestLexer.test(input,output, 196))
#     def test97(self):
#         input = """ "Hello\r """
#         output = """Unclosed String: Hello"""
#         self.assertTrue(TestLexer.test(input,output, 197))
#     def test98(self):
#         input = """ "abc \\t xyz\'T know" """
#         output = """abc \\t xyz'T know,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output, 198))
#     def test99(self):
#         input = """ "abc123\\a" """
#         output = """Illegal Escape In String: abc123\\a"""
#         self.assertTrue(TestLexer.test(input,output, 199))
#     def test100(self):
#         input = """ "Hello\b\r\t"""
#         output = """Unclosed String: Hello\b"""
#         self.assertTrue(TestLexer.test(input,output, 200))


# import unittest
# from TestUtils import TestLexer


# class LexerSuite(unittest.TestCase):
#     # id
#     def test1(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("test", "test,<EOF>", 'lexer01'))

#     def test2(self):
#         self.assertTrue(TestLexer.test("aCBbdc", "aCBbdc,<EOF>", 'lexer02'))

#     def test3(self):
#         self.assertTrue(TestLexer.test("aAsVN3", "aAsVN3,<EOF>", 'lexer03'))

#     def test4(self):
#         """test integers"""
#         self.assertTrue(TestLexer.test("123a123", "123,a123,<EOF>", 'lexer04'))

#     def test5(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("a_asA", "a_asA,<EOF>", 'lexer05'))

#     def test6(self):
#         self.assertTrue(TestLexer.test("$a1_", "$a1_,<EOF>", 'lexer06'))

#     def test7(self):
#         self.assertTrue(TestLexer.test("$123", "$123,<EOF>", 'lexer07'))

#     def test8(self):
#         self.assertTrue(TestLexer.test(
#             "12_sad$sd", "12,_sad,$sd,<EOF>", 'lexer08'))

#     def test9(self):
#         self.assertTrue(TestLexer.test("$___", "$___,<EOF>", 'lexer09'))

#     def test10(self):
#         self.assertTrue(TestLexer.test("$123", "$123,<EOF>", 'lexer10'))

#     # comment
#     def test11(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("## ##", "<EOF>", 'lexer11'))

#     def test12(self):
#         self.assertTrue(TestLexer.test("## aCBbdc ##", "<EOF>", 'lexer12'))

#     def test13(self):
#         self.assertTrue(TestLexer.test("## asdasd ## asdas ##",
#                                        "asdas,Error Token #", 'lexer13'))

#     def test14(self):
#         """test integers"""
#         self.assertTrue(TestLexer.test("## # #", "Error Token #", 'lexer14'))

#     def test15(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test(
#             "asd ##", "asd,Error Token #", 'lexer15'))

#     def test16(self):
#         self.assertTrue(TestLexer.test("#das #", "Error Token #", 'lexer16'))

#     def test17(self):
#         self.assertTrue(TestLexer.test(
#             "$##dg \n fgd##", "Error Token $", 'lexer17'))

#     def test18(self):
#         self.assertTrue(TestLexer.test("## EOF ##", "<EOF>", 'lexer18'))

#     def test19(self):
#         self.assertTrue(TestLexer.test("## \r ##", "<EOF>", 'lexer19'))

#     def test20(self):
#         self.assertTrue(TestLexer.test(
#             "# # as # # # #", "Error Token #", 'lexer20'))

#     # Int
#     def test21(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("Int", "Int,<EOF>", 'lexer21'))

#     def test22(self):
#         self.assertTrue(TestLexer.test("1", "1,<EOF>", 'lexer22'))

#     def test23(self):
#         self.assertTrue(TestLexer.test("12_3", "123,<EOF>", 'lexer23'))

#     def test24(self):
#         """test integers"""
#         self.assertTrue(TestLexer.test("_1", "_1,<EOF>", 'lexer24'))

#     def test25(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("2564_", "2564,_,<EOF>", 'lexer25'))

#     def test26(self):
#         self.assertTrue(TestLexer.test("345__31", "345,__31,<EOF>", 'lexer26'))

#     def test27(self):
#         self.assertTrue(TestLexer.test(
#             "2_65_88_68", "2658868,<EOF>", 'lexer27'))

#     def test28(self):
#         self.assertTrue(TestLexer.test("_0000", "_0000,<EOF>", 'lexer28'))

#     def test29(self):
#         self.assertTrue(TestLexer.test("0000", "00,00,<EOF>", 'lexer29'))

#     def test30(self):
#         self.assertTrue(TestLexer.test("0x0", "0x0,<EOF>", 'lexer30'))

#     def test31(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("0x00", "0x0,0,<EOF>", 'lexer31'))

#     def test32(self):
#         self.assertTrue(TestLexer.test("0x00123", "0x0,0123,<EOF>", 'lexer32'))

#     def test33(self):
#         self.assertTrue(TestLexer.test(
#             "0X13A_F_123", "0X13AF123,<EOF>", 'lexer33'))

#     def test34(self):
#         """test integers"""
#         self.assertTrue(TestLexer.test("0x_1", "0,x_1,<EOF>", 'lexer34'))

#     def test35(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("0XF_", "0XF,_,<EOF>", 'lexer35'))

#     def test36(self):
#         self.assertTrue(TestLexer.test(
#             "0x00001", "0x0,00,01,<EOF>", 'lexer36'))

#     def test37(self):
#         self.assertTrue(TestLexer.test(
#             "0x1_2ab2A", "0x12,ab2A,<EOF>", 'lexer37'))

#     def test38(self):
#         self.assertTrue(TestLexer.test("02", "02,<EOF>", 'lexer38'))

#     def test39(self):
#         self.assertTrue(TestLexer.test("0023", "00,23,<EOF>", 'lexer39'))

#     def test40(self):
#         self.assertTrue(TestLexer.test("0_4", "0,_4,<EOF>", 'lexer40'))

#     def test41(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("05_3", "053,<EOF>", 'lexer41'))

#     def test42(self):
#         self.assertTrue(TestLexer.test("0584_", "05,84,_,<EOF>", 'lexer42'))

#     def test43(self):
#         self.assertTrue(TestLexer.test("0b0", "0b0,<EOF>", 'lexer43'))

#     def test44(self):
#         """test integers"""
#         self.assertTrue(TestLexer.test("0B_657", "0,B_657,<EOF>", 'lexer44'))

#     def test45(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("0B112", "0B11,2,<EOF>", 'lexer45'))

#     def test46(self):
#         self.assertTrue(TestLexer.test(
#             "0b111001_12_", "0b1110011,2,_,<EOF>", 'lexer46'))

#     def test47(self):
#         self.assertTrue(TestLexer.test("0B1_1_0_0_0__2",
#                                        "0B11000,__2,<EOF>", 'lexer47'))

#     # float

#     def test48(self):
#         self.assertTrue(TestLexer.test("1.0", "1.0,<EOF>", 'lexer48'))

#     def test49(self):
#         self.assertTrue(TestLexer.test("1.0002", "1.0002,<EOF>", 'lexer49'))

#     def test50(self):
#         self.assertTrue(TestLexer.test(
#             "1_.0435", "1,_,.,0435,<EOF>", 'lexer50'))

#     def test51(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test(
#             "23_32._312", "2332.,_312,<EOF>", 'lexer51'))

#     def test52(self):
#         self.assertTrue(TestLexer.test(
#             "123_2.34_54", "1232.34,_54,<EOF>", 'lexer52'))

#     def test53(self):
#         self.assertTrue(TestLexer.test(
#             "4.50_0_0_0", "4.50,_0_0_0,<EOF>", 'lexer53'))

#     def test54(self):
#         """test integers"""
#         self.assertTrue(TestLexer.test(
#             "00.3423", "00,.,3423,<EOF>", 'lexer54'))

#     def test55(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("1e-2", "1e-2,<EOF>", 'lexer55'))

#     def test56(self):
#         self.assertTrue(TestLexer.test(
#             "1__323e+23", "1,__323e,+,23,<EOF>", 'lexer56'))

#     def test57(self):
#         self.assertTrue(TestLexer.test("23e_21", "23,e_21,<EOF>", 'lexer57'))

#     def test58(self):
#         self.assertTrue(TestLexer.test("56e32_", "56e32,_,<EOF>", 'lexer58'))

#     def test59(self):
#         self.assertTrue(TestLexer.test("23e2_4", "23e2,_4,<EOF>", 'lexer59'))

#     def test60(self):
#         self.assertTrue(TestLexer.test("26e0", "26e0,<EOF>", 'lexer60'))

#     def test61(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("63e001", "63e001,<EOF>", 'lexer61'))

#     def test62(self):
#         self.assertTrue(TestLexer.test(
#             "63e00_01", "63e00,_01,<EOF>", 'lexer62'))

#     def test63(self):
#         self.assertTrue(TestLexer.test(".12e33", ".12e33,<EOF>", 'lexer63'))

#     def test64(self):
#         """test integers"""
#         self.assertTrue(TestLexer.test(".34e", ".,34,e,<EOF>", 'lexer64'))

#     def test65(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test(
#             ".0002e1", ".0002e1,<EOF>", 'lexer65'))

#     def test66(self):
#         self.assertTrue(TestLexer.test(".23_e3", ".,23,_e3,<EOF>", 'lexer66'))

#     def test67(self):
#         self.assertTrue(TestLexer.test("2_3_5.6_3e+3_4",
#                                        "235.6,_3e,+,34,<EOF>", 'lexer67'))

#     def test68(self):
#         self.assertTrue(TestLexer.test(
#             "235.43e+_34", "235.43,e,+,_34,<EOF>", 'lexer68'))

#     def test69(self):
#         self.assertTrue(TestLexer.test("0076_003e0001",
#                                        "00,76003e0001,<EOF>", 'lexer69'))

#     # str
#     def test70(self):
#         self.assertTrue(TestLexer.test("\"sasd\"", "sasd,<EOF>", 'lexer70'))

#     def test71(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test(
#             "\"sa \t sd\"", "sa \t sd,<EOF>", 'lexer71'))

#     def test72(self):
#         self.assertTrue(TestLexer.test("\"sa v\n sgtr \b sd\"",
#                                        "Unclosed String: sa v", 'lexer72'))

#     def test73(self):
#         self.assertTrue(TestLexer.test("\"sa v \\n sgtr \b sd\"",
#                                        "sa v \\n sgtr \b sd,<EOF>", 'lexer73'))

#     def test74(self):
#         """test integers"""
#         self.assertTrue(TestLexer.test("\"sa v \\n  \\r sgtr \b sd\"",
#                                        "sa v \\n  \\r sgtr \b sd,<EOF>", 'lexer74'))

#     def test75(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\"This is a string containing tab \\t\"",
#                                        "This is a string containing tab \\t,<EOF>", 'lexer75'))

#     def test76(self):
#         self.assertTrue(TestLexer.test("\"asd \r gfd \"",
#                                        "Unclosed String: asd ", 'lexer76'))

#     def test77(self):
#         self.assertTrue(TestLexer.test("\"asdadf13^$s\n sdfwwr \"",
#                                        "Unclosed String: asdadf13^$s", 'lexer77'))

#     def test78(self):
#         self.assertTrue(TestLexer.test("\"9345jmb..ds/\'",
#                                        "Unclosed String: 9345jmb..ds/'", 'lexer78'))

#     def test79(self):
#         self.assertTrue(TestLexer.test("\"\' sdfsdf\"",
#                                        "' sdfsdf,<EOF>", 'lexer79'))

#     def test80(self):
#         self.assertTrue(TestLexer.test(
#             "\" dsfgsdf", "Unclosed String:  dsfgsdf", 'lexer80'))

#     def test81(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("\" 45 \\b dfsd \\c",
#                                        "Illegal Escape In String:  45 \\b dfsd \c", 'lexer81'))

#     def test82(self):
#         self.assertTrue(TestLexer.test("\" as \r gnbvcv \"",
#                                        "Unclosed String:  as ", 'lexer82'))

#     def test83(self):
#         self.assertTrue(TestLexer.test("\" hbnnd \n deqa \"",
#                                        "Unclosed String:  hbnnd ", 'lexer83'))

#     def test84(self):
#         """test integers"""
#         self.assertTrue(TestLexer.test(
#             "\" d \" \"", " d ,Unclosed String: ", 'lexer84'))

#     def test85(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test(
#             "\" o90p\" \"56 \"", " o90p,56 ,<EOF>", 'lexer85'))

#     def test86(self):
#         self.assertTrue(TestLexer.test("\" d \'5 \"",
#                                        " d '5 ,<EOF>", 'lexer86'))

#     def test87(self):
#         self.assertTrue(TestLexer.test("\" rt \\ aa \"",
#                                        "Illegal Escape In String:  rt \\ ", 'lexer87'))

#     def test88(self):
#         self.assertTrue(TestLexer.test("\" s \'\" d\" \"",
#                                        " s '\" d,Unclosed String: ", 'lexer88'))

#     def test89(self):
#         self.assertTrue(TestLexer.test("\" nvbtr \\ dfsd",
#                                        "Illegal Escape In String:  nvbtr \\ ", 'lexer89'))

#     def test90(self):
#         self.assertTrue(TestLexer.test(
#             "\"hjhh \n \"", "Unclosed String: hjhh ", 'lexer90'))

#     def test91(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("~", "Error Token ~", 'lexer91'))

#     def test92(self):
#         self.assertTrue(TestLexer.test("\"", "Unclosed String: ", 'lexer92'))

#     def test93(self):
#         self.assertTrue(TestLexer.test("\'", "Error Token \'", 'lexer93'))

#     def test94(self):
#         """test integers"""
#         self.assertTrue(TestLexer.test("\\", "Error Token \\", 'lexer94'))

#     def test95(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.test("^", "Error Token ^", 'lexer95'))

#     def test96(self):
#         self.assertTrue(TestLexer.test("$", "Error Token $", 'lexer96'))

#     def test97(self):
#         self.assertTrue(TestLexer.test(
#             "\"\"\"\"\"", ",,Unclosed String: ", 'lexer97'))

#     def test98(self):
#         self.assertTrue(TestLexer.test("``", "Error Token `", 'lexer98'))

#     def test99(self):
#         self.assertTrue(TestLexer.test("aVs_234", "aVs_234,<EOF>", 'lexer99'))

#     def test100(self):
#         self.assertTrue(TestLexer.test("/*", "/,*,<EOF>", 'lexer100'))

#     def test101(self):
#         self.assertTrue(TestLexer.test("\"asd '\" ", "Unclosed String: asd '\" ", 'lexer101'))

#     def test102(self):
#         self.assertTrue(TestLexer.test("\"aa\\bb", "Unclosed String: aa\\bb", 'lexer102'))
    
#     def test103(self):
#         self.assertTrue(TestLexer.test("\"asd \\a \\b\\c \"", "Illegal Escape In String: asd \\a", 'lexer103'))

#     def test104(self):
#         self.assertTrue(TestLexer.test("\"aa\\pp", "Illegal Escape In String: aa\\p", 'lexer104'))

#     def test105(self):
#         self.assertTrue(TestLexer.test(""" "abc \\h def " ""","""Illegal Escape In String: abc \\h""",'lexer105'))
    
#     def test106(self):
#         self.assertTrue(TestLexer.test(""" " abc \h def " ""","""Illegal Escape In String:  abc \\h""",'lexer106'))
        
#     def test107(self):
#         self.assertTrue(TestLexer.test(''' "Hello\\a ''',"Illegal Escape In String: Hello\\a",'lexer107'))

#     def test108(self):
#         input = """ "asd\bffg" """
#         output = """asd\bffg,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,'lexer108'))

#     def test109(self):
#         input = """ "aa\nn" """
#         output = """Unclosed String: aa"""
#         self.assertTrue(TestLexer.test(input,output,'lexer109'))

#     def test110(self):
#         input = """ 1.e5 """
#         output = """1.e5,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,'lexer110'))

#     def test111(self):
#         input = """ 1.0000000 """
#         output = """1.0000000,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,'lexer111'))

#     def test112(self):
#         input = """ 1.00e2_4 """
#         output = """1.00e2,_4,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,'lexer112'))

#     def test113(self):
#         input = """.."""
#         output = """.,.,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,'lexer113'))
    
#     def test114(self):
#         input = """ContructorDestructorClassSelf"""
#         output = """ContructorDestructorClassSelf,<EOF>"""
#         self.assertTrue(TestLexer.test(input,output,'lexer114'))

#     def test115(self):
#         test = """ "k \n" """
#         expect = """Unclosed String: k """
#         self.assertTrue(TestLexer.test(test, expect, 'lexer115'))

#     def test116(self):
#         test = """ "h\ng" """
#         expect = """Unclosed String: h"""
#         self.assertTrue(TestLexer.test(test, expect, 'lexer116'))

import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def testLexer1(self):
        input = '''##Test comment\a\b\c\d\s\e\r\g##'''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 1))

    def testLexer2(self):
        input = '''abc'''
        expect = '''abc,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 2))

    def testLexer3(self):
        input = '''_acbd'''
        expect = '''_acbd,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 3))

    def testLexer4(self):
        input = '''9abc'''
        expect = '''9,abc,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 4))

    def testLexer5(self):
        input = '''0x123'''
        expect = '''0x123,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 5))

    def testLexer6(self):
        input = '''1_2_3_4'''
        expect = '''1234,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 6))

    def testLexer7(self):
        input = '''1__234'''
        expect = '''1,__234,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 7))

    def testLexer8(self):
        input = '''0123'''
        expect = '''0123,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 8))

    def testLexer9(self):
        input = '''0b1101'''
        expect = '''0b1101,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 9))

    def testLexer10(self):
        input = '''0xABCD'''
        expect = '''0xABCD,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 10))

    def testLexer11(self):
        input = '''"test string"'''
        expect = '''test string,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 11))

    def testLexer12(self):
        input = '''"test string'"'''
        expect = '''Unclosed String: test string\'"'''
        self.assertTrue(TestLexer.test(input, expect, 12))

    def testLexer13(self):
        input = '''"test string""'''
        expect = '''test string,Unclosed String: '''
        self.assertTrue(TestLexer.test(input, expect, 13))

    def testLexer14(self):
        input = '''"test string'''
        expect = '''Unclosed String: test string'''
        self.assertTrue(TestLexer.test(input, expect, 14))

    def testLexer15(self):
        input = '''"anh\n"'''
        expect = '''Unclosed String: anh'''
        self.assertTrue(TestLexer.test(input, expect, 15))

    def testLexer16(self):
        input = '''"abc\\t'''
        expect = '''Unclosed String: abc\\t'''
        self.assertTrue(TestLexer.test(input, expect, 16))

    def testLexer17(self):
        input = '''"hello\\a\\b\\c"'''
        expect = '''Illegal Escape In String: hello\\a'''
        self.assertTrue(TestLexer.test(input, expect, 17))

    def testLexer18(self):
        input = '''"Hello\\h'''
        expect = '''Illegal Escape In String: Hello\\h'''
        self.assertTrue(TestLexer.test(input, expect, 18))

    def testLexer19(self):
        input = '''"asd\bffg"'''
        expect = '''asd\bffg,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 19))

    def testLexer20(self):
        input = '''"anh\ndz"'''
        expect = '''Unclosed String: anh'''
        self.assertTrue(TestLexer.test(input, expect, 20))

    def testLexer21(self):
        input = '''0'''
        expect = '''0,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 21))

    def testLexer22(self):
        input = '''00'''
        expect = '''00,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 22))

    def testLexer23(self):
        input = '''0x0'''
        expect = '''0x0,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 23))

    def testLexer24(self):
        input = '''0b0'''
        expect = '''0b0,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 24))

    def testLexer25(self):
        input = '''000'''
        expect = '''00,0,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 25))

    def testLexer26(self):
        input = '''0012_3'''
        expect = '''00,123,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 26))

    def testLexer27(self):
        input = '''0B012_3_4'''
        expect = '''0B0,1234,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 27))

    def testLexer28(self):
        input = '''0x0ABC_D'''
        expect = '''0x0,ABC_D,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 28))

    def testLexer29(self):
        input = '''1.'''
        expect = '''1.,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 29))

    def testLexer30(self):
        input = '''1.2'''
        expect = '''1.2,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 30))

    def testLexer31(self):
        input = '''12_3.04'''
        expect = '''123.04,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 31))

    def testLexer32(self):
        input = '''1e8'''
        expect = '''1e8,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 32))

    def testLexer33(self):
        input = '''.E3'''
        expect = '''.E3,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 33))

    def testLexer34(self):
        input = '''1.2e9'''
        expect = '''1.2e9,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 34))

    def testLexer35(self):
        input = '''1.E3'''
        expect = '''1.E3,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 35))

    def testLexer36(self):
        input = '''.e-2'''
        expect = '''.e-2,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 36))

    def testLexer37(self):
        input = '''.e22e3'''
        expect = '''.e22,e3,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 37))

    def testLexer38(self):
        input = '''$abc'''
        expect = '''$abc,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 38))

    def testLexer39(self):
        input = '''$_abcd'''
        expect = '''$_abcd,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 39))

    def testLexer40(self):
        input = '''$'''
        expect = '''Error Token $'''
        self.assertTrue(TestLexer.test(input, expect, 40))

    def testLexer41(self):
        input = '''$9'''
        expect = '''$9,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 41))

    def testLexer42(self):
        input = '''Break Continue If Elseif Else'''
        expect = '''Break,Continue,If,Elseif,Else,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 42))

    def testLexer43(self):
        input = '''Foreach True False Array In'''
        expect = '''Foreach,True,False,Array,In,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 43))

    def testLexer44(self):
        input = '''Int Float Boolean String Return'''
        expect = '''Int,Float,Boolean,String,Return,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 44))

    def testLexer45(self):
        input = '''Null Class Val Var Self Constructor Destructor New By'''
        expect = '''Null,Class,Val,Var,Self,Constructor,Destructor,New,By,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 45))

    def testLexer46(self):
        input = '''IfElse'''
        expect = '''IfElse,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 46))

    def testLexer47(self):
        input = '''TrueFalse'''
        expect = '''TrueFalse,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 47))

    def testLexer48(self):
        input = '''+ - * /'''
        expect = '''+,-,*,/,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 48))

    def testLexer49(self):
        input = '''! && || == = &'''
        expect = '''!,&&,||,==,=,Error Token &'''
        self.assertTrue(TestLexer.test(input, expect, 49))

    def testLexer50(self):
        input = '''!= < <= > >= <=='''
        expect = '''!=,<,<=,>,>=,<=,=,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 50))

    def testLexer51(self):
        input = '''==. +. . ::'''
        expect = '''==.,+.,.,::,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 51))

    def testLexer52(self):
        input = '''<<==.'''
        expect = '''<,<=,=,.,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 52))

    def testLexer53(self):
        input = '''()[],;:{}'''
        expect = '''(,),[,],,,;,:,{,},<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 53))

    def testLexer54(self):
        input = '''##'''
        expect = '''Error Token #'''
        self.assertTrue(TestLexer.test(input, expect, 54))

    def testLexer55(self):
        input = '''###'''
        expect = '''Error Token #'''
        self.assertTrue(TestLexer.test(input, expect, 55))

    def testLexer56(self):
        input = '''#'''
        expect = '''Error Token #'''
        self.assertTrue(TestLexer.test(input, expect, 56))

    def testLexer57(self):
        input = '''#####'''
        expect = '''Error Token #'''
        self.assertTrue(TestLexer.test(input, expect, 57))

    def testLexer58(self):
        input = '''""'''
        expect = ''',<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 58))

    def testLexer59(self):
        input = '''"'\\b\\f\\r\\n\\t\\\\"'''
        expect = ''''\\b\\f\\r\\n\\t\\\\,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 59))

    def testLexer60(self):
        input = '''0x_123'''
        expect = '''0,x_123,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 60))

    def testLexer61(self):
        input = '''0_123'''
        expect = '''0,_123,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 61))

    def testLexer62(self):
        input = '''3*4/2-9'''
        expect = '''3,*,4,/,2,-,9,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 62))

    def testLexer63(self):
        input = '''Var length, width: Int = 1, 5;'''
        expect = '''Var,length,,,width,:,Int,=,1,,,5,;,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 63))

    def testLexer64(self):
        input = '''If(3<4 && 2 || 1 && 3)'''
        expect = '''If,(,3,<,4,&&,2,||,1,&&,3,),<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 64))

    def testLexer65(self):
        input = '''"abc\f"'''
        expect = '''abc\f,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 65))

    def testLexer66(self):
        input = '''"abc\t'''
        expect = '''Unclosed String: abc\t'''
        self.assertTrue(TestLexer.test(input, expect, 66))

    def testLexer67(self):
        input = '''"abc\\'''
        expect = '''Illegal Escape In String: abc\\'''
        self.assertTrue(TestLexer.test(input, expect, 67))

    def testLexer68(self):
        input = '''1.3_4_5_6'''
        expect = '''1.3,_4_5_6,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 68))

    def testLexer69(self):
        input = '''1.3_456e9'''
        expect = '''1.3,_456e9,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 69))

    def testLexer70(self):
        input = '''1.2_345e-9'''
        expect = '''1.2,_345e,-,9,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 70))

    def testLexer71(self):
        input = '''"test'1"'''
        expect = '''test'1,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 71))

    def testLexer72(self):
        input = '''1_2_3_'''
        expect = '''123,_,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 72))

    def testLexer73(self):
        input = '''\b'''
        expect = '''Error Token \b'''
        self.assertTrue(TestLexer.test(input, expect, 73))

    def testLexer74(self):
        input = '''\f'''
        expect = '''Error Token \f'''
        self.assertTrue(TestLexer.test(input, expect, 74))

    def testLexer75(self):
        input = '''\r'''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 75))

    def testLexer76(self):
        input = '''Array[Int, 5]'''
        expect = '''Array,[,Int,,,5,],<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 76))

    def testLexer77(self):
        input = '''\''''
        expect = '''Error Token \''''
        self.assertTrue(TestLexer.test(input, expect, 77))

    def testLexer78(self):
        input = '''\\'''
        expect = '''Error Token \\'''
        self.assertTrue(TestLexer.test(input, expect, 78))

    def testLexer79(self):
        input = '''"Hi! '"Vanh'""'''
        expect = '''Hi! '"Vanh'",<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 79))

    def testLexer80(self):
        input = '''"string\\n'''
        expect = '''Unclosed String: string\\n'''
        self.assertTrue(TestLexer.test(input, expect, 80))

    def testLexer81(self):
        input = '''"string\\a\\e\\r'''
        expect = '''Illegal Escape In String: string\\a'''
        self.assertTrue(TestLexer.test(input, expect, 81))

    def testLexer82(self):
        input = '''"string\'\'\'\'\'"""""""'''
        expect = '''string\'\'\'\'\'",,,Unclosed String: '''
        self.assertTrue(TestLexer.test(input, expect, 82))

    def testLexer83(self):
        input = '''"###11223#"'''
        expect = '''###11223#,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 83))

    def testLexer84(self):
        input = '''"##1234##"'''
        expect = '''##1234##,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 84))

    def testLexer85(self):
        input = '''##\a\b\c\d\e\f\h\g\i\k\l\m\n\o\r\p\q\s\e\t\r\\x##'''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 85))

    def testLexer86(self):
        input = '''<EOF>'''
        expect = '''<,EOF,>,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 86))

    def testLexer87(self):
        input = '''D96'''
        expect = '''D96,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 87))

    def testLexer88(self):
        input = '''1.000000'''
        expect = '''1.000000,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 88))

    def testLexer89(self):
        input = '''.00000e+9'''
        expect = '''.00000e+9,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 89))

    def testLexer90(self):
        input = '''0.0e-3'''
        expect = '''0.0e-3,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 90))

    def testLexer91(self):
        input = '''00.0000'''
        expect = '''00,.,00,00,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 91))

    def testLexer92(self):
        input = '''01.0010'''
        expect = '''01,.,00,10,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 92))

    def testLexer93(self):
        input = '''01.0_010'''
        expect = '''01,.,0,_010,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 93))

    def testLexer94(self):
        input = '''0b1230x123'''
        expect = '''0b1,230,x123,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 94))

    def testLexer95(self):
        input = '''00109-0x0100b1010_921'''
        expect = '''00,109,-,0x0,100,b1010_921,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 95))

    def testLexer96(self):
        input = '''1.2.3.4.5.6.7.8'''
        expect = '''1.2,.,3.4,.,5.6,.,7.8,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 96))

    def testLexer97(self):
        input = '''.e+9-0b1001.3e9'''
        expect = '''.e+9,-,0b1001,.3e9,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 97))

    def testLexer98(self):
        input = '''0b1.9.120X0010001'''
        expect = '''0b1,.,9.120,X0010001,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 98))

    def testLexer99(self):
        input = '''0x0x0x0x000x0x0x00x0x0xx1'''
        expect = '''0x0,x0x0x000x0x0x00x0x0xx1,<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 99))

    def testLexer100(self):
        input = '''##nguyen viet anh-1912602##'''
        expect = '''<EOF>'''
        self.assertTrue(TestLexer.test(input, expect, 100))
