from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return render_template("index.html", user_name = name)

if __name__ == "__main__":
    app.run(debug=True)
