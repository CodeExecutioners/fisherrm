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
import logging
from main import BaseHandler
from google.appengine.api import mail

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
 
class EmailHandler(BaseHandler):
    def get(self):
        path = self.request.path
    def post(self):
        #sender_address must be gmail"
        sender_address = "fisher.robert26@gmail.com"
        subject = "Gift Certificate"
        name = self.request.get("giftInputName")
        recipient = self.request.get("giftInputRecipientName")
        email = self.request.get("giftInputEmail")
        address = self.request.get("giftInputAddress")
        city = self.request.get("giftInputCity")
        state = self.request.get("giftInputState")
        zip = self.request.get("giftInputZip")
        amount = self.request.get("giftInputAmount")
       
        if not mail.is_email_valid(sender_address):
            # prompt user to enter a valid address
            self.redirect('/InvalidMail')
        else:
            body = name + " would like to place an order for a gift certificate in the amount of " + amount + "\n"
            body += ("The gift certificate is for " + recipient + " and is to be sent to the address:\n")
            body += ("\n" + email+ "\n" + city + " " + state + " " + zip)
            logging.debug("Gift Email Body: " + body)
            html = "<p>Test</p>"
            mail.send_mail(sender_address, email, subject, body)
            self.redirect('/succes_message')
			
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}	
app = webapp2.WSGIApplication([
('/giftemail', EmailHandler),
 

], config=config, debug=True)