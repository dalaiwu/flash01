from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, my World 02!</p>"

if __name__ == '__main__':
    app.run()
