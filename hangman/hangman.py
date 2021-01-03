import webapp2
import jinja2
import os
import random

count=0


the_jinja_env = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape=True)

#this class with the argument is to get the key and response to direct it to the web page RequestHandler is a package while webapp2 is function
class HangClass(webapp2.RequestHandler):
    #function to perform when person loads into localhost:8080, get and post are built in to the https websites
    def get(self):
        welcome_template = the_jinja_env.get_template('hangman.html')#jinja env is a package that uses the function get template to take the html file that you choose which in this case is guess-game.html
        a_dictionary = {'greetings': 'Welcome to the Hangman Game !',}
        self.response.write(welcome_template.render(a_dictionary))#the self.response has been predefined in the RequestHandler which is used to initialized the function which in this case is write
# post is what data you want to past onto the website
    def post(self):
        result_template = the_jinja_env.get_template('hangman.html')
        guess_letter = self.request.get('guess_l')
        for index in range(0,len(word)):
            if(word[index] == guess_letter):
                if(index)

    def computeBlanks(word):
        x=len(word)
        str=""
        y=0
        while(y<x):
            str+="_"
            y+=
            return str

#the action in the html file will read the variable app because we gave action '/' in html and look for app in this python file and read what the app equals and look for the GuessClass since we specified it in the vaiable and perform the class
app = webapp2.WSGIApplication([('/',HangClass)],debug=True)
