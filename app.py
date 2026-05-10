from flask import Flask, render_template
import json

app = Flask(__name__)

# Load aircraft data
with open("aircrafts.json", "r") as file:
    aircrafts = json.load(file)

# Home Page
@app.route("/")
def home():
    return render_template("index.html", aircrafts=aircrafts)

# Aircraft Detail Page
@app.route("/aircraft/<int:id>")
def aircraft_detail(id):

    aircraft = next((a for a in aircrafts if a["id"] == id), None)

    return render_template("aircraft.html", aircraft=aircraft)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)