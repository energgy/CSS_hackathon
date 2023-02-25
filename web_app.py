## Create a stylish web app with python flask framework, which involves a chat bot that asks questions
## and gives answers based on the user's input. The chat bot uses an API
## to analyze the user's input and give a response based on the sentiment analysis.

# Import libraries
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Set up Text Analytics client and authenticate with API key
endpoint = "https://hackaton-css-serendipity.cognitiveservices.azure.com/"

# Create a flask app
app = Flask(__name__)
Bootstrap(app)

# Create a route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Create a route for the chat bot
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# Create a route for the chat bot
@app.route('/chatbot', methods=['POST'])
def chatbot_post():
    # Get the user's input
    user_input = request.form['user_input']
    # Analyze sentiment of input text
    sentiment_analysis = text_analytics_client.analyze_sentiment([user_input])[0]
    # Check for errors
    if not sentiment_analysis.is_error:
        # Print sentiment score and label
        print("Sentiment score: {}".format(sentiment_analysis.confidence_scores))
        print("Sentiment label: {}".format(sentiment_analysis.sentiment))
    else:
        print("Error: {}".format(sentiment_analysis.id))
    return render_template('chatbot.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

