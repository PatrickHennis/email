#!/usr/bin/python
import re, argparse
import mechanize
from mechanize import Browser
br = mechanize.Browser(factory=mechanize.RobustFactory())

parser = argparse.ArgumentParser()
parser.add_argument("userEmail", type=str, help="Target Email")
args = parser.parse_args()

email = args.userEmail

br.set_handle_robots( False )
br.addheaders = [('User-agent', 'Firefox')]

siteList = ["http://www.nngroup.com/articles/subscribe/"]

for site in siteList:
  br.open( site )
  for form in br.forms():
    br.select_form(form)
    if control.type == "text":
        control.value = email
  br.submit()
