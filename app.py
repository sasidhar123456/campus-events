from flask import Flask, render_template, request, redirect
app = Flask(__name__)
events = []
@app.route('/')
def index():
    return render_template("index.html", events=events)
@app.route('/add', methods=['POST'])
def add_event():
    name = request.form['name']
    date = request.form['date']
    location = request.form['location']
    description = request.form['description']
    event = {"id": len(events) + 1, "name": name, "date": date, "location": location, "description": description}
    events.append(event)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)