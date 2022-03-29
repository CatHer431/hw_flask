from flask import Flask

ques1 = Flask(__name__)

@ques1.route("/")
def home():
 name = 'Cathy'
 city_names = ["Paris", "London", "Rome", "Tahiti"]
 return f'''
 <html>
    <head>
        <title>Low Pass Question</title>
    </head>
    <body>
        <h1>Welcome {name}!</h1>
        <a href="https://google.com">not google</a>
        <ul>
         <li>{city_names[0]}</li>
	 <li>{city_names[1]}</li>
	 <li>{city_names[2]}</li>
	 <li>{city_names[3]}</li>
        </ul>
    </body>
 </html>'''

#if __name__ == '__main__':
#ques1.run()
