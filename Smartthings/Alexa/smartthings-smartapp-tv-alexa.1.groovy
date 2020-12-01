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

preferences {
    page(name:"controllerSetup")
}
def controllerSetup() {
	dynamicPage(name: "controllerSetup",title: "Controller Setup", install:true) {
        section("Select TV:") {
            input "tv", title: "TV","capability.tv"
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


mappings {
    path("/alexatv/:command") {
        action: [GET: "alexatvcommand"]
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