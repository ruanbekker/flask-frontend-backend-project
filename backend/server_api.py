from flask import Flask, request, jsonify, render_template
import json

df = open('/code/data.json', 'r')
data = json.loads(df.read())

app = Flask(__name__)

@app.route('/api/v1/term/<keyword>')
def search(keyword):
    results = []
    for each in data:
        if keyword in each['project_text']:
            results.append(each)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
