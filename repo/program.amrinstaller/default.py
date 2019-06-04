import sys, xbmcgui, xbmcaddon
import installer

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params.replace('?','')
            if (params[len(params)-1]=='/'):
                params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                splitparams={}
                splitparams=pairsofparams[i].split('=')
                if (len(splitparams))==2:
                    param[splitparams[0]]=splitparams[1]
        return param

params=get_params()
addon = xbmcaddon.Addon('program.amrinstaller')

try:
    mode=int(params["mode"])
except:
    mode=None

if mode==None:
    if addon.getSetting("save_location_addon") == "":
        import os
        default_dir = os.path.expanduser('~')
        addon.setSetting("save_location_addon", default_dir)
        xbmcgui.Dialog().ok("Installer", "Download directory has been set to default as your home OS folder. You can change it via addon setting.", "Path: " + default_dir)

    addon.openSettings()

elif mode==500:
    keyboard = xbmc.Keyboard("", heading = "Insert here your full url (must end with .zip)")
    keyboard.doModal()
    if (keyboard.isConfirmed()):
        url = keyboard.getText()
    keyboard = xbmc.Keyboard("", heading = "Insert here your filename (example plugin.video.addon.zip)")
    keyboard.doModal()
    if (keyboard.isConfirmed()):
        name = keyboard.getText()
    if (url != "" and name != "") or (url != None and name != None):
        installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==501:
    name = "plugin.video.livestreamspro"
    url="https://github.com/cttynul/plugin.video.livestreamspro/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==502:
    name = "plugin.video.f4mtester"
    url="https://github.com/cttynul/plugin.video.f4mtester/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==503:
    name = "plugin.video.vvvvid"
    url="https://github.com/cttynul/plugin.video.vvvvid/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==504:
    name = "plugin.video.kod"
    url="https://github.com/kodiondemand/addon/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==505:
    name = "plugin.video.netflix"
    url="https://github.com/CastagnaIT/plugin.video.netflix/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==506:
    name = "repository.kod"
    url="https://github.com/kodiondemand/kodiondemand.github.io/raw/master/repo/repository.kod-1.0.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==507:
    name = "repository.castagnait"
    url="https://github.com/castagnait/repository.castagnait/raw/master/repository.castagnait-1.0.0.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==508:
    name = "repository.sandmann79.plugins"
    url="https://github.com/Sandmann79/xbmc/releases/download/v1.0.2/repository.sandmann79.plugins-1.0.2.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==509:
    name = "repository.axbmcuser"
    url="https://github.com/axbmcuser/_repo/raw/master/repository.axbmcuser.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==510:
    name = "repository.kodil"
    url="https://github.com/kodil/kodil/raw/master/repository.kodil-1.0.1.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==511:
    name = "repository.neverwise"
    url="https://github.com/NeverWise/repository.neverwise/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==512:
    name = "script.module.urlresolver"
    url="https://github.com/tvaddonsco/script.module.urlresolver/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==513:
    name = "script.module.resolveurl"
    url="https://github.com/jsergio123/script.module.resolveurl/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==514:
    name = "script.module.liveresolver"
    url="https://github.com/kodil/kodil/raw/master/repo/script.module.liveresolver/script.module.liveresolver-0.1.50.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==515:
    name = "script.module.streamlink.crypto"
    url="https://github.com/tvaddonsco/tva-resolvers-repo/raw/master/zips/script.module.streamlink.crypto/script.module.streamlink.crypto-1.5.2.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==516:
    name = "script.module.streamlink.plugins"
    url="https://github.com/tvaddonsco/tva-resolvers-repo/raw/master/zips/script.module.streamlink.plugins/script.module.streamlink.plugins-1.0.3.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==517:
    name = "script.module.streamlink.base"
    url="https://github.com/tvaddonsco/tva-resolvers-repo/raw/master/zips/script.module.streamlink.base/script.module.streamlink.base-2019.05.08.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==518:
    name = "script.module.html5lib"
    url="https://github.com/kodil/kodil/raw/master/repo/script.module.html5lib/script.module.html5lib-0.999.0.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==519:
    name = "script.video.F4mProxy"
    url="https://archive.org/download/script.video.F4mProxy/script.video.F4mProxy.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==520:
    name = "plugin.video.f4mTester"
    url="https://archive.org/download/plugin.video.f4mTester/plugin.video.f4mTester.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==521:
    name = "plugin.video.raitv"
    url="https://github.com/nightflyer73/plugin.video.raitv/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==522:
    name = "plugin.video.mediasetplay"
    url="https://github.com/kodi-bino/plugin.video.mediasetplay/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==523:
    name = "plugin.video.rivedila7"
    url="https://github.com/luivit/plugin.video.rivedila7/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==524:
    name = "plugin.video.dplay"
    url="https://github.com/NeverWise/plugin.video.dplay/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))

elif mode==525:
    name = "program.plexus"
    url="https://github.com/tvaddonsco/program.plexus/archive/master.zip"
    installer.wizard(name, url, addon.getSetting("save_location_addon"))
