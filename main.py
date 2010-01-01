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
import md5
import pymarc

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db
from pymarc import Record, Field, marcxml, MARCReader

class SavedRecord(db.Model):
    iso2709 = db.TextProperty()
    date = db.DateTimeProperty(auto_now_add=True)

class Default(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'tpl/index.tpl')
        self.response.out.write(template.render(path, template_values))

# Save a record from the user
class SaveRecord(webapp.RequestHandler):
    def post(self):
        # TODO: Make sure record is valid! 
        savedrecord = SavedRecord()
        marc = cgi.escape(self.request.get('marc'))
        savedrecord.iso2709 = marc
        savedrecord.put()
        # TODO: Redirect to /record ? 
        # self.redirect('/')
        template_values = {
            'key': savedrecord.key()
        }
        path = os.path.join(os.path.dirname(__file__), 'tpl/saverecord.tpl')
        self.response.out.write(template.render(path, template_values))

# Show available options for a record identified by a key
class Record(webapp.RequestHandler):
    def get(self):
        key = cgi.escape(self.request.get('key'))
        savedrecord = db.get(key)
        template_values = {
            'key': key, 
            'marc': savedrecord.iso2709
        }
        path = os.path.join(os.path.dirname(__file__), 'tpl/record.tpl')
        self.response.out.write(template.render(path, template_values))

# Show MARCXML
class ShowXml(webapp.RequestHandler):
    def get(self):
        key = cgi.escape(self.request.get('key'))
        savedrecord = db.get(key)
        record = pymarc.Record(savedrecord.iso2709)
        self.response.headers["Content-Type"] = "text/xml"
        self.response.out.write(marcxml.record_to_xml(record))

# Show record in mnemonic format
class ShowMnem(webapp.RequestHandler):
    def get(self):
        key = cgi.escape(self.request.get('key'))
        savedrecord = db.get(key)
        record = pymarc.Record(savedrecord.iso2709)
       	self.response.headers["Content-Type"] = "text/plain"
        self.response.out.write(record)

# Show author
class Author(webapp.RequestHandler):
    def get(self):
        key = cgi.escape(self.request.get('key'))
        savedrecord = db.get(key)
        record = pymarc.Record(savedrecord.iso2709)
        template_values = {
            'key': key, 
            'author': record.author()
        }
        path = os.path.join(os.path.dirname(__file__), 'tpl/author.tpl')
        self.response.out.write(template.render(path, template_values))

def main():
  application = webapp.WSGIApplication([('/', Default), 
                                        ('/saverecord', SaveRecord), 
                                        ('/record', Record), 
                                        ('/marcxml', ShowXml), 
                                        ('/mnem', ShowMnem), 
                                        ('/author', Author)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
