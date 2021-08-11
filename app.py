from flask import Flask, render_template, request, jsonify, g
import os
from text_analysis import analyze_text

app = Flask(__name__)
app.config.update(**os.environ)


@app.route('/')
def expresso_route():
    return render_template('expresso.html')

    
@app.route('/analyze-text', methods=['POST'])
def analyze():
    html = request.form.get('html', '')
    text, tokens, metrics = analyze_text(html)
    return jsonify({'text': text, 'tokens': tokens, 'metrics': metrics})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
