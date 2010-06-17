import logging
import wsgiref.handlers
from google.appengine.ext import webapp
import os
from google.appengine.ext.webapp import template


class MainHandler(webapp.RequestHandler):
	def get(self):
		title="Where is My Bus?<br/>for DC Circulator"
		body='<p><b>Select Your Route</b></p>'
		body=body+"""
		<hr/>
		"""

		template_values = {'title': title,'body': body,}
		path = os.path.join(os.path.dirname(__file__), 'main.html')
		self.response.out.write(template.render(path, template_values))		
	

def main():
	application = webapp.WSGIApplication(
		[('/', MainHandler),
		],
		debug=True)
	wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
	main()
