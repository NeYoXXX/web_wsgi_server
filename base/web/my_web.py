import time

def application(environ, start_response):
    status = '200 OK'
    response = [('Content-Type','text/html')]
    start_response(status, response)
    return str(environ) + '==Hello world from a simple WSGI application!--->%s\n' % time.ctime()