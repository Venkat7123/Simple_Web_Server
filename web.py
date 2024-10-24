from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!DOCTYPE html>
<html>
<head>
    <title>My Web Server</title>
    <style>
        table{
            color: white;
            font-weight: 500;
            border-radius: 9px;
            border-color: red;
        }
        tr,th,td{
            border-radius: 5px;

        }
        td{
            font-size: 15px;
        }
        .name{
            color: black;
        }
        </style>
</head>
<body>
    <table border="1" bgcolor="black" align="center"cellpadding="20" >
    <caption class="name">LAPTOP CONFIGURATION</caption>
        <tr>
            <th>SYSTEM CONFIGURATION</th>
            <th>DESCRIPTION</th>
        </tr>
        <tr>
            <td>Operating System</td>
            <td>Windows 11</td>
        </tr>
        <tr>
            <td>Manufacturer</td>
            <td>Lenovo</td>
        </tr>
        <tr>
            <td>Processor</td>
            <td>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</td>
        </tr>
        <tr>
        <td>RAM</td>
        <td>16.0GB</td>
        </tr>
        <tr>
            <td>Secondary Memory</td>
            <td>512GB</td>
        </tr>
    </table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()