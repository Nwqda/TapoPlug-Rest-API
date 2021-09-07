#tapoPlugApi.py    
#@package   tapo_plug
#@author    Samy (Naqwada) <naqwada@pm.me>
#@license   MIT License (http://www.opensource.org/licenses/mit-license.php)
#@docs      https://gitlab.com/Naqwada/TapoPlug-Rest-API

import requests
import base64
import json
import time
from .tapoEncryption import generateKeyPair, decodeTapoKey, shaDigestEmail, encryptJsonData, decryptJsonData


'''
Get device information
'''
def getDeviceInfo(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "get_device_info",
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Get device running information
'''
def getDeviceRunningInfo(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "get_device_running_info",
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Turn ON the device.
'''
def plugOn(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "set_device_info",
    "params": {
      "device_on": True
    },
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Turn OFF the device.
'''
def plugOff(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "set_device_info",
    "params": {
      "device_on": False,
    },
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Get some diagnostic information's.
'''
def getDiagnoseStatus(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "get_diagnose_status",
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Get plug time usage.
'''
def getPlugUsage(deviceInfo):
  keys = loadKeys(deviceInfo)
  deviceID = json.loads(getDeviceInfo(deviceInfo))['result']['device_id']

  data = {
    "method": "get_device_usage",
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Can't really tell for what this used for now.
'''
def qsComponentNego(deviceInfo):
  keys = loadKeys(deviceInfo)
  deviceID = json.loads(getDeviceInfo(deviceInfo))['result']['device_id']

  data = {
    "method": "qs_component_nego",
    "params":   {
       "device_id":deviceID,
    },
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Change plug alias.
'''
def setNickname(deviceInfo):
  keys = loadKeys(deviceInfo)
  deviceID = json.loads(getDeviceInfo(deviceInfo))['result']['device_id']

  data = {
    "method": "set_device_info",
    "params": {
      "device_id": deviceID,
      "nickname": deviceInfo['nickname'],
    },
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Get LED status (ON/OFF).
'''
def getLedInfo(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "get_led_info",
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Turn OFF the LED.
'''
def ledOff(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "set_led_info",
    "params": {
        "led_status":False,
        "led_rule":"never", #never
        "night_mode":{
          "night_mode_type":"unknown",#custom
          "sunrise_offset":0,
          "sunset_offset":0,
          "start_time":0,
          "end_time":0
        }
    },
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Turn ON the LED.
'''
def ledOn(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "set_led_info",
    "params": {
        "led_status":True,
        "led_rule":"always", #never
        "night_mode":{
          "night_mode_type":"unknown",#custom
          "sunrise_offset":0,
          "sunset_offset":0,
          "start_time":0,
          "end_time":0
        }
    },
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Automatically turns OFF the device when the provided delay is expired.
'''
def plugOffCountdown(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "add_countdown_rule",
    "params": {
      "delay":int(deviceInfo['delay']),
      "desired_states":{
        "on":False
      },
      "enable":True,
      "remain":int(deviceInfo['delay'])
    },
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Automatically turns ON the device when the provided delay is expired.
'''
def plugOnCountdown(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "add_countdown_rule",
    "params": {
      "delay":int(deviceInfo['delay']),
      "desired_states":{
        "on":True
      },
      "enable":True,
      "remain":int(deviceInfo['delay'])
    },
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Should get device log, but always empty for me, I leave it here just in case.
'''
def getPlugLog(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "get_device_log",
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Get wireless access points information around the plug.
'''
def getWirelessScanInfo(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "get_wireless_scan_info",
    "params": {
      "start_index":0
    },
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  
  response = execRequest(deviceInfo, keys, data)
  return response

'''
Change plug wifi settings.
'''
def setWirelessInfo(deviceInfo):
  keys = loadKeys(deviceInfo)

  data = {
    "method": "set_qs_info",
    "params": {
      'account': {
          'password': base64.b64encode(deviceInfo['tapoEmail'].encode()).decode("utf-8"),
          'username': base64.b64encode(deviceInfo['tapoPassword'].encode()).decode("utf-8")
      },
      'time': {
          'latitude': 90,
          'longitude': -135,
          'region': deviceInfo['region'],
          'time_diff': 60,
          'timestamp': 1619885501
      },
      'wireless': {
          'key_type': deviceInfo['key_type'],
          'password': base64.b64encode(deviceInfo['password'].encode()).decode("utf-8"),
          'ssid': base64.b64encode(deviceInfo['ssid'].encode()).decode("utf-8")
      }
    },
    "requestTimeMils":0,
    "terminalUUID": "AA3512F85D2C603C3434C5BD9EA95B43"
  }
  return data
  response = execRequest(deviceInfo, keys, data)
  return response


'''
Generate Handshake.
'''
def generateHandshake(tapoIP, publicKey):

  data = {
    "method": "handshake",
    "params": {
      "key": publicKey,
    },
    "requestTimeMils":0
  }

  response = requests.post("http://{}/app".format(tapoIP), data=json.dumps(data), verify=False)

  if response.status_code != 200:
    error = {
      "code": response.status_code,
      "error": "Somthing's wrong."
    }

  return response


'''
Login in TP-Link cloud to get the authToken.
'''
def loginRequest(deviceInfo, decodedTapoKey, tapoCookie):
  emailHash = shaDigestEmail(deviceInfo['tapoEmail'])

  data = {
    "method": "login_device",
    "params": {
      "username": base64.b64encode(emailHash.encode()).decode("utf-8"),
      "password": base64.b64encode(deviceInfo['tapoPassword'].encode()).decode("utf-8"),
    },
    "requestTimeMils":0
  }

  encyptedJsonData = encryptJsonData(decodedTapoKey, json.dumps(data))

  secureData = {
    "method":"securePassthrough",
    "params":{
      "request": encyptedJsonData
      }
    }

  cookies = {
    tapoCookie[0] : tapoCookie[1],
  }

  response = requests.post("http://{}/app".format(deviceInfo['tapoIp']), cookies=cookies, data=json.dumps(secureData), verify=False)

  if response.status_code != 200:
    error = {
      "code": response.status_code,
      "error": "Somthing's wrong."
    }
  encryptedJsonResponse = json.loads(response.content.decode("utf-8"))['result']['response']
  
  decryptedJsonData = decryptJsonData(decodedTapoKey, encryptedJsonResponse)
  authToken = json.loads(decryptedJsonData)['result']['token']
  return authToken


'''
Encrypt json data and send request to the app.
'''
def execRequest(deviceInfo, keys, data):
  encyptedJsonData = encryptJsonData(keys['decodedTapoKey'], json.dumps(data))
  secureData = {
    "method":"securePassthrough",
    "params":{
      "request": encyptedJsonData
      }
  }

  cookies = {
    keys['tapoCookie'][0] : keys['tapoCookie'][1],
  }
  
  response = requests.post("http://{}/app?token={}".format(deviceInfo['tapoIp'],keys['tapoAuthToken']), cookies=cookies, data=json.dumps(secureData), verify=False)
  
  if response.status_code != 200:
    error = {
      "code": response.status_code,
      "error": "Somthing's wrong."
    }

  encryptedJsonResponse = json.loads(response.content.decode("utf-8"))['result']['response']
  
  decryptedJsonData = decryptJsonData(keys['decodedTapoKey'], encryptedJsonResponse)
  return "".join(n for n in decryptedJsonData if ord(n) >= 32 and ord(n) <= 126)


'''
Pack all necessary keys to communicate with the device.
'''
def loadKeys(deviceInfo):
  tapoKeyPair = generateKeyPair()
  handshakeRequest = generateHandshake(deviceInfo["tapoIp"], tapoKeyPair["publicKey"])
  tapoKey = json.loads(handshakeRequest.content.decode("utf-8"))['result']['key']
  tapoCookie = handshakeRequest.headers["Set-Cookie"].split(';')[0].split('=')
  decodedTapoKey = decodeTapoKey(tapoKey, tapoKeyPair)
  tapoAuthToken = loginRequest(deviceInfo, decodedTapoKey, tapoCookie)

  keys = {
    'tapoKeyPair': tapoKeyPair,
    'tapoKey': tapoKey,
    'decodedTapoKey': decodedTapoKey,
    'tapoCookie': tapoCookie,
    'tapoAuthToken': tapoAuthToken
  }

  return keys
