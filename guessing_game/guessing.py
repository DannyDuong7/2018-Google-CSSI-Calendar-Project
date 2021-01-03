#simple clock application from the book.
import datetime
import jinja2
import os
import webapp2
import random
from google.appengine.api import users

secret=random.randint(1,20)
counter = 0
word='correct'
template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

# this class's 'get' function is called when the main page is loaded.
class MainPage(webapp2.RequestHandler):
    def get(self):
        current_time = datetime.datetime.now();
        message='<p>The time is: %s</p>' % current_time
        user = users.get_current_user()
        #username = 'jxc064000'
        #print user.email()
        login_url = users.create_login_url(self.request.path)
        logout_url = users.create_logout_url(self.request.path)
        #login_url = 'index.html'
        #logout_url = 'index.html'
        #self.response.out.write(message)

        template = template_env.get_template('index.html')
        context = {
            'mode': 1,
            'current_time': current_time,
            'user': user,
            'login_url': login_url,
            'logout_url': logout_url,
        }
        self.response.out.write(template.render(context))

class GuessingPage(webapp2.RequestHandler):
    def post(self):
        global counter
        global word
        answer= self.request.get("answer")
        if (answer == secret):
            answer = "Correct"
            mode = 3
        elif (answer>secret):
            answer ="Too high, guess lower: "
        elif (answer<secret):
            answer="Too low, guess higher: "
        current_time=datetime.datetime.now()
        counter = counter +1
        template = template_env.get_template('index.html')
        context={
            'mode': 2,
            'current_time': current_time,
            'counter': counter,
            'answer': answer,
        }
        self.response.out.write(template.render(context))

class CorrectPage(webapp2.RequestHandler):
    def get(self):
        global counter
        template = template_env.get_template('index.html')
        context={
            'mode': 3,
            'current_time': current_time,
            'counter': counter,
            'answer': 'You won nothing ',
        }
        self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/', MainPage),
                ('/onSubmit', GuessingPage),
                ('/Correct',CorrectPage)],
                debug = True)
