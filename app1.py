from flask import Flask,jsonify, request
# initiating flask
app = Flask(__name__)

# creating tasks
tasks = [
    {
        # task 1
        "id":1,
        "Contact":"9987644456",
        "Name":"raju",
        "done":False

    },
    {
        # task 2
        "id":2,
        "Contact":"9876543222",
        "Name":"Rahul",
        "done":False
    }
]

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task = {
        "id":tasks[-1]["id"]+ 1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact",""),
        "done": False 
    }

    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
# running the app
if(__name__=="__main__"):
    app.run(debug = True)