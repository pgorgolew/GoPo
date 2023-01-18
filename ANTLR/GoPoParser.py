# Generated from GoPo.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,63,311,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,0,1,1,1,1,5,1,
        68,8,1,10,1,12,1,71,9,1,1,2,1,2,1,2,1,3,1,3,1,3,3,3,79,8,3,1,4,1,
        4,3,4,83,8,4,1,5,1,5,3,5,87,8,5,1,5,1,5,1,5,3,5,92,8,5,1,5,1,5,3,
        5,96,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,106,8,7,10,7,12,7,109,
        9,7,1,7,1,7,3,7,113,8,7,1,8,1,8,1,8,1,9,3,9,119,8,9,1,9,1,9,1,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,3,12,133,8,12,1,12,
        3,12,136,8,12,1,13,1,13,1,13,1,13,1,13,3,13,143,8,13,1,13,3,13,146,
        8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,
        159,8,13,3,13,161,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,179,8,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,5,14,202,8,14,10,14,12,14,205,9,14,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,217,8,15,1,
        16,1,16,1,16,1,16,1,16,1,16,5,16,225,8,16,10,16,12,16,228,9,16,3,
        16,230,8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,
        18,1,18,3,18,244,8,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,
        20,1,20,1,20,1,20,1,21,1,21,1,21,3,21,261,8,21,1,21,1,21,1,22,1,
        22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,
        25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,3,
        27,292,8,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,
        29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,0,1,28,31,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,0,7,1,0,29,31,1,0,27,28,1,0,23,26,1,0,21,22,1,0,43,44,1,0,
        27,33,1,0,21,26,330,0,62,1,0,0,0,2,69,1,0,0,0,4,72,1,0,0,0,6,78,
        1,0,0,0,8,82,1,0,0,0,10,95,1,0,0,0,12,97,1,0,0,0,14,101,1,0,0,0,
        16,114,1,0,0,0,18,118,1,0,0,0,20,122,1,0,0,0,22,125,1,0,0,0,24,132,
        1,0,0,0,26,160,1,0,0,0,28,178,1,0,0,0,30,216,1,0,0,0,32,218,1,0,
        0,0,34,233,1,0,0,0,36,238,1,0,0,0,38,247,1,0,0,0,40,253,1,0,0,0,
        42,257,1,0,0,0,44,264,1,0,0,0,46,268,1,0,0,0,48,272,1,0,0,0,50,277,
        1,0,0,0,52,281,1,0,0,0,54,285,1,0,0,0,56,295,1,0,0,0,58,300,1,0,
        0,0,60,305,1,0,0,0,62,63,3,2,1,0,63,64,5,0,0,1,64,1,1,0,0,0,65,68,
        3,4,2,0,66,68,3,8,4,0,67,65,1,0,0,0,67,66,1,0,0,0,68,71,1,0,0,0,
        69,67,1,0,0,0,69,70,1,0,0,0,70,3,1,0,0,0,71,69,1,0,0,0,72,73,3,6,
        3,0,73,74,5,59,0,0,74,5,1,0,0,0,75,79,3,24,12,0,76,79,3,12,6,0,77,
        79,3,22,11,0,78,75,1,0,0,0,78,76,1,0,0,0,78,77,1,0,0,0,79,7,1,0,
        0,0,80,83,3,14,7,0,81,83,3,20,10,0,82,80,1,0,0,0,82,81,1,0,0,0,83,
        9,1,0,0,0,84,86,5,39,0,0,85,87,5,59,0,0,86,85,1,0,0,0,86,87,1,0,
        0,0,87,88,1,0,0,0,88,89,3,2,1,0,89,91,5,40,0,0,90,92,5,59,0,0,91,
        90,1,0,0,0,91,92,1,0,0,0,92,96,1,0,0,0,93,96,3,4,2,0,94,96,3,8,4,
        0,95,84,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,11,1,0,0,0,97,98,
        5,60,0,0,98,99,5,36,0,0,99,100,3,28,14,0,100,13,1,0,0,0,101,102,
        5,46,0,0,102,107,3,16,8,0,103,104,5,48,0,0,104,106,3,16,8,0,105,
        103,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,
        112,1,0,0,0,109,107,1,0,0,0,110,111,5,47,0,0,111,113,3,18,9,0,112,
        110,1,0,0,0,112,113,1,0,0,0,113,15,1,0,0,0,114,115,3,28,14,0,115,
        116,3,18,9,0,116,17,1,0,0,0,117,119,5,59,0,0,118,117,1,0,0,0,118,
        119,1,0,0,0,119,120,1,0,0,0,120,121,3,10,5,0,121,19,1,0,0,0,122,
        123,5,49,0,0,123,124,3,16,8,0,124,21,1,0,0,0,125,126,5,18,0,0,126,
        127,5,37,0,0,127,128,3,28,14,0,128,129,5,38,0,0,129,23,1,0,0,0,130,
        133,3,32,16,0,131,133,5,60,0,0,132,130,1,0,0,0,132,131,1,0,0,0,133,
        135,1,0,0,0,134,136,3,26,13,0,135,134,1,0,0,0,135,136,1,0,0,0,136,
        25,1,0,0,0,137,142,5,41,0,0,138,143,3,34,17,0,139,143,3,36,18,0,
        140,143,3,38,19,0,141,143,3,40,20,0,142,138,1,0,0,0,142,139,1,0,
        0,0,142,140,1,0,0,0,142,141,1,0,0,0,143,145,1,0,0,0,144,146,3,26,
        13,0,145,144,1,0,0,0,145,146,1,0,0,0,146,161,1,0,0,0,147,158,5,41,
        0,0,148,159,3,42,21,0,149,159,3,44,22,0,150,159,3,46,23,0,151,159,
        3,48,24,0,152,159,3,50,25,0,153,159,3,52,26,0,154,159,3,54,27,0,
        155,159,3,56,28,0,156,159,3,58,29,0,157,159,3,60,30,0,158,148,1,
        0,0,0,158,149,1,0,0,0,158,150,1,0,0,0,158,151,1,0,0,0,158,152,1,
        0,0,0,158,153,1,0,0,0,158,154,1,0,0,0,158,155,1,0,0,0,158,156,1,
        0,0,0,158,157,1,0,0,0,159,161,1,0,0,0,160,137,1,0,0,0,160,147,1,
        0,0,0,161,27,1,0,0,0,162,163,6,14,-1,0,163,164,5,28,0,0,164,179,
        3,28,14,11,165,166,5,35,0,0,166,179,3,28,14,10,167,168,5,33,0,0,
        168,169,5,37,0,0,169,170,3,28,14,0,170,171,5,38,0,0,171,179,1,0,
        0,0,172,173,5,34,0,0,173,174,5,37,0,0,174,175,3,28,14,0,175,176,
        5,38,0,0,176,179,1,0,0,0,177,179,3,30,15,0,178,162,1,0,0,0,178,165,
        1,0,0,0,178,167,1,0,0,0,178,172,1,0,0,0,178,177,1,0,0,0,179,203,
        1,0,0,0,180,181,10,12,0,0,181,182,5,32,0,0,182,202,3,28,14,13,183,
        184,10,9,0,0,184,185,7,0,0,0,185,202,3,28,14,10,186,187,10,8,0,0,
        187,188,7,1,0,0,188,202,3,28,14,9,189,190,10,5,0,0,190,191,7,2,0,
        0,191,202,3,28,14,6,192,193,10,4,0,0,193,194,7,3,0,0,194,202,3,28,
        14,5,195,196,10,3,0,0,196,197,5,20,0,0,197,202,3,28,14,4,198,199,
        10,2,0,0,199,200,5,19,0,0,200,202,3,28,14,3,201,180,1,0,0,0,201,
        183,1,0,0,0,201,186,1,0,0,0,201,189,1,0,0,0,201,192,1,0,0,0,201,
        195,1,0,0,0,201,198,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,
        204,1,0,0,0,204,29,1,0,0,0,205,203,1,0,0,0,206,207,5,37,0,0,207,
        208,3,28,14,0,208,209,5,38,0,0,209,217,1,0,0,0,210,217,3,24,12,0,
        211,217,5,54,0,0,212,217,7,4,0,0,213,217,5,60,0,0,214,217,5,53,0,
        0,215,217,5,45,0,0,216,206,1,0,0,0,216,210,1,0,0,0,216,211,1,0,0,
        0,216,212,1,0,0,0,216,213,1,0,0,0,216,214,1,0,0,0,216,215,1,0,0,
        0,217,31,1,0,0,0,218,219,5,2,0,0,219,229,5,37,0,0,220,230,5,52,0,
        0,221,226,5,54,0,0,222,223,5,42,0,0,223,225,5,54,0,0,224,222,1,0,
        0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,227,230,1,0,
        0,0,228,226,1,0,0,0,229,220,1,0,0,0,229,221,1,0,0,0,229,230,1,0,
        0,0,230,231,1,0,0,0,231,232,5,38,0,0,232,33,1,0,0,0,233,234,5,3,
        0,0,234,235,5,37,0,0,235,236,7,1,0,0,236,237,5,38,0,0,237,35,1,0,
        0,0,238,239,5,4,0,0,239,243,5,37,0,0,240,241,7,5,0,0,241,244,5,54,
        0,0,242,244,5,34,0,0,243,240,1,0,0,0,243,242,1,0,0,0,244,245,1,0,
        0,0,245,246,5,38,0,0,246,37,1,0,0,0,247,248,5,5,0,0,248,249,5,37,
        0,0,249,250,7,6,0,0,250,251,5,54,0,0,251,252,5,38,0,0,252,39,1,0,
        0,0,253,254,5,7,0,0,254,255,5,37,0,0,255,256,5,38,0,0,256,41,1,0,
        0,0,257,258,5,8,0,0,258,260,5,37,0,0,259,261,5,54,0,0,260,259,1,
        0,0,0,260,261,1,0,0,0,261,262,1,0,0,0,262,263,5,38,0,0,263,43,1,
        0,0,0,264,265,5,11,0,0,265,266,5,37,0,0,266,267,5,38,0,0,267,45,
        1,0,0,0,268,269,5,12,0,0,269,270,5,37,0,0,270,271,5,38,0,0,271,47,
        1,0,0,0,272,273,5,17,0,0,273,274,5,37,0,0,274,275,5,54,0,0,275,276,
        5,38,0,0,276,49,1,0,0,0,277,278,5,16,0,0,278,279,5,37,0,0,279,280,
        5,38,0,0,280,51,1,0,0,0,281,282,5,15,0,0,282,283,5,37,0,0,283,284,
        5,38,0,0,284,53,1,0,0,0,285,286,5,14,0,0,286,287,5,37,0,0,287,288,
        5,60,0,0,288,291,5,1,0,0,289,292,3,6,3,0,290,292,3,10,5,0,291,289,
        1,0,0,0,291,290,1,0,0,0,292,293,1,0,0,0,293,294,5,38,0,0,294,55,
        1,0,0,0,295,296,5,13,0,0,296,297,5,37,0,0,297,298,5,54,0,0,298,299,
        5,38,0,0,299,57,1,0,0,0,300,301,5,9,0,0,301,302,5,37,0,0,302,303,
        5,54,0,0,303,304,5,38,0,0,304,59,1,0,0,0,305,306,5,10,0,0,306,307,
        5,37,0,0,307,308,5,54,0,0,308,309,5,38,0,0,309,61,1,0,0,0,25,67,
        69,78,82,86,91,95,107,112,118,132,135,142,145,158,160,178,201,203,
        216,226,229,243,260,291
    ]

