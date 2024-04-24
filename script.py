import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK resources (run only once)
nltk.download('punkt')
nltk.download('stopwords')

# File path to the random_paragraphs.txt within the Docker container
file_path = "random_paragraphs.txt"

# Read the contents of the file
with open(file_path, "r") as file:
    paragraph_text = file.read()

# Tokenize the text into words
word_tokens = nltk.word_tokenize(paragraph_text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_word_tokens = [word for word in word_tokens if word.lower() not in stop_words]

# Count the frequency of each word
word_frequencies = Counter(filtered_word_tokens)

# Display word frequency count
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")
