# Generated from GoPo.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GoPoParser import GoPoParser
else:
    from GoPoParser import GoPoParser

# This class defines a complete listener for a parse tree produced by GoPoParser.
class GoPoListener(ParseTreeListener):

    # Enter a parse tree produced by GoPoParser#parse.
    def enterParse(self, ctx:GoPoParser.ParseContext):
        pass

    # Exit a parse tree produced by GoPoParser#parse.
    def exitParse(self, ctx:GoPoParser.ParseContext):
        pass


    # Enter a parse tree produced by GoPoParser#block_newline.
    def enterBlock_newline(self, ctx:GoPoParser.Block_newlineContext):
        pass

    # Exit a parse tree produced by GoPoParser#block_newline.
    def exitBlock_newline(self, ctx:GoPoParser.Block_newlineContext):
        pass


    # Enter a parse tree produced by GoPoParser#stat_newline.
    def enterStat_newline(self, ctx:GoPoParser.Stat_newlineContext):
        pass

    # Exit a parse tree produced by GoPoParser#stat_newline.
    def exitStat_newline(self, ctx:GoPoParser.Stat_newlineContext):
        pass


    # Enter a parse tree produced by GoPoParser#stat.
    def enterStat(self, ctx:GoPoParser.StatContext):
        pass

    # Exit a parse tree produced by GoPoParser#stat.
    def exitStat(self, ctx:GoPoParser.StatContext):
        pass


    # Enter a parse tree produced by GoPoParser#conditon_stat.
    def enterConditon_stat(self, ctx:GoPoParser.Conditon_statContext):
        pass

    # Exit a parse tree produced by GoPoParser#conditon_stat.
    def exitConditon_stat(self, ctx:GoPoParser.Conditon_statContext):
        pass


    # Enter a parse tree produced by GoPoParser#stat_block_newline.
    def enterStat_block_newline(self, ctx:GoPoParser.Stat_block_newlineContext):
        pass

    # Exit a parse tree produced by GoPoParser#stat_block_newline.
    def exitStat_block_newline(self, ctx:GoPoParser.Stat_block_newlineContext):
        pass


    # Enter a parse tree produced by GoPoParser#assignment.
    def enterAssignment(self, ctx:GoPoParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GoPoParser#assignment.
    def exitAssignment(self, ctx:GoPoParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GoPoParser#if_stat.
    def enterIf_stat(self, ctx:GoPoParser.If_statContext):
        pass

    # Exit a parse tree produced by GoPoParser#if_stat.
    def exitIf_stat(self, ctx:GoPoParser.If_statContext):
        pass


    # Enter a parse tree produced by GoPoParser#condition_block.
    def enterCondition_block(self, ctx:GoPoParser.Condition_blockContext):
        pass

    # Exit a parse tree produced by GoPoParser#condition_block.
    def exitCondition_block(self, ctx:GoPoParser.Condition_blockContext):
        pass


    # Enter a parse tree produced by GoPoParser#condition_body.
    def enterCondition_body(self, ctx:GoPoParser.Condition_bodyContext):
        pass

    # Exit a parse tree produced by GoPoParser#condition_body.
    def exitCondition_body(self, ctx:GoPoParser.Condition_bodyContext):
        pass


    # Enter a parse tree produced by GoPoParser#while_stat.
    def enterWhile_stat(self, ctx:GoPoParser.While_statContext):
        pass

    # Exit a parse tree produced by GoPoParser#while_stat.
    def exitWhile_stat(self, ctx:GoPoParser.While_statContext):
        pass


    # Enter a parse tree produced by GoPoParser#print.
    def enterPrint(self, ctx:GoPoParser.PrintContext):
        pass

    # Exit a parse tree produced by GoPoParser#print.
    def exitPrint(self, ctx:GoPoParser.PrintContext):
        pass


    # Enter a parse tree produced by GoPoParser#list_expr.
    def enterList_expr(self, ctx:GoPoParser.List_exprContext):
        pass

    # Exit a parse tree produced by GoPoParser#list_expr.
    def exitList_expr(self, ctx:GoPoParser.List_exprContext):
        pass


    # Enter a parse tree produced by GoPoParser#list_expr_rec.
    def enterList_expr_rec(self, ctx:GoPoParser.List_expr_recContext):
        pass

    # Exit a parse tree produced by GoPoParser#list_expr_rec.
    def exitList_expr_rec(self, ctx:GoPoParser.List_expr_recContext):
        pass


    # Enter a parse tree produced by GoPoParser#expression.
    def enterExpression(self, ctx:GoPoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GoPoParser#expression.
    def exitExpression(self, ctx:GoPoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GoPoParser#atom.
    def enterAtom(self, ctx:GoPoParser.AtomContext):
        pass

    # Exit a parse tree produced by GoPoParser#atom.
    def exitAtom(self, ctx:GoPoParser.AtomContext):
        pass


    # Enter a parse tree produced by GoPoParser#list.
    def enterList(self, ctx:GoPoParser.ListContext):
        pass

    # Exit a parse tree produced by GoPoParser#list.
    def exitList(self, ctx:GoPoParser.ListContext):
        pass


    # Enter a parse tree produced by GoPoParser#sort.
    def enterSort(self, ctx:GoPoParser.SortContext):
        pass

    # Exit a parse tree produced by GoPoParser#sort.
    def exitSort(self, ctx:GoPoParser.SortContext):
        pass


    # Enter a parse tree produced by GoPoParser#map.
    def enterMap(self, ctx:GoPoParser.MapContext):
        pass

    # Exit a parse tree produced by GoPoParser#map.
    def exitMap(self, ctx:GoPoParser.MapContext):
        pass


    # Enter a parse tree produced by GoPoParser#filter.
    def enterFilter(self, ctx:GoPoParser.FilterContext):
        pass

    # Exit a parse tree produced by GoPoParser#filter.
    def exitFilter(self, ctx:GoPoParser.FilterContext):
        pass


    # Enter a parse tree produced by GoPoParser#reverse.
    def enterReverse(self, ctx:GoPoParser.ReverseContext):
        pass

    # Exit a parse tree produced by GoPoParser#reverse.
    def exitReverse(self, ctx:GoPoParser.ReverseContext):
        pass


    # Enter a parse tree produced by GoPoParser#drop.
    def enterDrop(self, ctx:GoPoParser.DropContext):
        pass

    # Exit a parse tree produced by GoPoParser#drop.
    def exitDrop(self, ctx:GoPoParser.DropContext):
        pass


    # Enter a parse tree produced by GoPoParser#count.
    def enterCount(self, ctx:GoPoParser.CountContext):
        pass

    # Exit a parse tree produced by GoPoParser#count.
    def exitCount(self, ctx:GoPoParser.CountContext):
        pass


    # Enter a parse tree produced by GoPoParser#sum.
    def enterSum(self, ctx:GoPoParser.SumContext):
        pass

    # Exit a parse tree produced by GoPoParser#sum.
    def exitSum(self, ctx:GoPoParser.SumContext):
        pass


    # Enter a parse tree produced by GoPoParser#contains.
    def enterContains(self, ctx:GoPoParser.ContainsContext):
        pass

    # Exit a parse tree produced by GoPoParser#contains.
    def exitContains(self, ctx:GoPoParser.ContainsContext):
        pass


    # Enter a parse tree produced by GoPoParser#is_empty.
    def enterIs_empty(self, ctx:GoPoParser.Is_emptyContext):
        pass

    # Exit a parse tree produced by GoPoParser#is_empty.
    def exitIs_empty(self, ctx:GoPoParser.Is_emptyContext):
        pass


    # Enter a parse tree produced by GoPoParser#clear.
    def enterClear(self, ctx:GoPoParser.ClearContext):
        pass

    # Exit a parse tree produced by GoPoParser#clear.
    def exitClear(self, ctx:GoPoParser.ClearContext):
        pass


    # Enter a parse tree produced by GoPoParser#foreach.
    def enterForeach(self, ctx:GoPoParser.ForeachContext):
        pass

    # Exit a parse tree produced by GoPoParser#foreach.
    def exitForeach(self, ctx:GoPoParser.ForeachContext):
        pass


    # Enter a parse tree produced by GoPoParser#add.
    def enterAdd(self, ctx:GoPoParser.AddContext):
        pass

    # Exit a parse tree produced by GoPoParser#add.
    def exitAdd(self, ctx:GoPoParser.AddContext):
        pass


    # Enter a parse tree produced by GoPoParser#remove.
    def enterRemove(self, ctx:GoPoParser.RemoveContext):
        pass

    # Exit a parse tree produced by GoPoParser#remove.
    def exitRemove(self, ctx:GoPoParser.RemoveContext):
        pass


    # Enter a parse tree produced by GoPoParser#remove_all.
    def enterRemove_all(self, ctx:GoPoParser.Remove_allContext):
        pass

    # Exit a parse tree produced by GoPoParser#remove_all.
    def exitRemove_all(self, ctx:GoPoParser.Remove_allContext):
        pass



del GoPoParser