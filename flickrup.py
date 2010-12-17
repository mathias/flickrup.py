#!/usr/bin/python
"""Usage: python flickrup.py
Edit this file with your API keys and your username!

Requires:
 - flickr.py from http://code.google.com/p/flickrpy/
"""

__author__ = "Matt Gauger <matt.gauger@gmail.com>"
__version__ = "0.0.1a"
__date__ = "2010-12-17"
__copyright__ = "Copyright 2010 Matt Gauger"

import sys
import os
import urllib
import flickr # http://code.google.com/p/flickrpy/

# Generate keys and FILL THESE OUT
# http://www.flickr.com/services/apps/create/noncommercial/
flickr.API_KEY = ''
flickr.API_SECRET = ''

# find this on http://www.flickr.com/account
# it's whatever it says next to "Your screen name"
me = flickr.people_findByUsername("")

page = 1
total_photos = found_photos = 0

while 1:
  try:
    photos = flickr.people_getPublicPhotos(me.id, 100, page)
    for photo in photos:
      total_photos += 1
      # skip if we already have this photo
      have_photo = os.path.exists("%s_%s_%s_o.jpg" % (photo.server, photo.id, photo.secret))
      if not have_photo:
        data = urllib.urlretrieve("http://static.flickr.com/%s/%s_%s_o.jpg" % (photo.server, photo.id, photo.secret), "%s_%s_%s_o.jpg" % (photo.server, photo.id, photo.secret))
        print "save %s" % photo.title
        found_photos += 1
    page += 1
  except AttributeError:
    break # This shouldn't happen!

print "Found %s photos, saved %s new photos" % (total_photos, found_photos)


