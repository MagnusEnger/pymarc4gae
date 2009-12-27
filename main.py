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

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from pymarc import Record, Field, marcxml, MARCReader

class Default(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <h1>pymarc4gae</h1>
              <p>Paste in some MARC in ISO2709 format and click the button to get back MARCXML.</p>
              <form action="/show" method="post">
                <div><textarea name="marc" rows="20" cols="120"></textarea></div>
                <div><input type="submit" value="Create MARCXML"></div>
              </form>
              <hr />
              <p>Created by <a href="http://libriotech.no/">Libriotech</a>. Based on <a href="http://github.com/edsu/pymarc">pymarc</a>. Work in progress...</p>
            </body>
          </html>""")

class ShowXml(webapp.RequestHandler):
    def post(self):
        # self.response.out.write(cgi.escape(self.request.get('marc')))
        record = Record(cgi.escape(self.request.get('marc')))			
        self.response.headers["Content-Type"] = "text/xml"
        self.response.out.write(marcxml.record_to_xml(record))

"""            
class ShowXml(webapp.RequestHandler):
    def get(self):
        self.response.out.write("Error")
"""

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
                                        ('/show', ShowXml), 
                                        ('/test', Test)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
