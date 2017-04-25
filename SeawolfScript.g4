grammar SeawolfScript;
 
 prog:   '{' stat+ '}' ;
 
 stat:   'print('expr');' NEWLINE                # printExpr
     |   ID '=' expr';' NEWLINE	     # assign
     |   ID'['expr']''=' expr';' NEWLINE	# assignIndex
     |   ID'['expr']''['expr']''='expr';' NEWLINE # assignMatrix
     |   'if''('expr')''{'stat_block'}'('else''{'stat_block'}')? 	     #If
     |   'while''('expr')''{'stat_block'}'	#While
     |   NEWLINE                     # blank
     ;
 stat_block: stat+;

 expr:   '-' expr		#Negative	
     |'['expr(','expr)* ']' 	   #Array
     |	 expr '[' expr ']'  	#Index
     |	 expr op=('*'|'/') expr      # MulDiv
     |   expr '%' expr		    #Mod
     |   expr '**' expr             #Exponent
     |   expr '//' expr		     #Floor
     |   expr op=('+'|'-') expr      # AddSub
     |   expr 'in' expr		#In
     |   expr op=('<'|'<='|'>'|'>='|'=='|'<>') expr #Cond
     |   'not' expr		     # Not
     |   expr 'and' expr   # And
     | 	 expr 'or' expr		     # Or
     |   INT                         # int
     |   REAL			     # Real
     |   STRING			     # String
     |   ID                          # id
     |   '(' expr ')'                # parens
    
     ;
 
 EXPONENT: '**';
 MUL :   '*' ; // assigns token name to '*' used above in grammar
 DIV :   '/' ;
 FLOOR:  '//' ;
 MOD :   '%' ;
 ADD :   '+' ;
 SUB :   '-' ;
 AND :   'and';
 OR  :   'or';
 NOT :   'not';
 IN : 'in';
 LTHAN: '<';
 GTHAN: '>';
 LTHANE: '<=';
 GTHANE: '>=';
 EQUAL: '==';
 NEQUAL: '<>';
 ID  :   [a-zA-Z][A-Za-z0-9_]* ;      // match identifiers
 STRING : '"' (~[\r\n"] | '""')* '"';
 INT :   [0-9]+ ;         // match integers
 REAL : [0-9]+ '.' [0-9]+;
 NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
 WS  :   [\t ]+ -> skip ; // toss out whitespace