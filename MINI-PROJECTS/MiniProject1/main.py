from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

# main page route
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/getData', methods=['POST'])
def getData():
    filePath="datajson/users.json"
    # open the file
    jsonFile = open(filePath, "r+")
    # want to check if file has data
    first_char = jsonFile.read(1)
    # if is empty (first time)
    if not first_char:
        print("The file is empty.")
        # put the data from the html form into the list
        theList = [request.form]
        # put into json
        json.dump(theList,jsonFile, indent=4)
        jsonFile.close()
    else:
        jsonFile.seek(0)
        print("The file has content.")
        theList = json.load(jsonFile)
        jsonFile.truncate(0)
        jsonFile.close()
        # open a new file - will overwrite
        jsonFile_write = open(filePath, "w")
        theList.append(request.form)
        json.dump(theList,jsonFile_write,indent=4)
        jsonFile_write.close()
    # send back response
    return({"added":"success"})
app.run(debug=True)
