#!/usr/bin/python
import paho.mqtt.publish as mqtt
import secret

device='KAON_KCF-3000NS'
key='KEY_POWER'

if __name__ == '__main__':
   topic='remote/ir/'+device+'/tx'
   mqtt.single(topic, key, 
      hostname=secret.mqtt_broker, port=secret.mqtt_port, client_id="",
      auth={'username': secret.mqtt_user, 'password': secret.mqtt_password})

