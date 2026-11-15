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

    # app.logger.info(request.args["id"])
    # app.logger.info(request.args["score"])
    filePath="Datajson/users.json"
    if os.path.exists(filePath):
        jsonFile = open(filePath, "r+")
        theList = json.load(jsonFile)
        # nameExists = False
        # oldData = ""
        # for el in theList:
        #     if el["id"].upper() ==  request.args["id"].upper():
        #         nameExists = True
        #         oldData = el["score"]
        #         el["score"] = request.args["score"]
        #         break # This exits the loop entirely
        #clear 
        jsonFile.truncate(0)
        jsonFile.close()
        jsonFile_write = open(filePath, "w")
        if nameExists ==True: 
            json.dump(theList,  jsonFile_write, indent =4)
            jsonFile_write.close()
            return({"inFile":"true","score":oldData})
        else:
            theList.append(request.args)
            json.dump(theList, jsonFile_write, indent =4)
            jsonFile_write.close()
            return({"inFile":"false"})
app.run(debug=True)
