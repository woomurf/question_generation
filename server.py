from flask import Flask, jsonify, render_template, request
from pipelines import pipeline 
import nltk 
import json

app = Flask(__name__)

nlp = pipeline("multitask-qa-qg")

def generate_QA(context):
    qa_list = nlp(context)

    return qa_list

@app.route("/generation", methods=["POST"])
def generation():
    data = request.data
    data = json.loads(data)
    context = data['context']

    qa_list = generate_QA(context)
    
    result = {"result": qa_list}

    return jsonify(result), 200

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)