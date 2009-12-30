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

import cgi
import os
import urllib

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from pymarc import Record, Field, marcxml, MARCReader

class Default(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'tpl/index.tpl')
        self.response.out.write(template.render(path, template_values))

class Record(webapp.RequestHandler):
    def get(self):
        template_values = {
            'marc': cgi.escape(self.request.get('marc')).replace(" ","+")
        }
        path = os.path.join(os.path.dirname(__file__), 'tpl/record.tpl')
        self.response.out.write(template.render(path, template_values))

class ShowXml(webapp.RequestHandler):
    def get(self):
        # self.response.out.write(cgi.escape(self.request.get('marc')))
        # record = Record(cgi.escape(self.request.get('marc')))	
        reader = MARCReader(cgi.escape(self.request.get('marc')))
        for record in reader: 		
            self.response.headers["Content-Type"] = "text/xml"
            self.response.out.write(marcxml.record_to_xml(record))

class Test(webapp.RequestHandler):
  def get(self):
    record = Record()
    field = Field(
        tag = '245',
        indicators = ['0','1'],
        subfields = [
            'a', 'The pragmatic programmer : ',
            'b', 'from journeyman to master /',
            'c', 'Andrew Hunt, David Thomas.'
        ]
    )
    record.add_field(field)
    # self.response.out.write(record.as_marc())
    self.response.headers["Content-Type"] = "text/xml"
    self.response.out.write(marcxml.record_to_xml(record))

def main():
  application = webapp.WSGIApplication([('/', Default), 
                                        ('/record', Record), 
                                        ('/marcxml', ShowXml), 
                                        ('/test', Test)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
