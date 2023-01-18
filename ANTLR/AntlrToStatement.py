from ANTLR.GoPoParser import GoPoParser
from ANTLR.Print import Print
from GoPoVisitor import GoPoVisitor


class AntlrToStatement(GoPoVisitor):
    def __init__(self):
        super(AntlrToStatement, self).__init__()

    def visitPrint(self, ctx:GoPoParser.PrintContext):
        content = self.visit(ctx.getChild(0))
        return Print(content)
