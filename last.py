import os
import urllib
import webapp2
import jinja2
import models

class UserReportedCountry(db.Model):
  country_name = db.StringProperty( required=True,
                          choices=['Afghanistan','Aring land Islands']
                         )

class UserReportedCity(db.Model):
  country = db.ReferenceProperty(UserReportedCountry, collection_name='cities')
  city_name = db.StringProperty(required=True)   

class UserReportedStatus(db.Model):
  city = db.ReferenceProperty(UserReportedCity, collection_name='statuses')
  status = db.BooleanProperty(required=True)
  date_time = db.DateTimeProperty(auto_now_add=True)


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	

class MainPage(webapp2.RequestHandler):
    def get(self):
        User_country=UserReportedCountry.all().fetch(1000)
        return self.response.out.write(template.render('#lessons','{'user_c':User_country}))	
	
	
	
class CalendarPage(webapp2.RequestHandler):
   def get(self):
        #self.response.write('Hello world!')
		template_values ={}
		template = JINJA_ENVIRONMENT.get_template('templates/calendar.html')
		self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([('/calendar', CalendarPage)],
                              debug=True)