My multi room audio system
==========================

Documentation of my multi room audio system, components and configurations.
This includes part of the home automation as these are somewhat interlinked
for audio control.

My goal is to implement a full media center with multi room audio capabilities
with LEGAL streaming only. I want to teach my kids there are legal options out
there and how to use them.

So, I only add Netflix, Viaplay, NRK and simular streaming sources.

Thoughts:
---------
My son had a party last weekend, Snapcast stopped working in middle of party and they had to resort to a laptop connected directly to the stereo.

My fault, probably due to a bug in my static group code as Snapcast is damned solid. But, implementing a home automation and multi room system I need to make it foolproof. Wife acceptance factor drops like a rock if stuff like that happens.

Components:
-----------
- [Snapcast](https://github.com/badaix/snapcast), originally by @badaix, I am using [my own version](https://github.com/frafall/snapcast) which includes metadata and static groups
- [Librespot](https://github.com/frafall/librespot) for Spotify Connect
- [Mopidy](https://www.mopidy.com/) for local music and radio
- [Libreelec](https://libreelec.tv/) for [Kodi](https://kodi.tv/) with addons:
  * [service.snapcast](https://github.com/frafall/service.snapcast)
  * [plugin.netflix](https://github.com/asciidisco/plugin.video.netflix)
  * [plugin-viaplay](https://github.com/emilsvennesson/kodi-viaplay)
  * [NRK](http://kodi.wiki/view/Add-on:NRK%20Nett-TV)
- [Home Assistant](https://home-assistant.io/)
- [Appdaemon dashboards](https://appdaemon.readthedocs.io/en/latest/)

Configuration:
--------------

Issues:
-------
- [ ] Netflix only works on Kodi 18 while Kodi 17 has issues with DVD playing
- [ ] Switching audio sources in Kodi while playing anything leads to
  errors, Kodi 17 [crashes](https://forum.libreelec.tv/thread/11000-kodi-crashes-on-selecting-audio-output/) totally while Kodi 18 freezes after a few switches. Bad carma for wife acceptance factor when the 'old style' hifi equivalence was turning a knob to swap speakers
- [ ] Librespot is currently fragmenting, no maintainer is active
- [ ] Librespot missing basics like metadata api, full queue/list handling
- [x] Snapcast missing metadata and have dynamic groups. Resolved, added both in my repository.
