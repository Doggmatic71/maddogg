# -*- coding: utf-8 -*-


# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: See My Bear Bass 
# Author: Code by Doggmatic71

import os           
import xbmc         
import xbmcaddon    
import xbmcplugin   
from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

debug        = Addon_Setting(setting='debug')       
addon_id     = xbmcaddon.Addon().getAddonInfo('id') 


BASE  = "plugin://plugin.video.youtube/playlist/"
YOUTUBE_CHANNEL_ID_1 = "PLGS6jOAoV1HaWxNZ1oXbtpkLeXyC5OKn3"
YOUTUBE_CHANNEL_ID_2 = "PLGS6jOAoV1Ha_hwZ3Nz-_28HCvU3iw9zj" 
YOUTUBE_CHANNEL_ID_3 = "PLGS6jOAoV1HamsXE29mLcmJufsbauG_rI" 
YOUTUBE_CHANNEL_ID_4 = "PLGS6jOAoV1HZNXvuHCZeBp07GgShRWwy-" 	
YOUTUBE_CHANNEL_ID_5 = "PLGS6jOAoV1HapNNetVTdXopMChoXNZ9xK" 
YOUTUBE_CHANNEL_ID_6 = "PLGS6jOAoV1HYDzVV5OrA5LQ7nt7y9SQ-H" 	
YOUTUBE_CHANNEL_ID_7 = "PLGS6jOAoV1Ha75pnMTYmb2TLL4zwnUFMn" 	
YOUTUBE_CHANNEL_ID_8 = "PLGS6jOAoV1HbRpJUhLALx-nO3tBn1jNEz" 	
YOUTUBE_CHANNEL_ID_9 = "PLGS6jOAoV1HaPbSMG83Xk62yWX0LtoE6n" 	
YOUTUBE_CHANNEL_ID_10 = "PLGS6jOAoV1Hb5DK1HzucV0J-xeegd3BDF" 	
YOUTUBE_CHANNEL_ID_11 = "PLGS6jOAoV1Ham0OpOrD1xyDTNwbr5IstN" 	

@route(mode='main_menu')
def Main_Menu():
	Add_Dir( 
        name="Bait Debate", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://img.youtube.com/vi/RV2dwkSs_Gc/maxresdefault.jpg")
		
	Add_Dir( 
        name="Shore Fishing", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://img.youtube.com/vi/LrcCLnItAqU/maxresdefault.jpg")
	
	Add_Dir( 
        name="Off Shore Fishing", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://img.youtube.com/vi/WotOlLYXU1Q/maxresdefault.jpg")
		
	Add_Dir( 
        name="Hunting TV", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://img.youtube.com/vi/IsdZ7dpg5XI/maxresdefault.jpg")
	
	Add_Dir( 
        name="Bow Hunting Tips", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="https://img.youtube.com/vi/3_mb4i0wrz4/maxresdefault.jpg")
	
	Add_Dir( 
        name="Rifle Hunting Tips", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="https://img.youtube.com/vi/LTYOdcyo3KI/maxresdefault.jpg")
	
	Add_Dir( 
        name="Cape & Quarter", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="https://img.youtube.com/vi/_4992EBr45k/maxresdefault.jpg")
	
	Add_Dir( 
        name="Butchering", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="https://img.youtube.com/vi/PoawhsmKIEY/maxresdefault.jpg")
	
	Add_Dir( 
        name="Bow Hunt or Die Season 8", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="https://archive.org/download/bowhuntordie/bowhuntordie.jpg")
	
	Add_Dir( 
        name="Bow Hunt or Die Season 7", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="https://archive.org/download/bowhuntordie/bowhuntordie.jpg")
	
	Add_Dir( 
        name="Bow Hunt or Die Season 6", url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
        icon="https://archive.org/download/bowhuntordie/bowhuntordie.jpg")
	

	
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()

@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)
#
if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))