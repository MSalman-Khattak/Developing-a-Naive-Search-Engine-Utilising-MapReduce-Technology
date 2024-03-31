# Query Vectorizer Reducer
import sys

# Initialize variables to store total term frequencies
total_tfs = {}

# Read input from standard input
for line in sys.stdin:
    # Parse the input obtained from mapper
    word, tf = line.strip().split('\t')
    
    # Aggregate the TFs of query words
    total_tfs[word] = total_tfs.get(word, 0) + int(tf)

# Generate the vectorized representation of the query
query_vector = [(word, tf) for word, tf in total_tfs.items()]

# Print the vectorized representation of the query
print(query_vector)