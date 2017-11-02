#!/usr/bin/python

import xml.etree.ElementTree as ET
import json
import sys

data = ET.parse(sys.stdin).getroot()[0].text.lower()
command      = data[:16]
response     = data[18:40]
responseFlag = data[16:18]
targetDevice = data[22:28]
hubId        = data[28:34]
hopCount     = int(data[34:36], 16) - int('20', 16)
level        = int(data[38:40], 16)

status = {'command': command,
          'response': response,
          'deviceId': targetDevice,
          'hubId': hubId,
          'hopCount': hopCount,
          'level': level}

print json.dumps(status, sort_keys=True, indent=4, separators=(',', ': '))

sys.exit(0)
