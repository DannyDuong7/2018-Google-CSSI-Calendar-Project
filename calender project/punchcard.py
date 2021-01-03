import logging
import webapp2
import jinja2
import os
import calendar
from google.appengine.api import users

the_jinja_env = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape=True)

c = calendar.TextCalendar(calendar.SUNDAY)
date = c.formatmonth(2018, 8)
#row = c.yeardatescalendar(2018)
row=""
counter=0
month=""
for i in c.itermonthdays(2018,8):
    counter+=1
    if(counter<35):
        row += str(i)+" "
#    else:
#        row += '\n'
#        counter=0
x = row.split(' ')


class LogIn(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        login_url = users.create_login_url(self.request.path)
        logout_url = users.create_logout_url(self.request.path)
        templateget = the_jinja_env.get_template('punchcard.html')
        context = {'greetings': 'Welcome to the Punch Card Calendar',
        'mode':1,
        'login_url': login_url,
        'logout_url': logout_url,
        'user':user,}
        self.response.out.write(templateget.render(context))
    def post(self):
        templatepost= the_jinja_env.get_template('punchcard.html')
        user = users.get_current_user()
        login_url = users.create_login_url(self.request.path)
        logout_url = users.create_logout_url(self.request.path)
        password=self.request.get('password')
        wrong=" "
        mode=1
        if(password=='cssi'):
            mode=2
        else:
            mode=1
            wrong = ": Wrong! Try again."
        context = {'greetings': 'Welcome to the Punch Card Calendar',
        'mode': mode,
        'login_url': login_url,
        'logout_url': logout_url,
        'user':user,
        'wrong':wrong
        }
        self.response.out.write(templatepost.render(context))


class Calendar(webapp2.RequestHandler):
    def post(self):
        templatepost = the_jinja_env.get_template('punchcard.html')
        pay=self.request.get('pay')
        context = {
                   'mode': 2,
                   'pay':pay,
                   }
        self.response.out.write(templatepost.render(context))


class ClockIn(webapp2.RequestHandler):
    def get(self):
        templateget = the_jinja_env.get_template("punchcard.html")
        hourlyrate = self.request.get('hourlyrate')
        d=self.request.get('select')
        display1 = self.request.get('display')
        enter=self.request.get('enter')
        context = {
        'display1': display1,
        'hourlyrate': hourlyrate,
	    'Date': d,
        'mode' : 3
        }
        self.response.out.write(templateget.render(context))
    def post(self):
        template = the_jinja_env.get_template("punchcard.html")
        hourlyrate = self.request.get('hourlyrate')
        d=self.request.get('select')
        display1 = self.request.get('display')
        enter=self.request.get('enter')
        context = {
        'display1': display1,
        'hourlyrate': hourlyrate,
	    'Date': d,
        'mode': 3
        }
        self.response.out.write(template.render(context))





app = webapp2.WSGIApplication(([('/',LogIn),('/onSubmit',Calendar),('/clock',ClockIn)]),debug=True)
