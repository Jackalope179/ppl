import unittest
from xml.etree.ElementTree import tostring
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test1(self):
        input = """
        Class main{}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test2(self):
        input = """
            Class Shape {
            $getNumOfShape( {
                Return self.length * self.width;
                    }
                }
        """
        
        expect = "Error on line 3 col 28: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test3(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {
            Return $numOfShape;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    
    def test4(self):
        input = """
        Class Rectangle: Shape {
            getArea() {
            Return self.length * self.width;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    
    def test5(self):
        input = """
        Class Program {
            getNumber() {
                Return 1;
            }

            main() {
                Var a,b: Int;
                a = a + 1;

                If (a > 0){
                    a = a + 1;
                    b = b + 2;
                    Var e, k: Boolean = True, False;
                    Var f: String = "Hello";
                    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                    Var $x, $y : Int = 0, 0;
                    Var c: Float;
                    Var c,d: Array[Int, 5];
                    c[0] = 1;
                    c[1] = 1;
                }
                ##Else {
                    Foreach (i In 1 .. 100 By 2) {
                        Out.printInt(i);
                    }
                }##
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test6(self):
        input = """
        Class Shape {
            Var $shape: Int = 3;
            Val $numOfShape, shape, shape2: Int = 0, "a" +."b", "Hello" ==. 2;

            Var shape3: Boolean = 3 > 2 || 5 && 6 / 4 * 3  % (1+2) + -1 + !!3 + shape[1] + A.method() +. "Hello"; 
            ##$getShape(len: Float; width: Int)({
                Return $shape;
            })##

            $getNumOfShape(len: Float; width: Int) {
                A.method();
            }

            Constructor (length: Int; width: Int) {
                ##Return 1;##
            }

            Destructor () {
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    
    def test7(self):
        """Simple program: int main() {} """
        input = """Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    
    