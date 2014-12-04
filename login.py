#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib
import webapp2
import jinja2
import models

from webapp2_extras import sessions

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

	
class LoginHandler(webapp2.RequestHandler):
	def dispatch(self):
		# Get a session store for this request.
		self.session_store = sessions.get_store(request=self.request)
		try:
        # Dispatch the request.
			webapp2.RequestHandler.dispatch(self)
		finally:
			# Save all sessions.
			self.session_store.save_sessions(self.response)
	def get(self):
		#insert a user
		#models.Users.insertUser('username', 'password', 'email@test-dancingoggin.appspot.com')
		self.session['initiated'] = 'false'
		self.session['user'] = ''
		template_values ={}
		path = self.request.path
		template = JINJA_ENVIRONMENT.get_template('templates/login.html')
		self.response.write(template.render(template_values))

	def post(self):
		username = self.request.get('username')
		password = self.request.get('password')
		loginSuccess = models.Users.loginProcess(username, password)
		if(loginSuccess):
			self.session['initiated'] = 'true'
			self.session['user'] = username
			self.redirect('/')
			#self.redirect('/adminLessons')
		else:
			self.redirect('/login')
	@webapp2.cached_property
	def session(self):
	    # Returns a session using the default cookie key.
	    return self.session_store.get_session()

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}		
app = webapp2.WSGIApplication([
    ('/login', LoginHandler),
	
],config = config, debug=True)
