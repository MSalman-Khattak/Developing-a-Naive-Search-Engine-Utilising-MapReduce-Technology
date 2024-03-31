# Document Count Reducer
import sys

current_word = None
doc_ids = set()

# Read input from standard input
for line in sys.stdin:
    # Parse the input obtained from mapper
    word, document_id = line.strip().split('\t')
    
    # If the word changes, emit the count of unique document IDs for the previous word
    if current_word and current_word != word:
        print(f"{current_word}\t{len(doc_ids)}")
        doc_ids = set()  # Reset document IDs for the new word
    
    current_word = word
    doc_ids.add(document_id)

# Emit the count of unique document IDs for the last word
if current_word:
    print(f"{current_word}\t{len(doc_ids)}")