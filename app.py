# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/home")
def home():

    name = "Vivaan Keluskar" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    F_name = "Narayan Keluskar"
    F_age = "45"

    return render_template('father.html' F_name = F_name, F_age = F_age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    M_name = "Varsha Keluskar"
    M_age = "42"

    return render_template('mother.html' M_name = M_name, M_age = M_age)

# define the route to friends webpage
@app.route("/friend")
def friend():

    Fr_name = "Avyukta Hebbar"
    Fr_age = "45"

    return render_template('friend.html' Fr_name = Fr_name, Fr_age = Fr_age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
