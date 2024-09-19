
# Task Statement

Sentiment Analysis of Tweets using Hadoop and MapReduce

## Overview

This guide provides instructions for testing Hadoop mapper and reducer scripts locally using sample tweet data.

### Mapper

**`mapper.py`**: Reads tweets and return key-value pairs with `tweet_id` as the key and sentiment as the value.

### Reducer

**`reducer.py`**: Aggregates sentiments by `tweet_id` and outputs the count of positive, neutral, and negative tweets for each `tweet_id`.

### Input Data

```
tweet_id,topic,sentiment,tweet
2401,Borderlands,Positive,"im getting on borderlands and i will murder you all ,"
2401,Borderlands,Neutral,"im getting on borderlands and I am feeling fine,"
2401,Borderlands,Negative,"im getting on borderlands and i am very upset,"
2402,Borderlands,Positive,"So I spent a few hours making something for fun..."
2402,Borderlands,Positive,"So I spent a couple of hours doing something for fun..."
```

### Intermediate Data

```
tweet_id	sentiment
2401	Positive
2401	Neutral
2401	Negative
2402	Positive
2402	Positive
```

### Output Data

```
tweet_id,(positive_count, neutral_count, negative_count)
2401,(1, 1, 1)
2402,(2, 0, 0)
```

# Directory Structure

## Directory Structure

- **Input Data**: `input_data/twitter_training.csv`
- **Mapper Script**: `mapper.py`
- **Reducer Script**: `reducer.py`
- **Output Directory**:
  - **Intermediate File**: `output_data/intermediate.txt`
  - **Final Output File**: `output_data/final_output.txt`
