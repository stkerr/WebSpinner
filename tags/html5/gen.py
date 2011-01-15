"""
Gen.py
This is just a helper file that will generate the python
tag files quickly, so they don't have to be done by hand
each time.
"""

def printfile(name, filename):
	output =  """
__author__=\"stkerr\"
__date__ =\"$Jan 14, 2011 10:40:00 AM$\"

import webspinner.tags.html5

class Tag_"""
	output += filename.title() 
	output += """(webspinner.Node):
	tag_string = \""""
	output += name 
	output += "\"\n"

	f = open("tag_" + filename + ".py", "w+")
	f.write(output)
	f.close()


printfile("article", "article")
printfile("aside", "aside")
printfile("audio", "audio")
printfile("canvas", "canvas")
printfile("command", "command")
printfile("datalist", "datalist")
printfile("details", "details")
printfile("embed", "embed")
printfile("eventsource", "eventsource")
printfile("figcaption", "figcaption")
printfile("figure", "figure")
printfile("footer", "footer")
printfile("header", "header")
printfile("hgroup", "hgroup")
printfile("keygen", "keygen")
printfile("mark", "mark")
printfile("menu", "menu")
printfile("meter", "meter")
printfile("nav", "nav")
printfile("output", "output")
printfile("progress", "progress")
printfile("section", "section")
printfile("source", "source")
printfile("summary", "summary")
printfile("time", "time")
printfile("video", "video")
