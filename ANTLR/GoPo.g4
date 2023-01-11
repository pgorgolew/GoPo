grammar GoPo;

/*
 * Parser Rules
 */

parse
 : block_newline EOF
 ;

block_newline
 : (stat_newline | conditon_stat)*
 ;

stat_newline
 : stat NEWLINES
 ;

stat
 : list_expr
 | assignment
 | print
 ;

conditon_stat
  : if_stat
  | while_stat
  ;

stat_block_newline
  : OBRACE NEWLINES? block_newline CBRACE NEWLINES?
  | stat_newline
  | conditon_stat
  ;

assignment		
  : ID ASSIGN expression
  ;

if_stat
  : IF condition_block (ELIF condition_block)* (ELSE condition_body)?
  ;

condition_block	
  : expression condition_body
  ;

condition_body
  :  NEWLINES? stat_block_newline
  ;

while_stat
  : WHILE condition_block
  ;

print		
  : PRINT OPAR expression CPAR
  ;

list_expr
  :  (list | ID) list_expr_rec?
  ;

list_expr_rec
  : DOT (sort | map | filter | reverse) list_expr_rec?
  | DOT (drop | count | sum | contains | is_empty | clear | foreach | add | remove | remove_all)
  ;

expression
 : expression POW expression
 | MINUS expression
 | NOT expression
 | expression (MULT | DIV | MOD) expression
 | expression (PLUS | MINUS) expression
 | ABS OPAR expression CPAR
 | LOG OPAR expression CPAR
 | expression (LTEQ | GTEQ | LT | GT) expression
 | expression (EQ | NEQ) expression
 | expression AND expression
 | expression OR expression
 | atom
 ;

atom
 : OPAR expression CPAR
 | list_expr
 | NUMBER
 | (TRUE | FALSE)
 | ID
 | STRING
 | NONE
 ;

//LIST CREATION
list		: LIST OPAR ( RANGE | NUMBER (COMMA NUMBER)* )? CPAR;

//LISTS METHODS RETURNING LISTS
sort		: SORT OPAR (PLUS | MINUS) CPAR;
map		: MAP OPAR (((ABS | POW | MOD | DIV | MULT | MINUS | PLUS) NUMBER) | LOG) CPAR;
filter	: FILTER OPAR (EQ | NEQ | GT | LT | GTEQ | LTEQ) NUMBER CPAR;
reverse	: REVERSE OPAR CPAR;

//LISTS METHODS RETURNING NUMBERS
drop		: DROP OPAR NUMBER? CPAR; // NUMBER IS AN INDEX
count		: COUNT OPAR CPAR;
sum		    : SUM OPAR CPAR;

//LISTS METHODS RETURNING BOOL
contains	: CONTAINS OPAR NUMBER CPAR;
is_empty	    : ISEMPTY OPAR CPAR;

//OTHERS LISTS METHODS
clear		: CLEAR OPAR CPAR;
foreach	    : FOREACH OPAR ID '->' (stat | stat_block_newline)  CPAR;
add		    : ADD OPAR NUMBER CPAR;
remove      : REMOVE OPAR NUMBER CPAR; // NUMBER IS a VALUE IN LIST
remove_all  : REMOVE_ALL OPAR NUMBER CPAR; // NUMBER IS a VALUE IN LIST
/*
 * Lexer Rules
 */

//LISTS KEYWORDS
LIST		    : 'list';
SORT		    : 'sort';
MAP		        : 'map';
FILTER	        : 'filter';
LIMIT	    	: 'limit';
REVERSE	        : 'reverse';
DROP		    : 'drop';
REMOVE          : 'remove';
REMOVE_ALL      : 'removeAll';
COUNT		    : 'count';
SUM	    	    : 'sum';
ADD		        : 'add';
FOREACH	        : 'forEach';
CLEAR		    : 'clear';
ISEMPTY	        : 'isEmpty';
CONTAINS	    : 'contains';

PRINT		: 'print';

OR 		    : 'or';
AND 		: 'and';
EQ 		    : '==';
NEQ 		: '!=';
GT 		    : '>';
LT 		    : '<';
GTEQ 		: '>=';
LTEQ 		: '<=';
PLUS 		: '+';
MINUS       : '-';
MULT 		: '*';
DIV 		: '/';
MOD 		: 'mod';
POW 		: 'pow';
ABS		    : 'abs';
LOG 		: 'log';
NOT 		: 'not';

ASSIGN 	    : '=';
OPAR 		: '(';
CPAR 		: ')';
OBRACE 	    : '{';
CBRACE 	    : '}';
DOT		    : '.';
COMMA		: ',';

TRUE 		: 'true';
FALSE 	    : 'false';
NONE 		: 'none';
IF 		    : 'if';
ELSE 		: 'else';
ELIF		: 'elif' | 'else if';
WHILE 	    : 'while';

// not used right now
FUNC		: 'func';
RETURN	    : 'return';

RANGE	    	: NUMBER '...' NUMBER ;
STRING  	    : '"' (~["\r\n] | '""')* '"' ;
NUMBER  	    : '-'? NUMBER_PLUS;
NUMBER_PLUS     : FLOAT | INT;
FLOAT	    	: INT '.' [0-9]*;
INT		        : '0' | ([1-9] [0-9]*) ;
NEWLINE 	    : ('\r' | '\n') ;
NEWLINES 	    : NEWLINE+ ;
ID		        : [a-zA-Z_] [a-zA-Z_0-9]* ;
COMMENT	        : '#' ~[\r\n]* -> skip ;
WHITESPACES     : [ \t]+ -> skip ;
ANY             : . ;
