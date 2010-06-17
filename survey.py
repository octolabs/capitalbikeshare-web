import logging
import wsgiref.handlers
from google.appengine.ext import webapp
import os
from google.appengine.ext.webapp import template

import cgi
import models


class SurveyHandler(webapp.RequestHandler):
	def post(self):
		title="Where is My Bus?<br/>for DC Circulator"
		body='<p><b>Select Your Route</b></p>'
		body=body+"""
		<hr/>
		"""
		
		survey=models.Survey()
		survey.data=cgi.escape(self.request.get('data'))
		survey.circulator=cgi.escape(self.request.get('group1'))
		survey.commute=str(self.request.get('group2',allow_multiple=True))
		survey.smartbike=cgi.escape(self.request.get('group3'))
		survey.cabi=cgi.escape(self.request.get('group4'))
		survey.email=cgi.escape(self.request.get('email'))
		
		survey.put()

		template_values = {'title': title,'body': body,}
		path = os.path.join(os.path.dirname(__file__), 'survey.html')
		self.response.out.write(template.render(path, template_values))		
	

def main():
	application = webapp.WSGIApplication(
		[('/survey', SurveyHandler),
		],
		debug=True)
	wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
	main()
