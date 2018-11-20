from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints
from twisted.web.static import File
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

root = Resource()
root.putChild(b"temp1", File(os.path.join(dir_path, "temp1")))
root.putChild(b"temp2", File(os.path.join(dir_path, "temp2")))
root.putChild(b"temp3", File(os.path.join(dir_path, "temp3")))

factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()