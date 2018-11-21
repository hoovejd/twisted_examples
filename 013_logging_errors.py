from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET
from twisted.internet import reactor, endpoints
from twisted.python.log import err

class DelayedResource(Resource):
    def _delayedRender(self, request):
        request.write(b"<html><body>Sorry to keep you waiting.</body></html>")
        request.finish()

    def _responseFailed(self, failure, call):
        call.cancel()
        err(failure, b"Async response demo interrupted response")

    def render_GET(self, request):
        call = reactor.callLater(5, self._delayedRender, request)
        request.notifyFinish().addErrback(self._responseFailed, call)
        return NOT_DONE_YET

root = Resource()
root.putChild(b"test", DelayedResource())
factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()