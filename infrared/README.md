Infrared control
================

I am using Lirc on my Libreelec based Raspberry Pi3 to control my old audio gear by infrared control.

I am running Libreelec 8.2.2 with my own hardware IR sender on pin 22, no reader but put it to 23 to avoid collition with my Digi+ audio card. The IR is an old Logitech IR dual LED extender.

To control the infrared remote I use MQTT as middleware, this is based on 
[cec-mqtt-bridge](https://github.com/michaelarnauts/cec-mqtt-bridge) by @michaelarnauts
which I [updated](http://github.com/frafall/cec-mqtt-bridge) to run on Libreelec.

TODO:
-----
- Move the lirc stuff into docker container, use 'docker run --privileged' to grant
  access to the GPIO

Configuration:
--------------
Check out [gpio-tx](https://forum.libreelec.tv/thread/12111-kernel-module-gpio-ir-sending-ir-codes)

1. Edit the /flash/config.txt to add Lirc modules:
  ```
  # mount -o remount,rw /flash
  # vi /flash/config.txt
  ...add the lines...
  dtoverlay=gpio-ir,gpio_pin=23
  dtoverlay=gpio-ir-tx,gpio_pin=22
  ..save and quit...
  # mount -o remount,ro /flash
  ```
2. Reboot
3. Verify module load:
  ```
  # lsmod | grep lirc
  lirc_rpi                5930  0
  lirc_dev                7007  1 lirc_rpi
  rc_core                20369  1 lirc_dev
  #
  ```
4. Simple [test.py](etc/test.py) program, direct your cell phone camera at leds to see blinking
5. Test Lirc configuration:
  - [lircd.conf](etc/lircd.conf)
  - [lircd.conf.d/RC-1047.conf](etc/lircd.conf.d/RC-1047.conf)
6. Try to run Lircd:
  ```
  # lircd -n /storage/infrared/etc/lircd.conf
  # irsend -d /run/lirc/lircd.socket SEND_ONCE Denon_RC-1047 KEY_POWER
  ```

7. Configure Libreelec 9 to run lircd at boot:
  - move [lircd.conf](etc/lircd.conf) to .config/lircd.conf 
  - move [lircd.conf.d/RC-1047.conf](etc/lircd.conf.d/RC-1047.conf) to .config/lircd.conf.d/
  - presence of .config/lircd.conf starts lircd at boot for Libreelec 9

8. Configure cec-mqtt-bridge (config.ini/lircrc)
   
9. Build the MQTT bridge docker
  ```
  # docker image build --tag mqtt-bridge .
  # docker run -d --net=host -v /var/run/lirc:/var/run/lirc \
    --restart unless-stopped --name mqtt-bridge mqtt-bridge
  ```

