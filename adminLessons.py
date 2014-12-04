import os
import urllib
import urllib2
import webapp2
import jinja2
import models
import json
from google.appengine.ext import ndb
from datetime import datetime
from main import BaseHandler
import sys
import logging
import webapp2

from webapp2_extras import sessions
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class AddLesson(BaseHandler):
	def get(self):
		template_values ={}
		template = JINJA_ENVIRONMENT.get_template('templates/addLesson.html')
		self.response.write(template.render(template_values))
		logging.debug("AddLesson Get done")
		
	
	
class UpdateLesson(BaseHandler):
	def post(self):
		logging.debug("AddLesson Post start")
		#get all the table data
		jsonstring = self.request.body
		self.response.out.write(jsonstring)
		jsonObject = json.loads(jsonstring)
		id = jsonObject[0]['value']
		type = jsonObject[1]['value']
		city = jsonObject[2]['value']
		location = jsonObject[3]['value']
		date = jsonObject[4]['value']
		time = jsonObject[5]['value']
		cost = jsonObject[6]['value']
		details = jsonObject[7]['value']
		models.LessonTest.updateLessonByID(id, type, city, date, time, location, cost, details)
		#models.LessonTest.insertLesson(type, city, date, time, location, cost, details)
		logging.debug("Addlesson Post done")
		#self.redirect('/lessons')	
		
	
	
class EditLesson(BaseHandler):
	def post(self):
		logging.debug("EditLesson POST start")
		id = self.request.body
		logging.debug("id: " +id)
		lesson = models.LessonTest.getLessonByID(id)
		template_values ={'lesson':lesson}
		template = JINJA_ENVIRONMENT.get_template('templates/editLesson.html')
		self.response.write(template.render(template_values))
		logging.debug("EditLesson Get done")
	
class DeleteLesson(BaseHandler):
	def post(self):
		logging.debug("DELETE LessonTest POST start")
		id = self.request.body
		logging.debug("id: " +id)
		lesson = models.LessonTest.deleteLessonByID(id)
		self.response.write("deleted")
		logging.debug("DeleteLesson Get done")
		
	
	
class AdminLessonsPage(BaseHandler):
	def get(self):
		#models.LessonTest.deleteAllLessons()
		user = self.session.get('user')
		logging.debug(user)
		if user == None:
			self.redirect('/login')
		privateLessons = models.LessonTest.getAllLessonsByType('Private & Group Lessons (by appointment)')
		dropInlessons = models.LessonTest.getAllLessonsByType('Group Lessons/Dances Drop-In')
		groupLessons = models.LessonTest.getAllLessonsByType('Group Lessons (4-6 week sessions)')
		
		#get LessonTest by city
		template_values ={'privateLessons': privateLessons,'dropInLessons':dropInlessons, 'groupLessons': groupLessons}
		template = JINJA_ENVIRONMENT.get_template('templates/adminLessons.html')
		self.response.write(template.render(template_values))
		
	

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}		
app = webapp2.WSGIApplication([
		('/adminLessons', AdminLessonsPage),
		('/addLesson', AddLesson),
		('/updateLesson', UpdateLesson),
		('/editLesson', EditLesson),
		('/deleteLesson', DeleteLesson),
		],config = config, debug=True)