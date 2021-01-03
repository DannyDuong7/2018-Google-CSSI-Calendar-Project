import webapp2
import jinja2
import os
import random


the_jinja_env = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape=True)

fortunelist=['You will get something today','You do not get anything']
fortune=random.choice(fortunelist)

class Main(webapp2.RequestHandler):
    def get(self):
        templateget=the_jinja_env.get_template('fortune.html')
        dictionary={'greetings':'Welcome to your daily fortune!','Signs':'Enter your zodias sign in the box below'}
        self.response.write(templateget.render(dictionary))

    def post(self):
        templatepost= the_jinja_env.get_template('fortune.html')
        zodiac = self.request.get('zodiac')
        zodiac_sign=str(zodiac)
        if (zodiac_sign=='Sagittarius'):
            self.response.write(fortune)
        dictionary={'greetings':'Welcome to your daily fortune!','Signs':'Enter your zodias sign in the box below'}
        self.response.write(templatepost.render(dictionary))

app = webapp2.WSGIApplication(([('/',Main)]),debug=True)
