import sys

# Read the list of relevant document IDs from the input
relevant_document_ids = set(sys.stdin.read().strip().split('\n'))

# Read the text corpus and extract relevant content for each document ID
for line in sys.stdin:
    document_id, content = line.strip().split('\t')
    if document_id in relevant_document_ids:
        # Output the relevant content
        print(content)
