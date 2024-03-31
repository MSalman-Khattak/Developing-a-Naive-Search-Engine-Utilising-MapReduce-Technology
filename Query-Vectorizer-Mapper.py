# Query Vectorizer Mapper
import sys

# Read input from standard input (query)
query = sys.stdin.readline().strip()

# Tokenize the query into words
query_words = query.split()

# Calculate term frequency (TF) for each word and emit key-value pairs
for word in query_words:
    tf = query_words.count(word)
    print(f"{word}\t{tf}")  # Emitting key-value pairs separated by tab