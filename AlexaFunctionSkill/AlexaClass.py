import json
import requests

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
            "shouldEndSession": true
        }
    }
    '''
    AlexaResponse = json.loads(RawJSON)
    #def __init__(self):
    #    data = json.loads(AlexaResponse)

    def setMessage(self, message):
        self.AlexaResponse['response']['outputSpeech']['text'] = message
        self.AlexaResponse['response']['card']['content'] = message
    
    def getMessage(self):
        return json.dumps(self.AlexaResponse)


class AlexaRequest:
    Debug = False

    def Log(self, req):
        print("#########################################################################################")
        print("Request Headers:")
        print("#########################################################################################")
        print(req.headers)
        print(" ")
        print("#########################################################################################")
        print("Request Body:")
        print("#########################################################################################")
        print(req.get_json())


    def handler(self, req):
        response = AlexaResponse()
        if self.Debug:
            self.Log(req)

        try:
            intentjson = req.get_json()
            intent = intentjson['request']['intent']['name']
            if intent == "mute":
                response.setMessage("OK, Muting Television.")
                self.STRequest("mute")
                return response.getMessage()
            elif intent == "channelup":
                response.setMessage("OK, Channel UP.")
                self.STRequest("channelup")
                return response.getMessage()
            elif intent == "channeldown":
                response.setMessage("OK, Channel Down.")
                self.STRequest("channeldown")
                return response.getMessage()
            elif intent == "channelincreaseby":
                number = intentjson['request']['intent']['slots']['number']['value']
                response.setMessage("OK, Moving channel up by " + number)
                cmd = "channelincreaseby-" + number
                self.STRequest(cmd)
                return response.getMessage()
            elif intent == "channeldecreaseby":
                number = intentjson['request']['intent']['slots']['number']['value']
                response.setMessage("OK, Moving channel down by " + number)
                cmd = "channeldecreaseby-" + number
                self.STRequest(cmd)
                return response.getMessage()
            elif intent == "channelto":
                number = intentjson['request']['intent']['slots']['number']['value']
                response.setMessage("OK, Changing channel to " + number)
                cmd = "channelto-" + number
                self.STRequest(cmd)
                return response.getMessage()            
            elif intent == "volumeupby":
                number = intentjson['request']['intent']['slots']['number']['value']
                response.setMessage("OK, Increasing volume by " + number)
                cmd = "volumeupby-" + number
                self.STRequest(cmd)
                return response.getMessage()
            elif intent == "volumedownby":
                number = intentjson['request']['intent']['slots']['number']['value']
                response.setMessage("OK, Decreasing volume by " + number)
                cmd = "volumedownby-" + number
                self.STRequest(cmd)
                return response.getMessage()
            elif intent == "volumedown":
                response.setMessage("OK, Volume Down")
                self.STRequest("volumedown")
                return response.getMessage()
            elif intent == "volumeup":
                response.setMessage("OK, Volume UP")
                self.STRequest("volumeup")
                return response.getMessage()
            elif intent == "power":
                response.setMessage("OK")
                self.STRequest("power")
                return response.getMessage()
            elif intent == "AMAZON.FallbackIntent":
                response.setMessage("Sorry, Television didn't recognized your command!")
                return response.getMessage()  
            elif intent == "AMAZON.CancelIntent":
                response.setMessage("OK, Cancelling")
                return response.getMessage()
            elif intent == "AMAZON.HelpIntent":
                response.setMessage("Hello wellcome to Alexa Television Skill. You can say somethings like: Television mute, or Television Volume UP, or Television volume up to 20, or Television change channel to 32.")
                return response.getMessage()
            elif intent == "AMAZON.StopIntent":
                response.setMessage("OK, Stopping")
                return response.getMessage()
            elif intent == "AMAZON.NavigateHomeIntent":
                response.setMessage("OK, Navigate Home Intent reached.")
                return response.getMessage()                                                                                                                                               
            else:
                response.setMessage("Sorry, your command didn't match to any valid command.")
                return response.getMessage()
        except:
            response.setMessage("Sorry, your command didn't match to any valid command.")
            return response.getMessage()
        
    def STRequest(self,cmd):
        # requests.get("https://graph-na02-useast1.api.smartthings.com/api/smartapps/installations/4ba0f9ec-c728-461d-b420-63608a397a07/alexatv/volumeupby-3?access_token=f438c5ca-76e2-4f2b-b5ef-3ad3960a5900")
        STEndPoint = "https://graph-na02-useast1.api.smartthings.com/api/smartapps/installations/"
        STAppID = "4ba0f9ec-c728-461d-b420-63608a397a07"
        STAppMap = "alexatv"
        STCommand = cmd
        STAccessToken = "?access_token=f438c5ca-76e2-4f2b-b5ef-3ad3960a5900"
        STRequest = STEndPoint + STAppID + "/" + STAppMap + "/" + STCommand + STAccessToken
        requests.get(STRequest)   
