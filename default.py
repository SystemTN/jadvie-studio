# -*- coding: utf-8 -*-
# please visit JadViE Studio's Kodi

import xbmc,xbmcgui,xbmcplugin,sys

plugin_handle = int(sys.argv[1])
xbmcplugin.setContent(plugin_handle, 'movies')
icon = xbmc.translatePath("special://home/addons/plugin.jadvie.studio.emby.for.kodi.-0.1/icon.png")
	
def add_video_item(url, infolabels, img=''):
    #url = 'http://edge2.everyon.tv/etv2/'+url+'/BratuMarian.m3u8'
    # rtmp://edge2.everyon.tv/etv2/phd1003
    #url = 'rtmp://lm7.everyon.tv/ptv7/'+url+' live=1'
    #url = 'http://lm7.everyon.tv/ptv7/'+url+'/BratuMarian.m3u8'
    #url = 'http://edge2.everyon.tv/etv2sb/'+url+'.m3u8'
    if 'rtmp://' in url: url = url + ' live=1' 
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem)
    return


add_video_item('https://od.lk/d/ODVfMzMyODAzM18/Save.Me.Ep03.part1.fix.mp4',{ 'title': 'JadViE'}, icon)
add_video_item('https://och8og.bn1303.livefilestore.com/y4m5rkOZBvOOJ-gGpplG-jqWtc-nSidUbjuJG98DrP6sDmHVStCpsXrsC1zExxfhDWPjOHVV2KWFqFYvXDv83P1ogMoo_LPetbzgZ9Y_HPl-erNXXkcYtf84ukeAxB5Qt29teJa3OkrBrdXGvSw1rYxiXVpR9kySuJHyhArZ42TJmm5ussNWfZ-8O-ZrV9VUH0Q/Buddies.in.India.2017.TM.mp4?download&psid=1',{ 'title': 'JadViE'}, icon)
add_video_item('https://fsb1.weshare.me/f007911de9ad2762/BEN_V_MUN_1H.mp4?download_token=c81ad062ee814d98b4ad3c3c8a4f255f36828c17037a18a22b5a456d77d93e8c',{ 'title': 'Football'}, icon)
add_video_item('https://filedn.com/lz8bImMGXfW0qwGWxcotF35/Because.This.Is.My.First.Life.E01.171009.360p-NEXT.mkv',{ 'title': 'Football'}, icon)
xbmcplugin.endOfDirectory(plugin_handle)
sys.exit(0)

