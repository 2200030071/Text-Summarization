from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)


def summarize_text_logic(text):
    # Simple text summarization logic: extract key sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    num_sentences = max(1, len(sentences) // 3)  # Take about one-third of the sentences
    summary = ' '.join(sentences[:num_sentences])
    return summary


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    summary = summarize_text_logic(text)
    return jsonify({"summary": summary})


if __name__ == '__main__':
    app.run(debug=True)