from flask import Flask,jsonify
app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def hello_world():
    response = {
        "response":"Hello World"
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()  