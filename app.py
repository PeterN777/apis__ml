import joblib
from flask_cors import CORS
from flask import Flask, jsonify, request
app= Flask(__name__)
CORS(app)
@app.route("/home")
def home():
    return "Welcome home 00001"

@app.route("/summation")
def add():
    num1=2
    num2=4
    answer = num1+num2
    return f"answer is {answer}"
# get - retrieve info from server without providing no info
# post - provide info to server
# put - update info to server
# patch - update some part of info to server
# delete - remove info from server.

@app.route("/product",methods=['POST'])
def multiply():
    num1= request.form['num1']
    num2= request.form['num2']
    print (type(num1))
    answer= int(num1)* int(num2)
    # return f"product of {num1} and {num2} is {answer}"
    return jsonify({"product": answer})

@app.route("/recipe", methods= ["POST"])
def recipe():
# Flour	Milk	Sugar	Butter	Egg	Baking Powder	Vanilla	Salt    
    flour = int( request.form["flour"])
    milk = int(request.form["milk"])
    sugar = int( request.form["sugar"])
    butter = int(request.form["butter"])
    egg = int(request.form["egg"])
    baking_powder = int(request.form["baking_powder"])
    vanilla = int(request.form["vanilla"])
    salt = int(request.form["salt"])

    model = joblib.load("Model4.joblib")
    recipe=[[flour,milk,sugar,butter,egg,baking_powder,vanilla,salt]] 
   
    outcome = model.predict(recipe)[0]

    # Convert NumPy scalar (e.g. np.str_, np.int64, np.float64) to a native Python type
    if hasattr(outcome, "item"):
        outcome = outcome.item()

    return jsonify({"recipe": str(outcome)})


# app.run(debug=True)