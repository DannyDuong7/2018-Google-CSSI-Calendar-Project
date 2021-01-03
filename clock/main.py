#simple clock application from the book.
import datetime
import jinja2
import os
import webapp2
from google.appengine.api import users

template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):
        current_time = datetime.datetime.now();
        message='<p>The time is: %s</p>' % current_time
        user = users.get_current_user()
        username = 'jxc064000'
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

application = webapp2.WSGIApplication([('/', MainPage),
                ('/onSubmit', CounterPage)],
                debug = True)
