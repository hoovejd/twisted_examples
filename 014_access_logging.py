from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor, endpoints
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
resource = File(os.path.join(dir_path, "temp1"))
factory = Site(resource, logPath=os.path.join(dir_path, "logs", "access-logging-demo.log"))
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()