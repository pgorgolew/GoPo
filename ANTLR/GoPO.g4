grammar GoPo;

/*
 * Parser Rules
 */

parse
 : block EOF
 ;

block
 : stat*
 ;

stat
 : assignment
 | if_stat
 | while_stat
 | print
 ;

assignment		
  : ID ASSIGN expr NEWLINE
  ;

if_stat
  : IF condition_block (ELIF condition_block)* (ELSE stat_block)? NEWLINE
  ;

condition_block	
  : expr stat_block
  ;

stat_block		
  : OBRACE block CBRACE
  | stat
  ;

while_stat		
  : WHILE expr stat_block NEWLINE
  ;

func_stat
  : FUNC OPAR (ID (COMMA ID)*)? CPAR stat_block RETURN expr NEWLINE
  ;

print		
  : PRINT OPAR expr CPAR NEWLINE
  ;

expr
  : list_expr
  | casual_expr
  ;

list_expr
  : (list | ID) list_expr		
  | DOT sort list_expr
  | DOT map list_expr
  | DOT filter list_expr
  | DOT skip list_expr
  | DOT limit list_expr	
  | DOT reverse list_expr
  | DOT drop NEWLINE
  | DOT count NEWLINE
  | DOT sum NEWLINE
  | DOT contains NEWLINE
  | DOT isempty NEWLINE
  | DOT clear NEWLINE
  | DOT foreach NEWLINE				
  | DOT add NEWLINE				
  | NEWLINE					

casual_expr
 : casual_expr POW casual_expr			          	#powExpr
 | MINUS casual_expr                           			#unaryMinusExpr
 | NOT casual_expr                            		 	#notExpr
 | casual_expr op=(MULT | DIV | MOD) casual_expr      	#multiplicationExpr
 | casual_expr op=(PLUS | MINUS) casual_expr          	#additiveExpr
 | ABS OPAR casual_expr CPAR          	    			#absoluteExpr
 | LOG OPAR casual_expr CPAR			    			#log10Expr
 | casual_expr op=(LTEQ | GTEQ | LT | GT) casual_expr 	#relationalExpr
 | casual_expr op=(EQ | NEQ) casual_expr              	#equalityExpr
 | casual_expr AND casual_expr                        	#andExpr
 | casual_expr OR casual_expr                         	#orExpr
 | atom                                 				#atomExpr
 ;

atom
 : OPAR casual_expr CPAR #parExpr
 | NUMBER		#numberAtom
 | (TRUE | FALSE) #booleanAtom
 | ID             #idAtom
 | STRING         #stringAtom
 | NULL           #nullAtom
 ;

#LIST CREATION
list		: LIST OPAR ( RANGE | NUMBER (COMMA NUMBER)* )? CPAR;

#LISTS METHODS RETURNING LISTS
sort		: SORT OPAR (PLUS | MINUS) CPAR;
map		: MAP OPAR ((OPERATOR NUMBER) | LOG) CPAR;
filter	: FILTER OPAR COMPARATOR NUMBER CPAR;
skip		: SKIP OPAR NUMBER_PLUS CPAR;
limit		: LIMIT OPAR NUMBER_PLUS CPAR;
reverse	: REVERSE OPAR CPAR:

#LISTS METHODS RETURNING NUMBERS
drop		: DROP OPAR NUMBER CPAR;
count		: COUNT OPAR CPAR;
sum		: SUM OPAR CPAR;

#LISTS METHODS RETURNING BOOL
contains	: CONTAINS OPAR NUMBER CPAR;
isempty	: ISEMPTY OPAR CPAR;

#OTHERS LISTS METHODS
clear		: CLEAR OPAR CPAR;
foreach	: FOREACH OPAR ID '->' stat_block CPAR;
add		: ADD OPAR NUMBER CPAR;

/*
 * Lexer Rules
 */

#LISTS KEYWORDS
LIST		: 'list';
SORT		: 'sort';
MAP		: 'map';
FILTER	: 'filter';
SKIP		: 'skip';
LIMIT		: 'limit';
REVERSE	: 'reverse';
DROP		: 'drop';
COUNT		: 'count';
SUM		: 'sum';
ADD		: 'add';
FOREACH	: 'foreach';
CLEAR		: 'clear';
ISEMPTY	: 'isEmpty';
CONTAINS	: 'contains';

OPERATOR	: ABS | POW | MOD | DIV | MULT | MINUS | PLUS;
COMPARATOR	: EQ | NEQ | GT | LT | GTEQ | LTEQ;
PRINT		: 'print';

OR 		: 'or';
AND 		: 'and';
EQ 		: '==';
NEQ 		: '!=';
GT 		: '>';
LT 		: '<';
GTEQ 		: '>=';
LTEQ 		: '<=';
PLUS 		: '+';
MINUS 	: '-';
MULT 		: '*';
DIV 		: '/';
MOD 		: 'mod';
POW 		: 'pow';
ABS		: 'abs';
LOG 		: 'log';
NOT 		: '!';

SCOL 		: ';';
ASSIGN 	: '=';
OPAR 		: '(';
CPAR 		: ')';
OBRACE 	: '{';
CBRACE 	: '}';
DOT		: '.';
COMMA		: ',';

TRUE 		: 'true';
FALSE 	: 'false';
NONE 		: 'none';
IF 		: 'if';
ELSE 		: 'else';
ELIF		: 'elif' | 'else if';
WHILE 	: 'while';
FUNC		: 'func';
RETURN	: 'return';

RANGE		: NUMBER '...' NUMBER;
STRING	: '"' (~["\r\n] | '""')* '"' ;
NUMBER_PLUS : FLOAT | INT;
NUMBER	: '-'? NUMBER_PLUS;
FLOAT		: (INT | DIGIT) '.' DIGIT*;
INT		: DIGITPLUS DIGIT* ;
NEWLINE 	: [\r\n]+ ;
DIGIT_PLUS  : [1-9] ;
DIGIT		: 0 | DIGITPLUS ;
ID		: [a-zA-Z_] [a-zA-Z_0-9]* ;
COMMENT	: '#' ~[\r\n]* -> skip ;
WHITESPACES : [ \t]+ -> skip ;
