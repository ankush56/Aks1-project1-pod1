from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', message="Superman")

if __name__ == "__main__":
    app.run(port=8000)
