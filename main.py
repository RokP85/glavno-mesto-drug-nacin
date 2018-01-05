#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import jinja2
import webapp2
import random


#           "GC_GET2/templates"
#       "GC_GET2"
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("zacetna stran.html")

class KvizHandler(BaseHandler):
    def get(self):
        params = {"drzava": generirano()}
        return self.render_template("glavno mesto.html", params=params)

    def post(self):
        vnos = self.request.get("vnos")

        if generirano() == "Kitajske" and vnos.lower() == "peking":
                return self.write("Drži glavno mesto Kitajske je Peking")
        elif generirano() == "Kanade" and vnos.lower() == "otawa":
                return self.write("Drži glavno mesto Kanade je Otawa")
        elif generirano() == "Indonezije" and vnos.lower() == "jakarta":
                return self.write("Drži glavno mesto Indonezije je Jakarta")
        elif generirano() == "Tunizije" and vnos.lower() == "tunis":
                return self.write("Drži glavno mesto Tunizije je Tunis")
        else:
            return self.write("Napačno mesto")


def generirano():
    drzava = ["Kitajske", "Kanade", "Indonezije", "Tunizije"]
    auto_izbor = random.choice(drzava)
    return auto_izbor


app = webapp2.WSGIApplication([
    webapp2.Route("/", MainHandler),
    webapp2.Route("/kviz", KvizHandler)
], debug=True)
