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
}

lambda_one_arg_by_operator = {
    GoPoParser.LOG: lambda x: log10(x),
    GoPoParser.ABS: abs,
    GoPoParser.MINUS: lambda x: -x
}


class VariableNotInitializedException(Exception):
    pass


class BaseVisitor(GoPoVisitor):
    def __init__(self):
        super().__init__()
        self.memory = dict()
        self.tmp_memory = dict()

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

        return list(range(int(start), int(end) + 1))

    def visitNumbersList(self, ctx: GoPoParser.NumbersListContext):
        return [self.convert_str_to_numeric(number.text) for number in ctx.numbers]

    def visitEmptyList(self, ctx: GoPoParser.EmptyListContext):
        return list()

    def visitList_expr(self, ctx:GoPoParser.List_exprContext):
        if ctx.getChildCount() > 1:
            list_child = ctx.getChild(0)
            if list_child.symbol.type == GoPoParser.ID:
                created_list = self.get_from_memory(list_child.accept(self))
            else:
                created_list = list_child.accept(self)

            self.tmp_memory['list'] = created_list
            ctx.getChild(1).accept(self)

            result = self.tmp_memory['list']
            self.tmp_memory.clear()
            return result

        return self.visitChildren(ctx)


    def visitList_expr_rec(self, ctx:GoPoParser.List_expr_recContext):
        ctx.getChild(1).accept(self)
        if ctx.getChildCount() > 2:
            ctx.getChild(2).accept(self)

    def visitAdd(self, ctx:GoPoParser.AddContext):
        added_number = self.convert_str_to_numeric(ctx.getChild(2).accept(self))
        self.tmp_memory['list'].append(added_number)

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