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
        if html.body and ('text/html' in flow.response.headers["content-type"]):     # inject only for HTML resources
            script = html.new_tag("script", type="application/javascript")
            script.insert(0, "alert('Hello world')")
            html.body.insert(0, script)
            flow.response.content = str(html)
            context.log("script injected")
