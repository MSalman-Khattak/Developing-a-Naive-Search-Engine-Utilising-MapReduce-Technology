# Relevance Analyzer Reducer
import sys

# Initialize a dictionary to store relevance scores for each document
relevance_scores = {}

# Read input from standard input
for line in sys.stdin:
    # Parse the input obtained from mapper
    document_id, relevance_score = line.strip().split('\t')
    
    # Aggregate relevance scores for each document
    relevance_scores[document_id] = float(relevance_score)

# Sort documents based on their relevance scores
sorted_documents = sorted(relevance_scores.items(), key=lambda x: x[1], reverse=True)

# Emit the sorted list of document IDs as the final output
for document_id, relevance_score in sorted_documents:
    print(document_id)