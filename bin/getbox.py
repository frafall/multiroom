#!/usr/bin/python
import paho.mqtt.publish as mqtt
from secrets import MQTTSecrets

device='KAON_KCF-3000NS'
key='KEY_POWER'

if __name__ == '__main__':
   topic='remote/ir/'+device+'/tx'
   conf = MQTTSecrets('notify')
   mqtt.single(topic, key, 
      hostname=conf.server, port=conf.port, client_id="",
      auth={'username': conf.user, 'password': conf.password})

