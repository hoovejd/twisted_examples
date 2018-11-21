from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET
from twisted.internet import reactor, endpoints

class DelayedResource(Resource):
    def _delayedRender(self, request):
        request.write(b"<html><body>Sorry to keep you waiting.</body></html>")
        request.finish()

    def render_GET(self, request):
        reactor.callLater(6, self._delayedRender, request)
        return NOT_DONE_YET

root = Resource()
root.putChild(b"test", DelayedResource())
factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()