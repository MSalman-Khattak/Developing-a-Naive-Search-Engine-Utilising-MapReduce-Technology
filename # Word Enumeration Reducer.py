# Word Enumeration Reducer
import sys

current_word = None
current_id = 0

# Read input from standard input
for line in sys.stdin:
    # Parse the input obtained from mapper
    word, _ = line.strip().split('\t')
    
    # If the word changes, assign a new ID
    if current_word != word:
        current_id += 1
        current_word = word
    
    # Emit key-value pairs where the key is the word and the value is its assigned ID
    print(f"{current_word}\t{current_id}")