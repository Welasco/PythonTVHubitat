import logging
from AlexaPy.AlexaClass import AlexaRequest
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    Alexa = AlexaRequest()
    msg = Alexa.handler(req)

    return func.HttpResponse(
            msg
    )
