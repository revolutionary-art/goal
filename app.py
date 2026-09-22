from flask import Flask, render_template, url_for

app =Flask(__name__, template_folder="Templates")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def aboutpage():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

 