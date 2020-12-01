/**
 *  Copyright 2015 SmartThings
 *
 *  Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 *  in compliance with the License. You may obtain a copy of the License at:
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software distributed under the License is distributed
 *  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License
 *  for the specific language governing permissions and limitations under the License.
 *
 *  Garage Door Push Button
 *
 *  Author: Andre Hass
 *
 *  Date: 2017-04-30
 */

preferences {
    input("hostaddress", "text", title: "IP Address for Server:", description: "Ex: 10.0.0.12 or 192.168.0.4 (no http://)")
    input("hostport", "number", title: "Port of Server", description: "port")
}

metadata {
	definition (name: "TV2", namespace: "TV", author: "Victor Santana") {
      	capability "TV"
		capability "Music Player"
        capability "Refresh"
        capability "Switch"

        command "back"
        command "up"
        command "down"
        command "left"
        command "right"
        command "myApps"
        command "ok"
        command "exit"
	}

	// simulator metadata
	simulator {
	}

	// UI tile definitions
	tiles {
		//standardTile("switch", "device.switch", width: 2, height: 2, canChangeIcon: true) {
		//	state "off", label: 'off', action: "on", icon: "st.samsung.da.RC_ic_power", backgroundColor: "#ffffff", nextState: "Turning on"
		//	state "on", label: 'on', action: "off", icon: "st.samsung.da.RC_ic_power", backgroundColor: "#00A0DC"
		//}
    	standardTile("power", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:"Power Off", icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/power.png", action:"Switch.off"
        }
        standardTile("mute", "device.mute", inactiveLabel:false, decoration:"flat") {
            state "default", label:"Mute", icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/mute.png", action:"Music Player.mute"
        }
        standardTile("volumeUp", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'Volume Up', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/volumeup.png", action:"TV.volumeUp"
        }
        standardTile("volumeDown", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'Volume Down', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/volumedown.png", action:"TV.volumeDown"
        }
        standardTile("channelUp", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'Channel Up', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/channelup.png", action:"TV.channelUp"
        }
        standardTile("channelDown", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'Channel Down', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/channeldown.png", action:"TV.channelDown"
        }
         standardTile("back", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'Back', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/back.png", action:"back"
        }
        standardTile("externalInput", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'Source', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/hdmi.png", action:"externalInput"
        }
        standardTile("up", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'Up', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/up.png", action:"up"
        }
        standardTile("left", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'Left', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/left.png", action:"left"
        }
        standardTile("down", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'down', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/down.png", action:"down"
        }
        standardTile("right", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'right', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/right.png", action:"right"
        }
        standardTile("myApps", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'My Apps', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/apps.png", action:"myApps"
        }
        standardTile("ok", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'Ok', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/ok.png;", action:"ok"
        } 
        standardTile("exit", "device.status", inactiveLabel:false, decoration:"flat") {
            state "default", label:'Exit', icon:"https://raw.githubusercontent.com/samlalor/LGSmartTV2012/Icons/home.png", action:"exit"
        }
        
        main (["power"])
		details(["power","externalInput", "exit", "mute","back","myApps", "volumeUp", "up", "channelUp", "left", "ok", "right", "volumeDown", "down", "channelDown"])		
	}
}

def parse(String description) {
}

def physicalgraph.device.HubAction push() {
	sendEvent(name: "switch", value: "on", isStateChange: true, displayed: false)
    sendEvent(name: "switch", value: "off", isStateChange: true, displayed: false)
    return sendRaspberryCommand('power')
	
	//sendEvent(name: "momentary", value: "pushed", isStateChange: true)
}


def on() {
	push()
}

def off() {
	push()

}

def channelUp() 
{
	log.debug "Executing 'channelUp'"
	return sendRaspberryCommand('channelup')
}

def channelDown() 
{
	log.debug "Executing 'channelDown'"
	return sendRaspberryCommand('channeldown')
}


// handle commands
def volumeUp() 
{
	log.debug "Executing 'volumeUp'"
	return sendRaspberryCommand('volumeup')
}

def volumeDown() 
{
	log.debug "Executing 'volumeDown'"
	return sendRaspberryCommand('volumedown')
}


def mute() 
{
	log.debug "Executing 'mute'"   
    return sendRaspberryCommand('mute')
}

def externalInput()
{
	return sendRaspberryCommand('source')
}

def back()
{
	return sendRaspberryCommand('return')
}

def up()
{
	return sendRaspberryCommand('up')
}

def down()
{
	return sendRaspberryCommand('down')
}

def left()
{
	return sendRaspberryCommand('left')
}

def right()
{
	return sendRaspberryCommand('right')
}

def myApps()
{
	return sendRaspberryCommand('apps')
}

def ok()
{
	return sendRaspberryCommand('ok')
}

def exit()
{
	return sendRaspberryCommand('exit')
}


// Processing multicommand

def channelincreaseby(String value)
{
    return sendRaspberryCommand("channelincreaseby-$value")
}

def channeldecreaseby(String value)
{
    return sendRaspberryCommand("channeldecreaseby-$value")
}

def channelto(String value)
{
    return sendRaspberryCommand("channelto-$value")
}

def volumeupby(String value)
{
    return sendRaspberryCommand("volumeupby-$value")
}

def volumedownby(String value)
{
    return sendRaspberryCommand("volumedownby-$value")
}


def physicalgraph.device.HubAction sendRaspberryCommand(String command) {

    log.debug "TV - command: $command"
    if(settings.hostaddress && settings.hostport){
		
        def host = settings.hostaddress
		def port = settings.hostport

		def path = "/api/tv/command/$command"

		def headers = [:] 
		headers.put("HOST", "$host:$port")
		headers.put("Content-Type", "application/json")

		log.debug "TV - The Header is $headers"

		def method = "GET"

		try {
			def hubAction = new physicalgraph.device.HubAction(
				method: method,
				path: path,
				//body: json,
				headers: headers,
			)

			log.debug hubAction
			hubAction
            return hubAction
		}
		catch (Exception e) {
			log.debug "TV - Hit Exception $e on $hubAction"
		}
	}
	else{
		
		log.debug "TV - RespberryPI IP address and port not set!"
	}
}