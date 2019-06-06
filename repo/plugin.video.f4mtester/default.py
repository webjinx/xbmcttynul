import xbmc, xbmcgui, xbmcaddon, xbmcplugin, re
import urllib, urllib2
import re, string
import threading
import os
import base64 as b
#from t0mm0.common.addon import Addon
#from t0mm0.common.net import Net
import urlparse
import xbmcplugin
import cookielib

__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')
addon_id = 'plugin.video.f4mTester'
selfAddon = xbmcaddon.Addon(id=addon_id)
sys.path.append(xbmc.translatePath(os.path.join(xbmc.translatePath(selfAddon.getAddonInfo('Path')), 'lib')))

#addon = Addon('plugin.video.f4mTester', sys.argv)
#net = Net()

mode =None
play=False

#play = addon.queries.get('play', None)
paramstring=sys.argv[2]
#url = addon.queries.get('playurl', None)
print paramstring
name=''
proxy_string=None
proxy_use_chunks=True
auth_string=''
streamtype='HDS'
setResolved=False
if paramstring:
    paramstring="".join(paramstring[1:])
    params=urlparse.parse_qs(paramstring)
    try:
        url = params['url'][0]
    except:pass
    try:
        name = params['name'][0]
    except:pass

    try:
        proxy_string = params['proxy'][0]
    except:pass
    try:
        auth_string = params['auth'][0]
    except:pass
    print 'auth_string',auth_string
    try:
        streamtype = params['streamtype'][0]
    except:pass
    print 'streamtype',streamtype

    

    swf=None
    try:
        swf = params['swf'][0]
    except:pass

    callbackpath=""
    try:
        callbackpath = params['callbackpath'][0]
    except:pass

    iconImage=""
    try:
        iconImage = params['iconImage'][0]
    except:pass    
 
    callbackparam=""
    try:
        callbackparam = params['callbackparam'][0]
    except:pass
    
    
    try:
        proxy_use_chunks_temp = params['proxy_for_chunks'][0]
        import json
        proxy_use_chunks=json.loads(proxy_use_chunks_temp)
    except:pass
    
    simpleDownloader=False
    try:
        simpleDownloader_temp = params['simpledownloader'][0]
        import json
        simpleDownloader=json.loads(simpleDownloader_temp)
    except:pass
	
	
    mode='play'

    try:    
        mode =  params['mode'][0]
    except: pass
    maxbitrate=0
    try:
        maxbitrate =  int(params['maxbitrate'][0])
    except: pass
    play=True

    try:
        setResolved = params['setresolved'][0]
        import json
        setResolved=json.loads(setResolved)
    except:setResolved=False
    
def playF4mLink(url,name,proxy=None,use_proxy_for_chunks=False,auth_string=None,streamtype='HDS',setResolved=False,swf="", callbackpath="", callbackparam="",iconImage=""):
    from F4mProxy import f4mProxyHelper
    player=f4mProxyHelper()
    try:
        maxbitrate = int(selfAddon.getSetting("bbcBitRateMax"))
    except:
        maxbitrate = 1500

    if maxbitrate != 800 or maxbitrate != 1500 or maxbitrate != 2200 or maxbitrate != 3700:
        maxbitrate = 800
        
    if setResolved:
        urltoplay,item=player.playF4mLink(url, name, proxy, use_proxy_for_chunks,maxbitrate,simpleDownloader,auth_string,streamtype,setResolved,swf,callbackpath, callbackparam,iconImage)
        item.setProperty("IsPlayable", "true")
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)

    else:
        xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
        player.playF4mLink(url, name, proxy, use_proxy_for_chunks,maxbitrate,simpleDownloader,auth_string,streamtype,setResolved,swf,callbackpath, callbackparam,iconImage)
    
    return   
    
def getUrl(url, cookieJar=None,post=None,referer=None,isJsonPost=False, acceptsession=None):
    cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
    #opener = urllib2.install_opener(opener)
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
    if isJsonPost:
        req.add_header('Content-Type','application/json')
    if acceptsession:
        req.add_header('Accept-Session',acceptsession)
        
    if referer:
        req.add_header('Referer',referer)
    response = opener.open(req,post,timeout=30)
    link=response.read()
    response.close()
    return link
   
def keyboard_user(msg="", autocomplete=""):
    text_input = None
    if not text_input:
        keyboard = xbmc.Keyboard(autocomplete, msg)
        keyboard.doModal()
        if keyboard.isConfirmed():
            text_input = keyboard.getText()
return text_input
    
def GUIEditExportName(name):

    exit = True 
    while (exit):
          kb = xbmc.Keyboard('default', 'heading', True)
          kb.setDefault(name)
          kb.setHeading('Enter Url')
          kb.setHiddenInput(False)
          kb.doModal()
          if (kb.isConfirmed()):
              name  = kb.getText()
              #name_correct = name_confirmed.count(' ')
              #if (name_correct):
              #   GUIInfo(2,__language__(33224)) 
              #else: 
              #     name = name_confirmed
              #     exit = False
          #else:
          #    GUIInfo(2,__language__(33225)) 
          exit = False
    return(name)
    
if mode ==None:
    selfAddon.openSettings()
    liz=xbmcgui.ListItem(b.b64decode("Q29kZWQgYnkgU2hhbmkgZWRpdGVkIGJ5IGN0dHludWwuIEVuam95IDop"),iconImage="", thumbnailImage=__icon__)
    liz.setInfo( type="Video", infoLabels={ "Title": b.b64decode("Q29kZWQgYnkgU2hhbmkgZWRpdGVkIGJ5IGN0dHludWwuIEVuam95IDop")} )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + "?" + urllib.urlencode({'mode':'quit'}), listitem=liz, isFolder=False, )

elif mode == "custom_url":
    # Insert stream type [TSDOWNLOADER|HLSRETRY|SIMPLE]
    # Insert your URL here:
    url = keyboard_user("Insert your URL")
    name = keyboard_user("Insert your channel name", "F4MChannel")
    streamtype = keyboard_user("Insert stream type [TSDOWNLOADER|HDS|HLSRETRY|SIMPLE]", "HDS")
    if not name in ['Custom','TESTING not F4M'] :
        playF4mLink(url,name, proxy_string, proxy_use_chunks,auth_string,streamtype,setResolved,swf , callbackpath, callbackparam,iconImage)
    else:
        listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ), path=url )
        xbmc.Player().play( url,listitem)


elif mode == "quit":
    exit()

elif mode == "play" or mode=="12":
    print 'PLAying ',mode,url,setResolved
    
    if not name in ['Custom','TESTING not F4M'] :
        playF4mLink(url,name, proxy_string, proxy_use_chunks,auth_string,streamtype,setResolved,swf , callbackpath, callbackparam,iconImage)
    else:
        listitem = xbmcgui.ListItem( label = str(name), iconImage = "DefaultVideo.png", thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ), path=url )
        xbmc.Player().play( url,listitem)
    
        #newUrl=GUIEditExportName('')
        #if not newUrl=='':
        #    playF4mLink(newUrl,name)




if not play:
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
    
 