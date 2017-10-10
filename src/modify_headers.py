def response(context, flow):
    context.log("response sent")
    flow.response.headers["foo"] = "bar"
