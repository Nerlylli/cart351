from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("pineapple.html")

@app.route('/favfruit')
def another():
    return render_template("pineapple_2.html")

@app.route('/three/<name>')
def three(name):
    someList = ["one", "two","three","four","five"]
    someDict = {"color":"yellow", "feature":"spiky","taste":"delicious"} 
    return render_template("pineapple_3.html", 
                           someNewVar = name,
                           someNewList = someList,
                           someNewDict = someDict
                           )

@app.route('/four')
def four():
    a_new_list = [1,2,3,4,5]
    b_new_list = ["yellow","orange","blue", "green", "turquoise","fuscia","navy"]

    return render_template("pineapple_4.html",
                           a_num_list = a_new_list,
                           color_list = b_new_list
                           )



@app.route('/five')
def five():
    userLoggedIn = True
    return render_template("pineapple_5.html",
                           user_bool = userLoggedIn 
                           )

app.run()