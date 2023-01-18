# Generated from GoPo.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GoPoParser import GoPoParser
else:
    from GoPoParser import GoPoParser

# This class defines a complete generic visitor for a parse tree produced by GoPoParser.

class GoPoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GoPoParser#parse.
    def visitParse(self, ctx:GoPoParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#block_newline.
    def visitBlock_newline(self, ctx:GoPoParser.Block_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#stat_newline.
    def visitStat_newline(self, ctx:GoPoParser.Stat_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#stat.
    def visitStat(self, ctx:GoPoParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#conditon_stat.
    def visitConditon_stat(self, ctx:GoPoParser.Conditon_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#stat_block_newline.
    def visitStat_block_newline(self, ctx:GoPoParser.Stat_block_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#assignment.
    def visitAssignment(self, ctx:GoPoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#if_stat.
    def visitIf_stat(self, ctx:GoPoParser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#condition_block.
    def visitCondition_block(self, ctx:GoPoParser.Condition_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#condition_body.
    def visitCondition_body(self, ctx:GoPoParser.Condition_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#while_stat.
    def visitWhile_stat(self, ctx:GoPoParser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#print.
    def visitPrint(self, ctx:GoPoParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#list_expr.
    def visitList_expr(self, ctx:GoPoParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#list_expr_rec.
    def visitList_expr_rec(self, ctx:GoPoParser.List_expr_recContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#logicExpr.
    def visitLogicExpr(self, ctx:GoPoParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#parentnessExpr.
    def visitParentnessExpr(self, ctx:GoPoParser.ParentnessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#atomExpr.
    def visitAtomExpr(self, ctx:GoPoParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#mathExprLeftRight.
    def visitMathExprLeftRight(self, ctx:GoPoParser.MathExprLeftRightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#mathOneExprFun.
    def visitMathOneExprFun(self, ctx:GoPoParser.MathOneExprFunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#listExprAtom.
    def visitListExprAtom(self, ctx:GoPoParser.ListExprAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#numberAtom.
    def visitNumberAtom(self, ctx:GoPoParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#boolAtom.
    def visitBoolAtom(self, ctx:GoPoParser.BoolAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#idAtom.
    def visitIdAtom(self, ctx:GoPoParser.IdAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#stringAtom.
    def visitStringAtom(self, ctx:GoPoParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#noneAtom.
    def visitNoneAtom(self, ctx:GoPoParser.NoneAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#rangeList.
    def visitRangeList(self, ctx:GoPoParser.RangeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#numbersList.
    def visitNumbersList(self, ctx:GoPoParser.NumbersListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#emptyList.
    def visitEmptyList(self, ctx:GoPoParser.EmptyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#sort.
    def visitSort(self, ctx:GoPoParser.SortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#mapOpWithNum.
    def visitMapOpWithNum(self, ctx:GoPoParser.MapOpWithNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#mapOpWithoutNum.
    def visitMapOpWithoutNum(self, ctx:GoPoParser.MapOpWithoutNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#filter.
    def visitFilter(self, ctx:GoPoParser.FilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#reverse.
    def visitReverse(self, ctx:GoPoParser.ReverseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#dropLast.
    def visitDropLast(self, ctx:GoPoParser.DropLastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#dropWithIndex.
    def visitDropWithIndex(self, ctx:GoPoParser.DropWithIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#count.
    def visitCount(self, ctx:GoPoParser.CountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#sum.
    def visitSum(self, ctx:GoPoParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#contains.
    def visitContains(self, ctx:GoPoParser.ContainsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#is_empty.
    def visitIs_empty(self, ctx:GoPoParser.Is_emptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#clear.
    def visitClear(self, ctx:GoPoParser.ClearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#foreach.
    def visitForeach(self, ctx:GoPoParser.ForeachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#add.
    def visitAdd(self, ctx:GoPoParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#remove.
    def visitRemove(self, ctx:GoPoParser.RemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#remove_all.
    def visitRemove_all(self, ctx:GoPoParser.Remove_allContext):
        return self.visitChildren(ctx)



del GoPoParser