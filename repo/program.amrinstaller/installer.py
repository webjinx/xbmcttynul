import urllib
import xbmcaddon, xbmcgui, xbmc, os

def wizard(name, url, path):
    #path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    if path=="":
        xbmcgui.Dialog().ok("Installer", "You have to set a download path in settings before using this.")
        return
    dp = xbmcgui.DialogProgress()
    dp.create("Installer","Downloading " + name,'', 'Please wait')
    lib=os.path.join(path, name +'.zip')
    download(url, lib, dp)
    xbmcgui.Dialog().ok("Installer", "Download completed! Kodi's from zip will popup, install your addon from there.", "Path: " + lib)
    xbmc.executebuiltin('InstallFromZip')

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("Installer","Downloading",' ', ' ')
    dp.update(0)
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url, dp):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        raise Exception("Canceled")
        dp.close()