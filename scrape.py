import urllib2

page = urllib2.urlopen("http://www.theverge.com")
html = page.read()

beg = html.index('<div class="c-masthead__tagline">')
end = html.index("</div>", beg + 1)

parsed = html[beg:end]

tagBeg = parsed.index('">', parsed.index("<a href="))
tagEnd = parsed.index("</a>")

tagline = parsed[tagBeg + 2:tagEnd]
