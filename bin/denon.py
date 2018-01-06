#!/usr/bin/python
import sys
import paho.mqtt.publish as mqtt
from secrets import MQTTSecrets

device='Denon_RC-1047'
key='KEY_POWER_OFF'

if __name__ == '__main__':
   conf = MQTTSecrets('notify')
   topic='remote/ir/'+device+'/tx'

   try:
      if(sys.argv[1] == "on" or sys.argv[1] == "1"):
         key = "KEY_POWER_ON"
   except IndexError:
      pass

   mqtt.single(topic, key, 
      hostname=conf.server, port=conf.port, client_id="",
      auth={'username': conf.user, 'password': conf.password})

