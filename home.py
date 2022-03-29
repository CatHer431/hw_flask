from flask import Flask

ques1 = Flask(__name__)

global name
global city_names
#city_names = ["Paris", "London", "Rome", "Tahiti"]

@ques1.route("/")
def home():
 return '''
 <html>
    <head>
        <title>Low Pass Question</title>
    </head>
    <body>
    <h1>Welcome """  + name + """ </h1>
    <a href="www.google.com">not google </a>
    <ul>
     {% for city in city_names %}
      <li>city.name</li>
     {% endfor %}
    </ul>
   </body>
 </html>
 ''' 



#ques1.run()
