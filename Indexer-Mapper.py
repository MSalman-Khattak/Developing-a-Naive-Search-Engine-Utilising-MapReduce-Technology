# Indexer Mapper
import sys

# Read input from standard input (each line represents a portion of the input text corpus)
for line in sys.stdin:
    # Tokenize the text into words and extract the document ID
    document_id, text = line.strip().split('\t')
    words = text.split()
    # Count term frequency (TF) for each word
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    # Emit key-value pairs where the key is the word and the value is a tuple containing the document ID and term frequency (TF)
    for word, count in word_count.items():
        print(f"{word}\t({document_id},{count})")  # Emitting key-value pairs separated by tab