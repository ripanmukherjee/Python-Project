# Here are all the imports you will need for your word cloud script and uploader widget
import wordcloud
from matplotlib import pyplot as plt

# Placeholder for file contents
file_contents = "Add sample file content text here to generate word cloud."


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''

    uninteresting_words = [
        "the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you",
        "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which",
        "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do",
        "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each",
        "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"
    ]

    contents = file_contents.strip().lower()
    # Create a translation table that replaces each punctuation with a space
    translation_table = str.maketrans(punctuations, ' ' * len(punctuations))
    contents = contents.translate(translation_table)
    words = contents.split()

    result = {}
    for word in words:
        if word.isalpha() and word not in uninteresting_words:
            result[word] = result.get(word, 0) + 1

    # Generate the word cloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies=result)
    return cloud.to_array()


# Display your wordcloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
