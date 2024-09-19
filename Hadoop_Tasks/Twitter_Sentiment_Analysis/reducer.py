import sys
from collections import defaultdict

# init the dict to store sentiment counts for each tweet_id
sentiment_counts = defaultdict(lambda: {'Positive': 0, 'Neutral': 0, 'Negative': 0})

for line in sys.stdin:
    line = line.strip()
    tweet_id, sentiment = line.split('\t', 1)

    # increment the count of the sentiment for each corresponding tweet_id
    if sentiment in sentiment_counts[tweet_id]:
        sentiment_counts[tweet_id][sentiment] += 1

# print header
print("tweet_id,(positive_count, neutral_count, negative_count)")

for tweet_id, counts in sentiment_counts.items():
    positive_count = counts['Positive']
    neutral_count = counts['Neutral']
    negative_count = counts['Negative']
    print(f"{tweet_id},({positive_count}, {neutral_count}, {negative_count})")
