import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

file = open('C:/','r')
content = file.read()

sports_articles = [
    content
]

analyzer = SentimentIntensityAnalyzer()

for i, article in enumerate(sports_articles, 1):
    sentiment = analyzer.polarity_scores(article)
    print(f"Article {i} Sentiment Analysis:")
    print("Article Text: ", article)
    print("Sentiment Scores (Positive/Negative/Neutral/Compound):", sentiment)
    print()

compound_scores = [analyzer.polarity_scores(article)["compound"] for article in sports_articles]
average_compound_score = sum(compound_scores) / len(compound_scores)

if average_compound_score >= 0.05:
    overall_sentiment = "positive"
elif average_compound_score <= -0.05:
    overall_sentiment = "negative"
else:
    overall_sentiment = "neutral"

print(f"Overall Sentiment of the Sports Articles: {overall_sentiment}")
