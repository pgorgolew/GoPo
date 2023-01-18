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


    # Visit a parse tree produced by GoPoParser#expression.
    def visitExpression(self, ctx:GoPoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#atom.
    def visitAtom(self, ctx:GoPoParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#list.
    def visitList(self, ctx:GoPoParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#sort.
    def visitSort(self, ctx:GoPoParser.SortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#map.
    def visitMap(self, ctx:GoPoParser.MapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#filter.
    def visitFilter(self, ctx:GoPoParser.FilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#reverse.
    def visitReverse(self, ctx:GoPoParser.ReverseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoPoParser#drop.
    def visitDrop(self, ctx:GoPoParser.DropContext):
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