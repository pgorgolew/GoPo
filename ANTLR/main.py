from antlr4 import *
from GoPoLexer import GoPoLexer
from GoPoParser import GoPoParser


def main():
    input_stream = FileStream("example.txt")
    lexer = GoPoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GoPoParser(stream)
    tree = parser.parse()


if __name__ == '__main__':
    main()
