from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def main_app():
    try:
        search_value = request.args.get('keyword')
        response = requests.get('http://localhost:5001/api/v1/term/' + search_value)
        return render_template('index.html', response=response.json())
    except:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
