/**
 *  AlexaTV
 *
 *  Author: Victor Santana
 *
 *  Date: 2019-01-06
 */

definition(
    name: "AlexaTV App",
    namespace: "AlexaTV",
    author: "Victor Santana",
    description: "SmartApp AlexaTV",
    iconUrl: "https://graph.api.smartthings.com/api/devices/icons/st.Home.home3-icn",
    iconX2Url: "https://graph.api.smartthings.com/api/devices/icons/st.Home.home3-icn?displaySize=2x",
    iconX3Url: "https://graph.api.smartthings.com/api/devices/icons/st.Home.home3-icn?displaySize=3x",
    singleInstance: true,
    oauth: true
)

import groovy.json.JsonBuilder
import groovy.json.JsonSlurper
import groovy.json.JsonOutput 

preferences {
    page(name:"controllerSetup")
    page(name: "accesstoken")
}
def controllerSetup() {
	dynamicPage(name: "controllerSetup",title: "Controller Setup", install:true) {
        section("Select TV:") {
            input "tv", title: "TV","capability.tv"
        }
        section("Get Access Token") {
			href (name: "accesstoken", 
			title: "Get Access Token", 
			description: "Tap to get Access Token",
			required: false,
			page: "accesstoken"
			)
		}        
    }
}

def installed() {
	log.debug "Installed with settings: ${settings}"
	initialize()
}

def updated() {
	log.debug "Updated with settings: ${settings}"
	//unsubscribe()
	initialize()
}


def initialize() {

}

def uninstalled() {
    removeChildDevices(getChildDevices())
}

private removeChildDevices(delete) {
    delete.each {
    	log.debug "deleting child device: ${it.deviceNetworkId}"
        deleteChildDevice(it.deviceNetworkId)
    }
}

def accesstoken() {
	dynamicPage(name: "accesstoken", title: none, install: true, uninstall: true) {
     	section("Get Access Token") {
        	paragraph textaccesstoken()
 		}
	}
}

private def textaccesstoken() {
    //createAccessToken()
	// atomicState.accessToken = createAccessToken()
	log.debug "accessToken: ${atomicState.accessToken}, ${state.accessToken}"
    if(!state.accessToken){
        createAccessToken()
    }
/*	
	if(!atomicState.accessToken) { //this is an access token for Ecobee to make a callback into Ecobee Suite Manager (this code)
		try {
			atomicState.accessToken = createAccessToken()
        } catch(Exception e) {
        
        }
    }
*/
	def text =
		"State accessToken: ${state.accessToken} \n\n" +
        "Public API URL: ${getFullApiServerUrl()}/alexatv/volumedownby-3?access_token=${state.accessToken} \n\n" +
        "Local API URL: ${getFullLocalApiServerUrl()}/alexatv/volumedownby-3?access_token=${state.accessToken} \n\n" +
        "Alexa Endpoint: ${getFullApiServerUrl()}/alexaskill?access_token=${state.accessToken} \n\n" +
        //"Test: ${fullLocalApiServerUrl()} e ${state.accessToken} e ${getFullApiServerUrl()}access_token=${atomicState.accessToken} \n\n" +
        ""
        // Test: http://192.168.2.201/apps/api/207/null e ba24bf78-c8e6-4918-b078-34156b03beb7 e https://cloud.hubitat.com/api/6130d76d-9312-4187-b4b2-46f821098b67/apps/207access_token=ba24bf78-c8e6-4918-b078-34156b03beb7 
}


mappings {
    path("/alexatv/:command") {
        action: [GET: "alexatvcommand"]
    }
    path("/alexaskill") {
        action: [
            POST: "alexaskill"
        ]
    }    
}

