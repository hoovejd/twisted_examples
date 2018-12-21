from twisted.web.template import Element, renderer, XMLFile, flattenString, flatten
from twisted.python.filepath import FilePath
from twisted.internet import reactor, endpoints, defer
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET

class ExampleElement(Element):

    loader = XMLFile(FilePath('simple_html_template.xml'))

    @renderer
    def header(self, request, tag):
        return tag('Header.')

    @renderer
    def footer(self, request, tag):
        return tag('Footer.')

class Root(Resource):
    isLeaf = True

    #def render_GET(self, request):



def done(output):
    return output.encode()

d = flattenString(None, ExampleElement())
d.addCallback(done)

resource = Root()
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()