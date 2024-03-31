# Developing-a-Naive-Search-Engine-Utilising-MapReduce-Technology



 Let's delve deeper into each script's functionality and how they contribute to the overall information retrieval process:

query processing phase.py:

Reads a list of relevant document IDs from the input. These IDs likely represent documents that are relevant to a specific query.
Iterates through the text corpus, extracting relevant content for each document ID present in the list of relevant IDs.
Outputs the relevant content for further processing or analysis.
Query Vectorizer Reducer.py:

Aggregates total term frequencies (TFs) for words in the query.
Generates a vectorized representation of the query, where each dimension corresponds to a unique word in the query, and the value represents the TF of that word.
Prints the vectorized representation of the query, which can be used in similarity calculations with document vectors.
Relevance Analyzer Reducer.py:

Calculates relevance scores for each document based on some relevance metric, likely involving a comparison between query and document vectors.
Sorts documents based on their relevance scores, typically in descending order.
Prints the sorted list of document IDs, potentially indicating the most relevant documents to a given query.
Word Enumeration Reducer.py:

Assigns a unique identifier (ID) to each unique word encountered in the input.
Prints word-ID pairs, which can be used for efficient storage and retrieval of word-related information in subsequent processing steps.
Document Count Reducer.py:

Counts the number of unique document IDs associated with each word in the input.
Prints word-count pairs, providing insights into the distribution of words across documents in the corpus.
Indexer Reducer.py:

Calculates the Inverse Document Frequency (IDF) for each word, which measures the rarity of the word across documents in the corpus.
Prints word-IDF pairs, which are essential for weighting terms in information retrieval tasks, such as TF-IDF scoring.
Relevance Analyzer Mapper.py:

Receives a query vector and document vectors as input.
Computes relevance scores between the query vector and each document vector.
Outputs document ID - relevance score pairs, aiding in the identification of relevant documents.
Document Count Mapper.py:

Tokenizes input text into words and associates each word with the document ID.
Emits word-document ID pairs, facilitating document-level analysis and indexing.
Indexer Mapper.py:

Tokenizes input text into words and calculates the term frequency (TF) for each word in each document.
Emits word-document ID-TF tuples, enabling the creation of an inverted index for efficient document retrieval based on query terms.
Query Vectorizer Mapper.py:

Reads a query and tokenizes it into words.
Calculates the term frequency (TF) for each word in the query.
Emits word-TF pairs, which can be used to construct a query vector for comparison with document vectors.
Word Enumeration Mapper.py:

Tokenizes input text into words.
Emits word-constant pairs, which are typically used for basic word counting or indexing purposes.
Together, these scripts facilitate various stages of the information retrieval process, including query processing, vectorization, relevance scoring, indexing, and document analysis. By understanding and appropriately utilizing each script within a pipeline, users can effectively retrieve and analyze relevant information from a text corpus based on specific queries or search criteria.
