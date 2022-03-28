from flask import Flask, render_template

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
# called view function
def home():
 name = "Cathy"
 city_names = ["Paris", "London", "Rome", "Tahiti"]
 return render_template('home.html', name = name, city_names=city_names)


myapp_obj.run()
