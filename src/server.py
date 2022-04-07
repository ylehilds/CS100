from CGIHTTPServer import CGIHTTPRequestHandler
from BaseHTTPServer import HTTPServer
# minimal web server.  serves files relative to the
# current directory.
PORT = 8000
httpd = HTTPServer(("", PORT), CGIHTTPRequestHandler)
#print "serving at port", PORT
httpd.serve_forever()