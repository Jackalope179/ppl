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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u0229\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\3\3\3\3\3\3\4\3\4\5\4\u00a1\n\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\7\5\u00b5\n\5\f\5\16\5\u00b8\13\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\5\7\u00c3\n\7\3\b\3\b\5\b\u00c7")
        buf.write("\n\b\3\b\3\b\3\t\3\t\3\t\5\t\u00ce\n\t\3\t\3\t\5\t\u00d2")
        buf.write("\n\t\3\t\3\t\5\t\u00d6\n\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n")
        buf.write("\u00de\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\7\13\u00e7")
        buf.write("\n\13\f\13\16\13\u00ea\13\13\5\13\u00ec\n\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\7\f\u00f4\n\f\f\f\16\f\u00f7\13\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\7\r\u00fe\n\r\f\r\16\r\u0101\13\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\7\16\u0109\n\16\f\16\16\16\u010c")
        buf.write("\13\16\3\17\3\17\3\17\3\17\7\17\u0112\n\17\f\17\16\17")
        buf.write("\u0115\13\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\38\38\38\38\39\39\39\3:\3:\3:\3:\3:\3;\3;\7")
        buf.write(";\u01e1\n;\f;\16;\u01e4\13;\3<\3<\6<\u01e8\n<\r<\16<\u01e9")
        buf.write("\3=\6=\u01ed\n=\r=\16=\u01ee\3>\3>\3?\3?\3@\3@\3A\3A\3")
        buf.write("B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\6G\u0204\nG\rG\16G\u0205")
        buf.write("\3G\3G\3H\3H\3H\5H\u020d\nH\3I\5I\u0210\nI\3J\3J\7J\u0214")
        buf.write("\nJ\fJ\16J\u0217\13J\3J\3J\3J\3K\3K\7K\u021e\nK\fK\16")
        buf.write("K\u0221\13K\3K\3K\3K\3K\3L\3L\3L\3\u0113\2M\3\3\5\4\7")
        buf.write("\5\t\6\13\2\r\2\17\2\21\7\23\b\25\t\27\n\31\13\33\f\35")
        buf.write("\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30")
        buf.write("\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U")
        buf.write(")W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w:y;")
        buf.write("{<}=\177>\u0081?\u0083@\u0085A\u0087B\u0089C\u008bD\u008d")
        buf.write("E\u008f\2\u0091\2\u0093F\u0095G\u0097H\3\2\22\6\2\n\f")
        buf.write("\16\17$$^^\4\2GGgg\4\2--//\3\2\63;\3\2aa\3\2\62;\4\2Z")
        buf.write("Zzz\4\2\62;CH\4\2DDdd\3\2\62\63\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\5\2\n\f\16\17\"\"\5\2\n\f\16\17$$\t\2))^^ddhhppt")
        buf.write("tvv\4\3\n\f\16\17\2\u0246\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\3\u0099\3\2\2\2\5\u009b\3\2\2\2\7\u00a0")
        buf.write("\3\2\2\2\t\u00a2\3\2\2\2\13\u00bd\3\2\2\2\r\u00bf\3\2")
        buf.write("\2\2\17\u00c4\3\2\2\2\21\u00d5\3\2\2\2\23\u00dd\3\2\2")
        buf.write("\2\25\u00eb\3\2\2\2\27\u00ed\3\2\2\2\31\u00f8\3\2\2\2")
        buf.write("\33\u0102\3\2\2\2\35\u010d\3\2\2\2\37\u011b\3\2\2\2!\u0120")
        buf.write("\3\2\2\2#\u0126\3\2\2\2%\u012f\3\2\2\2\'\u0132\3\2\2\2")
        buf.write(")\u0139\3\2\2\2+\u013e\3\2\2\2-\u0146\3\2\2\2/\u014b\3")
        buf.write("\2\2\2\61\u0151\3\2\2\2\63\u0157\3\2\2\2\65\u015a\3\2")
        buf.write("\2\2\67\u015e\3\2\2\29\u0164\3\2\2\2;\u016c\3\2\2\2=\u0173")
        buf.write("\3\2\2\2?\u017a\3\2\2\2A\u017f\3\2\2\2C\u0185\3\2\2\2")
        buf.write("E\u0189\3\2\2\2G\u018d\3\2\2\2I\u0199\3\2\2\2K\u01a4\3")
        buf.write("\2\2\2M\u01a8\3\2\2\2O\u01ab\3\2\2\2Q\u01ad\3\2\2\2S\u01af")
        buf.write("\3\2\2\2U\u01b1\3\2\2\2W\u01b3\3\2\2\2Y\u01b5\3\2\2\2")
        buf.write("[\u01b7\3\2\2\2]\u01ba\3\2\2\2_\u01bd\3\2\2\2a\u01c0\3")
        buf.write("\2\2\2c\u01c2\3\2\2\2e\u01c5\3\2\2\2g\u01c7\3\2\2\2i\u01c9")
        buf.write("\3\2\2\2k\u01cc\3\2\2\2m\u01cf\3\2\2\2o\u01d2\3\2\2\2")
        buf.write("q\u01d6\3\2\2\2s\u01d9\3\2\2\2u\u01de\3\2\2\2w\u01e5\3")
        buf.write("\2\2\2y\u01ec\3\2\2\2{\u01f0\3\2\2\2}\u01f2\3\2\2\2\177")
        buf.write("\u01f4\3\2\2\2\u0081\u01f6\3\2\2\2\u0083\u01f8\3\2\2\2")
        buf.write("\u0085\u01fa\3\2\2\2\u0087\u01fc\3\2\2\2\u0089\u01fe\3")
        buf.write("\2\2\2\u008b\u0200\3\2\2\2\u008d\u0203\3\2\2\2\u008f\u020c")
        buf.write("\3\2\2\2\u0091\u020f\3\2\2\2\u0093\u0211\3\2\2\2\u0095")
        buf.write("\u021b\3\2\2\2\u0097\u0226\3\2\2\2\u0099\u009a\7<\2\2")
        buf.write("\u009a\4\3\2\2\2\u009b\u009c\7\60\2\2\u009c\u009d\7\60")
        buf.write("\2\2\u009d\6\3\2\2\2\u009e\u00a1\5-\27\2\u009f\u00a1\5")
        buf.write("/\30\2\u00a0\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\b")
        buf.write("\3\2\2\2\u00a2\u00b6\7$\2\2\u00a3\u00a4\7^\2\2\u00a4\u00b5")
        buf.write("\7d\2\2\u00a5\u00a6\7^\2\2\u00a6\u00b5\7h\2\2\u00a7\u00a8")
        buf.write("\7^\2\2\u00a8\u00b5\7t\2\2\u00a9\u00aa\7^\2\2\u00aa\u00b5")
        buf.write("\7p\2\2\u00ab\u00ac\7^\2\2\u00ac\u00b5\7v\2\2\u00ad\u00ae")
        buf.write("\7^\2\2\u00ae\u00b5\7)\2\2\u00af\u00b0\7^\2\2\u00b0\u00b5")
        buf.write("\7^\2\2\u00b1\u00b2\7)\2\2\u00b2\u00b5\7$\2\2\u00b3\u00b5")
        buf.write("\n\2\2\2\u00b4\u00a3\3\2\2\2\u00b4\u00a5\3\2\2\2\u00b4")
        buf.write("\u00a7\3\2\2\2\u00b4\u00a9\3\2\2\2\u00b4\u00ab\3\2\2\2")
        buf.write("\u00b4\u00ad\3\2\2\2\u00b4\u00af\3\2\2\2\u00b4\u00b1\3")
        buf.write("\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b9\u00ba\7$\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00bc\b\5\2\2\u00bc\n\3\2\2\2\u00bd\u00be\5\25")
        buf.write("\13\2\u00be\f\3\2\2\2\u00bf\u00c2\7\60\2\2\u00c0\u00c3")
        buf.write("\5\25\13\2\u00c1\u00c3\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3\16\3\2\2\2\u00c4\u00c6\t\3\2\2\u00c5")
        buf.write("\u00c7\t\4\2\2\u00c6\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\u00c8\3\2\2\2\u00c8\u00c9\5\25\13\2\u00c9\20\3")
        buf.write("\2\2\2\u00ca\u00cb\5\13\6\2\u00cb\u00cd\5\r\7\2\u00cc")
        buf.write("\u00ce\5\17\b\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2")
        buf.write("\2\u00ce\u00d6\3\2\2\2\u00cf\u00d2\5\13\6\2\u00d0\u00d2")
        buf.write("\5\r\7\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d3\u00d4\5\17\b\2\u00d4\u00d6\3\2\2")
        buf.write("\2\u00d5\u00ca\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d6\u00d7")
        buf.write("\3\2\2\2\u00d7\u00d8\b\t\3\2\u00d8\22\3\2\2\2\u00d9\u00de")
        buf.write("\5\25\13\2\u00da\u00de\5\31\r\2\u00db\u00de\5\33\16\2")
        buf.write("\u00dc\u00de\5\27\f\2\u00dd\u00d9\3\2\2\2\u00dd\u00da")
        buf.write("\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\u00e0\b\n\4\2\u00e0\24\3\2\2\2\u00e1")
        buf.write("\u00ec\7\62\2\2\u00e2\u00e8\t\5\2\2\u00e3\u00e4\t\6\2")
        buf.write("\2\u00e4\u00e7\t\7\2\2\u00e5\u00e7\t\7\2\2\u00e6\u00e3")
        buf.write("\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ec\3\2\2\2")
        buf.write("\u00ea\u00e8\3\2\2\2\u00eb\u00e1\3\2\2\2\u00eb\u00e2\3")
        buf.write("\2\2\2\u00ec\26\3\2\2\2\u00ed\u00ee\7\62\2\2\u00ee\u00ef")
        buf.write("\t\b\2\2\u00ef\u00f5\t\t\2\2\u00f0\u00f1\t\6\2\2\u00f1")
        buf.write("\u00f4\t\t\2\2\u00f2\u00f4\t\t\2\2\u00f3\u00f0\3\2\2\2")
        buf.write("\u00f3\u00f2\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3")
        buf.write("\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\30\3\2\2\2\u00f7\u00f5")
        buf.write("\3\2\2\2\u00f8\u00f9\7\62\2\2\u00f9\u00ff\t\7\2\2\u00fa")
        buf.write("\u00fb\t\6\2\2\u00fb\u00fe\t\7\2\2\u00fc\u00fe\t\7\2\2")
        buf.write("\u00fd\u00fa\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\u0101\3")
        buf.write("\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\32")
        buf.write("\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0103\7\62\2\2\u0103")
        buf.write("\u0104\t\n\2\2\u0104\u010a\t\13\2\2\u0105\u0106\t\6\2")
        buf.write("\2\u0106\u0109\t\13\2\2\u0107\u0109\t\13\2\2\u0108\u0105")
        buf.write("\3\2\2\2\u0108\u0107\3\2\2\2\u0109\u010c\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\34\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010d\u010e\7%\2\2\u010e\u010f\7%\2\2\u010f")
        buf.write("\u0113\3\2\2\2\u0110\u0112\13\2\2\2\u0111\u0110\3\2\2")
        buf.write("\2\u0112\u0115\3\2\2\2\u0113\u0114\3\2\2\2\u0113\u0111")
        buf.write("\3\2\2\2\u0114\u0116\3\2\2\2\u0115\u0113\3\2\2\2\u0116")
        buf.write("\u0117\7%\2\2\u0117\u0118\7%\2\2\u0118\u0119\3\2\2\2\u0119")
        buf.write("\u011a\b\17\5\2\u011a\36\3\2\2\2\u011b\u011c\7U\2\2\u011c")
        buf.write("\u011d\7g\2\2\u011d\u011e\7n\2\2\u011e\u011f\7h\2\2\u011f")
        buf.write(" \3\2\2\2\u0120\u0121\7D\2\2\u0121\u0122\7t\2\2\u0122")
        buf.write("\u0123\7g\2\2\u0123\u0124\7c\2\2\u0124\u0125\7m\2\2\u0125")
        buf.write("\"\3\2\2\2\u0126\u0127\7E\2\2\u0127\u0128\7q\2\2\u0128")
        buf.write("\u0129\7p\2\2\u0129\u012a\7v\2\2\u012a\u012b\7k\2\2\u012b")
        buf.write("\u012c\7p\2\2\u012c\u012d\7w\2\2\u012d\u012e\7g\2\2\u012e")
        buf.write("$\3\2\2\2\u012f\u0130\7K\2\2\u0130\u0131\7h\2\2\u0131")
        buf.write("&\3\2\2\2\u0132\u0133\7G\2\2\u0133\u0134\7n\2\2\u0134")
        buf.write("\u0135\7u\2\2\u0135\u0136\7g\2\2\u0136\u0137\7k\2\2\u0137")
        buf.write("\u0138\7h\2\2\u0138(\3\2\2\2\u0139\u013a\7G\2\2\u013a")
        buf.write("\u013b\7n\2\2\u013b\u013c\7u\2\2\u013c\u013d\7g\2\2\u013d")
        buf.write("*\3\2\2\2\u013e\u013f\7H\2\2\u013f\u0140\7q\2\2\u0140")
        buf.write("\u0141\7t\2\2\u0141\u0142\7g\2\2\u0142\u0143\7c\2\2\u0143")
        buf.write("\u0144\7e\2\2\u0144\u0145\7j\2\2\u0145,\3\2\2\2\u0146")
        buf.write("\u0147\7V\2\2\u0147\u0148\7t\2\2\u0148\u0149\7w\2\2\u0149")
        buf.write("\u014a\7g\2\2\u014a.\3\2\2\2\u014b\u014c\7H\2\2\u014c")
        buf.write("\u014d\7c\2\2\u014d\u014e\7n\2\2\u014e\u014f\7u\2\2\u014f")
        buf.write("\u0150\7g\2\2\u0150\60\3\2\2\2\u0151\u0152\7C\2\2\u0152")
        buf.write("\u0153\7t\2\2\u0153\u0154\7t\2\2\u0154\u0155\7c\2\2\u0155")
        buf.write("\u0156\7{\2\2\u0156\62\3\2\2\2\u0157\u0158\7K\2\2\u0158")
        buf.write("\u0159\7p\2\2\u0159\64\3\2\2\2\u015a\u015b\7K\2\2\u015b")
        buf.write("\u015c\7p\2\2\u015c\u015d\7v\2\2\u015d\66\3\2\2\2\u015e")
        buf.write("\u015f\7H\2\2\u015f\u0160\7n\2\2\u0160\u0161\7q\2\2\u0161")
        buf.write("\u0162\7c\2\2\u0162\u0163\7v\2\2\u01638\3\2\2\2\u0164")
        buf.write("\u0165\7D\2\2\u0165\u0166\7q\2\2\u0166\u0167\7q\2\2\u0167")
        buf.write("\u0168\7n\2\2\u0168\u0169\7g\2\2\u0169\u016a\7c\2\2\u016a")
        buf.write("\u016b\7p\2\2\u016b:\3\2\2\2\u016c\u016d\7U\2\2\u016d")
        buf.write("\u016e\7v\2\2\u016e\u016f\7t\2\2\u016f\u0170\7k\2\2\u0170")
        buf.write("\u0171\7p\2\2\u0171\u0172\7i\2\2\u0172<\3\2\2\2\u0173")
        buf.write("\u0174\7T\2\2\u0174\u0175\7g\2\2\u0175\u0176\7v\2\2\u0176")
        buf.write("\u0177\7w\2\2\u0177\u0178\7t\2\2\u0178\u0179\7p\2\2\u0179")
        buf.write(">\3\2\2\2\u017a\u017b\7P\2\2\u017b\u017c\7w\2\2\u017c")
        buf.write("\u017d\7n\2\2\u017d\u017e\7n\2\2\u017e@\3\2\2\2\u017f")
        buf.write("\u0180\7E\2\2\u0180\u0181\7n\2\2\u0181\u0182\7c\2\2\u0182")
        buf.write("\u0183\7u\2\2\u0183\u0184\7u\2\2\u0184B\3\2\2\2\u0185")
        buf.write("\u0186\7X\2\2\u0186\u0187\7c\2\2\u0187\u0188\7n\2\2\u0188")
        buf.write("D\3\2\2\2\u0189\u018a\7X\2\2\u018a\u018b\7c\2\2\u018b")
        buf.write("\u018c\7t\2\2\u018cF\3\2\2\2\u018d\u018e\7E\2\2\u018e")
        buf.write("\u018f\7q\2\2\u018f\u0190\7p\2\2\u0190\u0191\7u\2\2\u0191")
        buf.write("\u0192\7v\2\2\u0192\u0193\7t\2\2\u0193\u0194\7w\2\2\u0194")
        buf.write("\u0195\7e\2\2\u0195\u0196\7v\2\2\u0196\u0197\7q\2\2\u0197")
        buf.write("\u0198\7t\2\2\u0198H\3\2\2\2\u0199\u019a\7F\2\2\u019a")
        buf.write("\u019b\7g\2\2\u019b\u019c\7u\2\2\u019c\u019d\7v\2\2\u019d")
        buf.write("\u019e\7t\2\2\u019e\u019f\7w\2\2\u019f\u01a0\7e\2\2\u01a0")
        buf.write("\u01a1\7v\2\2\u01a1\u01a2\7q\2\2\u01a2\u01a3\7t\2\2\u01a3")
        buf.write("J\3\2\2\2\u01a4\u01a5\7P\2\2\u01a5\u01a6\7g\2\2\u01a6")
        buf.write("\u01a7\7y\2\2\u01a7L\3\2\2\2\u01a8\u01a9\7D\2\2\u01a9")
        buf.write("\u01aa\7{\2\2\u01aaN\3\2\2\2\u01ab\u01ac\7-\2\2\u01ac")
        buf.write("P\3\2\2\2\u01ad\u01ae\7/\2\2\u01aeR\3\2\2\2\u01af\u01b0")
        buf.write("\7,\2\2\u01b0T\3\2\2\2\u01b1\u01b2\7\61\2\2\u01b2V\3\2")
        buf.write("\2\2\u01b3\u01b4\7\'\2\2\u01b4X\3\2\2\2\u01b5\u01b6\7")
        buf.write("#\2\2\u01b6Z\3\2\2\2\u01b7\u01b8\7(\2\2\u01b8\u01b9\7")
        buf.write("(\2\2\u01b9\\\3\2\2\2\u01ba\u01bb\7~\2\2\u01bb\u01bc\7")
        buf.write("~\2\2\u01bc^\3\2\2\2\u01bd\u01be\7?\2\2\u01be\u01bf\7")
        buf.write("?\2\2\u01bf`\3\2\2\2\u01c0\u01c1\7?\2\2\u01c1b\3\2\2\2")
        buf.write("\u01c2\u01c3\7#\2\2\u01c3\u01c4\7?\2\2\u01c4d\3\2\2\2")
        buf.write("\u01c5\u01c6\7>\2\2\u01c6f\3\2\2\2\u01c7\u01c8\7@\2\2")
        buf.write("\u01c8h\3\2\2\2\u01c9\u01ca\7>\2\2\u01ca\u01cb\7?\2\2")
        buf.write("\u01cbj\3\2\2\2\u01cc\u01cd\7@\2\2\u01cd\u01ce\7?\2\2")
        buf.write("\u01cel\3\2\2\2\u01cf\u01d0\7-\2\2\u01d0\u01d1\7\60\2")
        buf.write("\2\u01d1n\3\2\2\2\u01d2\u01d3\7?\2\2\u01d3\u01d4\7?\2")
        buf.write("\2\u01d4\u01d5\7\60\2\2\u01d5p\3\2\2\2\u01d6\u01d7\7<")
        buf.write("\2\2\u01d7\u01d8\7<\2\2\u01d8r\3\2\2\2\u01d9\u01da\7x")
        buf.write("\2\2\u01da\u01db\7q\2\2\u01db\u01dc\7k\2\2\u01dc\u01dd")
        buf.write("\7f\2\2\u01ddt\3\2\2\2\u01de\u01e2\t\f\2\2\u01df\u01e1")
        buf.write("\t\r\2\2\u01e0\u01df\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3v\3\2\2\2\u01e4")
        buf.write("\u01e2\3\2\2\2\u01e5\u01e7\7&\2\2\u01e6\u01e8\t\r\2\2")
        buf.write("\u01e7\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01e7\3")
        buf.write("\2\2\2\u01e9\u01ea\3\2\2\2\u01eax\3\2\2\2\u01eb\u01ed")
        buf.write("\t\7\2\2\u01ec\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01efz\3\2\2\2\u01f0")
        buf.write("\u01f1\7*\2\2\u01f1|\3\2\2\2\u01f2\u01f3\7+\2\2\u01f3")
        buf.write("~\3\2\2\2\u01f4\u01f5\7}\2\2\u01f5\u0080\3\2\2\2\u01f6")
        buf.write("\u01f7\7\177\2\2\u01f7\u0082\3\2\2\2\u01f8\u01f9\7=\2")
        buf.write("\2\u01f9\u0084\3\2\2\2\u01fa\u01fb\7]\2\2\u01fb\u0086")
        buf.write("\3\2\2\2\u01fc\u01fd\7_\2\2\u01fd\u0088\3\2\2\2\u01fe")
        buf.write("\u01ff\7\60\2\2\u01ff\u008a\3\2\2\2\u0200\u0201\7.\2\2")
        buf.write("\u0201\u008c\3\2\2\2\u0202\u0204\t\16\2\2\u0203\u0202")
        buf.write("\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0203\3\2\2\2\u0205")
        buf.write("\u0206\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208\bG\5\2")
        buf.write("\u0208\u008e\3\2\2\2\u0209\u020d\n\17\2\2\u020a\u020b")
        buf.write("\7^\2\2\u020b\u020d\t\20\2\2\u020c\u0209\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020d\u0090\3\2\2\2\u020e\u0210\t\21\2")
        buf.write("\2\u020f\u020e\3\2\2\2\u0210\u0092\3\2\2\2\u0211\u0215")
        buf.write("\7$\2\2\u0212\u0214\5\u008fH\2\u0213\u0212\3\2\2\2\u0214")
        buf.write("\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2")
        buf.write("\u0216\u0218\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u0219\5")
        buf.write("\u0091I\2\u0219\u021a\bJ\6\2\u021a\u0094\3\2\2\2\u021b")
        buf.write("\u021f\7$\2\2\u021c\u021e\5\u008fH\2\u021d\u021c\3\2\2")
        buf.write("\2\u021e\u0221\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220")
        buf.write("\3\2\2\2\u0220\u0222\3\2\2\2\u0221\u021f\3\2\2\2\u0222")
        buf.write("\u0223\7^\2\2\u0223\u0224\n\20\2\2\u0224\u0225\bK\7\2")
        buf.write("\u0225\u0096\3\2\2\2\u0226\u0227\13\2\2\2\u0227\u0228")
        buf.write("\bL\b\2\u0228\u0098\3\2\2\2\36\2\u00a0\u00b4\u00b6\u00c2")
        buf.write("\u00c6\u00cd\u00d1\u00d5\u00dd\u00e6\u00e8\u00eb\u00f3")
        buf.write("\u00f5\u00fd\u00ff\u0108\u010a\u0113\u01e2\u01e9\u01ee")
        buf.write("\u0205\u020c\u020f\u0215\u021f\t\3\5\2\3\t\3\3\n\4\b\2")
        buf.write("\2\3J\5\3K\6\3L\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    BOOL = 3
    STR = 4
    FLOAT = 5
    INT = 6
    INT_DEC = 7
    INT_HEX = 8
    INT_OCTAL = 9
    INT_BINARY = 10
    COMMENT = 11
    SELF = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSEIF = 16
    ELSE = 17
    FOREACH = 18
    TRUE = 19
    FALSE = 20
    ARRAY = 21
    IN = 22
    INTTYPE = 23
    FLOATTYPE = 24
    BOOLTYPE = 25
    STRINGTYPE = 26
    RETURN = 27
    NULL = 28
    CLASS = 29
    VAL = 30
    VAR = 31
    CONSTRUCTOR = 32
    DESTRUCTOR = 33
    NEW = 34
    BY = 35
    ADD = 36
    SUB = 37
    MUL = 38
    DIV = 39
    RM = 40
    NOT = 41
    AND = 42
    OR = 43
    EQ = 44
    ASSG = 45
    NEQ = 46
    LT = 47
    GT = 48
    LTE = 49
    GTE = 50
    STR_CONCAT = 51
    STR_COMPARE = 52
    ACCESS = 53
    VOIDTYPE = 54
    ID = 55
    SID = 56
    INTLIT = 57
    LB = 58
    RB = 59
    LP = 60
    RP = 61
    SEMI = 62
    LS = 63
    RS = 64
    DOT = 65
    COMMA = 66
    WS = 67
    UNCLOSE_STRING = 68
    ILLEGAL_ESCAPE = 69
    ERROR_TOKEN = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'..'", "'Self'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
            "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", 
            "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'+.'", "'==.'", "'::'", "'void'", "'('", "')'", "'{'", "'}'", 
            "';'", "'['", "']'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BOOL", "STR", "FLOAT", "INT", "INT_DEC", "INT_HEX", "INT_OCTAL", 
            "INT_BINARY", "COMMENT", "SELF", "BREAK", "CONTINUE", "IF", 
            "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", 
            "INTTYPE", "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", "RETURN", 
            "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "ADD", "SUB", "MUL", "DIV", "RM", "NOT", "AND", 
            "OR", "EQ", "ASSG", "NEQ", "LT", "GT", "LTE", "GTE", "STR_CONCAT", 
            "STR_COMPARE", "ACCESS", "VOIDTYPE", "ID", "SID", "INTLIT", 
            "LB", "RB", "LP", "RP", "SEMI", "LS", "RS", "DOT", "COMMA", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "T__0", "T__1", "BOOL", "STR", "INTPART", "FRACPART", 
                  "EXPART", "FLOAT", "INT", "INT_DEC", "INT_HEX", "INT_OCTAL", 
                  "INT_BINARY", "COMMENT", "SELF", "BREAK", "CONTINUE", 
                  "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                  "IN", "INTTYPE", "FLOATTYPE", "BOOLTYPE", "STRINGTYPE", 
                  "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "ADD", "SUB", "MUL", "DIV", 
                  "RM", "NOT", "AND", "OR", "EQ", "ASSG", "NEQ", "LT", "GT", 
                  "LTE", "GTE", "STR_CONCAT", "STR_COMPARE", "ACCESS", "VOIDTYPE", 
                  "ID", "SID", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", 
                  "LS", "RS", "DOT", "COMMA", "WS", "CHARACTERS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

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
            actions[3] = self.STR_action 
            actions[7] = self.FLOAT_action 
            actions[8] = self.INT_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_TOKEN_action 
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

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	if self.text[-1] in ['\n', '\r', '\t', '\f', '\b']:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise  ErrorToken(self.text)
     


