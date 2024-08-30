''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    # Checking if text is blank or not
    if text_to_analyze == "":
        return "Input text is empty!!"
    res = sentiment_analyzer(text_to_analyze)
    if res['label'] is not None:
        label_split = res['label'].split('_')
        label = label_split[1]
        return f"The given has been identified as {label} with a score of {res['score']}", 200
    return "Invalid Input! Try Again"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
