from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "u5512331"

#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