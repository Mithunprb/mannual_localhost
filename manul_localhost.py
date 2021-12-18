import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer
import argparse



def test(HandlerClass=SimpleHTTPRequestHandler,
         ServerClass=HTTPServer,):

    protocol = "HTTP/1.0"
    host = ''
    port = args['port']
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if ':' in arg:
            host, port = arg.split(':')
            port = int(port)
        else:
            try:
                port = int(sys.argv[1])
            except:
                host = sys.argv[1]

    server_address = (host, port)

    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", 
        type=int, default=8000, help="Port in which you want HTTP protocol")

    args = vars(parser.parse_args())
    test()