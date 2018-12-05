from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints

class ShowSession(Resource):
    def render_GET(self, request):
        return b'Your session id is: ' + request.getSession().uid

class ExpireSession(Resource):
    def render_GET(self, request):
        request.getSession().expire()
        return b'Your session has been expired.'

root = Resource()
root.putChild(b"show", ShowSession())
root.putChild(b"expire", ExpireSession())

factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()