class GoPoParser ( Parser ):

    grammarFileName = "GoPo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "'list'", "'sort'", "'map'", "'filter'", 
                     "'limit'", "'reverse'", "'drop'", "'remove'", "'removeAll'", 
                     "'count'", "'sum'", "'add'", "'forEach'", "'clear'", 
                     "'isEmpty'", "'contains'", "'print'", "'or'", "'and'", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", 
                     "'-'", "'*'", "'/'", "'mod'", "'pow'", "'abs'", "'log'", 
                     "'not'", "'='", "'('", "')'", "'{'", "'}'", "'.'", 
                     "','", "'true'", "'false'", "'none'", "'if'", "'else'", 
                     "<INVALID>", "'while'", "'func'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LIST", "SORT", "MAP", "FILTER", 
                      "LIMIT", "REVERSE", "DROP", "REMOVE", "REMOVE_ALL", 
                      "COUNT", "SUM", "ADD", "FOREACH", "CLEAR", "ISEMPTY", 
                      "CONTAINS", "PRINT", "OR", "AND", "EQ", "NEQ", "GT", 
                      "LT", "GTEQ", "LTEQ", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "POW", "ABS", "LOG", "NOT", "ASSIGN", "OPAR", 
                      "CPAR", "OBRACE", "CBRACE", "DOT", "COMMA", "TRUE", 
                      "FALSE", "NONE", "IF", "ELSE", "ELIF", "WHILE", "FUNC", 
                      "RETURN", "RANGE", "STRING", "NUMBER", "NUMBER_PLUS", 
                      "FLOAT", "INT", "NEWLINE", "NEWLINES", "ID", "COMMENT", 
                      "WHITESPACES", "ANY" ]

    RULE_parse = 0
    RULE_block_newline = 1
    RULE_stat_newline = 2
    RULE_stat = 3
    RULE_conditon_stat = 4
    RULE_stat_block_newline = 5
    RULE_assignment = 6
    RULE_if_stat = 7
    RULE_condition_block = 8
    RULE_condition_body = 9
    RULE_while_stat = 10
    RULE_print = 11
    RULE_list_expr = 12
    RULE_list_expr_rec = 13
    RULE_expression = 14
    RULE_atom = 15
    RULE_list = 16
    RULE_sort = 17
    RULE_map = 18
    RULE_filter = 19
    RULE_reverse = 20
    RULE_drop = 21
    RULE_count = 22
    RULE_sum = 23
    RULE_contains = 24
    RULE_is_empty = 25
    RULE_clear = 26
    RULE_foreach = 27
    RULE_add = 28
    RULE_remove = 29
    RULE_remove_all = 30

    ruleNames =  [ "parse", "block_newline", "stat_newline", "stat", "conditon_stat", 
                   "stat_block_newline", "assignment", "if_stat", "condition_block", 
                   "condition_body", "while_stat", "print", "list_expr", 
                   "list_expr_rec", "expression", "atom", "list", "sort", 
                   "map", "filter", "reverse", "drop", "count", "sum", "contains", 
                   "is_empty", "clear", "foreach", "add", "remove", "remove_all" ]

    EOF = Token.EOF
    T__0=1
    LIST=2
    SORT=3
    MAP=4
    FILTER=5
    LIMIT=6
    REVERSE=7
    DROP=8
    REMOVE=9
    REMOVE_ALL=10
    COUNT=11
    SUM=12
    ADD=13
    FOREACH=14
    CLEAR=15
    ISEMPTY=16
    CONTAINS=17
    PRINT=18
    OR=19
    AND=20
    EQ=21
    NEQ=22
    GT=23
    LT=24
    GTEQ=25
    LTEQ=26
    PLUS=27
    MINUS=28
    MULT=29
    DIV=30
    MOD=31
    POW=32
    ABS=33
    LOG=34
    NOT=35
    ASSIGN=36
    OPAR=37
    CPAR=38
    OBRACE=39
    CBRACE=40
    DOT=41
    COMMA=42
    TRUE=43
    FALSE=44
    NONE=45
    IF=46
    ELSE=47
    ELIF=48
    WHILE=49
    FUNC=50
    RETURN=51
    RANGE=52
    STRING=53
    NUMBER=54
    NUMBER_PLUS=55
    FLOAT=56
    INT=57
    NEWLINE=58
    NEWLINES=59
    ID=60
    COMMENT=61
    WHITESPACES=62
    ANY=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_newline(self):
            return self.getTypedRuleContext(GoPoParser.Block_newlineContext,0)


        def EOF(self):
            return self.getToken(GoPoParser.EOF, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = GoPoParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.block_newline()
            self.state = 63
            self.match(GoPoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoPoParser.Stat_newlineContext)
            else:
                return self.getTypedRuleContext(GoPoParser.Stat_newlineContext,i)


        def conditon_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoPoParser.Conditon_statContext)
            else:
                return self.getTypedRuleContext(GoPoParser.Conditon_statContext,i)


        def getRuleIndex(self):
            return GoPoParser.RULE_block_newline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_newline" ):
                listener.enterBlock_newline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_newline" ):
                listener.exitBlock_newline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_newline" ):
                return visitor.visitBlock_newline(self)
            else:
                return visitor.visitChildren(self)




    def block_newline(self):

        localctx = GoPoParser.Block_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block_newline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1153554823304708100) != 0:
                self.state = 67
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 18, 60]:
                    self.state = 65
                    self.stat_newline()
                    pass
                elif token in [46, 49]:
                    self.state = 66
                    self.conditon_stat()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self):
            return self.getTypedRuleContext(GoPoParser.StatContext,0)


        def NEWLINES(self):
            return self.getToken(GoPoParser.NEWLINES, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_stat_newline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_newline" ):
                listener.enterStat_newline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_newline" ):
                listener.exitStat_newline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_newline" ):
                return visitor.visitStat_newline(self)
            else:
                return visitor.visitChildren(self)




    def stat_newline(self):

        localctx = GoPoParser.Stat_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.stat()
            self.state = 73
            self.match(GoPoParser.NEWLINES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_expr(self):
            return self.getTypedRuleContext(GoPoParser.List_exprContext,0)


        def assignment(self):
            return self.getTypedRuleContext(GoPoParser.AssignmentContext,0)


        def print_(self):
            return self.getTypedRuleContext(GoPoParser.PrintContext,0)


        def getRuleIndex(self):
            return GoPoParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = GoPoParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditon_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stat(self):
            return self.getTypedRuleContext(GoPoParser.If_statContext,0)


        def while_stat(self):
            return self.getTypedRuleContext(GoPoParser.While_statContext,0)


        def getRuleIndex(self):
            return GoPoParser.RULE_conditon_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditon_stat" ):
                listener.enterConditon_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditon_stat" ):
                listener.exitConditon_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditon_stat" ):
                return visitor.visitConditon_stat(self)
            else:
                return visitor.visitChildren(self)




    def conditon_stat(self):

        localctx = GoPoParser.Conditon_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditon_stat)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.if_stat()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.while_stat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_block_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBRACE(self):
            return self.getToken(GoPoParser.OBRACE, 0)

        def block_newline(self):
            return self.getTypedRuleContext(GoPoParser.Block_newlineContext,0)


        def CBRACE(self):
            return self.getToken(GoPoParser.CBRACE, 0)

        def NEWLINES(self, i:int=None):
            if i is None:
                return self.getTokens(GoPoParser.NEWLINES)
            else:
                return self.getToken(GoPoParser.NEWLINES, i)

        def stat_newline(self):
            return self.getTypedRuleContext(GoPoParser.Stat_newlineContext,0)


        def conditon_stat(self):
            return self.getTypedRuleContext(GoPoParser.Conditon_statContext,0)


        def getRuleIndex(self):
            return GoPoParser.RULE_stat_block_newline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_block_newline" ):
                listener.enterStat_block_newline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_block_newline" ):
                listener.exitStat_block_newline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_block_newline" ):
                return visitor.visitStat_block_newline(self)
            else:
                return visitor.visitChildren(self)




    def stat_block_newline(self):

        localctx = GoPoParser.Stat_block_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stat_block_newline)
        self._la = 0 # Token type
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(GoPoParser.OBRACE)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==59:
                    self.state = 85
                    self.match(GoPoParser.NEWLINES)


                self.state = 88
                self.block_newline()
                self.state = 89
                self.match(GoPoParser.CBRACE)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==59:
                    self.state = 90
                    self.match(GoPoParser.NEWLINES)


                pass
            elif token in [2, 18, 60]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.stat_newline()
                pass
            elif token in [46, 49]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.conditon_stat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GoPoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(GoPoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(GoPoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GoPoParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = GoPoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(GoPoParser.ID)
            self.state = 98
            self.match(GoPoParser.ASSIGN)
            self.state = 99
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GoPoParser.IF, 0)

        def condition_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoPoParser.Condition_blockContext)
            else:
                return self.getTypedRuleContext(GoPoParser.Condition_blockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(GoPoParser.ELIF)
            else:
                return self.getToken(GoPoParser.ELIF, i)

        def ELSE(self):
            return self.getToken(GoPoParser.ELSE, 0)

        def condition_body(self):
            return self.getTypedRuleContext(GoPoParser.Condition_bodyContext,0)


        def getRuleIndex(self):
            return GoPoParser.RULE_if_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stat" ):
                listener.enterIf_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stat" ):
                listener.exitIf_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stat" ):
                return visitor.visitIf_stat(self)
            else:
                return visitor.visitChildren(self)




    def if_stat(self):

        localctx = GoPoParser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(GoPoParser.IF)
            self.state = 102
            self.condition_block()
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 103
                    self.match(GoPoParser.ELIF)
                    self.state = 104
                    self.condition_block() 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 110
                self.match(GoPoParser.ELSE)
                self.state = 111
                self.condition_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GoPoParser.ExpressionContext,0)


        def condition_body(self):
            return self.getTypedRuleContext(GoPoParser.Condition_bodyContext,0)


        def getRuleIndex(self):
            return GoPoParser.RULE_condition_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_block" ):
                listener.enterCondition_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_block" ):
                listener.exitCondition_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_block" ):
                return visitor.visitCondition_block(self)
            else:
                return visitor.visitChildren(self)




    def condition_block(self):

        localctx = GoPoParser.Condition_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.expression(0)
            self.state = 115
            self.condition_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat_block_newline(self):
            return self.getTypedRuleContext(GoPoParser.Stat_block_newlineContext,0)


        def NEWLINES(self):
            return self.getToken(GoPoParser.NEWLINES, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_condition_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_body" ):
                listener.enterCondition_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_body" ):
                listener.exitCondition_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_body" ):
                return visitor.visitCondition_body(self)
            else:
                return visitor.visitChildren(self)




    def condition_body(self):

        localctx = GoPoParser.Condition_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 117
                self.match(GoPoParser.NEWLINES)


            self.state = 120
            self.stat_block_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(GoPoParser.WHILE, 0)

        def condition_block(self):
            return self.getTypedRuleContext(GoPoParser.Condition_blockContext,0)


        def getRuleIndex(self):
            return GoPoParser.RULE_while_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stat" ):
                listener.enterWhile_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stat" ):
                listener.exitWhile_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stat" ):
                return visitor.visitWhile_stat(self)
            else:
                return visitor.visitChildren(self)




    def while_stat(self):

        localctx = GoPoParser.While_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(GoPoParser.WHILE)
            self.state = 123
            self.condition_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(GoPoParser.PRINT, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(GoPoParser.ExpressionContext,0)


        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = GoPoParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(GoPoParser.PRINT)
            self.state = 126
            self.match(GoPoParser.OPAR)
            self.state = 127
            self.expression(0)
            self.state = 128
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(GoPoParser.ListContext,0)


        def ID(self):
            return self.getToken(GoPoParser.ID, 0)

        def list_expr_rec(self):
            return self.getTypedRuleContext(GoPoParser.List_expr_recContext,0)


        def getRuleIndex(self):
            return GoPoParser.RULE_list_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_expr" ):
                listener.enterList_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_expr" ):
                listener.exitList_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = GoPoParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 130
                self.list_()
                pass
            elif token in [60]:
                self.state = 131
                self.match(GoPoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 134
                self.list_expr_rec()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expr_recContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(GoPoParser.DOT, 0)

        def sort(self):
            return self.getTypedRuleContext(GoPoParser.SortContext,0)


        def map_(self):
            return self.getTypedRuleContext(GoPoParser.MapContext,0)


        def filter_(self):
            return self.getTypedRuleContext(GoPoParser.FilterContext,0)


        def reverse(self):
            return self.getTypedRuleContext(GoPoParser.ReverseContext,0)


        def list_expr_rec(self):
            return self.getTypedRuleContext(GoPoParser.List_expr_recContext,0)


        def drop(self):
            return self.getTypedRuleContext(GoPoParser.DropContext,0)


        def count(self):
            return self.getTypedRuleContext(GoPoParser.CountContext,0)


        def sum_(self):
            return self.getTypedRuleContext(GoPoParser.SumContext,0)


        def contains(self):
            return self.getTypedRuleContext(GoPoParser.ContainsContext,0)


        def is_empty(self):
            return self.getTypedRuleContext(GoPoParser.Is_emptyContext,0)


        def clear(self):
            return self.getTypedRuleContext(GoPoParser.ClearContext,0)


        def foreach(self):
            return self.getTypedRuleContext(GoPoParser.ForeachContext,0)


        def add(self):
            return self.getTypedRuleContext(GoPoParser.AddContext,0)


        def remove(self):
            return self.getTypedRuleContext(GoPoParser.RemoveContext,0)


        def remove_all(self):
            return self.getTypedRuleContext(GoPoParser.Remove_allContext,0)


        def getRuleIndex(self):
            return GoPoParser.RULE_list_expr_rec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_expr_rec" ):
                listener.enterList_expr_rec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_expr_rec" ):
                listener.exitList_expr_rec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr_rec" ):
                return visitor.visitList_expr_rec(self)
            else:
                return visitor.visitChildren(self)




    def list_expr_rec(self):

        localctx = GoPoParser.List_expr_recContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_expr_rec)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(GoPoParser.DOT)
                self.state = 142
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 138
                    self.sort()
                    pass
                elif token in [4]:
                    self.state = 139
                    self.map_()
                    pass
                elif token in [5]:
                    self.state = 140
                    self.filter_()
                    pass
                elif token in [7]:
                    self.state = 141
                    self.reverse()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 145
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 144
                    self.list_expr_rec()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(GoPoParser.DOT)
                self.state = 158
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 148
                    self.drop()
                    pass
                elif token in [11]:
                    self.state = 149
                    self.count()
                    pass
                elif token in [12]:
                    self.state = 150
                    self.sum_()
                    pass
                elif token in [17]:
                    self.state = 151
                    self.contains()
                    pass
                elif token in [16]:
                    self.state = 152
                    self.is_empty()
                    pass
                elif token in [15]:
                    self.state = 153
                    self.clear()
                    pass
                elif token in [14]:
                    self.state = 154
                    self.foreach()
                    pass
                elif token in [13]:
                    self.state = 155
                    self.add()
                    pass
                elif token in [9]:
                    self.state = 156
                    self.remove()
                    pass
                elif token in [10]:
                    self.state = 157
                    self.remove_all()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(GoPoParser.MINUS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoPoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GoPoParser.ExpressionContext,i)


        def NOT(self):
            return self.getToken(GoPoParser.NOT, 0)

        def ABS(self):
            return self.getToken(GoPoParser.ABS, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def LOG(self):
            return self.getToken(GoPoParser.LOG, 0)

        def atom(self):
            return self.getTypedRuleContext(GoPoParser.AtomContext,0)


        def POW(self):
            return self.getToken(GoPoParser.POW, 0)

        def MULT(self):
            return self.getToken(GoPoParser.MULT, 0)

        def DIV(self):
            return self.getToken(GoPoParser.DIV, 0)

        def MOD(self):
            return self.getToken(GoPoParser.MOD, 0)

        def PLUS(self):
            return self.getToken(GoPoParser.PLUS, 0)

        def LTEQ(self):
            return self.getToken(GoPoParser.LTEQ, 0)

        def GTEQ(self):
            return self.getToken(GoPoParser.GTEQ, 0)

        def LT(self):
            return self.getToken(GoPoParser.LT, 0)

        def GT(self):
            return self.getToken(GoPoParser.GT, 0)

        def EQ(self):
            return self.getToken(GoPoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(GoPoParser.NEQ, 0)

        def AND(self):
            return self.getToken(GoPoParser.AND, 0)

        def OR(self):
            return self.getToken(GoPoParser.OR, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GoPoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 163
                self.match(GoPoParser.MINUS)
                self.state = 164
                self.expression(11)
                pass
            elif token in [35]:
                self.state = 165
                self.match(GoPoParser.NOT)
                self.state = 166
                self.expression(10)
                pass
            elif token in [33]:
                self.state = 167
                self.match(GoPoParser.ABS)
                self.state = 168
                self.match(GoPoParser.OPAR)
                self.state = 169
                self.expression(0)
                self.state = 170
                self.match(GoPoParser.CPAR)
                pass
            elif token in [34]:
                self.state = 172
                self.match(GoPoParser.LOG)
                self.state = 173
                self.match(GoPoParser.OPAR)
                self.state = 174
                self.expression(0)
                self.state = 175
                self.match(GoPoParser.CPAR)
                pass
            elif token in [2, 37, 43, 44, 45, 53, 54, 60]:
                self.state = 177
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 201
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = GoPoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 180
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 181
                        self.match(GoPoParser.POW)
                        self.state = 182
                        self.expression(13)
                        pass

                    elif la_ == 2:
                        localctx = GoPoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 183
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 184
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 185
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = GoPoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 186
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 187
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 188
                        self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = GoPoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 190
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 191
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = GoPoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 193
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 194
                        self.expression(5)
                        pass

                    elif la_ == 6:
                        localctx = GoPoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 195
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 196
                        self.match(GoPoParser.AND)
                        self.state = 197
                        self.expression(4)
                        pass

                    elif la_ == 7:
                        localctx = GoPoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 199
                        self.match(GoPoParser.OR)
                        self.state = 200
                        self.expression(3)
                        pass

             
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(GoPoParser.ExpressionContext,0)


        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def list_expr(self):
            return self.getTypedRuleContext(GoPoParser.List_exprContext,0)


        def NUMBER(self):
            return self.getToken(GoPoParser.NUMBER, 0)

        def TRUE(self):
            return self.getToken(GoPoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(GoPoParser.FALSE, 0)

        def ID(self):
            return self.getToken(GoPoParser.ID, 0)

        def STRING(self):
            return self.getToken(GoPoParser.STRING, 0)

        def NONE(self):
            return self.getToken(GoPoParser.NONE, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = GoPoParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(GoPoParser.OPAR)
                self.state = 207
                self.expression(0)
                self.state = 208
                self.match(GoPoParser.CPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.list_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.match(GoPoParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                _la = self._input.LA(1)
                if not(_la==43 or _la==44):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 213
                self.match(GoPoParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 214
                self.match(GoPoParser.STRING)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 215
                self.match(GoPoParser.NONE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(GoPoParser.LIST, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def RANGE(self):
            return self.getToken(GoPoParser.RANGE, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(GoPoParser.NUMBER)
            else:
                return self.getToken(GoPoParser.NUMBER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoPoParser.COMMA)
            else:
                return self.getToken(GoPoParser.COMMA, i)

        def getRuleIndex(self):
            return GoPoParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = GoPoParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(GoPoParser.LIST)
            self.state = 219
            self.match(GoPoParser.OPAR)
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.state = 220
                self.match(GoPoParser.RANGE)
                pass
            elif token in [54]:
                self.state = 221
                self.match(GoPoParser.NUMBER)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42:
                    self.state = 222
                    self.match(GoPoParser.COMMA)
                    self.state = 223
                    self.match(GoPoParser.NUMBER)
                    self.state = 228
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [38]:
                pass
            else:
                pass
            self.state = 231
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SORT(self):
            return self.getToken(GoPoParser.SORT, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def PLUS(self):
            return self.getToken(GoPoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GoPoParser.MINUS, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_sort

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSort" ):
                listener.enterSort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSort" ):
                listener.exitSort(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSort" ):
                return visitor.visitSort(self)
            else:
                return visitor.visitChildren(self)




    def sort(self):

        localctx = GoPoParser.SortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_sort)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(GoPoParser.SORT)
            self.state = 234
            self.match(GoPoParser.OPAR)
            self.state = 235
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 236
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP(self):
            return self.getToken(GoPoParser.MAP, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def LOG(self):
            return self.getToken(GoPoParser.LOG, 0)

        def NUMBER(self):
            return self.getToken(GoPoParser.NUMBER, 0)

        def ABS(self):
            return self.getToken(GoPoParser.ABS, 0)

        def POW(self):
            return self.getToken(GoPoParser.POW, 0)

        def MOD(self):
            return self.getToken(GoPoParser.MOD, 0)

        def DIV(self):
            return self.getToken(GoPoParser.DIV, 0)

        def MULT(self):
            return self.getToken(GoPoParser.MULT, 0)

        def MINUS(self):
            return self.getToken(GoPoParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(GoPoParser.PLUS, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_map

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap" ):
                listener.enterMap(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap" ):
                listener.exitMap(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap" ):
                return visitor.visitMap(self)
            else:
                return visitor.visitChildren(self)




    def map_(self):

        localctx = GoPoParser.MapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_map)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(GoPoParser.MAP)
            self.state = 239
            self.match(GoPoParser.OPAR)
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27, 28, 29, 30, 31, 32, 33]:
                self.state = 240
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 17045651456) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 241
                self.match(GoPoParser.NUMBER)
                pass
            elif token in [34]:
                self.state = 242
                self.match(GoPoParser.LOG)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 245
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(GoPoParser.FILTER, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def NUMBER(self):
            return self.getToken(GoPoParser.NUMBER, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def EQ(self):
            return self.getToken(GoPoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(GoPoParser.NEQ, 0)

        def GT(self):
            return self.getToken(GoPoParser.GT, 0)

        def LT(self):
            return self.getToken(GoPoParser.LT, 0)

        def GTEQ(self):
            return self.getToken(GoPoParser.GTEQ, 0)

        def LTEQ(self):
            return self.getToken(GoPoParser.LTEQ, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilter" ):
                listener.enterFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilter" ):
                listener.exitFilter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilter" ):
                return visitor.visitFilter(self)
            else:
                return visitor.visitChildren(self)




    def filter_(self):

        localctx = GoPoParser.FilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_filter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(GoPoParser.FILTER)
            self.state = 248
            self.match(GoPoParser.OPAR)
            self.state = 249
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 250
            self.match(GoPoParser.NUMBER)
            self.state = 251
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReverseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REVERSE(self):
            return self.getToken(GoPoParser.REVERSE, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_reverse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReverse" ):
                listener.enterReverse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReverse" ):
                listener.exitReverse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReverse" ):
                return visitor.visitReverse(self)
            else:
                return visitor.visitChildren(self)




    def reverse(self):

        localctx = GoPoParser.ReverseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_reverse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(GoPoParser.REVERSE)
            self.state = 254
            self.match(GoPoParser.OPAR)
            self.state = 255
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DROP(self):
            return self.getToken(GoPoParser.DROP, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def NUMBER(self):
            return self.getToken(GoPoParser.NUMBER, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_drop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrop" ):
                listener.enterDrop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrop" ):
                listener.exitDrop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrop" ):
                return visitor.visitDrop(self)
            else:
                return visitor.visitChildren(self)




    def drop(self):

        localctx = GoPoParser.DropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_drop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(GoPoParser.DROP)
            self.state = 258
            self.match(GoPoParser.OPAR)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 259
                self.match(GoPoParser.NUMBER)


            self.state = 262
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COUNT(self):
            return self.getToken(GoPoParser.COUNT, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_count

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCount" ):
                listener.enterCount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCount" ):
                listener.exitCount(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCount" ):
                return visitor.visitCount(self)
            else:
                return visitor.visitChildren(self)




    def count(self):

        localctx = GoPoParser.CountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_count)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(GoPoParser.COUNT)
            self.state = 265
            self.match(GoPoParser.OPAR)
            self.state = 266
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUM(self):
            return self.getToken(GoPoParser.SUM, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_sum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum" ):
                listener.enterSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum" ):
                listener.exitSum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)




    def sum_(self):

        localctx = GoPoParser.SumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_sum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(GoPoParser.SUM)
            self.state = 269
            self.match(GoPoParser.OPAR)
            self.state = 270
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContainsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTAINS(self):
            return self.getToken(GoPoParser.CONTAINS, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def NUMBER(self):
            return self.getToken(GoPoParser.NUMBER, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_contains

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContains" ):
                listener.enterContains(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContains" ):
                listener.exitContains(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContains" ):
                return visitor.visitContains(self)
            else:
                return visitor.visitChildren(self)




    def contains(self):

        localctx = GoPoParser.ContainsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_contains)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(GoPoParser.CONTAINS)
            self.state = 273
            self.match(GoPoParser.OPAR)
            self.state = 274
            self.match(GoPoParser.NUMBER)
            self.state = 275
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Is_emptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ISEMPTY(self):
            return self.getToken(GoPoParser.ISEMPTY, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_is_empty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIs_empty" ):
                listener.enterIs_empty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIs_empty" ):
                listener.exitIs_empty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIs_empty" ):
                return visitor.visitIs_empty(self)
            else:
                return visitor.visitChildren(self)




    def is_empty(self):

        localctx = GoPoParser.Is_emptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_is_empty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(GoPoParser.ISEMPTY)
            self.state = 278
            self.match(GoPoParser.OPAR)
            self.state = 279
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClearContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLEAR(self):
            return self.getToken(GoPoParser.CLEAR, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_clear

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClear" ):
                listener.enterClear(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClear" ):
                listener.exitClear(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClear" ):
                return visitor.visitClear(self)
            else:
                return visitor.visitChildren(self)




    def clear(self):

        localctx = GoPoParser.ClearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_clear)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(GoPoParser.CLEAR)
            self.state = 282
            self.match(GoPoParser.OPAR)
            self.state = 283
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForeachContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(GoPoParser.FOREACH, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def ID(self):
            return self.getToken(GoPoParser.ID, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def stat(self):
            return self.getTypedRuleContext(GoPoParser.StatContext,0)


        def stat_block_newline(self):
            return self.getTypedRuleContext(GoPoParser.Stat_block_newlineContext,0)


        def getRuleIndex(self):
            return GoPoParser.RULE_foreach

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForeach" ):
                listener.enterForeach(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForeach" ):
                listener.exitForeach(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach" ):
                return visitor.visitForeach(self)
            else:
                return visitor.visitChildren(self)




    def foreach(self):

        localctx = GoPoParser.ForeachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_foreach)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(GoPoParser.FOREACH)
            self.state = 286
            self.match(GoPoParser.OPAR)
            self.state = 287
            self.match(GoPoParser.ID)
            self.state = 288
            self.match(GoPoParser.T__0)
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 289
                self.stat()
                pass

            elif la_ == 2:
                self.state = 290
                self.stat_block_newline()
                pass


            self.state = 293
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(GoPoParser.ADD, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def NUMBER(self):
            return self.getToken(GoPoParser.NUMBER, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)




    def add(self):

        localctx = GoPoParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(GoPoParser.ADD)
            self.state = 296
            self.match(GoPoParser.OPAR)
            self.state = 297
            self.match(GoPoParser.NUMBER)
            self.state = 298
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RemoveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REMOVE(self):
            return self.getToken(GoPoParser.REMOVE, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def NUMBER(self):
            return self.getToken(GoPoParser.NUMBER, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_remove

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemove" ):
                listener.enterRemove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemove" ):
                listener.exitRemove(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemove" ):
                return visitor.visitRemove(self)
            else:
                return visitor.visitChildren(self)




    def remove(self):

        localctx = GoPoParser.RemoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_remove)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(GoPoParser.REMOVE)
            self.state = 301
            self.match(GoPoParser.OPAR)
            self.state = 302
            self.match(GoPoParser.NUMBER)
            self.state = 303
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Remove_allContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REMOVE_ALL(self):
            return self.getToken(GoPoParser.REMOVE_ALL, 0)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)

        def NUMBER(self):
            return self.getToken(GoPoParser.NUMBER, 0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_remove_all

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemove_all" ):
                listener.enterRemove_all(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemove_all" ):
                listener.exitRemove_all(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemove_all" ):
                return visitor.visitRemove_all(self)
            else:
                return visitor.visitChildren(self)




    def remove_all(self):

        localctx = GoPoParser.Remove_allContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_remove_all)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(GoPoParser.REMOVE_ALL)
            self.state = 306
            self.match(GoPoParser.OPAR)
            self.state = 307
            self.match(GoPoParser.NUMBER)
            self.state = 308
            self.match(GoPoParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




