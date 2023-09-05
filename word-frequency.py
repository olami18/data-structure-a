import re
from collections import defaultdict

def word_frequency(sentence):
    # Remove punctuation and split into words
    words = re.findall(r'\b\w+\b', sentence.lower())
    
    frequency = defaultdict(int)

    for word in words:
        frequency[word] += 1

    return dict(frequency)

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
