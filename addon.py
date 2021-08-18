import xbmcaddon
import xbmcvfs
import subprocess
addonPath = xbmcaddon.Addon('script.retroarch.menu').getAddonInfo('path')
startCommand = xbmcaddon.Addon('script.retroarch.menu').getSettingString('start command')
logFile = xbmcvfs.translatePath('special://temp/retroarch.log')
subprocess.Popen(['/bin/bash', addonPath + 'resources/bin/retroarch.sh', startCommand, logFile], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
