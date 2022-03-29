from flask import Flask

ques1 = Flask(__name__)

name = 'Cathy'
city_names = ["Paris", "London", "Rome", "Tahiti"]

@ques1.route("/")
def home(): 
 html = '''
     <head>
        <title>Low Pass Question</title>
     </head>
     <body>
      <h1>Welcome ''' + name + '''! </h1>
      <a href="www.google.com">not google </a>
      <ul>
 '''
 for city in city_names:
  html = html + "<li>" + city + "</li>"
 html = html + '''</ul> </body>'''
 return html

#ques1.run()
