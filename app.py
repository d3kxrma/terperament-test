from flask import Flask, render_template, url_for, request
import json

app = Flask(__name__)

@app.route("/")
def main():
    questions = json.load(open("questions.json", encoding="utf-8"))
    return render_template("index.html", questions=questions)

@app.route("/answer", methods=["POST"])
def answer():
    score = sum([int(x) for x in request.form.values()])
    results = json.load(open("results.json", encoding="utf-8"))
    for result in results.values():
        if (score >= int(result["minimum"]) and score <= int(result["maximum"])):
            return render_template("answer.html", type=result["type"], text = result["text"])

if __name__ == "__main__":
    app.run(debug=False)