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
        expect = "Error on line 17 col 24: $x"
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
    
    '''-----------Test Statement------------'''

    def test8(self):
        input = """
        Var NoninClass: Int = 5;
        """
        expect = "Error on line 2 col 8: Var"
        self.assertTrue(TestParser.test(input,expect,208))

    def test9(self):
        input = """
        Class Number{
            Var a: Int;
            getValue() {
            Val $Nonstatic: Int = 5;
            }
        }
        """
        expect = "Error on line 5 col 16: $Nonstatic"
        self.assertTrue(TestParser.test(input,expect,209))

    def test10(self):
        input = """
        Class Number{
            Var a: Array[Array[Int, 5], 5];

            print(a,b: Int; c: String){
                Out.printInt(a[0][0]);
            }

            getValue() {
            a = Array("Hello", "Hi", "HelloWorld");
            Var Nonstatic: Int = 5;
            Val var1, var2, var3: Int = 5, 5 > 6, Self.a;
            Self.print(e,d,g);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

    def test11(self):
        input = """
        Class Number{
            Var a: Int;
            getValue() {
            If(Self.a < 0){
                a = a + 1;
            }
            Elseif (a < 10){
                a = a - 1;
            }
            Elseif (a < 100){
                a = a * 2;
            }
            Else {
             Out.printInt(a);   
            }
            }            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def test12(self):
        input = """
        Class Number{
            Var a: Int;
            getValue() {
            Foreach(i In 1 .. 10 By 2){
                Out.printInt(i);
                If(i > 5){
                    Return 1+1;
                    Break;
                }
                Else{
                    Return Self.a;
                    Continue;
                }
                Return "Hello";
            }
            }            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    
    def test14(self):
        input = """
        Class Number{
            Var a: Int;
            Return a;
        }
        """
        expect = "Error on line 4 col 12: Return"
        self.assertTrue(TestParser.test(input,expect,214))

    def test15(self):
        input = """
        Class Number{
            Var a: Int;
            a = a + 1;
            getValue(){
                Return a;
            }
        }
        """
        expect = "Error on line 4 col 14: ="
        self.assertTrue(TestParser.test(input,expect,215))
    
    def test16(self):
        """Simple program: int main() {} """
        input = """
            Class Shape {
                Val $numOfShape: Int = 10;
                Val immutableAttribute: Int = 5;
                Var length, width: Int;

                $getNumOfShape() {
                    return 100;
                }
            }
        """
        expect = "Error on line 8 col 27: 100"
        self.assertTrue(TestParser.test(input,expect,216))
    
    def test17(self):
        input = """
        Class A{
            Var value: Int;
            getValue() {
                Out.printInt(value);
            }
        }
        Class Shape {
            Var a: Array[Int,5] = Array(1,2,3,4,5);
            Val $b: Array[Array[Int,2],3] = Array(
                Array(1,2),
                Array(3,4),
                Array(5,6)
            );

            $printStatic(){
                Out.printInt(a);
            }

            printArray() {
                Var a: A = New A();
                ## Get static method ##
                Shape::$printStatic();

                ## Get static attribute ##
                Shape::$b;
                
                ## Get non-static method ##
                a.getValue();
                
                ## Get non-static attribute ##
                a.value;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))

    def test18(self):
        input = """
        Class Shape {
            getValue(){
                Var a: Int = 5;
                {
                    Out.printInt(a);
                    Out.printInt(a);
                }
            }
        }
        """
        expect = "Error on line 5 col 16: {"
        self.assertTrue(TestParser.test(input,expect,218))

    def test19(self):
        input = """
        Class Shape {
            getValue()(){
                Var a: Int = 5;
                {
                    Out.printInt(a);
                    Out.printInt(a);
                }
            }
        }
        """
        expect = "Error on line 3 col 22: ("
        self.assertTrue(TestParser.test(input,expect,219))

    def test20(self):
        input = """
        Class Shape {
            getValue(()){
            }
        }
        """
        expect = "Error on line 3 col 21: ("
        self.assertTrue(TestParser.test(input,expect,220))

    def test21(self):
        input = """
        Class Shape {
            getValue(){
                Foreach(i In 1 .. 10 By 2){
                    Foreach(j In 1 .. 10 By 2){
                        Out.printInt(i,j);
                        }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test22(self):
        input = """
        Class Shape {
            Var a:B = New B();
            getValue(){
                Var a: Int = 5;
                If( 1 <= (2 && 5) >= 6 || 3 == 3){
                    a = 2;
                }
                Elseif( 1<= 2 && 5 >= 6){
                    a=2;
                    a = New B();
                    Var a: $B = New B();
                }
            }
        }
        """
        expect = "Error on line 12 col 27: $B"
        self.assertTrue(TestParser.test(input,expect,222))