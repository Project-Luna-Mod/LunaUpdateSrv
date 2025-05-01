from flask import Flask, jsonify, send_file
import json
app = Flask(__name__)

@app.route('/')
def index():
    with open("update.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/file')
def download_file():
    return send_file('update.zip', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)