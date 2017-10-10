from bs4 import BeautifulSoup   # nice representation of the DOM
# from libmproxy.protocol.http import decoded
# from mitmproxy import ctx


class Proxy:
    def __init__(self, script):
        self.script = script

    def response(self, context, flow):
        html = BeautifulSoup(flow.response.context)
        context.log(html)


def start(context, argv):
    # ctx.log.info("Script loaded")
    if len(argv) < 2:
        raise ValueError("Script name must be provided as the first parameter")
    return Proxy(argv[1])
