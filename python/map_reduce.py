def map_function(document_id, review_comment):
    # Simple sentiment analysis logic (for illustration purposes)
    positive_words = {"good", "great", "excellent", "positive", "happy"}
    negative_words = {"bad", "poor", "negative", "sad", "terrible"}
    
    # Split the comment into words
    words = review_comment.lower().split()
    
    # Initialize sentiment scores
    positive_score = 0
    negative_score = 0
    
    # Analyze words for sentiment
    for word in words:
        if word in positive_words:
            positive_score += 1
        elif word in negative_words:
            negative_score += 1
    
    # Determine sentiment
    if positive_score > negative_score:
        sentiment = "positive"
    elif negative_score > positive_score:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    # Emit sentiment as key with a count of 1
    emit(sentiment, 1)


def reduce_function(sentiment, counts):
    # Sum up the counts for each sentiment
    total_count = sum(counts)
    
    # Emit the final result
    emit(sentiment, total_count)
