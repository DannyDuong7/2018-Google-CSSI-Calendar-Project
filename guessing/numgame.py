import webapp2
import jinja2
import os
import random

the_jinja_env = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape=True)

r=random.randint(1,100)

#this class with the argument is to get the key and response to direct it to the web page RequestHandler is a package while webapp2 is function
class GuessClass(webapp2.RequestHandler):
    #function to perform when person loads into localhost:8080, get and post are built in to the https websites
    def get(self):
        welcome_template = the_jinja_env.get_template('guess-game.html')#jinja env is a package that uses the function get template to take the html file that you choose which in this case is guess-game.html
        a_dictionary = {'greetings': 'Welcome to the Guessing Game !',}
        self.response.write(welcome_template.render(a_dictionary))#the self.response has been predefined in the RequestHandler which is used to initialized the function which in this case is write
# post is what data you want to past onto the website
    def post(self):
        result_template = the_jinja_env.get_template('guess-game.html')
        guessno = self.request.get('guess_no')
        guessint = int(guessno)
        if(guessint < r):
            self.response.write('Too low. Go back and try again')
        elif(guessint > r):
            self.response.write('Too high. Go back and try again')
        else:
            self.response.write('You got the correct answer')

#the action in the html file will read the variable app because we gave action '/' in html and look for app in this python file and read what the app equals and look for the GuessClass since we specified it in the vaiable and perform the class
app = webapp2.WSGIApplication([('/',GuessClass)],debug=True)
