from email.mime import image
import os
import json
import urllib
from xml.dom.minidom import Document
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        name = self.request.get('name')
        url = "https://ghibliapi.herokuapp.com/films?title="+name; 
        data = urllib.urlopen(url).read()
        
        data = json.loads(data)

        if(data):
            title = data[0]['title']
            orgTitle = data[0]['original_title']
            imgsrc = data[0]['image']
            banner = data[0]['movie_banner']
            director = data[0]['director']
            producer = data[0]['producer']
            desc = data[0]['description']
            rdate = data[0]['release_date']
            rtime = data[0]['running_time']
            rtScore = data[0]['rt_score']

            template_values = {
                "title": title,
                "orgTitle": orgTitle ,
                "director": director,
                "banner":banner,
                "producer": producer,
                "description": desc,
                "image":imgsrc,
                "rdate": rdate,
                "rtime": rtime,
                "rtScore": rtScore
            }
        
            path = os.path.join(os.path.dirname(__file__), 'results.html')
            self.response.out.write(template.render(path, template_values))
        else:
            template_values = {}
            path = os.path.join(os.path.dirname(__file__), 'error.html')
            self.response.out.write(template.render(path, template_values))
        
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)