def alexatvcommand() {

    def cmd = params.command
    log.debug "AlexaTV SmartApp - Received Command: $cmd"
    
    // TV Action
    def checkcmd = cmd.indexOf("-")
    if(checkcmd < 0){
        if(cmd=="mute"){
            tv.mute()
        }
        else if (cmd=="channelup"){
            tv.channelUp()
        }
        else if (cmd=="channeldown"){
            tv.channelDown()
        }
        else if (cmd=="power"){
            tv.on()
        }
        else if (cmd=="volumeup"){
            tv.volumeUp()
        } 
        else if (cmd=="volumedown"){
            tv.volumeDown()
        }
        else{
            httpError(400, "$command is not a valid command for all switches specified")
        }        
    }    
    else{
        def multicommand = cmd.split("-")
        if (multicommand[0]=="channelincreaseby"){
            tv.channelincreaseby(multicommand[1])
        }
        else if (multicommand[0]=="channeldecreaseby"){
            tv.channeldecreaseby(multicommand[1])
        }
        else if (multicommand[0]=="channelto"){
            tv.channelto(multicommand[1])
        }
        else if (multicommand[0]=="volumeupby"){
            tv.volumeupby(multicommand[1])
        }
        else if (multicommand[0]=="volumedownby"){
            tv.volumedownby(multicommand[1])
        }
        else{
            httpError(400, "$command is not a valid command for all switches specified")
        }
    }
}

def alexaskill() {

    // Production Code
    
    def alexarequestjson = request.JSON
    def alexaResponseBody = alexarequesthandler(alexarequestjson)
    log.debug("Alexa Response Body: $alexaResponseBody")
    def alexaresponsespeech = alexaResponseBody.response.outputSpeech.text
    log.debug("Alexa Response JSON outputSpeech Text: $alexaresponsespeech")
    
 
    //def rawjson = JsonOutput.toJson(responsetest)
    //log.debug("Alexa Response RAW JSON: $responsetest")
    //return [data: alexaResponseBody, status: 200]
    //render contentType: 'text/html', data: "status received...ok", status: 200
    //render contentType: 'application/json', data: alexaResponseBody, status: 200
    
    def resultJson = new groovy.json.JsonOutput().toJson(alexaResponseBody)
    render contentType: 'application/json', data: resultJson, status: 200
    //return alexaResponseBody
}

