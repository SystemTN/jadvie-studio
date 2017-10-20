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

add_video_item('https://www.dl.dropboxusercontent.com/s/ssrwpvrk7hip256/Xin%20%C4%90%E1%BB%ABng%20H%C3%A1i%20Hoa%20-%20B%E1%BA%B1ng%20C%C6%B0%E1%BB%9Dng%20%5BOfficial%20Audio%5D%20-%20YouTube.MP4?dl=0',{ 'title': 'Dropbox'}, icon)

add_video_item('https://od.lk/d/ODVfMzMyODAzM18/Save.Me.Ep03.part1.fix.mp4',{ 'title': 'OpenDrive'}, icon)

add_video_item('https://och8og.bn1303.livefilestore.com/y4m5rkOZBvOOJ-gGpplG-jqWtc-nSidUbjuJG98DrP6sDmHVStCpsXrsC1zExxfhDWPjOHVV2KWFqFYvXDv83P1ogMoo_LPetbzgZ9Y_HPl-erNXXkcYtf84ukeAxB5Qt29teJa3OkrBrdXGvSw1rYxiXVpR9kySuJHyhArZ42TJmm5ussNWfZ-8O-ZrV9VUH0Q/Buddies.in.India.2017.TM.mp4?download&psid=1',{ 'title': 'Buddies in India 2017 - Thuyết Minh - Đại Náo Thiên Trúc 2017'}, img='https://i.moveek.com/media/cache/poster/media/cef8eb6517ee00a078347f51da0bcd27453ba27d.jpg')

add_video_item('https://onedrive.live.com/download?cid=295BD6ACA1A92117&resid=295BD6ACA1A92117%219966&authkey=AKeM3zwrHZCvgQ4',{ 'title': 'Detective Dee 2017 - Thuyết Minh - Địch Nhân Kiệt Kỳ Án 2017'}, img='https://vuviphim.com/wp-content/uploads/2017/05/Dich-Nhan-Kiet-Ky-An-Detective-Dee-2017-Poster.jpg')

add_video_item('https://fsb1.weshare.me/f007911de9ad2762/BEN_V_MUN_1H.mp4?download_token=c81ad062ee814d98b4ad3c3c8a4f255f36828c17037a18a22b5a456d77d93e8c',{ 'title': 'Football'}, icon)

add_video_item('https://filedn.com/lz8bImMGXfW0qwGWxcotF35/Because.This.Is.My.First.Life.E01.171009.360p-NEXT.mkv',{ 'title': 'pCloud'}, icon)
xbmcplugin.endOfDirectory(plugin_handle)
sys.exit(0)
