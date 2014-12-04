import os
import urllib
import urllib2
import webapp2
import jinja2
import models
import json
from google.appengine.ext import ndb
from datetime import datetime
import sys
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class CKEditorPage(webapp2.RequestHandler):
	def get(self):
		editors = models.Editor.getAllEditors()
		template_values = {'editors': editors}
		template = JINJA_ENVIRONMENT.get_template('templates/ckeditorTest.html')
		self.response.write(template.render(template_values))
			
	def post(self):
		logging.debug("POSTED CKEDITOR DATA")
		data = self.request.body
		logging.debug(data)
		
		models.Editor.insertEditor(data)
		#models.Editor.getAllEditors()
		self.redirect('/ckeditor')
		

app = webapp2.WSGIApplication([
			('/ckeditor', CKEditorPage),
			],debug=True)