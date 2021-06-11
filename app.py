from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sentences = request.form['text'].split(". ")
        values = []
        analyzer = SentimentIntensityAnalyzer()
        for sentence in sentences:
            values.append(float(analyzer.polarity_scores(sentence)['compound']))
        average = sum(values) / len(values)

        if average > 0:
            results = "Positive!"
        if average < 0:
            results = "Negative!"
        return render_template('main.html', result=results)

    return render_template('main.html')
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
