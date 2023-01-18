from ANTLR.Statement import Statement


class Print(Statement):
    def __init__(self, content):
        self.content = content
