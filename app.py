from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "erez"
    return render_template("index.html", name=name)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

def run():
    app.run(debug=True)

if __name__ == "__main__":
    run()