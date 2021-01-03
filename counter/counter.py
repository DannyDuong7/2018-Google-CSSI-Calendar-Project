#simple clock application from the book.
import datetime
import jinja2
import os
import webapp2
import cloudstorage as gcs
from google.appengine.api import app_identity
from google.appengine.api import users

counter = 0
word='correct'
template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

def createFile(filename):
    write_retry_params = gcs.RetryParams(backoff_factor=1.1)
    file = gcs.open(filename, 'w',
            content_type = 'text/plain',
            options = {'x-goog-meta-1': 'meta1',
                       'x-goog-meta-2': 'meta2'},
            retry_params = write_retry_params)
    file.write("this is the first line\n")
    file.write("this is the second line\n")
    file.close()

def readFile(filename):
    file = gcs.open(filename)
    line = file.readline()
    file.close()
    return line

# this class's 'get' function is called when the main page is loaded.
class MainPage(webapp2.RequestHandler):
    def get(self):
        current_time = datetime.datetime.now();
        bucketname = os.environ.get('BUCKET_NAME',
            app_identity.get_default_gcs_bucket_name())
        createFile('/' + bucketname + '/jcssi.txt')
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
            'bucket': bucketname
        }
        self.response.out.write(template.render(context))

class CounterPage(webapp2.RequestHandler):
    def post(self):
        global counter
        global word
        answer= self.request.get("answer")
        bucketname = os.environ.get('BUCKET_NAME',
            app_identity.get_default_gcs_bucket_name())
        line = readFile('/' + bucketname + "/jcssi.txt")
        if (answer == 'computer'):
            answer = "Correct!"
        else:
            answer = "Wrong! Try again."
        current_time=datetime.datetime.now()
        counter = counter +1
        template = template_env.get_template('index.html')
        context={
            'mode': 2,
            'current_time': current_time,
            'counter': counter,
            'answer': answer,
            'line': line,
        }
        self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/', MainPage),
                ('/onSubmit', CounterPage)],
                debug = True)
