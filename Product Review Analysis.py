# Task 1: Keyword Highlighter
# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    for keyword in keywords:
        if keyword in review:
            review = review.replace(keyword, keyword.upper())
    print(review)

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(review):
    positive_count = 0
    negative_count = 0
    words = review.split()
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1
    return positive_count, negative_count

for review in reviews:
    positive_count, negative_count = sentiment_tally(review)
    print(f"Positive words: {positive_count}, Negative words: {negative_count}")

# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

for review in reviews:
    summary = review[:30]
    if len(review) > 30:
        last_space = summary.rfind(" ")
        summary = summary[:last_space] + "…"
    print(summary)
