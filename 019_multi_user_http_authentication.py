from zope.interface import implementer
import os
from twisted.cred.portal import IRealm, Portal
from twisted.cred.checkers import FilePasswordDB
from twisted.web.static import File
from twisted.web.resource import IResource
from twisted.web.guard import HTTPAuthSessionWrapper, DigestCredentialFactory
from twisted.web.server import Site
from twisted.internet import reactor, endpoints

dir_path = os.path.dirname(os.path.realpath(__file__))
passwd_file = os.path.join(dir_path, "httpd.password")

@implementer(IRealm)
class PublicHTMLRealm(object):
    def requestAvatar(self, avatarId, mind, *interfaces):
        print("avatarID: " + avatarId)
        if IResource in interfaces:
            return (IResource, File("%s" % (avatarId,)), lambda: None)
        raise NotImplementedError()

portal = Portal(PublicHTMLRealm(), [FilePasswordDB(passwd_file)])
credentialFactory = DigestCredentialFactory("md5", "example.org")
resource = HTTPAuthSessionWrapper(portal, [credentialFactory])


factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()