# Document Count Mapper
import sys

# Read input from standard input (each line represents a portion of the input text corpus)
for line in sys.stdin:
    # Tokenize the text into words
    words = line.strip().split()
    # Emit key-value pairs where the key is the word and the value is the document ID
    for word in words:
        document_id = "1"  # Assuming there's only one document
        print(f"{word}\t{document_id}")  # Emitting key-value pairs separated by tab