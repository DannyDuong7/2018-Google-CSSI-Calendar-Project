import webapp2
import jinja2
import os
import random

the_jinja_env = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape=True)

wordlist=['newyork','chicago', 'dallas', 'losangles','keller']
word=random.choice(wordlist)

count=0
blankarray=[]
while count < len(word):
    blankarray.append("_ ")
    count += 1
blankword= "".join(blankarray)
dictionary={}

class Main(webapp2.RequestHandler):
    def get(self):
        templateget=the_jinja_env.get_template('hang2.html')
        dictionary={"greeting":"Welcome to the hangman game !", "blankarray":"".join(blankarray),}
        self.response.write(templateget.render(dictionary))
    #in this post function the python will go to the html file because we establish that this function will perform with the html file and it as it runs it looks for any variables that is not in the html in the python file

    def post(self):
        templatepost= the_jinja_env.get_template('hang2.html')
        guess = self.request.get('guess')
        for index in range(0,len(word)):
            if (guess in word[index]):
                blankarray[index]=guess
            updatedstring="".join(blankarray)

        dictionary = {"greeting": "Welcome to the hangman game","blankarray":"".join(blankarray),}
        self.response.write(templatepost.render(dictionary))


app = webapp2.WSGIApplication(([('/',Main)]),debug=True)
