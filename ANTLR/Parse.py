from ANTLR.Statement import Statement


class Parse:
    def __init__(self):
        self.statement = []

    def add_statement(self, statement: Statement):
        self.statement.append(statement)