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
  : IF if_block=condition_block (ELIF elif_blocks+=condition_block)* (ELSE else_block=condition_body)?
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
  :  list list_expr_rec?
  |  ID list_expr_rec
  ;

list_expr_rec
  : DOT (sort | map | filter | reverse) list_expr_rec?
  | DOT (drop | count | sum | contains | is_empty | clear | foreach | add | remove | remove_all)
  ;

expression
 : left=expression op=POW right=expression                               #mathExprLeftRight
 | OPAR expression CPAR                                                  #parentnessExpr
 | op=MINUS expression                                                   #mathOneExprFun
 | op=ABS OPAR expression CPAR                                           #mathOneExprFun
 | op=LOG OPAR expression CPAR                                           #mathOneExprFun
 | left=expression op=(MULT | DIV | MOD) right=expression                #mathExprLeftRight
 | left=expression op=(PLUS | MINUS) right=expression                    #mathExprLeftRight
 | left=expression op=(LTEQ | GTEQ | LT | GT) right=expression           #logicExpr
 | left=expression op=(EQ | NEQ) right=expression                        #logicExpr
 | left=expression op=AND right=expression                               #logicExpr
 | left=expression op=OR right=expression                                #logicExpr
 | op=NOT expression                                                     #logicExpr
 | atom                                                                  #atomExpr
 ;

atom
 : ID                                                       #idAtom
 | list_expr                                                #listExprAtom
 | NUMBER                                                   #numberAtom
 | (TRUE | FALSE)                                           #boolAtom
 | STRING                                                   #stringAtom
 | NONE                                                     #noneAtom
 ;

//LIST CREATION
list
  : LIST OPAR RANGE CPAR                                                #rangeList
  | LIST OPAR numbers+=NUMBER (COMMA numbers+=NUMBER)* CPAR             #numbersList
  | LIST OPAR CPAR                                                      #emptyList
  ;

//LISTS METHODS RETURNING LISTS
sort		: SORT OPAR (PLUS | MINUS) CPAR;
map
  : MAP OPAR op=(POW | MOD | DIV | MULT | MINUS | PLUS) NUMBER CPAR         #mapOpWithNum
  | MAP OPAR op=(ABS| LOG) CPAR                                             #mapOpWithoutNum
  ;
filter	: FILTER OPAR op=(EQ | NEQ | GT | LT | GTEQ | LTEQ) NUMBER CPAR;
reverse	: REVERSE OPAR CPAR;

//LISTS METHODS RETURNING NUMBERS
drop
  : DROP OPAR CPAR                                                          #dropLast
  | DROP OPAR NUMBER CPAR                                                   #dropWithIndex
  ;
count		: COUNT OPAR CPAR;
sum		    : SUM OPAR CPAR;

//LISTS METHODS RETURNING BOOL
contains	: CONTAINS OPAR NUMBER CPAR;
is_empty	: ISEMPTY OPAR CPAR;

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

RANGE	    	: INT '...' INT ;
STRING  	    : '"' (~["\r\n] | '""')* '"' ;
NUMBER  	    : '-'? NUMBER_PLUS;
NUMBER_PLUS     : FLOAT | INT;
FLOAT	    	: INT '.' [0-9]*;
INT		        : '0' | ([1-9] [0-9]*) ;
NEWLINES	    : ('\r' | '\n')+ ;
ID		        : [a-zA-Z_] [a-zA-Z_0-9]* ;
COMMENT	        : '#' ~[\r\n]* -> skip ;
WHITESPACES     : [ \t]+ -> skip ;
ANY             : . ;
