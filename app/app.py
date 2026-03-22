from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the home page for Cloud Engineer Intern Coding Challenge "

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/info")
def info():
    return {
        "name": "Intern Coding Challenge",
        "version": 1.0,
        "author": "Cole"
    }

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        debug=False,
        port=8000,
        ssl_context=("certs/cert.pem", "certs/key.pem"))