from ANTLR.GoPoParser import GoPoParser
from ANTLR.Parse import Parse
from GoPoVisitor import GoPoVisitor
from AntlrToStatement import AntlrToStatement


class BaseVisitor(GoPoVisitor):
    # def __init__(self):
    #     super().__init__()

    def visitParse(self, ctx:GoPoParser.PrintContext):
        visitor = AntlrToStatement()
        parse = Parse()

        for i in range(0, ctx.getChildCount()):
            if i == ctx.getChildCount():
                print("LAST")
            else:
                parse.add_statement(visitor.visit(ctx.getChild(i)))


        return parse