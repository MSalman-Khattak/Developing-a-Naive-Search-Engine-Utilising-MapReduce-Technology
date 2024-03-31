# Word Enumeration Mapper
import sys

# Read input from standard input (each line represents a portion of the input text corpus)
for line in sys.stdin:
    # Tokenize the text into words
    words = line.strip().split()
    # Emit key-value pairs where the key is the word and the value is a constant (like 1)
    for word in words:
        print(f"{word}\t1")  # Emitting key-value pairs separated by tab