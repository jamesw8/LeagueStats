from flask import Flask
import kittens
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/<username>")
def username(username):
	json = kittens.lookUp(username)
	return json

if __name__ == "__main__":
	app.run()