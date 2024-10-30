from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello, this is CICD pipeline"

@app.route("/about")
def about():
    return "this is about page testing "



if __name__ =='__main__' :
    app.run(host = "0.0.0.0",port = 5000)