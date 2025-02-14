from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Example Latin vocabulary
nouns = {
    "amicus": {"meaning": "friend"},
    "puella": {"meaning": "girl"},
    "domus": {"meaning": "house"},
    "rex": {"meaning": "king"}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_question')
def get_question():
    word = random.choice(list(nouns.keys()))
    return jsonify({"latin": word, "meaning": nouns[word]["meaning"]})

if __name__ == '__main__':
    app.run(debug=True)
