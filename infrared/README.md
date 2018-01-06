Infrared control
================

I am using Lirc on my Libreelec based Raspberry Pi3 to control my old audio gear by infrared control.

I am running Libreelec 8.2.2 with my own hardware IR sender on pin 22, no reader but put it to 23 to avoid collition with my Digi+ audio card. The IR is an old Logitech IR dual LED extender.

Configuration:
--------------
1. Edit the /flash/config.txt to add Lirc modules:
  ```
  # mount -o remount,rw /flash
  # vi /flash/config.txt
  ...add the lines...
  dtoverlay=lirc-rpi
  dtparam=gpio_out_pin=22
  dtparam=gpio_in_pin=23
  dtparam=debug=1
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

