# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0238\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\5\2\u0096")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\7\3\u00aa\n\3\f\3\16\3\u00ad\13")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\7\5\u00b7\n\5\f\5\16")
        buf.write("\5\u00ba\13\5\3\6\3\6\5\6\u00be\n\6\3\6\6\6\u00c1\n\6")
        buf.write("\r\6\16\6\u00c2\3\7\3\7\3\7\5\7\u00c8\n\7\3\7\3\7\5\7")
        buf.write("\u00cc\n\7\3\7\3\7\5\7\u00d0\n\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\5\b\u00d8\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\7\t\u00e1")
        buf.write("\n\t\f\t\16\t\u00e4\13\t\5\t\u00e6\n\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\7\n\u00ef\n\n\f\n\16\n\u00f2\13\n\5\n\u00f4")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u00fc\n\13\f\13")
        buf.write("\16\13\u00ff\13\13\5\13\u0101\n\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\7\f\u010a\n\f\f\f\16\f\u010d\13\f\5\f\u010f\n")
        buf.write("\f\3\r\3\r\3\r\3\r\7\r\u0115\n\r\f\r\16\r\u0118\13\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\38\38\7")
        buf.write("8\u01df\n8\f8\168\u01e2\138\39\39\69\u01e6\n9\r9\169\u01e7")
        buf.write("\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\6D\u01ff\nD\rD\16D\u0200\3D\3D\3E\3E\3E\3F")
        buf.write("\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\5F\u0219")
        buf.write("\nF\3G\5G\u021c\nG\3H\3H\7H\u0220\nH\fH\16H\u0223\13H")
        buf.write("\3H\3H\3H\3I\3I\7I\u022a\nI\fI\16I\u022d\13I\3I\3I\5I")
        buf.write("\u0231\nI\3I\3I\5I\u0235\nI\3I\3I\3\u0116\2J\3\3\5\4\7")
        buf.write("\2\t\2\13\2\r\5\17\6\21\7\23\b\25\t\27\n\31\13\33\f\35")
        buf.write("\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30")
        buf.write("\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U")
        buf.write(")W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w:y;")
        buf.write("{<}=\177>\u0081?\u0083@\u0085A\u0087B\u0089C\u008b\2\u008d")
        buf.write("\2\u008fD\u0091E\3\2\26\6\2\f\f\17\17$$^^\3\2\62;\4\2")
        buf.write("GGgg\4\2--//\3\2\63;\3\2aa\4\2ZZzz\4\2\63;CH\4\2\62;C")
        buf.write("H\3\2\639\3\2\629\4\2DDdd\3\2\63\63\3\2\62\63\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\4\3\f\f\17\17\t")
        buf.write("\2))^^ddhhppttvv\3\2$$\2\u0261\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0095\3\2\2\2\5\u0097")
        buf.write("\3\2\2\2\7\u00b2\3\2\2\2\t\u00b4\3\2\2\2\13\u00bb\3\2")
        buf.write("\2\2\r\u00cf\3\2\2\2\17\u00d7\3\2\2\2\21\u00e5\3\2\2\2")
        buf.write("\23\u00e7\3\2\2\2\25\u00f5\3\2\2\2\27\u0102\3\2\2\2\31")
        buf.write("\u0110\3\2\2\2\33\u011e\3\2\2\2\35\u0123\3\2\2\2\37\u0129")
        buf.write("\3\2\2\2!\u0132\3\2\2\2#\u0135\3\2\2\2%\u013c\3\2\2\2")
        buf.write("\'\u0141\3\2\2\2)\u0149\3\2\2\2+\u014e\3\2\2\2-\u0154")
        buf.write("\3\2\2\2/\u015a\3\2\2\2\61\u015d\3\2\2\2\63\u0161\3\2")
        buf.write("\2\2\65\u0167\3\2\2\2\67\u016f\3\2\2\29\u0176\3\2\2\2")
        buf.write(";\u017d\3\2\2\2=\u0182\3\2\2\2?\u0188\3\2\2\2A\u018c\3")
        buf.write("\2\2\2C\u0190\3\2\2\2E\u019c\3\2\2\2G\u01a7\3\2\2\2I\u01ab")
        buf.write("\3\2\2\2K\u01ae\3\2\2\2M\u01b0\3\2\2\2O\u01b2\3\2\2\2")
        buf.write("Q\u01b4\3\2\2\2S\u01b6\3\2\2\2U\u01b8\3\2\2\2W\u01ba\3")
        buf.write("\2\2\2Y\u01bd\3\2\2\2[\u01c0\3\2\2\2]\u01c3\3\2\2\2_\u01c5")
        buf.write("\3\2\2\2a\u01c8\3\2\2\2c\u01ca\3\2\2\2e\u01cc\3\2\2\2")
        buf.write("g\u01cf\3\2\2\2i\u01d2\3\2\2\2k\u01d5\3\2\2\2m\u01d9\3")
        buf.write("\2\2\2o\u01dc\3\2\2\2q\u01e3\3\2\2\2s\u01e9\3\2\2\2u\u01eb")
        buf.write("\3\2\2\2w\u01ed\3\2\2\2y\u01ef\3\2\2\2{\u01f1\3\2\2\2")
        buf.write("}\u01f3\3\2\2\2\177\u01f5\3\2\2\2\u0081\u01f7\3\2\2\2")
        buf.write("\u0083\u01f9\3\2\2\2\u0085\u01fb\3\2\2\2\u0087\u01fe\3")
        buf.write("\2\2\2\u0089\u0204\3\2\2\2\u008b\u0218\3\2\2\2\u008d\u021b")
        buf.write("\3\2\2\2\u008f\u021d\3\2\2\2\u0091\u0227\3\2\2\2\u0093")
        buf.write("\u0096\5)\25\2\u0094\u0096\5+\26\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0094\3\2\2\2\u0096\4\3\2\2\2\u0097\u00ab\7$\2")
        buf.write("\2\u0098\u0099\7^\2\2\u0099\u00aa\7d\2\2\u009a\u009b\7")
        buf.write("^\2\2\u009b\u00aa\7h\2\2\u009c\u009d\7^\2\2\u009d\u00aa")
        buf.write("\7t\2\2\u009e\u009f\7^\2\2\u009f\u00aa\7p\2\2\u00a0\u00a1")
        buf.write("\7^\2\2\u00a1\u00aa\7v\2\2\u00a2\u00a3\7^\2\2\u00a3\u00aa")
        buf.write("\7)\2\2\u00a4\u00a5\7^\2\2\u00a5\u00aa\7^\2\2\u00a6\u00a7")
        buf.write("\7)\2\2\u00a7\u00aa\7$\2\2\u00a8\u00aa\n\2\2\2\u00a9\u0098")
        buf.write("\3\2\2\2\u00a9\u009a\3\2\2\2\u00a9\u009c\3\2\2\2\u00a9")
        buf.write("\u009e\3\2\2\2\u00a9\u00a0\3\2\2\2\u00a9\u00a2\3\2\2\2")
        buf.write("\u00a9\u00a4\3\2\2\2\u00a9\u00a6\3\2\2\2\u00a9\u00a8\3")
        buf.write("\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac")
        buf.write("\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae")
        buf.write("\u00af\7$\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\b\3\2\2")
        buf.write("\u00b1\6\3\2\2\2\u00b2\u00b3\5\21\t\2\u00b3\b\3\2\2\2")
        buf.write("\u00b4\u00b8\7\60\2\2\u00b5\u00b7\t\3\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b9\3\2\2\2\u00b9\n\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb")
        buf.write("\u00bd\t\4\2\2\u00bc\u00be\t\5\2\2\u00bd\u00bc\3\2\2\2")
        buf.write("\u00bd\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00c1\t")
        buf.write("\3\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\f\3\2\2\2\u00c4\u00c5")
        buf.write("\5\7\4\2\u00c5\u00c7\5\t\5\2\u00c6\u00c8\5\13\6\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00d0\3\2\2\2")
        buf.write("\u00c9\u00cc\5\7\4\2\u00ca\u00cc\5\t\5\2\u00cb\u00c9\3")
        buf.write("\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce")
        buf.write("\5\13\6\2\u00ce\u00d0\3\2\2\2\u00cf\u00c4\3\2\2\2\u00cf")
        buf.write("\u00cb\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\b\7\3\2")
        buf.write("\u00d2\16\3\2\2\2\u00d3\u00d8\5\21\t\2\u00d4\u00d8\5\25")
        buf.write("\13\2\u00d5\u00d8\5\27\f\2\u00d6\u00d8\5\23\n\2\u00d7")
        buf.write("\u00d3\3\2\2\2\u00d7\u00d4\3\2\2\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d7\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\b")
        buf.write("\b\4\2\u00da\20\3\2\2\2\u00db\u00e6\7\62\2\2\u00dc\u00e2")
        buf.write("\t\6\2\2\u00dd\u00de\t\7\2\2\u00de\u00e1\t\3\2\2\u00df")
        buf.write("\u00e1\t\3\2\2\u00e0\u00dd\3\2\2\2\u00e0\u00df\3\2\2\2")
        buf.write("\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3")
        buf.write("\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00db")
        buf.write("\3\2\2\2\u00e5\u00dc\3\2\2\2\u00e6\22\3\2\2\2\u00e7\u00e8")
        buf.write("\7\62\2\2\u00e8\u00f3\t\b\2\2\u00e9\u00f4\7\62\2\2\u00ea")
        buf.write("\u00f0\t\t\2\2\u00eb\u00ec\t\7\2\2\u00ec\u00ef\t\n\2\2")
        buf.write("\u00ed\u00ef\t\n\2\2\u00ee\u00eb\3\2\2\2\u00ee\u00ed\3")
        buf.write("\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3")
        buf.write("\u00e9\3\2\2\2\u00f3\u00ea\3\2\2\2\u00f4\24\3\2\2\2\u00f5")
        buf.write("\u0100\7\62\2\2\u00f6\u0101\7\62\2\2\u00f7\u00fd\t\13")
        buf.write("\2\2\u00f8\u00f9\t\7\2\2\u00f9\u00fc\t\f\2\2\u00fa\u00fc")
        buf.write("\t\f\2\2\u00fb\u00f8\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc")
        buf.write("\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u00f6\3")
        buf.write("\2\2\2\u0100\u00f7\3\2\2\2\u0101\26\3\2\2\2\u0102\u0103")
        buf.write("\7\62\2\2\u0103\u010e\t\r\2\2\u0104\u010f\7\62\2\2\u0105")
        buf.write("\u010b\t\16\2\2\u0106\u0107\t\7\2\2\u0107\u010a\t\17\2")
        buf.write("\2\u0108\u010a\t\17\2\2\u0109\u0106\3\2\2\2\u0109\u0108")
        buf.write("\3\2\2\2\u010a\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b")
        buf.write("\u010c\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2")
        buf.write("\u010e\u0104\3\2\2\2\u010e\u0105\3\2\2\2\u010f\30\3\2")
        buf.write("\2\2\u0110\u0111\7%\2\2\u0111\u0112\7%\2\2\u0112\u0116")
        buf.write("\3\2\2\2\u0113\u0115\13\2\2\2\u0114\u0113\3\2\2\2\u0115")
        buf.write("\u0118\3\2\2\2\u0116\u0117\3\2\2\2\u0116\u0114\3\2\2\2")
        buf.write("\u0117\u0119\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\7")
        buf.write("%\2\2\u011a\u011b\7%\2\2\u011b\u011c\3\2\2\2\u011c\u011d")
        buf.write("\b\r\5\2\u011d\32\3\2\2\2\u011e\u011f\7U\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\u0121\7n\2\2\u0121\u0122\7h\2\2\u0122\34")
        buf.write("\3\2\2\2\u0123\u0124\7D\2\2\u0124\u0125\7t\2\2\u0125\u0126")
        buf.write("\7g\2\2\u0126\u0127\7c\2\2\u0127\u0128\7m\2\2\u0128\36")
        buf.write("\3\2\2\2\u0129\u012a\7E\2\2\u012a\u012b\7q\2\2\u012b\u012c")
        buf.write("\7p\2\2\u012c\u012d\7v\2\2\u012d\u012e\7k\2\2\u012e\u012f")
        buf.write("\7p\2\2\u012f\u0130\7w\2\2\u0130\u0131\7g\2\2\u0131 \3")
        buf.write("\2\2\2\u0132\u0133\7K\2\2\u0133\u0134\7h\2\2\u0134\"\3")
        buf.write("\2\2\2\u0135\u0136\7G\2\2\u0136\u0137\7n\2\2\u0137\u0138")
        buf.write("\7u\2\2\u0138\u0139\7g\2\2\u0139\u013a\7k\2\2\u013a\u013b")
        buf.write("\7h\2\2\u013b$\3\2\2\2\u013c\u013d\7G\2\2\u013d\u013e")
        buf.write("\7n\2\2\u013e\u013f\7u\2\2\u013f\u0140\7g\2\2\u0140&\3")
        buf.write("\2\2\2\u0141\u0142\7H\2\2\u0142\u0143\7q\2\2\u0143\u0144")
        buf.write("\7t\2\2\u0144\u0145\7g\2\2\u0145\u0146\7c\2\2\u0146\u0147")
        buf.write("\7e\2\2\u0147\u0148\7j\2\2\u0148(\3\2\2\2\u0149\u014a")
        buf.write("\7V\2\2\u014a\u014b\7t\2\2\u014b\u014c\7w\2\2\u014c\u014d")
        buf.write("\7g\2\2\u014d*\3\2\2\2\u014e\u014f\7H\2\2\u014f\u0150")
        buf.write("\7c\2\2\u0150\u0151\7n\2\2\u0151\u0152\7u\2\2\u0152\u0153")
        buf.write("\7g\2\2\u0153,\3\2\2\2\u0154\u0155\7C\2\2\u0155\u0156")
        buf.write("\7t\2\2\u0156\u0157\7t\2\2\u0157\u0158\7c\2\2\u0158\u0159")
        buf.write("\7{\2\2\u0159.\3\2\2\2\u015a\u015b\7K\2\2\u015b\u015c")
        buf.write("\7p\2\2\u015c\60\3\2\2\2\u015d\u015e\7K\2\2\u015e\u015f")
        buf.write("\7p\2\2\u015f\u0160\7v\2\2\u0160\62\3\2\2\2\u0161\u0162")
        buf.write("\7H\2\2\u0162\u0163\7n\2\2\u0163\u0164\7q\2\2\u0164\u0165")
        buf.write("\7c\2\2\u0165\u0166\7v\2\2\u0166\64\3\2\2\2\u0167\u0168")
        buf.write("\7D\2\2\u0168\u0169\7q\2\2\u0169\u016a\7q\2\2\u016a\u016b")
        buf.write("\7n\2\2\u016b\u016c\7g\2\2\u016c\u016d\7c\2\2\u016d\u016e")
        buf.write("\7p\2\2\u016e\66\3\2\2\2\u016f\u0170\7U\2\2\u0170\u0171")
        buf.write("\7v\2\2\u0171\u0172\7t\2\2\u0172\u0173\7k\2\2\u0173\u0174")
        buf.write("\7p\2\2\u0174\u0175\7i\2\2\u01758\3\2\2\2\u0176\u0177")
        buf.write("\7T\2\2\u0177\u0178\7g\2\2\u0178\u0179\7v\2\2\u0179\u017a")
        buf.write("\7w\2\2\u017a\u017b\7t\2\2\u017b\u017c\7p\2\2\u017c:\3")
        buf.write("\2\2\2\u017d\u017e\7P\2\2\u017e\u017f\7w\2\2\u017f\u0180")
        buf.write("\7n\2\2\u0180\u0181\7n\2\2\u0181<\3\2\2\2\u0182\u0183")
        buf.write("\7E\2\2\u0183\u0184\7n\2\2\u0184\u0185\7c\2\2\u0185\u0186")
        buf.write("\7u\2\2\u0186\u0187\7u\2\2\u0187>\3\2\2\2\u0188\u0189")
        buf.write("\7X\2\2\u0189\u018a\7c\2\2\u018a\u018b\7n\2\2\u018b@\3")
        buf.write("\2\2\2\u018c\u018d\7X\2\2\u018d\u018e\7c\2\2\u018e\u018f")
        buf.write("\7t\2\2\u018fB\3\2\2\2\u0190\u0191\7E\2\2\u0191\u0192")
        buf.write("\7q\2\2\u0192\u0193\7p\2\2\u0193\u0194\7u\2\2\u0194\u0195")
        buf.write("\7v\2\2\u0195\u0196\7t\2\2\u0196\u0197\7w\2\2\u0197\u0198")
        buf.write("\7e\2\2\u0198\u0199\7v\2\2\u0199\u019a\7q\2\2\u019a\u019b")
        buf.write("\7t\2\2\u019bD\3\2\2\2\u019c\u019d\7F\2\2\u019d\u019e")
        buf.write("\7g\2\2\u019e\u019f\7u\2\2\u019f\u01a0\7v\2\2\u01a0\u01a1")
        buf.write("\7t\2\2\u01a1\u01a2\7w\2\2\u01a2\u01a3\7e\2\2\u01a3\u01a4")
        buf.write("\7v\2\2\u01a4\u01a5\7q\2\2\u01a5\u01a6\7t\2\2\u01a6F\3")
        buf.write("\2\2\2\u01a7\u01a8\7P\2\2\u01a8\u01a9\7g\2\2\u01a9\u01aa")
        buf.write("\7y\2\2\u01aaH\3\2\2\2\u01ab\u01ac\7D\2\2\u01ac\u01ad")
        buf.write("\7{\2\2\u01adJ\3\2\2\2\u01ae\u01af\7-\2\2\u01afL\3\2\2")
        buf.write("\2\u01b0\u01b1\7/\2\2\u01b1N\3\2\2\2\u01b2\u01b3\7,\2")
        buf.write("\2\u01b3P\3\2\2\2\u01b4\u01b5\7\61\2\2\u01b5R\3\2\2\2")
        buf.write("\u01b6\u01b7\7\'\2\2\u01b7T\3\2\2\2\u01b8\u01b9\7#\2\2")
        buf.write("\u01b9V\3\2\2\2\u01ba\u01bb\7(\2\2\u01bb\u01bc\7(\2\2")
        buf.write("\u01bcX\3\2\2\2\u01bd\u01be\7~\2\2\u01be\u01bf\7~\2\2")
        buf.write("\u01bfZ\3\2\2\2\u01c0\u01c1\7?\2\2\u01c1\u01c2\7?\2\2")
        buf.write("\u01c2\\\3\2\2\2\u01c3\u01c4\7?\2\2\u01c4^\3\2\2\2\u01c5")
        buf.write("\u01c6\7#\2\2\u01c6\u01c7\7?\2\2\u01c7`\3\2\2\2\u01c8")
        buf.write("\u01c9\7>\2\2\u01c9b\3\2\2\2\u01ca\u01cb\7@\2\2\u01cb")
        buf.write("d\3\2\2\2\u01cc\u01cd\7>\2\2\u01cd\u01ce\7?\2\2\u01ce")
        buf.write("f\3\2\2\2\u01cf\u01d0\7@\2\2\u01d0\u01d1\7?\2\2\u01d1")
        buf.write("h\3\2\2\2\u01d2\u01d3\7-\2\2\u01d3\u01d4\7\60\2\2\u01d4")
        buf.write("j\3\2\2\2\u01d5\u01d6\7?\2\2\u01d6\u01d7\7?\2\2\u01d7")
        buf.write("\u01d8\7\60\2\2\u01d8l\3\2\2\2\u01d9\u01da\7<\2\2\u01da")
        buf.write("\u01db\7<\2\2\u01dbn\3\2\2\2\u01dc\u01e0\t\20\2\2\u01dd")
        buf.write("\u01df\t\21\2\2\u01de\u01dd\3\2\2\2\u01df\u01e2\3\2\2")
        buf.write("\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1p\3\2")
        buf.write("\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e5\7&\2\2\u01e4\u01e6")
        buf.write("\t\21\2\2\u01e5\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8r\3\2\2\2\u01e9")
        buf.write("\u01ea\7*\2\2\u01eat\3\2\2\2\u01eb\u01ec\7+\2\2\u01ec")
        buf.write("v\3\2\2\2\u01ed\u01ee\7}\2\2\u01eex\3\2\2\2\u01ef\u01f0")
        buf.write("\7\177\2\2\u01f0z\3\2\2\2\u01f1\u01f2\7=\2\2\u01f2|\3")
        buf.write("\2\2\2\u01f3\u01f4\7]\2\2\u01f4~\3\2\2\2\u01f5\u01f6\7")
        buf.write("_\2\2\u01f6\u0080\3\2\2\2\u01f7\u01f8\7\60\2\2\u01f8\u0082")
        buf.write("\3\2\2\2\u01f9\u01fa\7.\2\2\u01fa\u0084\3\2\2\2\u01fb")
        buf.write("\u01fc\7<\2\2\u01fc\u0086\3\2\2\2\u01fd\u01ff\t\22\2\2")
        buf.write("\u01fe\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u01fe\3")
        buf.write("\2\2\2\u0200\u0201\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0203")
        buf.write("\bD\5\2\u0203\u0088\3\2\2\2\u0204\u0205\13\2\2\2\u0205")
        buf.write("\u0206\bE\6\2\u0206\u008a\3\2\2\2\u0207\u0208\7^\2\2\u0208")
        buf.write("\u0219\7d\2\2\u0209\u020a\7^\2\2\u020a\u0219\7h\2\2\u020b")
        buf.write("\u020c\7^\2\2\u020c\u0219\7t\2\2\u020d\u020e\7^\2\2\u020e")
        buf.write("\u0219\7p\2\2\u020f\u0210\7^\2\2\u0210\u0219\7v\2\2\u0211")
        buf.write("\u0212\7^\2\2\u0212\u0219\7)\2\2\u0213\u0214\7^\2\2\u0214")
        buf.write("\u0219\7^\2\2\u0215\u0216\7)\2\2\u0216\u0219\7$\2\2\u0217")
        buf.write("\u0219\n\2\2\2\u0218\u0207\3\2\2\2\u0218\u0209\3\2\2\2")
        buf.write("\u0218\u020b\3\2\2\2\u0218\u020d\3\2\2\2\u0218\u020f\3")
        buf.write("\2\2\2\u0218\u0211\3\2\2\2\u0218\u0213\3\2\2\2\u0218\u0215")
        buf.write("\3\2\2\2\u0218\u0217\3\2\2\2\u0219\u008c\3\2\2\2\u021a")
        buf.write("\u021c\t\23\2\2\u021b\u021a\3\2\2\2\u021c\u008e\3\2\2")
        buf.write("\2\u021d\u0221\7$\2\2\u021e\u0220\5\u008bF\2\u021f\u021e")
        buf.write("\3\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222\u0224\3\2\2\2\u0223\u0221\3\2\2\2")
        buf.write("\u0224\u0225\5\u008dG\2\u0225\u0226\bH\7\2\u0226\u0090")
        buf.write("\3\2\2\2\u0227\u022b\7$\2\2\u0228\u022a\5\u008bF\2\u0229")
        buf.write("\u0228\3\2\2\2\u022a\u022d\3\2\2\2\u022b\u0229\3\2\2\2")
        buf.write("\u022b\u022c\3\2\2\2\u022c\u0234\3\2\2\2\u022d\u022b\3")
        buf.write("\2\2\2\u022e\u0230\7^\2\2\u022f\u0231\n\24\2\2\u0230\u022f")
        buf.write("\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0235\3\2\2\2\u0232")
        buf.write("\u0233\7)\2\2\u0233\u0235\n\25\2\2\u0234\u022e\3\2\2\2")
        buf.write("\u0234\u0232\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0237\b")
        buf.write("I\b\2\u0237\u0092\3\2\2\2#\2\u0095\u00a9\u00ab\u00b8\u00bd")
        buf.write("\u00c2\u00c7\u00cb\u00cf\u00d7\u00e0\u00e2\u00e5\u00ee")
        buf.write("\u00f0\u00f3\u00fb\u00fd\u0100\u0109\u010b\u010e\u0116")
        buf.write("\u01e0\u01e7\u0200\u0218\u021b\u0221\u022b\u0230\u0234")
        buf.write("\t\3\3\2\3\7\3\3\b\4\b\2\2\3E\5\3H\6\3I\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL = 1
    STR = 2
    FLOAT = 3
    INT = 4
    INT_DEC = 5
    INT_HEX = 6
    INT_OCTAL = 7
    INT_BINARY = 8
    COMMENT = 9
    SELF = 10
    BREAK = 11
    CONTINUE = 12
    IF = 13
    ELSEIF = 14
    ELSE = 15
    FOREACH = 16
    TRUE = 17
    FALSE = 18
    ARRAY = 19
    IN = 20
    INTTYPE = 21
    FLOATTYPE = 22
    BOOLTYPE = 23
    STRINGTYPE = 24
    RETURN = 25
    NULL = 26
    CLASS = 27
    VAL = 28
    VAR = 29
    CONSTRUCTOR = 30
    DESTRUCTOR = 31
    NEW = 32
    BY = 33
    ADD = 34
    SUB = 35
    MUL = 36
    DIV = 37
    RM = 38
    NOT = 39
    AND = 40
    OR = 41
    EQ = 42
    ASSG = 43
    NEQ = 44
    LT = 45
    GT = 46
    LTE = 47
    GTE = 48
    STR_CONCAT = 49
    STR_COMPARE = 50
    ACCESS = 51
    ID = 52
    SID = 53
    LB = 54
    RB = 55
    LP = 56
    RP = 57
    SEMI = 58
    LS = 59
    RS = 60
    DOT = 61
    COMMA = 62
    IS = 63
    WS = 64
    ERROR_TOKEN = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Self'", "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
            "'Foreach'", "'True'", "'False'", "'Array'", "'In'", "'Int'", 
            "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", 
            "'Val'", "'Var'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'+.'", 
            "'==.'", "'::'", "'('", "')'", "'{'", "'}'", "';'", "'['", "']'", 
            "'.'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL", "STR", "FLOAT", "INT", "INT_DEC", "INT_HEX", "INT_OCTAL", 
            "INT_BINARY", "COMMENT", "SELF", "BREAK", "CONTINUE", "IF", 
            "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", 
            "INTTYPE", "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", "RETURN", 
            "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "ADD", "SUB", "MUL", "DIV", "RM", "NOT", "AND", 
            "OR", "EQ", "ASSG", "NEQ", "LT", "GT", "LTE", "GTE", "STR_CONCAT", 
            "STR_COMPARE", "ACCESS", "ID", "SID", "LB", "RB", "LP", "RP", 
            "SEMI", "LS", "RS", "DOT", "COMMA", "IS", "WS", "ERROR_TOKEN", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BOOL", "STR", "INTPART", "DECIMALPART", "EXPART", "FLOAT", 
                  "INT", "INT_DEC", "INT_HEX", "INT_OCTAL", "INT_BINARY", 
                  "COMMENT", "SELF", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INTTYPE", 
                  "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", "RETURN", "NULL", 
                  "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                  "BY", "ADD", "SUB", "MUL", "DIV", "RM", "NOT", "AND", 
                  "OR", "EQ", "ASSG", "NEQ", "LT", "GT", "LTE", "GTE", "STR_CONCAT", 
                  "STR_COMPARE", "ACCESS", "ID", "SID", "LB", "RB", "LP", 
                  "RP", "SEMI", "LS", "RS", "DOT", "COMMA", "IS", "WS", 
                  "ERROR_TOKEN", "CHARACTERS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.STR_action 
            actions[5] = self.FLOAT_action 
            actions[6] = self.INT_action 
            actions[67] = self.ERROR_TOKEN_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1];

     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text.replace('_', '');

     

    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text.replace('_', '');

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise  ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	if self.text[-1] in ['\n', '\r', '\t', '\f', '\b']:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	raise IllegalEscape(self.text[1:])

     


