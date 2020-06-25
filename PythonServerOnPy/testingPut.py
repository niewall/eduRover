import os
from http.server import HTTPServer, BaseHTTPRequestHandler

ip = "192.168.178.58"

class Serv(BaseHTTPRequestHandler):

    def do_PUT(self):  # For whole Programms    //in cmd: curl -T input.txt http://192.168.2.186:8080/
        filename = os.path.basename(self.path)
        print(self.path)
        file_length = int(self.headers['Content-Length'])
        with open(filename, 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))
        self.send_response(201, 'Created')
        self.end_headers()
        reply_body = 'Raspberry saved "%s"\n' % filename
        self.wfile.write(reply_body.encode('utf-8'))

httpd = HTTPServer((ip, 8080), Serv)
httpd.serve_forever()