from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints

def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return [b'Hello, world!']

resource = WSGIResource(reactor, reactor.getThreadPool(), application)
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()