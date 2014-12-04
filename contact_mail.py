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

from google.appengine.api import mail

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class Login2Handler(webapp2.RequestHandler):
	def get(self):
		#insert a user
		#models.Users.insertUser('testUsername', 'testPassword', 'testEmail@dancingoggin.appspot.com')
		template_values ={}
		path = self.request.path
		template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
		self.response.write(template.render(template_values))
	def post(self):
		notification_address = "fisher.robert26@gmail.com"
		sender_address = "<fisher.robert26@gmail.com>"
		subject = self.request.get("inputSubject")
		subject2 = "(Email from user Dancin goggin) Subject: "+subject
		name=self.request.get("inputName")
		phone=self.request.get("inputPhone")
		user_address = self.request.get("inputEmail")
		body = "\nName: "+name+"\nPhone: "+phone+"\nMessage: \n"+self.request.get("inputMessage")+"\nEmail: "+user_address

		
		
		subject_confirmation = "Confirmation, mail received."
		if subject == "Appointment":
			body_confirmation = "\nYour request for an appointment was received succesfully and an administrator will get in touch with you to plan the appointment: \n\n This is what you sent:\n Subject: "+subject+""+body
		if subject == "Shoes":
			body = "\nName: "+name+"\nPhone: "+phone+"\nMessage: \n"+self.request.get("inputMessage")+"\nShoes size: "+self.request.get("size")+"\nGender: "+self.request.get("gender")+"\nEmail: "+user_address
			body_confirmation = "\nYour request for shoes was received succesfully and an administrator will get in touch with you as soon as possible: \n\n This is what you sent:\n Subject: "+subject+""+body
		else:
			body_confirmation = "\nYour email was received succesfully and an administrator will get in touch with you as soon as possible: \n\n This is what you sent:\n Subject: "+subject+""+body
		mail.send_mail(sender_address, user_address, subject_confirmation, body_confirmation)
		algo="assignacion"
		mail.send_mail(sender_address, sender_address, subject2, body)
		self.redirect('/succes_message')
		
		
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}	
app = webapp2.WSGIApplication([
	('/contact_mail', Login2Handler),
		

], config = config, debug=True)