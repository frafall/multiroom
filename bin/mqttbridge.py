#!/usr/bin/python
'''
Implement a MQTT to libnotify bridge.

Author: github.com/frafall

This will listen on MQTT for topic 'notify/<filtertag>'
and display the notification on the desktop.

TODO:
- split into MQTT listener and display class to simplify growl impl
- move to json payload
'''
import os
import sys
import gi

gi.require_version("Notify", "0.7")
from gi.repository import Notify

import paho.mqtt.client as paho

sys.path.append(os.getenv('HOME') + '/Apps/lib')
from secrets import MQTTSecrets

class MQTTNotificationBridge(paho.Client):
   def __init__(self, topic, server='127.0.0.1', port=1883, user=None, password=None):
      paho.Client.__init__(self, clean_session=True)
      self._topic = topic

      Notify.init('mqttBridge')
      self.username_pw_set(user, password)
      self.connect_async(server, port, 60)

   def notify(self, header, message, ttl=-1, urgency=0):
      icon = '/home/mhe/Apps/bin/mosquitto-colour-deselected-64x64.png'
      msg = Notify.Notification.new(header, message, icon)
      msg.set_timeout(ttl)
      msg.set_urgency(urgency)
      msg.show()

   def on_connect(self, client, userdata, flags, rc):
      if rc == 0:
         self.notify("mqttBridge", "(re)connected to server!")
         self.subscribe(self._topic, 0)

      # Not sure this will be triggered using client.loop_forever
      else:
         self.notify("mqttBridge", "Connection failed: " + paho.connack_string(rc))
 
   def on_disconnect(self, client, obj, rc):
      if rc == 0:
         self.notify("mqttBridge", "Terminating!")

      # Not sure this will be triggered using client.loop_forever
      else: 
         self.notify("mqttBridge", "Lost connection to server!")
         self.reconnect()
 
   def on_message(self, client, obj, msg):
      message = msg.payload + ' \n\n(Topic: ' + msg.topic + ' - QoS: ' + str(msg.qos) + ')'
      self.notify(msg.topic, message)
 
if __name__ == '__main__':
   conf = MQTTSecrets('notify')
   notifier = MQTTNotificationBridge(conf.topic, conf.server, conf.port, conf.user, conf.password)
   notifier.loop_forever(retry_first_connection=True)

