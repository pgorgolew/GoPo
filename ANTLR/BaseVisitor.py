from tokenize import String

from GoPoVisitor import GoPoVisitor
from GoPoParser import GoPoParser
from math import log10

lambda_two_args_by_operator = {
    GoPoParser.MINUS: lambda x, y: x - y,
    GoPoParser.PLUS: lambda x, y: x + y,
    GoPoParser.POW: lambda x, y: x ** y,
    GoPoParser.MULT: lambda x, y: x * y,
    GoPoParser.DIV: lambda x, y: x / y,
    GoPoParser.MOD: lambda x, y: x % y,
    GoPoParser.LTEQ: lambda x, y: x <= y,
    GoPoParser.GTEQ: lambda x, y: x >= y,
    GoPoParser.LT: lambda x, y: x < y,
    GoPoParser.GT: lambda x, y: x > y,
    GoPoParser.EQ: lambda x, y: x == y,
    GoPoParser.NEQ: lambda x, y: x != y
}

lambda_one_arg_by_operator = {
    GoPoParser.LOG: log10,
    GoPoParser.ABS: abs,
    GoPoParser.MINUS: lambda x: -x
}


class VariableNotInitializedException(Exception):
    pass


class VariableNotInList(Exception):
    pass


class BaseVisitor(GoPoVisitor):
    def __init__(self):
        super().__init__()
        self.memory = dict()
        self.tmp_memory = dict()
        self.returned_value_from_list_function = None

    def visitChildren(self, node):
        if node.getChildCount() == 1:
            return node.getChild(0).accept(self)

        return super().visitChildren(node)

    def visitTerminal(self, node):
        return node.getText()

    def visitParse(self, ctx: GoPoParser.ParseContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: GoPoParser.AssignmentContext):
        variable_name = ctx.getChild(0).accept(self)
        # print([method_name for method_name in dir(ctx.getChild(2))
        #                   if callable(getattr(ctx.getChild(2), method_name))])
        variable_value = ctx.getChild(2).accept(self)
        self.memory[variable_name] = variable_value

    def visitParentnessExpr(self, ctx: GoPoParser.ParentnessExprContext):
        return ctx.getChild(1).accept(self)

    def visitMathExprLeftRight(self, ctx: GoPoParser.MathExprLeftRightContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operation = lambda_two_args_by_operator[ctx.op.type]
        return operation(left, right)

    def visitMathOneExprFun(self, ctx: GoPoParser.MathOneExprFunContext):
        expression_result = ctx.expression().accept(self)
        operation = lambda_one_arg_by_operator[ctx.op.type]
        return operation(expression_result)

    def visitLogicExpr(self, ctx: GoPoParser.LogicExprContext):
        if ctx.op.type == GoPoParser.NOT:
            return not self.visit(ctx.expression())

        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operation = lambda_two_args_by_operator[ctx.op.type]
        return operation(left, right)

    def visitCondition_block(self, ctx: GoPoParser.Condition_blockContext):
        if not self.visit(ctx.expression()):
            return False

        self.visit(ctx.condition_body())
        return True

    def visitIf_stat(self, ctx: GoPoParser.If_statContext):
        if self.visit(ctx.if_block):
            return

        for elif_block in ctx.elif_blocks:
            if self.visit(elif_block):
                return

        if ctx.else_block is not None:
            self.visit(ctx.else_block)

    def visitWhile_stat(self, ctx: GoPoParser.While_statContext):
        while self.visit(ctx.condition_block()):
            pass

    def visitNumberAtom(self, ctx: GoPoParser.NumberAtomContext):
        res = ctx.getChild(0).accept(self)
        res = self.convert_str_to_numeric(res)

        return res

    def visitBoolAtom(self, ctx: GoPoParser.BoolAtomContext):
        return ctx.getChild(0).getSymbol().type == GoPoParser.TRUE

    def visitIdAtom(self, ctx: GoPoParser.IdAtomContext):
        var_name = ctx.getChild(0).accept(self)
        return self.get_from_memory(var_name)

    def visitStringAtom(self, ctx: GoPoParser.StringAtomContext):
        return ctx.getChild(0).accept(self)[1: -1]  # getting rid of " at the end and beginning

    def visitNoneAtom(self, ctx: GoPoParser.NoneAtomContext):
        return None

    def visitRangeList(self, ctx: GoPoParser.RangeListContext):
        used_range = ctx.getChild(2).accept(self)
        start, end = used_range.split("...")
        step = 1 if start < end else -1

        return list(range(int(start), int(end) + step, step))

    def visitNumbersList(self, ctx: GoPoParser.NumbersListContext):
        return [self.convert_str_to_numeric(number.text) for number in ctx.numbers]

    def visitEmptyList(self, ctx: GoPoParser.EmptyListContext):
        return list()

    def visitList_expr(self, ctx: GoPoParser.List_exprContext):
        if ctx.getChildCount() > 1:
            list_child = ctx.getChild(0)
            if hasattr(list_child, 'symbol') and list_child.symbol.type == GoPoParser.ID:
                tmp_list = self.get_from_memory(list_child.accept(self))
            else:
                tmp_list = list_child.accept(self)

            self.tmp_memory['list'] = tmp_list
            ctx.getChild(1).accept(self)

            if self.returned_value_from_list_function is not None:
                result = self.returned_value_from_list_function
                self.returned_value_from_list_function = None
                return result

            result = self.tmp_memory['list']
            self.tmp_memory.clear()
            return result

        return self.visitChildren(ctx)

    def visitList_expr_rec(self, ctx: GoPoParser.List_expr_recContext):
        ctx.getChild(1).accept(self)
        if ctx.getChildCount() > 2:
            ctx.getChild(2).accept(self)

    def visitAdd(self, ctx: GoPoParser.AddContext):
        added_number = self.convert_str_to_numeric(ctx.getChild(2).accept(self))
        self.tmp_memory['list'].append(added_number)

    def visitRemove(self, ctx: GoPoParser.RemoveContext):
        number_to_remove = self.convert_str_to_numeric(ctx.getChild(2).accept(self))
        if number_to_remove not in self.tmp_memory['list']:
            raise VariableNotInList(f"{number_to_remove} not in list")

        self.tmp_memory['list'].remove(number_to_remove)
        return self.visitChildren(ctx)

    def visitFilter(self, ctx: GoPoParser.FilterContext):
        operator = ctx.op.type
        function = lambda_two_args_by_operator[operator]
        value = self.convert_str_to_numeric(self.visit(ctx.getChild(3)))

        self.tmp_memory['list'] = [x for x in self.tmp_memory['list'] if function(x, value)]

        return self.visitChildren(ctx)

    def visitRemove_all(self, ctx: GoPoParser.Remove_allContext):
        number_to_remove = self.convert_str_to_numeric(ctx.getChild(2).accept(self))
        if number_to_remove not in self.tmp_memory['list']:
            raise VariableNotInList(f"{number_to_remove} not in list")

        self.tmp_memory['list'] = list(filter(lambda e: e != number_to_remove, self.tmp_memory['list']))
        return self.visitChildren(ctx)

    def visitReverse(self, ctx: GoPoParser.ReverseContext):
        self.tmp_memory['list'].reverse()
        return self.visitChildren(ctx)

    def visitSort(self, ctx: GoPoParser.SortContext):
        is_descending = False if ctx.op.type == GoPoParser.PLUS else True
        self.tmp_memory['list'].sort(reverse=is_descending)

        return self.visitChildren(ctx)

    def visitMapOpWithNum(self, ctx:GoPoParser.MapOpWithNumContext):
        value = self.convert_str_to_numeric(self.visit(ctx.getChild(3)))
        function = lambda_two_args_by_operator[ctx.op.type]
        self.tmp_memory['list'] = [function(x, value) for x in self.tmp_memory['list']]

        return self.visitChildren(ctx)

    def visitMapOpWithoutNum(self, ctx:GoPoParser.MapOpWithoutNumContext):
        function = lambda_one_arg_by_operator[ctx.op.type]
        self.tmp_memory['list'] = list(map(function, self.tmp_memory['list']))

        return self.visitChildren(ctx)

    def visitDropLast(self, ctx:GoPoParser.DropLastContext):
        self.returned_value_from_list_function = self.tmp_memory['list'].pop()
        
        return self.visitChildren(ctx)

    def visitDropWithIndex(self, ctx:GoPoParser.DropWithIndexContext):
        index = self.convert_str_to_numeric(self.visit(ctx.getChild(2)))
        self.returned_value_from_list_function = self.tmp_memory['list'].pop(index)

        return self.visitChildren(ctx)

    @staticmethod
    def convert_str_to_numeric(s):
        try:
            s = int(s)
        except ValueError:
            s = float(s)
        return s

    def get_from_memory(self, var_name):
        if var_name not in self.memory:
            raise VariableNotInitializedException(f"{var_name} was not initialized before")

        return self.memory[var_name]
