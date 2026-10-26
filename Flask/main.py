from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello CART 351!'

@app.route("/about")
def about():
    return '<h1 style = "color:purple"> About Cart 351!</h1>'

@app.route("/user/<name>")
def user_profile(name):
    return f"<h2> This is <span style = 'color:green'>{name}'s</span> profile page" 

# @app.route("/another/<dynamicVar>")
# def another_route(dynamicVar):
#     # we will use templates sooN!
#     return f"<h2> the 100th letter of {dynamicVar} is {dynamicVar[99]}</h2>"

# Routine Exercise
#Task: You will creating a simple web page that converts cat names into cat-latin:) - made up..

@app.route("/catlatin/<word>")
def cat_latin(word):
    if (word[-1].lower() != "y"): #[-1] is the last characther
        return f"{word}y"
    return f"{word[:-1]}iful"

app.run()
