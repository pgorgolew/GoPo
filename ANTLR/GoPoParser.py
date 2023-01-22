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
        4,1,62,321,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,0,1,1,1,1,5,1,
        68,8,1,10,1,12,1,71,9,1,1,2,1,2,1,2,1,3,1,3,1,3,3,3,79,8,3,1,4,1,
        4,3,4,83,8,4,1,5,1,5,3,5,87,8,5,1,5,1,5,1,5,3,5,92,8,5,1,5,1,5,3,
        5,96,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,106,8,7,10,7,12,7,109,
        9,7,1,7,1,7,3,7,113,8,7,1,8,1,8,1,8,1,9,3,9,119,8,9,1,9,1,9,1,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,3,12,133,8,12,1,12,
        1,12,3,12,137,8,12,1,13,1,13,1,13,1,13,1,13,3,13,144,8,13,1,13,3,
        13,147,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,3,13,160,8,13,3,13,162,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        3,14,184,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,207,
        8,14,10,14,12,14,210,9,14,1,15,1,15,1,15,1,15,1,15,1,15,3,15,218,
        8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,229,8,16,
        10,16,12,16,232,9,16,1,16,1,16,1,16,1,16,3,16,238,8,16,1,17,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,
        254,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,3,21,273,8,21,1,22,1,22,1,22,1,22,
        1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,
        1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,302,8,27,
        1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,30,
        1,30,1,30,1,30,1,30,1,30,0,1,28,31,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,0,8,1,0,
        29,31,1,0,27,28,1,0,23,26,1,0,21,22,1,0,43,44,1,0,27,32,1,0,33,34,
        1,0,21,26,340,0,62,1,0,0,0,2,69,1,0,0,0,4,72,1,0,0,0,6,78,1,0,0,
        0,8,82,1,0,0,0,10,95,1,0,0,0,12,97,1,0,0,0,14,101,1,0,0,0,16,114,
        1,0,0,0,18,118,1,0,0,0,20,122,1,0,0,0,22,125,1,0,0,0,24,136,1,0,
        0,0,26,161,1,0,0,0,28,183,1,0,0,0,30,217,1,0,0,0,32,237,1,0,0,0,
        34,239,1,0,0,0,36,253,1,0,0,0,38,255,1,0,0,0,40,261,1,0,0,0,42,272,
        1,0,0,0,44,274,1,0,0,0,46,278,1,0,0,0,48,282,1,0,0,0,50,287,1,0,
        0,0,52,291,1,0,0,0,54,295,1,0,0,0,56,305,1,0,0,0,58,310,1,0,0,0,
        60,315,1,0,0,0,62,63,3,2,1,0,63,64,5,0,0,1,64,1,1,0,0,0,65,68,3,
        4,2,0,66,68,3,8,4,0,67,65,1,0,0,0,67,66,1,0,0,0,68,71,1,0,0,0,69,
        67,1,0,0,0,69,70,1,0,0,0,70,3,1,0,0,0,71,69,1,0,0,0,72,73,3,6,3,
        0,73,74,5,58,0,0,74,5,1,0,0,0,75,79,3,24,12,0,76,79,3,12,6,0,77,
        79,3,22,11,0,78,75,1,0,0,0,78,76,1,0,0,0,78,77,1,0,0,0,79,7,1,0,
        0,0,80,83,3,14,7,0,81,83,3,20,10,0,82,80,1,0,0,0,82,81,1,0,0,0,83,
        9,1,0,0,0,84,86,5,39,0,0,85,87,5,58,0,0,86,85,1,0,0,0,86,87,1,0,
        0,0,87,88,1,0,0,0,88,89,3,2,1,0,89,91,5,40,0,0,90,92,5,58,0,0,91,
        90,1,0,0,0,91,92,1,0,0,0,92,96,1,0,0,0,93,96,3,4,2,0,94,96,3,8,4,
        0,95,84,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,11,1,0,0,0,97,98,
        5,59,0,0,98,99,5,36,0,0,99,100,3,28,14,0,100,13,1,0,0,0,101,102,
        5,46,0,0,102,107,3,16,8,0,103,104,5,48,0,0,104,106,3,16,8,0,105,
        103,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,
        112,1,0,0,0,109,107,1,0,0,0,110,111,5,47,0,0,111,113,3,18,9,0,112,
        110,1,0,0,0,112,113,1,0,0,0,113,15,1,0,0,0,114,115,3,28,14,0,115,
        116,3,18,9,0,116,17,1,0,0,0,117,119,5,58,0,0,118,117,1,0,0,0,118,
        119,1,0,0,0,119,120,1,0,0,0,120,121,3,10,5,0,121,19,1,0,0,0,122,
        123,5,49,0,0,123,124,3,16,8,0,124,21,1,0,0,0,125,126,5,18,0,0,126,
        127,5,37,0,0,127,128,3,28,14,0,128,129,5,38,0,0,129,23,1,0,0,0,130,
        132,3,32,16,0,131,133,3,26,13,0,132,131,1,0,0,0,132,133,1,0,0,0,
        133,137,1,0,0,0,134,135,5,59,0,0,135,137,3,26,13,0,136,130,1,0,0,
        0,136,134,1,0,0,0,137,25,1,0,0,0,138,143,5,41,0,0,139,144,3,34,17,
        0,140,144,3,36,18,0,141,144,3,38,19,0,142,144,3,40,20,0,143,139,
        1,0,0,0,143,140,1,0,0,0,143,141,1,0,0,0,143,142,1,0,0,0,144,146,
        1,0,0,0,145,147,3,26,13,0,146,145,1,0,0,0,146,147,1,0,0,0,147,162,
        1,0,0,0,148,159,5,41,0,0,149,160,3,42,21,0,150,160,3,44,22,0,151,
        160,3,46,23,0,152,160,3,48,24,0,153,160,3,50,25,0,154,160,3,52,26,
        0,155,160,3,54,27,0,156,160,3,56,28,0,157,160,3,58,29,0,158,160,
        3,60,30,0,159,149,1,0,0,0,159,150,1,0,0,0,159,151,1,0,0,0,159,152,
        1,0,0,0,159,153,1,0,0,0,159,154,1,0,0,0,159,155,1,0,0,0,159,156,
        1,0,0,0,159,157,1,0,0,0,159,158,1,0,0,0,160,162,1,0,0,0,161,138,
        1,0,0,0,161,148,1,0,0,0,162,27,1,0,0,0,163,164,6,14,-1,0,164,165,
        5,37,0,0,165,166,3,28,14,0,166,167,5,38,0,0,167,184,1,0,0,0,168,
        169,5,28,0,0,169,184,3,28,14,11,170,171,5,33,0,0,171,172,5,37,0,
        0,172,173,3,28,14,0,173,174,5,38,0,0,174,184,1,0,0,0,175,176,5,34,
        0,0,176,177,5,37,0,0,177,178,3,28,14,0,178,179,5,38,0,0,179,184,
        1,0,0,0,180,181,5,35,0,0,181,184,3,28,14,2,182,184,3,30,15,0,183,
        163,1,0,0,0,183,168,1,0,0,0,183,170,1,0,0,0,183,175,1,0,0,0,183,
        180,1,0,0,0,183,182,1,0,0,0,184,208,1,0,0,0,185,186,10,13,0,0,186,
        187,5,32,0,0,187,207,3,28,14,14,188,189,10,8,0,0,189,190,7,0,0,0,
        190,207,3,28,14,9,191,192,10,7,0,0,192,193,7,1,0,0,193,207,3,28,
        14,8,194,195,10,6,0,0,195,196,7,2,0,0,196,207,3,28,14,7,197,198,
        10,5,0,0,198,199,7,3,0,0,199,207,3,28,14,6,200,201,10,4,0,0,201,
        202,5,20,0,0,202,207,3,28,14,5,203,204,10,3,0,0,204,205,5,19,0,0,
        205,207,3,28,14,4,206,185,1,0,0,0,206,188,1,0,0,0,206,191,1,0,0,
        0,206,194,1,0,0,0,206,197,1,0,0,0,206,200,1,0,0,0,206,203,1,0,0,
        0,207,210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,29,1,0,0,0,
        210,208,1,0,0,0,211,218,5,59,0,0,212,218,3,24,12,0,213,218,5,54,
        0,0,214,218,7,4,0,0,215,218,5,53,0,0,216,218,5,45,0,0,217,211,1,
        0,0,0,217,212,1,0,0,0,217,213,1,0,0,0,217,214,1,0,0,0,217,215,1,
        0,0,0,217,216,1,0,0,0,218,31,1,0,0,0,219,220,5,2,0,0,220,221,5,37,
        0,0,221,222,5,52,0,0,222,238,5,38,0,0,223,224,5,2,0,0,224,225,5,
        37,0,0,225,230,5,54,0,0,226,227,5,42,0,0,227,229,5,54,0,0,228,226,
        1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,233,
        1,0,0,0,232,230,1,0,0,0,233,238,5,38,0,0,234,235,5,2,0,0,235,236,
        5,37,0,0,236,238,5,38,0,0,237,219,1,0,0,0,237,223,1,0,0,0,237,234,
        1,0,0,0,238,33,1,0,0,0,239,240,5,3,0,0,240,241,5,37,0,0,241,242,
        7,1,0,0,242,243,5,38,0,0,243,35,1,0,0,0,244,245,5,4,0,0,245,246,
        5,37,0,0,246,247,7,5,0,0,247,248,5,54,0,0,248,254,5,38,0,0,249,250,
        5,4,0,0,250,251,5,37,0,0,251,252,7,6,0,0,252,254,5,38,0,0,253,244,
        1,0,0,0,253,249,1,0,0,0,254,37,1,0,0,0,255,256,5,5,0,0,256,257,5,
        37,0,0,257,258,7,7,0,0,258,259,5,54,0,0,259,260,5,38,0,0,260,39,
        1,0,0,0,261,262,5,7,0,0,262,263,5,37,0,0,263,264,5,38,0,0,264,41,
        1,0,0,0,265,266,5,8,0,0,266,267,5,37,0,0,267,273,5,38,0,0,268,269,
        5,8,0,0,269,270,5,37,0,0,270,271,5,54,0,0,271,273,5,38,0,0,272,265,
        1,0,0,0,272,268,1,0,0,0,273,43,1,0,0,0,274,275,5,11,0,0,275,276,
        5,37,0,0,276,277,5,38,0,0,277,45,1,0,0,0,278,279,5,12,0,0,279,280,
        5,37,0,0,280,281,5,38,0,0,281,47,1,0,0,0,282,283,5,17,0,0,283,284,
        5,37,0,0,284,285,5,54,0,0,285,286,5,38,0,0,286,49,1,0,0,0,287,288,
        5,16,0,0,288,289,5,37,0,0,289,290,5,38,0,0,290,51,1,0,0,0,291,292,
        5,15,0,0,292,293,5,37,0,0,293,294,5,38,0,0,294,53,1,0,0,0,295,296,
        5,14,0,0,296,297,5,37,0,0,297,298,5,59,0,0,298,301,5,1,0,0,299,302,
        3,6,3,0,300,302,3,10,5,0,301,299,1,0,0,0,301,300,1,0,0,0,302,303,
        1,0,0,0,303,304,5,38,0,0,304,55,1,0,0,0,305,306,5,13,0,0,306,307,
        5,37,0,0,307,308,5,54,0,0,308,309,5,38,0,0,309,57,1,0,0,0,310,311,
        5,9,0,0,311,312,5,37,0,0,312,313,5,54,0,0,313,314,5,38,0,0,314,59,
        1,0,0,0,315,316,5,10,0,0,316,317,5,37,0,0,317,318,5,54,0,0,318,319,
        5,38,0,0,319,61,1,0,0,0,25,67,69,78,82,86,91,95,107,112,118,132,
        136,143,146,159,161,183,206,208,217,230,237,253,272,301
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
                      "FLOAT", "INT", "NEWLINES", "ID", "COMMENT", "WHITESPACES", 
                      "ANY" ]

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
    NEWLINES=58
    ID=59
    COMMENT=60
    WHITESPACES=61
    ANY=62

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
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 577094071001284612) != 0:
                self.state = 67
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 18, 59]:
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
                if _la==58:
                    self.state = 85
                    self.match(GoPoParser.NEWLINES)


                self.state = 88
                self.block_newline()
                self.state = 89
                self.match(GoPoParser.CBRACE)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==58:
                    self.state = 90
                    self.match(GoPoParser.NEWLINES)


                pass
            elif token in [2, 18, 59]:
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
            self.if_block = None # Condition_blockContext
            self._condition_block = None # Condition_blockContext
            self.elif_blocks = list() # of Condition_blockContexts
            self.else_block = None # Condition_bodyContext

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
            localctx.if_block = self.condition_block()
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 103
                    self.match(GoPoParser.ELIF)
                    self.state = 104
                    localctx._condition_block = self.condition_block()
                    localctx.elif_blocks.append(localctx._condition_block) 
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
                localctx.else_block = self.condition_body()


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
            if _la==58:
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


        def list_expr_rec(self):
            return self.getTypedRuleContext(GoPoParser.List_expr_recContext,0)


        def ID(self):
            return self.getToken(GoPoParser.ID, 0)

        def getRuleIndex(self):
            return GoPoParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = GoPoParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_expr)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.list_()
                self.state = 132
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 131
                    self.list_expr_rec()


                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(GoPoParser.ID)
                self.state = 135
                self.list_expr_rec()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr_rec" ):
                return visitor.visitList_expr_rec(self)
            else:
                return visitor.visitChildren(self)




    def list_expr_rec(self):

        localctx = GoPoParser.List_expr_recContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_expr_rec)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(GoPoParser.DOT)
                self.state = 143
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 139
                    self.sort()
                    pass
                elif token in [4]:
                    self.state = 140
                    self.map_()
                    pass
                elif token in [5]:
                    self.state = 141
                    self.filter_()
                    pass
                elif token in [7]:
                    self.state = 142
                    self.reverse()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 146
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 145
                    self.list_expr_rec()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.match(GoPoParser.DOT)
                self.state = 159
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 149
                    self.drop()
                    pass
                elif token in [11]:
                    self.state = 150
                    self.count()
                    pass
                elif token in [12]:
                    self.state = 151
                    self.sum_()
                    pass
                elif token in [17]:
                    self.state = 152
                    self.contains()
                    pass
                elif token in [16]:
                    self.state = 153
                    self.is_empty()
                    pass
                elif token in [15]:
                    self.state = 154
                    self.clear()
                    pass
                elif token in [14]:
                    self.state = 155
                    self.foreach()
                    pass
                elif token in [13]:
                    self.state = 156
                    self.add()
                    pass
                elif token in [9]:
                    self.state = 157
                    self.remove()
                    pass
                elif token in [10]:
                    self.state = 158
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


        def getRuleIndex(self):
            return GoPoParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LogicExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoPoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GoPoParser.ExpressionContext,i)

        def NOT(self):
            return self.getToken(GoPoParser.NOT, 0)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr" ):
                return visitor.visitLogicExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParentnessExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)
        def expression(self):
            return self.getTypedRuleContext(GoPoParser.ExpressionContext,0)

        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentnessExpr" ):
                return visitor.visitParentnessExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(GoPoParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class MathExprLeftRightContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoPoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GoPoParser.ExpressionContext,i)

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
        def MINUS(self):
            return self.getToken(GoPoParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathExprLeftRight" ):
                return visitor.visitMathExprLeftRight(self)
            else:
                return visitor.visitChildren(self)


    class MathOneExprFunContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(GoPoParser.ExpressionContext,0)

        def MINUS(self):
            return self.getToken(GoPoParser.MINUS, 0)
        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)
        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)
        def ABS(self):
            return self.getToken(GoPoParser.ABS, 0)
        def LOG(self):
            return self.getToken(GoPoParser.LOG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathOneExprFun" ):
                return visitor.visitMathOneExprFun(self)
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
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                localctx = GoPoParser.ParentnessExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 164
                self.match(GoPoParser.OPAR)
                self.state = 165
                self.expression(0)
                self.state = 166
                self.match(GoPoParser.CPAR)
                pass
            elif token in [28]:
                localctx = GoPoParser.MathOneExprFunContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                localctx.op = self.match(GoPoParser.MINUS)
                self.state = 169
                self.expression(11)
                pass
            elif token in [33]:
                localctx = GoPoParser.MathOneExprFunContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 170
                localctx.op = self.match(GoPoParser.ABS)
                self.state = 171
                self.match(GoPoParser.OPAR)
                self.state = 172
                self.expression(0)
                self.state = 173
                self.match(GoPoParser.CPAR)
                pass
            elif token in [34]:
                localctx = GoPoParser.MathOneExprFunContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                localctx.op = self.match(GoPoParser.LOG)
                self.state = 176
                self.match(GoPoParser.OPAR)
                self.state = 177
                self.expression(0)
                self.state = 178
                self.match(GoPoParser.CPAR)
                pass
            elif token in [35]:
                localctx = GoPoParser.LogicExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 180
                localctx.op = self.match(GoPoParser.NOT)
                self.state = 181
                self.expression(2)
                pass
            elif token in [2, 43, 44, 45, 53, 54, 59]:
                localctx = GoPoParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 182
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 206
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = GoPoParser.MathExprLeftRightContext(self, GoPoParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 186
                        localctx.op = self.match(GoPoParser.POW)
                        self.state = 187
                        localctx.right = self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = GoPoParser.MathExprLeftRightContext(self, GoPoParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 188
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 189
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 190
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = GoPoParser.MathExprLeftRightContext(self, GoPoParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 191
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 192
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 193
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = GoPoParser.LogicExprContext(self, GoPoParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 194
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 195
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 196
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = GoPoParser.LogicExprContext(self, GoPoParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 197
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 198
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 199
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 6:
                        localctx = GoPoParser.LogicExprContext(self, GoPoParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 200
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 201
                        localctx.op = self.match(GoPoParser.AND)
                        self.state = 202
                        localctx.right = self.expression(5)
                        pass

                    elif la_ == 7:
                        localctx = GoPoParser.LogicExprContext(self, GoPoParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 203
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 204
                        localctx.op = self.match(GoPoParser.OR)
                        self.state = 205
                        localctx.right = self.expression(4)
                        pass

             
                self.state = 210
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


        def getRuleIndex(self):
            return GoPoParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(GoPoParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdAtom" ):
                return visitor.visitIdAtom(self)
            else:
                return visitor.visitChildren(self)


    class NoneAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NONE(self):
            return self.getToken(GoPoParser.NONE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoneAtom" ):
                return visitor.visitNoneAtom(self)
            else:
                return visitor.visitChildren(self)


    class ListExprAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_expr(self):
            return self.getTypedRuleContext(GoPoParser.List_exprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExprAtom" ):
                return visitor.visitListExprAtom(self)
            else:
                return visitor.visitChildren(self)


    class StringAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(GoPoParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringAtom" ):
                return visitor.visitStringAtom(self)
            else:
                return visitor.visitChildren(self)


    class BoolAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(GoPoParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(GoPoParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolAtom" ):
                return visitor.visitBoolAtom(self)
            else:
                return visitor.visitChildren(self)


    class NumberAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(GoPoParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberAtom" ):
                return visitor.visitNumberAtom(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = GoPoParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                localctx = GoPoParser.IdAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(GoPoParser.ID)
                pass

            elif la_ == 2:
                localctx = GoPoParser.ListExprAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.list_expr()
                pass

            elif la_ == 3:
                localctx = GoPoParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.match(GoPoParser.NUMBER)
                pass

            elif la_ == 4:
                localctx = GoPoParser.BoolAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                _la = self._input.LA(1)
                if not(_la==43 or _la==44):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 5:
                localctx = GoPoParser.StringAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 215
                self.match(GoPoParser.STRING)
                pass

            elif la_ == 6:
                localctx = GoPoParser.NoneAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 216
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


        def getRuleIndex(self):
            return GoPoParser.RULE_list

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EmptyListContext(ListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.ListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIST(self):
            return self.getToken(GoPoParser.LIST, 0)
        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)
        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyList" ):
                return visitor.visitEmptyList(self)
            else:
                return visitor.visitChildren(self)


    class RangeListContext(ListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.ListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIST(self):
            return self.getToken(GoPoParser.LIST, 0)
        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)
        def RANGE(self):
            return self.getToken(GoPoParser.RANGE, 0)
        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeList" ):
                return visitor.visitRangeList(self)
            else:
                return visitor.visitChildren(self)


    class NumbersListContext(ListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.ListContext
            super().__init__(parser)
            self._NUMBER = None # Token
            self.numbers = list() # of Tokens
            self.copyFrom(ctx)

        def LIST(self):
            return self.getToken(GoPoParser.LIST, 0)
        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)
        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumbersList" ):
                return visitor.visitNumbersList(self)
            else:
                return visitor.visitChildren(self)



    def list_(self):

        localctx = GoPoParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = GoPoParser.RangeListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(GoPoParser.LIST)
                self.state = 220
                self.match(GoPoParser.OPAR)
                self.state = 221
                self.match(GoPoParser.RANGE)
                self.state = 222
                self.match(GoPoParser.CPAR)
                pass

            elif la_ == 2:
                localctx = GoPoParser.NumbersListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(GoPoParser.LIST)
                self.state = 224
                self.match(GoPoParser.OPAR)
                self.state = 225
                localctx._NUMBER = self.match(GoPoParser.NUMBER)
                localctx.numbers.append(localctx._NUMBER)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42:
                    self.state = 226
                    self.match(GoPoParser.COMMA)
                    self.state = 227
                    localctx._NUMBER = self.match(GoPoParser.NUMBER)
                    localctx.numbers.append(localctx._NUMBER)
                    self.state = 232
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 233
                self.match(GoPoParser.CPAR)
                pass

            elif la_ == 3:
                localctx = GoPoParser.EmptyListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.match(GoPoParser.LIST)
                self.state = 235
                self.match(GoPoParser.OPAR)
                self.state = 236
                self.match(GoPoParser.CPAR)
                pass


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
            self.op = None # Token

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
            self.state = 239
            self.match(GoPoParser.SORT)
            self.state = 240
            self.match(GoPoParser.OPAR)
            self.state = 241
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 242
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


        def getRuleIndex(self):
            return GoPoParser.RULE_map

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MapOpWithoutNumContext(MapContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.MapContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def MAP(self):
            return self.getToken(GoPoParser.MAP, 0)
        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)
        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)
        def ABS(self):
            return self.getToken(GoPoParser.ABS, 0)
        def LOG(self):
            return self.getToken(GoPoParser.LOG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapOpWithoutNum" ):
                return visitor.visitMapOpWithoutNum(self)
            else:
                return visitor.visitChildren(self)


    class MapOpWithNumContext(MapContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.MapContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def MAP(self):
            return self.getToken(GoPoParser.MAP, 0)
        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)
        def NUMBER(self):
            return self.getToken(GoPoParser.NUMBER, 0)
        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapOpWithNum" ):
                return visitor.visitMapOpWithNum(self)
            else:
                return visitor.visitChildren(self)



    def map_(self):

        localctx = GoPoParser.MapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_map)
        self._la = 0 # Token type
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = GoPoParser.MapOpWithNumContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.match(GoPoParser.MAP)
                self.state = 245
                self.match(GoPoParser.OPAR)
                self.state = 246
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 8455716864) != 0):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.match(GoPoParser.NUMBER)
                self.state = 248
                self.match(GoPoParser.CPAR)
                pass

            elif la_ == 2:
                localctx = GoPoParser.MapOpWithoutNumContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(GoPoParser.MAP)
                self.state = 250
                self.match(GoPoParser.OPAR)
                self.state = 251
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==33 or _la==34):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 252
                self.match(GoPoParser.CPAR)
                pass


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
            self.op = None # Token

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
            self.state = 255
            self.match(GoPoParser.FILTER)
            self.state = 256
            self.match(GoPoParser.OPAR)
            self.state = 257
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 258
            self.match(GoPoParser.NUMBER)
            self.state = 259
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
            self.state = 261
            self.match(GoPoParser.REVERSE)
            self.state = 262
            self.match(GoPoParser.OPAR)
            self.state = 263
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


        def getRuleIndex(self):
            return GoPoParser.RULE_drop

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DropLastContext(DropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.DropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DROP(self):
            return self.getToken(GoPoParser.DROP, 0)
        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)
        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropLast" ):
                return visitor.visitDropLast(self)
            else:
                return visitor.visitChildren(self)


    class DropWithIndexContext(DropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GoPoParser.DropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DROP(self):
            return self.getToken(GoPoParser.DROP, 0)
        def OPAR(self):
            return self.getToken(GoPoParser.OPAR, 0)
        def NUMBER(self):
            return self.getToken(GoPoParser.NUMBER, 0)
        def CPAR(self):
            return self.getToken(GoPoParser.CPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropWithIndex" ):
                return visitor.visitDropWithIndex(self)
            else:
                return visitor.visitChildren(self)



    def drop(self):

        localctx = GoPoParser.DropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_drop)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = GoPoParser.DropLastContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(GoPoParser.DROP)
                self.state = 266
                self.match(GoPoParser.OPAR)
                self.state = 267
                self.match(GoPoParser.CPAR)
                pass

            elif la_ == 2:
                localctx = GoPoParser.DropWithIndexContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(GoPoParser.DROP)
                self.state = 269
                self.match(GoPoParser.OPAR)
                self.state = 270
                self.match(GoPoParser.NUMBER)
                self.state = 271
                self.match(GoPoParser.CPAR)
                pass


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
            self.state = 274
            self.match(GoPoParser.COUNT)
            self.state = 275
            self.match(GoPoParser.OPAR)
            self.state = 276
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
            self.state = 278
            self.match(GoPoParser.SUM)
            self.state = 279
            self.match(GoPoParser.OPAR)
            self.state = 280
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
            self.state = 282
            self.match(GoPoParser.CONTAINS)
            self.state = 283
            self.match(GoPoParser.OPAR)
            self.state = 284
            self.match(GoPoParser.NUMBER)
            self.state = 285
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
            self.state = 287
            self.match(GoPoParser.ISEMPTY)
            self.state = 288
            self.match(GoPoParser.OPAR)
            self.state = 289
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
            self.state = 291
            self.match(GoPoParser.CLEAR)
            self.state = 292
            self.match(GoPoParser.OPAR)
            self.state = 293
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
            self.state = 295
            self.match(GoPoParser.FOREACH)
            self.state = 296
            self.match(GoPoParser.OPAR)
            self.state = 297
            self.match(GoPoParser.ID)
            self.state = 298
            self.match(GoPoParser.T__0)
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 299
                self.stat()
                pass

            elif la_ == 2:
                self.state = 300
                self.stat_block_newline()
                pass


            self.state = 303
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
            self.state = 305
            self.match(GoPoParser.ADD)
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
            self.state = 310
            self.match(GoPoParser.REMOVE)
            self.state = 311
            self.match(GoPoParser.OPAR)
            self.state = 312
            self.match(GoPoParser.NUMBER)
            self.state = 313
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
            self.state = 315
            self.match(GoPoParser.REMOVE_ALL)
            self.state = 316
            self.match(GoPoParser.OPAR)
            self.state = 317
            self.match(GoPoParser.NUMBER)
            self.state = 318
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
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




