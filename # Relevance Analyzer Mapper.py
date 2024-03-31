# Relevance Analyzer Mapper
import sys
import ast

# Read the query vector from the input
query_vector_str = sys.stdin.readline().strip()

# Parse the query vector string into a list of tuples
query_vector = ast.literal_eval(query_vector_str)

# Read document vectors from standard input
for line in sys.stdin:
    # Parse the input obtained from mapper
    document_id, document_vector_str = line.strip().split('\t')
    document_vector = ast.literal_eval(document_vector_str)
    
    # Calculate the relevance score between the query vector and document vector
    relevance_score = sum(query_tf * document_tf for (word, query_tf), (word, document_tf) in zip(query_vector, document_vector))
    
    # Emit key-value pairs where key is document ID and value is relevance score
    print(f"{document_id}\t{relevance_score}")