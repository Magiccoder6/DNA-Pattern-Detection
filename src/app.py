from flask import Flask, jsonify, render_template, request

from dna import DNA

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.post('/test_sequence')
def test_sequence():
    data = request.json
    text_value = data.get('text')

    dna_sequence = text_value
    dfa = DNA(dna_sequence)
    result, found = dfa.analyze()
    
    return jsonify({"result": result, "found": found})