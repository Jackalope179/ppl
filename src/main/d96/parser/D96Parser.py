# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K")
        buf.write("\u0109\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\6\2F\n\2\r\2\16\2G")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4V")
        buf.write("\n\4\3\5\3\5\3\5\3\5\5\5\\\n\5\3\6\3\6\5\6`\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\bn\n\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\5\tu\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u008d\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\5\20\u00a4\n\20\3\21\3\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00af\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\5\24\u00b8\n\24\3\25\3")
        buf.write("\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\5\31\u00d6\n\31\3\32\3\32\3")
        buf.write("\32\5\32\u00db\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\5\34\u00ed")
        buf.write("\n\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\5\"\u0107")
        buf.write("\n\"\3\"\2\2#\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<>@B\2\3\3\2\"#\2\u00fb\2E\3\2\2")
        buf.write("\2\4K\3\2\2\2\6U\3\2\2\2\b[\3\2\2\2\n_\3\2\2\2\fa\3\2")
        buf.write("\2\2\16m\3\2\2\2\20t\3\2\2\2\22v\3\2\2\2\24|\3\2\2\2\26")
        buf.write("\u0082\3\2\2\2\30\u008c\3\2\2\2\32\u008e\3\2\2\2\34\u0096")
        buf.write("\3\2\2\2\36\u00a3\3\2\2\2 \u00a5\3\2\2\2\"\u00ae\3\2\2")
        buf.write("\2$\u00b0\3\2\2\2&\u00b7\3\2\2\2(\u00b9\3\2\2\2*\u00bb")
        buf.write("\3\2\2\2,\u00bd\3\2\2\2.\u00bf\3\2\2\2\60\u00d5\3\2\2")
        buf.write("\2\62\u00da\3\2\2\2\64\u00dc\3\2\2\2\66\u00ec\3\2\2\2")
        buf.write("8\u00ee\3\2\2\2:\u00f0\3\2\2\2<\u00f3\3\2\2\2>\u00f6\3")
        buf.write("\2\2\2@\u00fa\3\2\2\2B\u0106\3\2\2\2DF\5\4\3\2ED\3\2\2")
        buf.write("\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\7\2\2\3J")
        buf.write("\3\3\2\2\2KL\7!\2\2LM\7\16\2\2MN\5\6\4\2NO\7>\2\2OP\5")
        buf.write("\b\5\2PQ\7?\2\2Q\5\3\2\2\2RS\7C\2\2SV\7\16\2\2TV\3\2\2")
        buf.write("\2UR\3\2\2\2UT\3\2\2\2V\7\3\2\2\2WX\5\n\6\2XY\5\b\5\2")
        buf.write("Y\\\3\2\2\2Z\\\5\n\6\2[W\3\2\2\2[Z\3\2\2\2\\\t\3\2\2\2")
        buf.write("]`\5\f\7\2^`\5\22\n\2_]\3\2\2\2_^\3\2\2\2`\13\3\2\2\2")
        buf.write("ab\t\2\2\2bc\5\16\b\2cd\7C\2\2de\7F\2\2ef\7)\2\2fg\5\20")
        buf.write("\t\2gh\7D\2\2h\r\3\2\2\2ij\7\16\2\2jk\7B\2\2kn\5\16\b")
        buf.write("\2ln\7\16\2\2mi\3\2\2\2ml\3\2\2\2n\17\3\2\2\2op\5,\27")
        buf.write("\2pq\7B\2\2qr\5\20\t\2ru\3\2\2\2su\5,\27\2to\3\2\2\2t")
        buf.write("s\3\2\2\2u\21\3\2\2\2vw\7\16\2\2wx\7<\2\2xy\5\30\r\2y")
        buf.write("z\7=\2\2z{\5B\"\2{\23\3\2\2\2|}\7$\2\2}~\7<\2\2~\177\5")
        buf.write("\30\r\2\177\u0080\7=\2\2\u0080\u0081\5B\"\2\u0081\25\3")
        buf.write("\2\2\2\u0082\u0083\7%\2\2\u0083\u0084\7<\2\2\u0084\u0085")
        buf.write("\7=\2\2\u0085\u0086\5B\"\2\u0086\27\3\2\2\2\u0087\u0088")
        buf.write("\5\16\b\2\u0088\u0089\7C\2\2\u0089\u008a\7F\2\2\u008a")
        buf.write("\u008d\3\2\2\2\u008b\u008d\3\2\2\2\u008c\u0087\3\2\2\2")
        buf.write("\u008c\u008b\3\2\2\2\u008d\31\3\2\2\2\u008e\u008f\7#\2")
        buf.write("\2\u008f\u0090\5\36\20\2\u0090\u0091\7C\2\2\u0091\u0092")
        buf.write("\7F\2\2\u0092\u0093\7)\2\2\u0093\u0094\5\20\t\2\u0094")
        buf.write("\u0095\7D\2\2\u0095\33\3\2\2\2\u0096\u0097\7\"\2\2\u0097")
        buf.write("\u0098\5\36\20\2\u0098\u0099\7C\2\2\u0099\u009a\7F\2\2")
        buf.write("\u009a\u009b\7)\2\2\u009b\u009c\5\20\t\2\u009c\u009d\7")
        buf.write("D\2\2\u009d\35\3\2\2\2\u009e\u009f\5 \21\2\u009f\u00a0")
        buf.write("\7B\2\2\u00a0\u00a1\5\36\20\2\u00a1\u00a4\3\2\2\2\u00a2")
        buf.write("\u00a4\5 \21\2\u00a3\u009e\3\2\2\2\u00a3\u00a2\3\2\2\2")
        buf.write("\u00a4\37\3\2\2\2\u00a5\u00a6\7\17\2\2\u00a6!\3\2\2\2")
        buf.write("\u00a7\u00af\5$\23\2\u00a8\u00af\5.\30\2\u00a9\u00af\5")
        buf.write("\64\33\2\u00aa\u00af\5> \2\u00ab\u00af\5\32\16\2\u00ac")
        buf.write("\u00af\5\34\17\2\u00ad\u00af\5@!\2\u00ae\u00a7\3\2\2\2")
        buf.write("\u00ae\u00a8\3\2\2\2\u00ae\u00a9\3\2\2\2\u00ae\u00aa\3")
        buf.write("\2\2\2\u00ae\u00ab\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad")
        buf.write("\3\2\2\2\u00af#\3\2\2\2\u00b0\u00b1\5&\24\2\u00b1\u00b2")
        buf.write("\7)\2\2\u00b2\u00b3\5,\27\2\u00b3\u00b4\7D\2\2\u00b4%")
        buf.write("\3\2\2\2\u00b5\u00b8\5(\25\2\u00b6\u00b8\5*\26\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\'\3\2\2\2\u00b9")
        buf.write("\u00ba\7\16\2\2\u00ba)\3\2\2\2\u00bb\u00bc\5,\27\2\u00bc")
        buf.write("+\3\2\2\2\u00bd\u00be\7\3\2\2\u00be-\3\2\2\2\u00bf\u00c0")
        buf.write("\7\23\2\2\u00c0\u00c1\7<\2\2\u00c1\u00c2\5,\27\2\u00c2")
        buf.write("\u00c3\7=\2\2\u00c3\u00c4\5B\"\2\u00c4\u00c5\5\60\31\2")
        buf.write("\u00c5\u00c6\5\62\32\2\u00c6/\3\2\2\2\u00c7\u00c8\7\24")
        buf.write("\2\2\u00c8\u00c9\7<\2\2\u00c9\u00ca\5,\27\2\u00ca\u00cb")
        buf.write("\7=\2\2\u00cb\u00cc\5B\"\2\u00cc\u00cd\5\60\31\2\u00cd")
        buf.write("\u00d6\3\2\2\2\u00ce\u00cf\7\24\2\2\u00cf\u00d0\7<\2\2")
        buf.write("\u00d0\u00d1\5,\27\2\u00d1\u00d2\7=\2\2\u00d2\u00d3\5")
        buf.write("B\"\2\u00d3\u00d6\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00c7")
        buf.write("\3\2\2\2\u00d5\u00ce\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6")
        buf.write("\61\3\2\2\2\u00d7\u00d8\7\25\2\2\u00d8\u00db\5B\"\2\u00d9")
        buf.write("\u00db\3\2\2\2\u00da\u00d7\3\2\2\2\u00da\u00d9\3\2\2\2")
        buf.write("\u00db\63\3\2\2\2\u00dc\u00dd\7\26\2\2\u00dd\u00de\7<")
        buf.write("\2\2\u00de\u00df\5(\25\2\u00df\u00e0\7\32\2\2\u00e0\u00e1")
        buf.write("\5,\27\2\u00e1\u00e2\7\4\2\2\u00e2\u00e3\5,\27\2\u00e3")
        buf.write("\u00e4\5\66\34\2\u00e4\u00e5\7=\2\2\u00e5\u00e6\7>\2\2")
        buf.write("\u00e6\u00e7\58\35\2\u00e7\u00e8\7?\2\2\u00e8\65\3\2\2")
        buf.write("\2\u00e9\u00ea\7\'\2\2\u00ea\u00ed\5,\27\2\u00eb\u00ed")
        buf.write("\3\2\2\2\u00ec\u00e9\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed")
        buf.write("\67\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef9\3\2\2\2\u00f0\u00f1")
        buf.write("\7\21\2\2\u00f1\u00f2\7D\2\2\u00f2;\3\2\2\2\u00f3\u00f4")
        buf.write("\7\22\2\2\u00f4\u00f5\7D\2\2\u00f5=\3\2\2\2\u00f6\u00f7")
        buf.write("\7\37\2\2\u00f7\u00f8\5,\27\2\u00f8\u00f9\7D\2\2\u00f9")
        buf.write("?\3\2\2\2\u00fa\u00fb\7\16\2\2\u00fb\u00fc\7+\2\2\u00fc")
        buf.write("\u00fd\7\20\2\2\u00fd\u00fe\7<\2\2\u00fe\u00ff\5\20\t")
        buf.write("\2\u00ff\u0100\7=\2\2\u0100\u0101\7D\2\2\u0101A\3\2\2")
        buf.write("\2\u0102\u0103\5\"\22\2\u0103\u0104\5B\"\2\u0104\u0107")
        buf.write("\3\2\2\2\u0105\u0107\5\"\22\2\u0106\u0102\3\2\2\2\u0106")
        buf.write("\u0105\3\2\2\2\u0107C\3\2\2\2\20GU[_mt\u008c\u00a3\u00ae")
        buf.write("\u00b7\u00d5\u00da\u00ec\u0106")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'expr'", "'..'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'\n'", "'='", "'.'", "'::'", "'!'", "'&&'", 
                     "'||'", "'*'", "'/'", "'%'", "'+'", "'-'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'+.'", "'==.'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "':'", 
                     "';'", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NUM_LIT", 
                      "INT_LIT", "OCT_LIT", "HEX_LIT", "BIN_LIT", "DEC_LIT", 
                      "BOOL_LIT", "FLOAT_LIT", "STRING_LIT", "ID", "NON_STATIC_ID", 
                      "STATIC_ID", "BREAK", "CONT", "IF", "ELIF", "ELSE", 
                      "FOREACH", "TRUE", "FALSE", "ARR", "IN", "INT", "FLOAT", 
                      "BOOL", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                      "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "NEWLINE", 
                      "EQUAL", "MA_DOT", "MA_DCOLON", "EXCLA", "D_AND", 
                      "D_OR", "MUL", "DIV", "MOD", "ADD", "SUB", "D_EQUAL", 
                      "DIFF", "LESS", "BIGGER", "LESS_EQUAL", "BIGGER_EQUAL", 
                      "SUB_DOT", "DEQ_DOT", "LB", "RB", "LCB", "RCB", "LSB", 
                      "RSB", "COMMA", "COLON", "SEMI", "UNDER", "TYP", "COMMENT", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_dcl = 1
    RULE_super_class = 2
    RULE_class_body = 3
    RULE_declare = 4
    RULE_attr_dcl = 5
    RULE_id_list = 6
    RULE_expr_list = 7
    RULE_method_dcl = 8
    RULE_constructor_dcl = 9
    RULE_destructor_dcl = 10
    RULE_params = 11
    RULE_var_dcl = 12
    RULE_const_dcl = 13
    RULE_nonstatic_list = 14
    RULE_nonstatic = 15
    RULE_stmt = 16
    RULE_ass_stmt = 17
    RULE_lhs = 18
    RULE_scalar = 19
    RULE_idx_expr = 20
    RULE_expr = 21
    RULE_if_stmt = 22
    RULE_elseif_stmt = 23
    RULE_else_stmt = 24
    RULE_loop_stmt = 25
    RULE_by_stmt = 26
    RULE_loop_body = 27
    RULE_break_stmt = 28
    RULE_cont_stmt = 29
    RULE_return_stmt = 30
    RULE_method_invo_stmt = 31
    RULE_block_stmt = 32

    ruleNames =  [ "program", "class_dcl", "super_class", "class_body", 
                   "declare", "attr_dcl", "id_list", "expr_list", "method_dcl", 
                   "constructor_dcl", "destructor_dcl", "params", "var_dcl", 
                   "const_dcl", "nonstatic_list", "nonstatic", "stmt", "ass_stmt", 
                   "lhs", "scalar", "idx_expr", "expr", "if_stmt", "elseif_stmt", 
                   "else_stmt", "loop_stmt", "by_stmt", "loop_body", "break_stmt", 
                   "cont_stmt", "return_stmt", "method_invo_stmt", "block_stmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NUM_LIT=3
    INT_LIT=4
    OCT_LIT=5
    HEX_LIT=6
    BIN_LIT=7
    DEC_LIT=8
    BOOL_LIT=9
    FLOAT_LIT=10
    STRING_LIT=11
    ID=12
    NON_STATIC_ID=13
    STATIC_ID=14
    BREAK=15
    CONT=16
    IF=17
    ELIF=18
    ELSE=19
    FOREACH=20
    TRUE=21
    FALSE=22
    ARR=23
    IN=24
    INT=25
    FLOAT=26
    BOOL=27
    STRING=28
    RETURN=29
    NULL=30
    CLASS=31
    VAL=32
    VAR=33
    CONSTRUCTOR=34
    DESTRUCTOR=35
    NEW=36
    BY=37
    NEWLINE=38
    EQUAL=39
    MA_DOT=40
    MA_DCOLON=41
    EXCLA=42
    D_AND=43
    D_OR=44
    MUL=45
    DIV=46
    MOD=47
    ADD=48
    SUB=49
    D_EQUAL=50
    DIFF=51
    LESS=52
    BIGGER=53
    LESS_EQUAL=54
    BIGGER_EQUAL=55
    SUB_DOT=56
    DEQ_DOT=57
    LB=58
    RB=59
    LCB=60
    RCB=61
    LSB=62
    RSB=63
    COMMA=64
    COLON=65
    SEMI=66
    UNDER=67
    TYP=68
    COMMENT=69
    WS=70
    ERROR_CHAR=71
    UNCLOSE_STRING=72
    ILLEGAL_ESCAPE=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_dclContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_dclContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.class_dcl()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 71
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def super_class(self):
            return self.getTypedRuleContext(D96Parser.Super_classContext,0)


        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_dcl" ):
                return visitor.visitClass_dcl(self)
            else:
                return visitor.visitChildren(self)




    def class_dcl(self):

        localctx = D96Parser.Class_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(D96Parser.CLASS)
            self.state = 74
            self.match(D96Parser.ID)
            self.state = 75
            self.super_class()
            self.state = 76
            self.match(D96Parser.LCB)
            self.state = 77
            self.class_body()
            self.state = 78
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Super_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_super_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuper_class" ):
                return visitor.visitSuper_class(self)
            else:
                return visitor.visitChildren(self)




    def super_class(self):

        localctx = D96Parser.Super_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_super_class)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(D96Parser.COLON)
                self.state = 81
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare(self):
            return self.getTypedRuleContext(D96Parser.DeclareContext,0)


        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.declare()
                self.state = 86
                self.class_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_dcl(self):
            return self.getTypedRuleContext(D96Parser.Attr_dclContext,0)


        def method_dcl(self):
            return self.getTypedRuleContext(D96Parser.Method_dclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)




    def declare(self):

        localctx = D96Parser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declare)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.attr_dcl()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.method_dcl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def TYP(self):
            return self.getToken(D96Parser.TYP, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_dcl" ):
                return visitor.visitAttr_dcl(self)
            else:
                return visitor.visitChildren(self)




    def attr_dcl(self):

        localctx = D96Parser.Attr_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 96
            self.id_list()
            self.state = 97
            self.match(D96Parser.COLON)
            self.state = 98
            self.match(D96Parser.TYP)
            self.state = 99
            self.match(D96Parser.EQUAL)
            self.state = 100
            self.expr_list()
            self.state = 101
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_id_list)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(D96Parser.ID)
                self.state = 104
                self.match(D96Parser.COMMA)
                self.state = 105
                self.id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr_list)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.expr()
                self.state = 110
                self.match(D96Parser.COMMA)
                self.state = 111
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def params(self):
            return self.getTypedRuleContext(D96Parser.ParamsContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_dcl" ):
                return visitor.visitMethod_dcl(self)
            else:
                return visitor.visitChildren(self)




    def method_dcl(self):

        localctx = D96Parser.Method_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_method_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(D96Parser.ID)
            self.state = 117
            self.match(D96Parser.LB)
            self.state = 118
            self.params()
            self.state = 119
            self.match(D96Parser.RB)
            self.state = 120
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def params(self):
            return self.getTypedRuleContext(D96Parser.ParamsContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_dcl" ):
                return visitor.visitConstructor_dcl(self)
            else:
                return visitor.visitChildren(self)




    def constructor_dcl(self):

        localctx = D96Parser.Constructor_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constructor_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 123
            self.match(D96Parser.LB)
            self.state = 124
            self.params()
            self.state = 125
            self.match(D96Parser.RB)
            self.state = 126
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor_dcl" ):
                return visitor.visitDestructor_dcl(self)
            else:
                return visitor.visitChildren(self)




    def destructor_dcl(self):

        localctx = D96Parser.Destructor_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_destructor_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(D96Parser.DESTRUCTOR)
            self.state = 129
            self.match(D96Parser.LB)
            self.state = 130
            self.match(D96Parser.RB)
            self.state = 131
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def TYP(self):
            return self.getToken(D96Parser.TYP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = D96Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_params)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.id_list()
                self.state = 134
                self.match(D96Parser.COLON)
                self.state = 135
                self.match(D96Parser.TYP)
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def nonstatic_list(self):
            return self.getTypedRuleContext(D96Parser.Nonstatic_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def TYP(self):
            return self.getToken(D96Parser.TYP, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dcl" ):
                return visitor.visitVar_dcl(self)
            else:
                return visitor.visitChildren(self)




    def var_dcl(self):

        localctx = D96Parser.Var_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_var_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(D96Parser.VAR)
            self.state = 141
            self.nonstatic_list()
            self.state = 142
            self.match(D96Parser.COLON)
            self.state = 143
            self.match(D96Parser.TYP)
            self.state = 144
            self.match(D96Parser.EQUAL)
            self.state = 145
            self.expr_list()
            self.state = 146
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def nonstatic_list(self):
            return self.getTypedRuleContext(D96Parser.Nonstatic_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def TYP(self):
            return self.getToken(D96Parser.TYP, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_const_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_dcl" ):
                return visitor.visitConst_dcl(self)
            else:
                return visitor.visitChildren(self)




    def const_dcl(self):

        localctx = D96Parser.Const_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_const_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(D96Parser.VAL)
            self.state = 149
            self.nonstatic_list()
            self.state = 150
            self.match(D96Parser.COLON)
            self.state = 151
            self.match(D96Parser.TYP)
            self.state = 152
            self.match(D96Parser.EQUAL)
            self.state = 153
            self.expr_list()
            self.state = 154
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nonstatic_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonstatic(self):
            return self.getTypedRuleContext(D96Parser.NonstaticContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def nonstatic_list(self):
            return self.getTypedRuleContext(D96Parser.Nonstatic_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_nonstatic_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonstatic_list" ):
                return visitor.visitNonstatic_list(self)
            else:
                return visitor.visitChildren(self)




    def nonstatic_list(self):

        localctx = D96Parser.Nonstatic_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_nonstatic_list)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.nonstatic()
                self.state = 157
                self.match(D96Parser.COMMA)
                self.state = 158
                self.nonstatic_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.nonstatic()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonstaticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NON_STATIC_ID(self):
            return self.getToken(D96Parser.NON_STATIC_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_nonstatic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonstatic" ):
                return visitor.visitNonstatic(self)
            else:
                return visitor.visitChildren(self)




    def nonstatic(self):

        localctx = D96Parser.NonstaticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_nonstatic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(D96Parser.NON_STATIC_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ass_stmt(self):
            return self.getTypedRuleContext(D96Parser.Ass_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def loop_stmt(self):
            return self.getTypedRuleContext(D96Parser.Loop_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def var_dcl(self):
            return self.getTypedRuleContext(D96Parser.Var_dclContext,0)


        def const_dcl(self):
            return self.getTypedRuleContext(D96Parser.Const_dclContext,0)


        def method_invo_stmt(self):
            return self.getTypedRuleContext(D96Parser.Method_invo_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmt)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.ass_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.loop_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.return_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 169
                self.var_dcl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 170
                self.const_dcl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 171
                self.method_invo_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ass_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_ass_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss_stmt" ):
                return visitor.visitAss_stmt(self)
            else:
                return visitor.visitChildren(self)




    def ass_stmt(self):

        localctx = D96Parser.Ass_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ass_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.lhs()
            self.state = 175
            self.match(D96Parser.EQUAL)
            self.state = 176
            self.expr()
            self.state = 177
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar(self):
            return self.getTypedRuleContext(D96Parser.ScalarContext,0)


        def idx_expr(self):
            return self.getTypedRuleContext(D96Parser.Idx_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lhs)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.scalar()
                pass
            elif token in [D96Parser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.idx_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar" ):
                return visitor.visitScalar(self)
            else:
                return visitor.visitChildren(self)




    def scalar(self):

        localctx = D96Parser.ScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_scalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idx_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idx_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_expr" ):
                return visitor.visitIdx_expr(self)
            else:
                return visitor.visitChildren(self)




    def idx_expr(self):

        localctx = D96Parser.Idx_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_idx_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(D96Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def elseif_stmt(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(D96Parser.Else_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(D96Parser.IF)
            self.state = 190
            self.match(D96Parser.LB)
            self.state = 191
            self.expr()
            self.state = 192
            self.match(D96Parser.RB)
            self.state = 193
            self.block_stmt()
            self.state = 194
            self.elseif_stmt()
            self.state = 195
            self.else_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(D96Parser.ELIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def elseif_stmt(self):
            return self.getTypedRuleContext(D96Parser.Elseif_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = D96Parser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_elseif_stmt)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(D96Parser.ELIF)
                self.state = 198
                self.match(D96Parser.LB)
                self.state = 199
                self.expr()
                self.state = 200
                self.match(D96Parser.RB)
                self.state = 201
                self.block_stmt()
                self.state = 202
                self.elseif_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(D96Parser.ELIF)
                self.state = 205
                self.match(D96Parser.LB)
                self.state = 206
                self.expr()
                self.state = 207
                self.match(D96Parser.RB)
                self.state = 208
                self.block_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = D96Parser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else_stmt)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(D96Parser.ELSE)
                self.state = 214
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def scalar(self):
            return self.getTypedRuleContext(D96Parser.ScalarContext,0)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def by_stmt(self):
            return self.getTypedRuleContext(D96Parser.By_stmtContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def loop_body(self):
            return self.getTypedRuleContext(D96Parser.Loop_bodyContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_loop_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_stmt" ):
                return visitor.visitLoop_stmt(self)
            else:
                return visitor.visitChildren(self)




    def loop_stmt(self):

        localctx = D96Parser.Loop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_loop_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(D96Parser.FOREACH)
            self.state = 219
            self.match(D96Parser.LB)
            self.state = 220
            self.scalar()
            self.state = 221
            self.match(D96Parser.IN)
            self.state = 222
            self.expr()
            self.state = 223
            self.match(D96Parser.T__1)
            self.state = 224
            self.expr()
            self.state = 225
            self.by_stmt()
            self.state = 226
            self.match(D96Parser.RB)
            self.state = 227
            self.match(D96Parser.LCB)
            self.state = 228
            self.loop_body()
            self.state = 229
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class By_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_by_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBy_stmt" ):
                return visitor.visitBy_stmt(self)
            else:
                return visitor.visitChildren(self)




    def by_stmt(self):

        localctx = D96Parser.By_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_by_stmt)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(D96Parser.BY)
                self.state = 232
                self.expr()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_loop_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_body" ):
                return visitor.visitLoop_body(self)
            else:
                return visitor.visitChildren(self)




    def loop_body(self):

        localctx = D96Parser.Loop_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_loop_body)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(D96Parser.BREAK)
            self.state = 239
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cont_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONT(self):
            return self.getToken(D96Parser.CONT, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_cont_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCont_stmt" ):
                return visitor.visitCont_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cont_stmt(self):

        localctx = D96Parser.Cont_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(D96Parser.CONT)
            self.state = 242
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(D96Parser.RETURN)
            self.state = 245
            self.expr()
            self.state = 246
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invo_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def MA_DCOLON(self):
            return self.getToken(D96Parser.MA_DCOLON, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invo_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invo_stmt" ):
                return visitor.visitMethod_invo_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invo_stmt(self):

        localctx = D96Parser.Method_invo_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_method_invo_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(D96Parser.ID)
            self.state = 249
            self.match(D96Parser.MA_DCOLON)
            self.state = 250
            self.match(D96Parser.STATIC_ID)
            self.state = 251
            self.match(D96Parser.LB)
            self.state = 252
            self.expr_list()
            self.state = 253
            self.match(D96Parser.RB)
            self.state = 254
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_block_stmt)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.stmt()
                self.state = 257
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





