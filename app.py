from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hey Flask!!!"

@app.route('/contact')
def contact():
    return "Contact Page..."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
