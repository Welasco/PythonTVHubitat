import json

class AlexaResponse:
    RawJSON = '''
    {
        "version": "1.0",
        "sessionAttributes": {
            "supportedHoroscopePeriods": {
                "daily": true,
                "weekly": false,
                "monthly": false
                }
            },
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Uhuuuu so far so good!"
            },
            "card": {
                "type": "Simple",
                "title": "Television",
                "content": "Today will provide you a new learning opportunity.  Stick with it and the possibilities will be endless."
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Can I help you with anything else?"
                }
            },
            "shouldEndSession": false
        }
    }
    '''
    AlexaResponse = json.loads(RawJSON)
    #def __init__(self):
    #    data = json.loads(AlexaResponse)
    

    def setMessage(self, message):
        self.AlexaResponse['response']['outputSpeech']['text'] = message
        self.AlexaResponse['response']['card']['content'] = message


class AlexaRequest:
    def handler(self, req):
        intentjson = req.get_json()
        intent = intentjson['request']['intent']['name']

        response = AlexaResponse()

        if intent == "mute":
            response.setMessage("OK, Muting Television.")
            return response.AlexaResponse
        elif intent == "channelup":
            response.setMessage("OK, Channel UP.")
            return response.AlexaResponse
        elif intent == "channeldown":
            response.setMessage("OK, Channel Down.")
            return response.AlexaResponse
        elif intent == "channelincreaseby":
            number = intentjson['request']['intent']['slots']['number']['value']
            response.setMessage("OK, Moving channel up by " + number)
            return response.AlexaResponse
        elif intent == "channeldecreaseby":
            number = intentjson['request']['intent']['slots']['number']['value']
            response.setMessage("OK, Moving channel down by " + number)
            return response.AlexaResponse
        elif intent == "channelto":
            number = intentjson['request']['intent']['slots']['number']['value']
            response.setMessage("OK, Changing channel to " + number)
            return response.AlexaResponse            
        elif intent == "volumeupby":
            number = intentjson['request']['intent']['slots']['number']['value']
            response.setMessage("OK, Increasing volume by " + number)
            return response.AlexaResponse
        elif intent == "volumedownby":
            number = intentjson['request']['intent']['slots']['number']['value']
            response.setMessage("OK, Decreasing volume by " + number)
            return response.AlexaResponse
        elif intent == "volumedown":
            response.setMessage("OK, Volume Down")
            return response.AlexaResponse
        elif intent == "volumeup":
            response.setMessage("OK, Volume UP")
            return response.AlexaResponse
        elif intent == "power":
            response.setMessage("OK")
            return response.AlexaResponse
        elif intent == "AMAZON.FallbackIntent":
            response.setMessage("Sorry, Television didn't recognized your command!")
            return response.AlexaResponse  
        elif intent == "AMAZON.CancelIntent":
            response.setMessage("OK, Cancelling")
            return response.AlexaResponse
        elif intent == "AMAZON.HelpIntent":
            response.setMessage("Hello wellcome to Alexa Television Skill. You can say somethings like: Television mute, or Television Volume UP, or Television volume up to 20, or Television change channel to 32.")
            return response.AlexaResponse
        elif intent == "AMAZON.StopIntent":
            response.setMessage("OK, Stopping")
            return response.AlexaResponse
        elif intent == "AMAZON.NavigateHomeIntent":
            response.setMessage("OK, Navigate Home Intent reached.")
            return response.AlexaResponse                                                                                                                                               
        else:
            response.setMessage("Sorry, your command didn't match to any valid command.")
            return response.AlexaResponse                                     

