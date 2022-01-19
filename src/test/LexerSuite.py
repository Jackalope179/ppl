import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # Test comment  ANTLR
    def test1(self):
        self.assertTrue(TestLexer.test("##Hello","Error Token #",1))  

    def test2(self):
        self.assertTrue(TestLexer.test("##Hello##","<EOF>",2))  

    def test3(self):
        self.assertTrue(TestLexer.test("##Hello\nHello##","<EOF>",3))

    def test4(self):
        self.assertTrue(TestLexer.test("#Hello\n#Hello","Error Token #",4))

    '''Check normal ID'''
    def test5(self):
        self.assertTrue(TestLexer.test("Hello","Hello,<EOF>",5))
    
    def test6(self):
        self.assertTrue(TestLexer.test("_Hello","_Hello,<EOF>",6))

    def test7(self):
        self.assertTrue(TestLexer.test("_Hello_","_Hello_,<EOF>",7))

    def test8(self):
        self.assertTrue(TestLexer.test("_Hello_123","_Hello_123,<EOF>",8))

    def test9(self):
        self.assertTrue(TestLexer.test("$0_Hello_123_","$0_Hello_123_,<EOF>",9))

    ''' Check Static ID'''
    def test10(self):
        self.assertTrue(TestLexer.test("$","Error Token $",10))

    def test16(self):
        self.assertTrue(TestLexer.test("$0_123_4_5","$0_123_4_5,<EOF>",16))

    def test11(self):
        self.assertTrue(TestLexer.test("$0","$0,<EOF>",11))

    '''Check integer'''
    def test12(self):
        self.assertTrue(TestLexer.test("123","123,<EOF>",12))

    def test13(self):
        self.assertTrue(TestLexer.test("0","0,<EOF>",13))
        
    def test14(self):
        self.assertTrue(TestLexer.test("_123","_123,<EOF>",14))
    
    def test15(self):
        self.assertTrue(TestLexer.test("123_4_5","12345,<EOF>",15))

    def test17(self):
        self.assertTrue(TestLexer.test("0123","0123,<EOF>",17))

    def test18(self):
        self.assertTrue(TestLexer.test("0x_12_3","0,x_12_3,<EOF>",18))

    def test19(self):
        self.assertTrue(TestLexer.test("0x1_2a_3b_f","0x12,a_3b_f,<EOF>",19))

    def test20(self):
        self.assertTrue(TestLexer.test("0b1111","0b1111,<EOF>",20))

    def test21(self):
        self.assertTrue(TestLexer.test("0b111__11","0b111,__11,<EOF>",21))
    
    ''' Check Float'''
    def test22(self):
        self.assertTrue(TestLexer.test("1.234","1.234,<EOF>",22))

    def test23(self):
        self.assertTrue(TestLexer.test("1.234e5","1.234e5,<EOF>",23))
    
    def test24(self):
        self.assertTrue(TestLexer.test("1.234e-5","1.234e-5,<EOF>",24))

    def test25(self):
        self.assertTrue(TestLexer.test("7E-10","7E-10,<EOF>",25))

    def test26(self):
        self.assertTrue(TestLexer.test("1_234.567","1234.567,<EOF>",26))
    
    def test27(self):
        self.assertTrue(TestLexer.test("0x56.567e-10","0x56,.567e-10,<EOF>",27))

    def test28(self):
        self.assertTrue(TestLexer.test("0x56.567e-10_","0x56,.567e-10,_,<EOF>",28))
    
    def test29(self):
        self.assertTrue(TestLexer.test("1.e123_56","1.e12356,<EOF>",29))

    def test30(self):
        self.assertTrue(TestLexer.test(".0123",".,0123,<EOF>",30))
    
    def test31(self):
        self.assertTrue(TestLexer.test(".123",".,123,<EOF>",31))

    def test32(self):
        self.assertTrue(TestLexer.test("e135","e135,<EOF>",32))

    def test33(self):
        self.assertTrue(TestLexer.test("0.12_5e-120","0.125e-120,<EOF>",33))

    def test34(self):
        self.assertTrue(TestLexer.test("00.12_5e-120","00,.125e-120,<EOF>",34))
    
    def test35(self):
        self.assertTrue(TestLexer.test("00123","00123,<EOF>",35))

    def test36(self):
        self.assertTrue(TestLexer.test("00","00,<EOF>",36))

    def test37(self):
        self.assertTrue(TestLexer.test("12.00001","12.0,0001,<EOF>",37))

    def test38(self):
        self.assertTrue(TestLexer.test("08123","08123,<EOF>",38))

    def test39(self):
        self.assertTrue(TestLexer.test("0x123n",",<EOF>",39))

    
    def test_invalid_float(self):
        self.assertTrue(TestLexer.test(".0123 e135 00.12_5e-120 0x12ab", ".,0123,e135,00,.125e-120,0x12,ab,<EOF>", 110))

    ''' Test String'''
    def test39(self):
        self.assertTrue(TestLexer.test("\"Hello\"","Hello,<EOF>",39))
    
    def test40(self):
        self.assertTrue(TestLexer.test("\"Hello\\n\"","Hello\\n,<EOF>",40))

    def test41(self):
        self.assertTrue(TestLexer.test('''"This is a string containing tab \\t"''',"This is a string containing tab \\t,<EOF>",41))
    
    def test42(self):
        self.assertTrue(TestLexer.test('''"This is a string containing backslash \\\\"''',"This is a string containing backslash \\\\,<EOF>",42))

    def test43(self):
        self.assertTrue(TestLexer.test(''' "Test case string '"" ''','''Test case string '",<EOF>''',43))

    def test44(self):
        self.assertTrue(TestLexer.test(''' "Test case string "" ''',",<EOF>",44)) 
    
    def test44(self):
        self.assertTrue(TestLexer.test(''' "Test case string '" ''',"Test case string ',<EOF>",55))



    def test45(self):
        self.assertTrue(TestLexer.test('''"Test case \n string "''',",<EOF>",46))
    '''Test error'''
    def test45(self):
        self.assertTrue(TestLexer.test(''' "Hello\\a ''',"Unclosed String: Hello\\a ",45))

    def test46(self):
        self.assertTrue(TestLexer.test(''' "Hello\nHello new line "''',"Unclosed String: Hello",46))
    
    def test47(self):
        self.assertTrue(TestLexer.test(''' "abc\\h def" ''',"Illegal Escape In String: abc\\h",47))
    
    def test48(self):
        self.assertTrue(TestLexer.test(''' "Hello new line "" ''',"Hello new line ,Unclosed String:  ",48))

    def test49(self):
        self.assertTrue(TestLexer.test(''' "Hello new line ""\n"''',"Hello new line ,Unclosed String: ",49))

    def test50(self):
        self.assertTrue(TestLexer.test(''' "Hello new line ""abc\n''',"Hello new line ,Unclosed String: abc",50))
    
    # def test51(self):
    #     self.assertTrue(TestLexer.test(''' "Hello new line \\a\\b\\c"''',"Illegal Escape In String: Hello new line \\a",51))
    
    def test52(self):
        self.assertTrue(TestLexer.test(''' " Hello new line \\\ "''' ,''' Hello new line \\\\ ,<EOF>''',52))
    
    def test53(self):
        self.assertTrue(TestLexer.test(''' " Hello new line \\\\ "''' ," Hello new line \\\\ ,<EOF>",53))
    
    def test54(self):
        self.assertTrue(TestLexer.test(''' " Hello new line \\\"''' ,"Illegal Escape In String:  Hello new line \\\"",54))
    
    # def test_lowercase_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test(".0123","abc,<EOF>",1))
    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.test("e135","aCBbdc,<EOF>",102))
    # def test_mixed_id(self):
    #     self.assertTrue(TestLexer.test("00.125e-120","aAsVN,3,<EOF>",103))
    # def test_mixed_id1(self):
    #     self.assertTrue(TestLexer.test("##khang","aAsVN,3,<EOF>",104))
    # def test_mixed_id2(self):
    #     self.assertTrue(TestLexer.test("123.","aAsVN,3,<EOF>",105))
    # def test_mixed_id3(self):
    #     self.assertTrue(TestLexer.test("##Hello##.","aAsVN,3,<EOF>",106))
    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",107))
