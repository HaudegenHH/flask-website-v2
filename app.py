from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Berlin, Germany",
        "salary": "€35K"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Frankfurt, Germany",
        "salary": "€45K"
    },
    {
        "id": 3,
        "title": "Frontend Engineer",
        "location": "remote",
    },
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "Hamburg, Germany",
        "salary": "€50K"
    },  
]


@app.route("/")
def index():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)