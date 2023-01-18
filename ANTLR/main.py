from antlr4 import *
from GoPoLexer import GoPoLexer
from GoPoParser import GoPoParser
from BaseVisitor import BaseVisitor


def main():
    input_stream = FileStream("testing_visitor.txt")
    lexer = GoPoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GoPoParser(stream)
    tree = parser.parse()
    if parser.getNumberOfSyntaxErrors() != 0:
        print("File contains {} "
              "syntax errors".format(parser.getNumberOfSyntaxErrors()))
        return

    visitor = BaseVisitor()
    visitor.visit(tree)


if __name__ == '__main__':
    main()
