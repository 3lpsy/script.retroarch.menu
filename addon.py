import xbmcaddon
import xbmcvfs
import subprocess

addonPath = xbmcaddon.Addon('script.retroarch.menu').getAddonInfo('path')

startRetroarchCommand = xbmcaddon.Addon('script.retroarch.menu').getSettingString('start-retroarch')
stopKodiCommand = xbmcaddon.Addon('script.retroarch.menu').getSettingString('stop-kodi')
restartKodiCommand = xbmcaddon.Addon('script.retroarch.menu').getSettingString('restart-kodi')

logFile = xbmcvfs.translatePath('special://temp/retroarch.log')

subprocess.Popen([
    '/bin/bash', 
    addonPath + 'resources/bin/retroarch.sh', 
    startRetroarchCommand, 
    stopKodiCommand, 
    restartKodiCommand, 
    logFile
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
