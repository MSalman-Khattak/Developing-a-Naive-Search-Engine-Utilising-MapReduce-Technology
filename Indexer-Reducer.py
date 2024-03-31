# Indexer Reducer
import sys
import math

current_word = None
doc_counts = set()

# Read input from standard input
for line in sys.stdin:
    # Parse the input obtained from mapper
    word, doc_info = line.strip().split('\t')
    document_id, term_frequency = doc_info.strip('()').split(',')
    
    # If the word changes, calculate the Inverse Document Frequency (IDF) and emit key-value pairs
    if current_word and current_word != word:
        idf = math.log10(1 + len(doc_counts))  # Calculate IDF
        print(f"{current_word}\t{idf}")  # Emitting key-value pairs separated by tab
        doc_counts = set()  # Reset document counts for the new word
    
    current_word = word
    doc_counts.add(document_id)

# Emit the IDF for the last word
if current_word:
    idf = math.log10(1 + len(doc_counts))  # Calculate IDF
    print(f"{current_word}\t{idf}")  # Emitting key-value pairs separated by tab