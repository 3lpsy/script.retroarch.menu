# script.retroarch.menu
A fork of script.retroarch.menu

## About
This addon is a glorified script launcher and is very specific to my setup running Kodi and Retroarch via Systemd services and under cage/wayland. To stop kodi, it leverages `kodi-send` by default as this allows retroarch to takeover the TTY. Attempts at using systemctl to stop the service caused the script to top executing once stopped. You can of course use whatever commands work for you.