def alexarequesthandler(reqjson){
    def intent = reqjson.request.intent.name
    def alexaResponseMsg = alexaresponse()
    // Test and Loggin
    def alexaresponsetest = alexaResponseMsg.response.outputSpeech.text
    log.debug("Alexa Response JSON outputSpeech Text: $alexaresponsetest")
    log.debug("Alexa Intent Text: $intent")
    def number = null
    def button = null
    switch(intent){
        case "skip":
            alexaResponseMsg.response.outputSpeech.text = "OK, Skiping."
            alexaResponseMsg.response.card.content = "OK, Skiping."
            tv.ok()
            return alexaResponseMsg
            // return        
        case "mute":
            alexaResponseMsg.response.outputSpeech.text = "OK, Muting Television."
            alexaResponseMsg.response.card.content = "OK, Muting Television."
            tv.mute()
            return alexaResponseMsg
            // return
        case "channelup":
            alexaResponseMsg.response.outputSpeech.text = "OK, Channel UP."
            alexaResponseMsg.response.card.content = "OK, Channel UP."
            tv.channelUp()
            return alexaResponseMsg
            // return
        case "channeldown":
            alexaResponseMsg.response.outputSpeech.text = "OK, Channel down."
            alexaResponseMsg.response.card.content = "OK, Channel down."
            tv.channelDown()
            return alexaResponseMsg
            // return
        case "channelincreaseby":
            number = reqjson.request.intent.slots.number.value
            alexaResponseMsg.response.outputSpeech.text = "OK, Moving channel up by $number"
            alexaResponseMsg.response.card.content = "OK, Moving channel up by $number"
            tv.channelincreaseby(number)
            return alexaResponseMsg
            // return
        case "channeldecreaseby":
            number = reqjson.request.intent.slots.number.value
            alexaResponseMsg.response.outputSpeech.text = "OK, Moving channel down by $number"
            alexaResponseMsg.response.card.content = "OK, Moving channel down by $number"
            tv.channeldecreaseby(number)
            return alexaResponseMsg
            // return
        case "channelto":
            number = reqjson.request.intent.slots.number.value
            alexaResponseMsg.response.outputSpeech.text = "OK, Changing channel to $number"
            alexaResponseMsg.response.card.content = "OK, Changing channel to $number"
            tv.channelto(number)
            return alexaResponseMsg
            // return
        case "volumeupby":
            number = reqjson.request.intent.slots.number.value
            alexaResponseMsg.response.outputSpeech.text = "OK, Increasing volume by $number"
            alexaResponseMsg.response.card.content = "OK, Increasing volume by $number"
            tv.volumeupby(number)
            return alexaResponseMsg
            // return
        case "volumedownby":
            number = reqjson.request.intent.slots.number.value
            alexaResponseMsg.response.outputSpeech.text = "OK, Decreasing volume by $number"
            alexaResponseMsg.response.card.content = "OK, Decreasing volume by $number"
            tv.volumedownby(number)
            return alexaResponseMsg
            // return
        case "volumedown":
            alexaResponseMsg.response.outputSpeech.text = "OK, Volume Down."
            alexaResponseMsg.response.card.content = "OK, Volume Down."
            tv.volumeDown()
            return alexaResponseMsg
            // return
        case "volumeup":
            alexaResponseMsg.response.outputSpeech.text = "OK, Volume UP."
            alexaResponseMsg.response.card.content = "OK, Volume UP."
            tv.volumeUp()
            return alexaResponseMsg
            // return
        case "power":
            alexaResponseMsg.response.outputSpeech.text = "OK"
            alexaResponseMsg.response.card.content = "OK"
            tv.on()
            return alexaResponseMsg
            // return
        case "pressbutton":
            button = reqjson.request.intent.slots.button.value
            alexaResponseMsg.response.outputSpeech.text = "OK, Pressing button $button"
            alexaResponseMsg.response.card.content = "OK, Pressing button $button"
            tv.pressbutton(button)
            return alexaResponseMsg     
            // return
        case "play":
            alexaResponseMsg.response.outputSpeech.text = "OK, Playing!"
            alexaResponseMsg.response.card.content = "OK, Playing!"
            tv.pressbutton("play")
            return alexaResponseMsg  
            // return
        case "pause":
            alexaResponseMsg.response.outputSpeech.text = "OK, Pausing!"
            alexaResponseMsg.response.card.content = "OK, Pausing!"
            tv.pressbutton("pause")
            return alexaResponseMsg  
            // return
        case "stop":
            alexaResponseMsg.response.outputSpeech.text = "OK, Stopping!"
            alexaResponseMsg.response.card.content = "OK, Stopping!"
            tv.pressbutton("stop")
            return alexaResponseMsg  
            // return
        case "exit":
            alexaResponseMsg.response.outputSpeech.text = "OK, Exiting!"
            alexaResponseMsg.response.card.content = "OK, Exiting!"
            tv.pressbutton("exit")
            return alexaResponseMsg  
            // return                                                      
        case "AMAZON.FallbackIntent":
            alexaResponseMsg.response.outputSpeech.text = "Sorry, Television didn't recognized your command!"
            alexaResponseMsg.response.card.content = "Sorry, Television didn't recognized your command!"
            return alexaResponseMsg
            // return
        case "AMAZON.CancelIntent":
            alexaResponseMsg.response.outputSpeech.text = "OK, Cancelling"
            alexaResponseMsg.response.card.content = "OK, Cancelling"
            return alexaResponseMsg
            // return
        case "AMAZON.HelpIntent":
            alexaResponseMsg.response.outputSpeech.text = "Hello wellcome to Alexa Television Skill. You can say somethings like: Television mute, or Television Volume UP, or Television volume up to 20, or Television change channel to 32."
            alexaResponseMsg.response.card.content = "Hello wellcome to Alexa Television Skill. You can say somethings like: Television mute, or Television Volume UP, or Television volume up to 20, or Television change channel to 32."
            return alexaResponseMsg
            // return
        case "AMAZON.StopIntent":
            alexaResponseMsg.response.outputSpeech.text = "OK, Stopping"
            alexaResponseMsg.response.card.content = "OK, Stopping"
            return alexaResponseMsg
            // return
        case "AMAZON.NavigateHomeIntent":
            alexaResponseMsg.response.outputSpeech.text = "OK, Navigate Home Intent reached."
            alexaResponseMsg.response.card.content = "OK, Navigate Home Intent reached."
            return alexaResponseMsg
            // return
        default:
            alexaResponseMsg.response.outputSpeech.text = "Sorry, your command didn't match to any valid command."
            alexaResponseMsg.response.card.content = "Sorry, your command didn't match to any valid command."
            return alexaResponseMsg
            // return
    }
}

def alexaresponse(){
    def rawjson = '''
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
    def jsonSlurper = new JsonSlurper()
    def alexajson = null;
    alexajson = jsonSlurper.parseText(rawjson)
    return alexajson
}