# -*- coding: utf-8 -*-
import os
from xbmcvfs import translatePath
import xbmcaddon

ADDON = xbmcaddon.Addon()

# Urls
IMG_PUBLIC = "https://jioimages.cdn.jio.com/imagespublic/"
IMG_CATCHUP = "https://jiotv.catchup.cdn.jio.com/dare_images/images/"
IMG_CATCHUP_SHOWS = "https://jiotv.catchup.cdn.jio.com/dare_images/shows/"
PLAY_URL = "plugin://plugin.video.jiotv/resources/lib/main/play/?"
PLAY_EX_URL = "plugin://plugin.video.jiotv/resources/lib/main/play_ex/?_pickle_="
FEATURED_SRC = "https://tv.media.jio.com/apis/v1.6/getdata/featurednew?start=0&limit=30&langId=6"
CHANNELS_SRC = "https://jiotv.data.cdn.jio.com/apis/v1.3/getMobileChannelList/get/?os=android&devicetype=phone&usertype=JIO&version=290&langId=6"
GET_CHANNEL_URL = "https://tv.media.jio.com/apis/v2.0/getchannelurl/getchannelurl?langId=6&userLanguages=All"
CATCHUP_SRC = "https://jiotv.data.cdn.jio.com/apis/v1.3/getepg/get?offset={0}&channel_id={1}&langId=6"
M3U_SRC = os.path.join(translatePath(
    ADDON.getAddonInfo("profile")), "playlist.m3u")
M3U_CHANNEL = "\n#EXTINF:0 tvg-id=\"{tvg_id}\" tvg-name=\"{channel_name}\" group-title=\"{group_title}\" tvg-chno=\"{tvg_chno}\" tvg-logo=\"{tvg_logo}\"{catchup},{channel_name}\n{play_url}"
EPG_SRC = "https://kodi.botallen.com/tv/epg.xml.gz"
DICTIONARY_URL = "https://jiotvapi.cdn.jio.com/apis/v1.3/dictionary/dictionary?langId=6"