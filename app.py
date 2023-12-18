from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Sacramento, CA",
    "salary": "$10,000"
  },
  {
    "id": 2,
    "title": "Data Engineer",
    "location": "San Mateo, CA"
  },
  {
    "id": 3,
    "title": "Software Developer",
    "location": "New York, NY",
    "salary": "$20,000"
  },
  {
    "id": 4,
    "title": "Data Scientist",
    "location": "Merced, CA",
    "salary": "$210,000"
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company="Miles'")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)