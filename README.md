# Setup for ANTLR
1. create venv and activate
2. pip install antlr4-tools
3. antlr4
4. pip install antlr4-python3-runtime

# Running ANTLR

Command for generating parser code

```antlr4 -o <ANTLR_DIR_PATH> -listener -visitor -Dlanguage=Python3 -lib <ANTLR_DIR_PATH> <GRAMMAR_PATH>```

Command for tree view and gui with input from terminal

```antlr4-parse GoPo.g4 parse -tree -gui```

Command for tree view and gui with file example

```antlr4-parse GoPo.g4 parse -tree -gui example.txt```