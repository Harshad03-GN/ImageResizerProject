import logging
import azure.functions as func
from azure.functions import HttpRequest, HttpResponse
from azure.functions.decorators import FunctionApp, http_trigger

app = FunctionApp()

@app.function_name(name="HttpTrigger")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger_func(req: HttpRequest) -> HttpResponse:
    logging.info("HTTP trigger function processed a request.")

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}!", status_code=200)
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body.",
            status_code=400
        )
