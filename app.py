from flask import Flask, render_template, request
from text_summ import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary, orgtext, lenorg, lensum = summarizer(rawtext)
        return render_template('summary.html', summary=summary, orgtext=orgtext, lenorg=lenorg, lensum=lensum)

if __name__ == "__main__":
    app.run(debug=True)
