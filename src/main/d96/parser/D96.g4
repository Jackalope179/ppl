grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// program: mptype 'main' LB RB LP body? RP EOF;

// Program declaration
program: decls EOF;

decls: class_declaration decls | class_declaration;

class_declaration: CLASS ID super_class LP (class_members | ) RP;
super_class: ':' ID | ;
class_members: cl_member class_members | cl_member;
cl_member: attr_decl | method_decl ;

/* Attribute declaration */ 
attr_decl: (VAL | VAR ) idlist ':' type_name ( '=' exprlist | ) SEMI;

/* Expression/ID list */ 
exprlist: expr COMMA exprlist | expr;
idlist: ID COMMA idlist |ID;

/* Constructor declaration */
constructor: CONSTRUCTOR LB (paramslist | ) RB blk_stmt;
destructor:  DESTRUCTOR LB RB blk_stmt;	

/* Method declaration */
method_decl: ID LB (paramslist | ) RB blk_stmt;
paramslist: params SEMI paramslist | params;
params: idlist ':' type_name;

/***
** Expression
***/

bool_expr: expr;
ari_expr: expr;
string_expr: expr;
rel_expr: expr;
idx_expr: expr;
mem_access_expr: expr;
ob_creation_expr: expr;

expr:  expr  (STR_CONCAT | STR_COMPARE) expr | expr1;
expr1: expr1 (EQ |  NEQ | LT | GT | LTE | GTE) expr1 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | RM) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: expr7  index_op | expr8;
index_op: LS expr RS 
		| LS expr RS index_op ;
expr8: expr DOT expr9
	| expr9 ACCESS expr9
	| expr DOT expr9 LB exprlist RB
	| expr9 ACCESS expr9 LB exprlist RB
	| expr9;
expr9: NEW expr10 LB exprlist RB |expr10;
expr10: SELF| operands;
operands: literals
		| ID
		| func_call_expr
		| expr;
		
/* Function call expression */
func_call_expr: ID LB (exprlist | ) RB;

/***
** Statements 
***/
stmt: assg_stm 
	| if_stm
	| for_stm
	| break_stm
	| continue_stm
	| return_stm
	| invocatoin_stm
	| blk_stmt ; 


/* Assignment statement */

assg_stm: assg_term '=' expr;
assg_term: ID | idx_expr;


/* If statement */
if_stm: IF LB bool_expr RB blk_stmt else_if_stm;

else_if_stm: ELSEIF bool_expr blk_stmt else_if_stm
			| ELSE stmt
			| ; 

/* For/In statement */

/* for statement */
for_stm: FOREACH LB ID IN exprf '..' exprf (BY exprf | ) RB blk_stmt;
exprf: INT;

/* Break statement */
break_stm: BREAK SEMI;

/* Continue statement */ 
continue_stm: CONTINUE SEMI;

/* Return statement */
return_stm: RETURN expr SEMI;

//  Invocation statement
invocatoin_stm: ID ACCESS ID LB exprlist RB SEMI;

/* Block statement */
blk_stmt: LP (stmtlist| ) RP;
stmtlist: stmt stmtlist| stmt; 


// Index expressions
element_expression: expr index_operators;
index_operators: expr  |  expr  index_operators;

/***
** Type and value 
***/
type_name: primitive_typ | array_typ | class_typ;

/* Primitive type */
primitive_typ: INTTYPE | FLOATTYPE | STRINGTYPE | BOOLTYPE ;

/* Array type */
array_typ: ARRAY LS typ ',' INT RS;
typ: primitive_typ | array_typ;


/* Class type */
class_typ: ID;



/* Program comment */
COMMENT: '##' .*? '##' -> skip;

/* ID */

/* Keywords */
SELF: 'Self';
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'ElseIf';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INTTYPE: 'Int';
FLOATTYPE: 'Float';
BOOLTYPE: 'Boolean';
STRINGTYPE: 'String';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';

MAIN: 'main';
PROGRAM: 'Program';


/*** 
 ** Operators 
*/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
RM: '%';


NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
ASSG: '=';
NEQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

STR_CONCAT: '+.';
STR_COMPARE: '==.';
DOT: '.';
ACCESS: '::';

/* Literals */

/* Float Literal */
literals: FLOAT | INT | STR | BOOL | array_literal;

fragment INTPART: INT_DEC;
fragment FRACPART: '.' (INT_DEC | );
fragment EXPART: [eE][+-]? INTPART;
FLOAT: INTPART FRACPART EXPART? |  (INTPART | FRACPART) EXPART;

/* Integer Literals */

INT: INT_DEC  | INT_OCTAL | INT_BINARY | INT_HEX;

INT_DEC: '0'|([1-9] | ([_][0-9]| [0-9])*){
	self.text = self.text.replace('_', '');
};
INT_HEX: '0'[xX][0-9a-fA-F]([-][0-9a-fA-F] | [0-9a-fA-F])*{
	self.text = self.text.replace('_', '');
};
INT_OCTAL: '0'[0-7]([_][0-7] | [0-7])*{
	self.text = self.text.replace('_', '');
};
INT_BINARY: '0'[bB][01]([_][01] | [01])*{
	self.text = self.text.replace('_', '');
};

/* Boolean Literal */
BOOL: 'True' | 'False';

/* String Literal */
STR: ('"' ('\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\\\' | '\'"' | ~["])* '"'){
	self.text = self.text[1:-1];
};

/** Array Literals
 ***/
array_literal: idxlit | mullit;

/* Indexed Array literal */
idxlit: ARRAY LB exprlist RB;

/* Multi Array literal */
mullit: ARRAY LB arrlist RB;
arrlist: arr COMMA arrlist | arr;
arr: idxlit | mullit; 

mptype: INTTYPE | VOIDTYPE;

body: funcall SEMI;

exp: funcall | INTLIT;

funcall: ID LB exp? RB;

// INTTYPE: 'int';

VOIDTYPE: 'void';

ID:  '$'?[a-zA-Z_][a-zA-Z0-9_]*;

// ID: [a-zA-Z]+;

INTLIT: [0-9]+;

LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

LS: '[';

RS: ']';

COMMA : ',';


WS: [ \t\r\n\f\b]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;



