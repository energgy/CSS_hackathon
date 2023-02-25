import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Set up Text Analytics client and authenticate with API key
endpoint = "https://hackaton-css-serendipity.cognitiveservices.azure.com/"
credential = AzureKeyCredential("6a1504350e484b63882efe45cfe1ac2a")
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Analyze sentiment of input text
input_text = "I feel so sad and hopeless today."
sentiment_analysis = text_analytics_client.analyze_sentiment([input_text])[0]

# Check for errors
if not sentiment_analysis.is_error:
    # Print sentiment score and label
    print("Sentiment score: {}".format(sentiment_analysis.confidence_scores))
    print("Sentiment label: {}".format(sentiment_analysis.sentiment))
else:
    print("Error: {}".format(sentiment_analysis.id))



