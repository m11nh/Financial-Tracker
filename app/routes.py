from app import app
from app.client import start_client, pickle_update
from flask import render_template, request
import datetime

system = start_client()
currDate = datetime.datetime.now()
currDateString=(currDate.strftime("%d")+"-"+currDate.strftime("%m")+"-"+currDate.strftime("%Y"))
print(currDateString)
print(currDate.strftime("%d"))
print(currDate.strftime("%m"))
print(currDate.strftime("%Y"))

@app.route('/', methods=["GET", "POST"])
def index(): 
    if (request.method == "GET"): 
        return render_template("static.html", currDate=currDate)
    elif (request.method == "POST"): 
        print(request.form.get('expenseAmount'))
        return render_template("static.html", currDate = currDate)
    else: 
        return render_template("static.html", currDate=currDate)