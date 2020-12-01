import json
from AlexaClass import AlexaRequest
from flask import Flask, render_template, request, jsonify, Response, make_response
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"
    #return render_template('home.html')


@app.route("/api/tv/")
def tv():
    return "TV!"


@app.route('/alexa/testskill', methods=['POST'])
def television():
    Alexa = AlexaRequest()
    Alexa.Debug = True
    msg = Alexa.handler(request)
    r = '''
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
    #return Response("{'a':'b'}", status=201, mimetype='application/json')
    #return Response(msg, status=201, mimetype='application/json;charset=utf-8')
    #resmsg.headers['Access-Control-Allow-Origin'] = '*'


    resmsg = make_response(msg, 200)
    resmsg.set_cookie('JSESSIONID','1BEBF89CA2FEB87DC4229868F00BD638-n2',httponly=True, secure=True)
    resmsg.mimetype = 'application/json;charset=utf-8'
    resmsg.headers['X-Frame-Options'] = 'SAMEORIGIN'
    resmsg.headers['X-RateLimit-Current'] = 0
    resmsg.headers['X-RateLimit-Limit'] = 250
    resmsg.headers['X-RateLimit-TTL'] = 60
    return resmsg

    #return msg

if __name__ == "__main__":
    app.run(host='0.0.0.0')
