from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    blob_score = TextBlob(text).sentiment.polarity  # TextBlob sentiment score
    vader_score = analyzer.polarity_scores(text)["compound"]  # VADER sentiment score
    avg_score = (blob_score + vader_score) / 2  # Average score
    if avg_score > 0.05:
        return "Positive"
    elif avg_score < -0.05:
        return "Negative"
    else:
        return "Neutral"

# Example
print(analyze_sentiment("The government policies are excellent!"))
