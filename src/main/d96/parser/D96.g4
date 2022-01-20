grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// Program declaration
program: decls EOF;

decls: class_declaration decls | class_declaration;

class_declaration: CLASS ID (':' ID | ) LP (class_members | )  RP;
class_members: cl_member class_members | cl_member;
cl_member: attr_decl | method_decl ;

attr_decl: (VAL | VAR ) idlist ':' type_name ( '=' exprlist | ) SEMI;
method_decl: (SID | ID) LB (paramslist | ) RB blk_stmt | constructor | destructor;


exprlist: expr COMMA exprlist | expr;
idlist: (ID | SID) COMMA idlist | ID | SID;

constructor: CONSTRUCTOR LB (paramslist | ) RB nr_blk_stmt;
destructor:  DESTRUCTOR LB RB nr_blk_stmt;	

nr_blk_stmt: LP (stmtlists| ) RP;
stmtlists: nr_stmt stmtlists| nr_stmt; 
nr_stmt: assg_stm 
	| if_stm
	| for_stm
	| break_stm
	| continue_stm
	| invocatoin_stm
	| decl_stm;
paramslist: params SEMI paramslist | params;
params: non_st_idlist ':' type_name;
non_st_idlist:  ID COMMA idlist | ID ;

/*-------------------------------------------- Test 1------------------------------------------ */

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
expr8: expr8 DOT expr9
	| expr8 ACCESS expr9
	| expr8 DOT expr9 LB (exprlist | ) RB
	| expr8 ACCESS expr9 LB (exprlist| ) RB
	| expr9;
expr9: NEW ID LB (exprlist | ) RB | operands;
operands: LB expr RB
		| literals
		| ID
		| SID
		| SELF
		;

/*----------------------------------------- Statement -------------------------------------------*/
stmt: assg_stm 
	| if_stm
	| for_stm
	| break_stm
	| continue_stm
	| return_stm
	| invocatoin_stm
	| decl_stm;

decl_stm: (VAL | VAR ) non_st_idlist ':' type_name ( '=' exprlist | ) SEMI;

// /* Assignment statement */

assg_stm: assg_term '=' expr SEMI;
assg_term: expr;


// /* If statement */
if_stm: IF LB expr RB blk_stmt else_if_stm;

else_if_stm: ELSEIF LB expr RB blk_stmt else_if_stm
			| ELSE blk_stmt
			| ; 

// /* for statement */
for_stm: FOREACH LB (ID | SID) IN INT '..' INT (BY INT | ) RB blk_stmt;

// /* Break statement */
break_stm: BREAK SEMI;

// /* Continue statement */ 
continue_stm: CONTINUE SEMI;

// /* Return statement */
return_stm: RETURN expr SEMI;

// //  Invocation statement
invocatoin_stm: expr DOT (SID | ID) SEMI
			  | ID ACCESS SID SEMI
			  | expr DOT (SID | ID) LB (exprlist | ) RB SEMI
			  | ID ACCESS SID LB (exprlist | ) RB SEMI;

// /* Block statement */
blk_stmt: LP (stmtlist| ) RP;
stmtlist: stmt stmtlist| stmt; 


// // Index expressions
element_expression: expr index_operators;
index_operators: expr  |  expr  index_operators;

/*--------------------------type and value-----------------------------*/
type_name: primitive_typ | array_typ | class_typ;

primitive_typ: INTTYPE | FLOATTYPE | STRINGTYPE | BOOLTYPE ;

array_typ: ARRAY LS typ ',' INT RS;
typ: primitive_typ | array_typ;

class_typ: ID;

/*-------------------------------------------------------------------- */

literals: FLOAT | INT | STR | BOOL | array_literal;

/** Array Literals
 ***/
array_literal: idxlit | mullit;

/* Indexed Array literal */
idxlit: ARRAY LB exprlist RB;

/* Multi Array literal */
mullit: ARRAY LB arrlist RB;
arrlist: arr COMMA arrlist | arr;
arr: idxlit | mullit; 


/* --------------------------------------------------------------------------- */
mptype: INTTYPE | VOIDTYPE;

body: funcall SEMI;

exp: funcall | INTLIT;

funcall: ID LB exp? RB;


/*----------------------------------- Lexical -------------------------------------------*/

BOOL: TRUE | FALSE;

STR: ('"' ('\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\\\' | '\'"' | ~["\n\t\b\r\f\\])* '"'){
	self.text = self.text[1:-1];
};

// NUMBER: (FLOAT | INT){
// 	self.text = self.text.replace('_', '');
// };

fragment INTPART: INT_DEC;
fragment FRACPART: '.' (INT_DEC | );
fragment EXPART: [eE][+-]? INT_DEC;

FLOAT: (INTPART FRACPART EXPART? |  (INTPART | FRACPART) EXPART){
	self.text = self.text.replace('_', '');
};


INT: (INT_DEC | INT_OCTAL | INT_BINARY | INT_HEX){
	self.text = self.text.replace('_', '');
};


INT_DEC: '0'|([1-9]([_][0-9]| [0-9])*);
INT_HEX: ('0'[xX][0-9A-F]([_][0-9A-F] | [0-9A-F])*);
INT_OCTAL: ('0'[0-9]([_][0-9] | [0-9])*);
INT_BINARY: ('0'[bB][01]([_][01] | [01])*);

/* Program comment */
COMMENT: '##' .*? '##' -> skip;

/* Keywords */
SELF: 'Self';
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
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
ACCESS: '::';

VOIDTYPE: 'void';

ID:  [a-zA-Z_][a-zA-Z0-9_]*;

SID: '$'[a-zA-Z0-9_]+;

INTLIT: [0-9]+;

LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

LS: '[';

RS: ']';

DOT: '.';

COMMA : ',';


WS: [ \t\r\n\f\b]+ -> skip; // skip spaces, tabs, newlines

fragment CHARACTERS: (~[\n\r\t\f\b"] | '\\'[nrtfb'\\]);
fragment ERROR_CHAR:  [\n\r\t\f\b] |  EOF;

UNCLOSE_STRING: '"' CHARACTERS* ERROR_CHAR{
	if self.text[-1] in ['\n', '\r', '\t', '\f', '\b']:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};


ILLEGAL_ESCAPE: '"' CHARACTERS* '\\'~[nrtbf'\\]{
	raise IllegalEscape(self.text[1:])
};

ERROR_TOKEN: .{raise  ErrorToken(self.text)};



