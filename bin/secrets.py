#!/usr/bin/python
"""
Module to read the secrets from ~/.ssh/secrets.ini
My way to make sure I don't get confedential information
into github. 

ex secrets.ini:

   [mqtt]
   broker   = 127.0.0.1
   port     = 1883

   [notify]
   user     = sample_notify
   password = sample_notify_password
   topic    = notify/#

TODO:
Add command line to create the needed file if it does not exist.
"""
import os
from ConfigParser import ConfigParser

class ConfigSecrets(ConfigParser):
   def __init__(self, secrets=None):
      ConfigParser.__init__(self)
      if secrets == None:
         secrets = os.getenv('HOME') + '/.ssh/secrets.ini'
      self.read(secrets)

class MQTTSecrets(ConfigSecrets):
   def __init__(self, section, secrets=None):
      ConfigSecrets.__init__(self, secrets)
      self.section = section

   @property
   def port(self):
      return self.getint('mqtt', 'port')

   @property
   def server(self):
      return self.get('mqtt', 'broker')

   @property
   def user(self):
      return self.get(self.section, 'user')

   @property
   def password(self):
      return self.get(self.section, 'password')

   @property
   def topic(self):
      return self.get(self.section, 'topic')

if __name__ == '__main__':
   secrets = MQTTSecrets('notify')
   print(secrets.server)
   print(secrets.user)
   print(secrets.topic)

