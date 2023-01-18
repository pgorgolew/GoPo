# Setup for ANTLR
1. create venv and activate
2. pip install antlr4-tools
3. antlr4
4. pip install antlr4-python3-runtime

# Running ANTLR

Command for generating parser code

```antlr4 -Dlanguage=Python3 GoPo.g4  -visitor -no-listener```

Command for tree view and gui with input from terminal

```antlr4-parse GoPo.g4 parse -tree -gui```

Command for tree view and gui with file example

```antlr4-parse GoPo.g4 parse -tree -gui example.txt```