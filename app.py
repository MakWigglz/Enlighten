from flask import Flask, render_template, jsonify
from models import topics
from knowledge_handler import get_knowledge

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', topics=topics.keys())

@app.route('/subtopics/<topic>')
def get_subtopics(topic):
    if topic in topics:
        return jsonify(topics[topic].subtopics)
    return jsonify([])

@app.route('/content/<topic>/<subtopic>')
def get_content(topic, subtopic):
    content = get_knowledge(topic, subtopic)
    return jsonify({"content": content})

if __name__ == '__main__':
    app.run(debug=True)