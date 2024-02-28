from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory('static/', 'manifest.json')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory('static/', 'sw.js')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')