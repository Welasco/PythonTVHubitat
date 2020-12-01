import json
from test import AlexaResponse as Alexa
from collections import namedtuple


AlexaMsg = Alexa()

print(AlexaMsg.AlexaResponse['response']['outputSpeech']['text'])
AlexaMsg.setMessage("Test")

print(AlexaMsg.AlexaResponse['response']['outputSpeech']['text'])









#data = json.loads(Alexa.Response, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
#data2 = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
"""
data2 = '''
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

data = json.loads(data2, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
print(data.version)
print(data.response.reprompt.outputSpeech.text)

data3 = Alexa.data
print(data3['response']['reprompt']['outputSpeech']['type'])

data3['response']['reprompt']['outputSpeech']['type'] = "new value"

print(data3['response']['reprompt']['outputSpeech']['type'])
#print(data.hometown)
#print(data.hometown.name)
"""