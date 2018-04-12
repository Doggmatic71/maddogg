# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Polaris 
# Author: Gracie


import os           
import xbmc         
import xbmcaddon    
import xbmcplugin   


from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

# Added by MuadDib
from koding import Keyboard 
from ytpsearch import *

debug        = Addon_Setting(setting='debug')       
addon_id     = xbmcaddon.Addon().getAddonInfo('id') 


BASE  = "plugin://plugin.video.youtube/playlist/"

YOUTUBE_CHANNEL_ID_1 = "PLhgG6tflTqsgxBT3Cd6zcIYiy1PXPuFtZ"
YOUTUBE_CHANNEL_ID_2 = "PLhgG6tflTqsgrvmOiJqUyJ8dxjtUX8oeL"
YOUTUBE_CHANNEL_ID_3 = "PLhgG6tflTqshVAfYsgSR5kS-8lfSfJ_gk"
YOUTUBE_CHANNEL_ID_4 = "PLhgG6tflTqsijVhnPBdEtbhK1eMvWePW7"
YOUTUBE_CHANNEL_ID_5 = "PLhgG6tflTqsiw8GijN6yS7wfhJmme97XB"
YOUTUBE_CHANNEL_ID_6 = "PLhgG6tflTqsg8JcNwpHVHssm0-OOlTJDm"
YOUTUBE_CHANNEL_ID_7 = "PLhgG6tflTqsgZ6en5jvrvHWkpw5K0m15a"
YOUTUBE_CHANNEL_ID_8 = "PLhgG6tflTqsgCuTdtz4HoG454diMxxeFm"
YOUTUBE_CHANNEL_ID_9 = "PLhgG6tflTqshEbOmGNsN0Yl5TbJLw-uUK"
YOUTUBE_CHANNEL_ID_10 = "PLhgG6tflTqshV-DlIB8RHRkMfndHmI8dA"
YOUTUBE_CHANNEL_ID_11 = "PLhgG6tflTqsi3PKMvca4xEgt9kxdaTPsH"
YOUTUBE_CHANNEL_ID_12 = "PLhgG6tflTqsjsQ16R0QzSF2O-vY4mNCsP"
YOUTUBE_CHANNEL_ID_13 = "PLhgG6tflTqsjXsHqed3a2tGm6Kpf5GJpO"
YOUTUBE_CHANNEL_ID_14 = "PLhgG6tflTqsg3bU9LHIShIQvubcNGt-N4"
YOUTUBE_CHANNEL_ID_15 = "PLhgG6tflTqshUWuHp-qvWsq41aJdKfRFt"
YOUTUBE_CHANNEL_ID_16 = "PLhgG6tflTqsjVCNnPT-kALaqZDYVBE2VB"
YOUTUBE_CHANNEL_ID_17 = "PLhgG6tflTqshDDGEbW413tLyxoxDFmpD4"
YOUTUBE_CHANNEL_ID_18 = "PLhgG6tflTqsivwvewLAMxWsTDr66V-HpI"
YOUTUBE_CHANNEL_ID_19 = "PLhgG6tflTqsh-SkwsuCNu-PUbiQohPyeO"
YOUTUBE_CHANNEL_ID_20 = "PLhgG6tflTqsiyfVygh9vnksgz8dm9Vmh-"
YOUTUBE_CHANNEL_ID_21 = "PLhgG6tflTqsjPEGtf15KPv7gYUtJcejy-"
YOUTUBE_CHANNEL_ID_22 = "PLhgG6tflTqsjEYXxDEwSVKSfGXwHmzIi9"
YOUTUBE_CHANNEL_ID_23 = "PLhgG6tflTqsjv-MS5zn6ObOTl1O5C7Etq"
YOUTUBE_CHANNEL_ID_24 = "PLhgG6tflTqsjhxcgn33t_23Sj-qstxuja"
YOUTUBE_CHANNEL_ID_25 = "PLhgG6tflTqsjYf-BqMqOQnh98WZvp_rPo"

# Added by MuadDib
PLAYLISTS = [ YOUTUBE_CHANNEL_ID_1, YOUTUBE_CHANNEL_ID_2, YOUTUBE_CHANNEL_ID_3, YOUTUBE_CHANNEL_ID_4, YOUTUBE_CHANNEL_ID_5, YOUTUBE_CHANNEL_ID_6, YOUTUBE_CHANNEL_ID_7, YOUTUBE_CHANNEL_ID_8, YOUTUBE_CHANNEL_ID_9, YOUTUBE_CHANNEL_ID_10, YOUTUBE_CHANNEL_ID_11, YOUTUBE_CHANNEL_ID_12, YOUTUBE_CHANNEL_ID_13, YOUTUBE_CHANNEL_ID_14, YOUTUBE_CHANNEL_ID_15, YOUTUBE_CHANNEL_ID_16, YOUTUBE_CHANNEL_ID_17, YOUTUBE_CHANNEL_ID_18, YOUTUBE_CHANNEL_ID_19, YOUTUBE_CHANNEL_ID_20 ]



@route(mode='main_menu')
def Main_Menu():
	Add_Dir( 
		name="Special Requests", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_04-27-01/photo_2018-04-10_04-27-01.jpg")
		
	Add_Dir( 
		name="Space and Exploration", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_04-23-46/photo_2018-04-10_04-23-46.jpg")
		
	Add_Dir( 
		name="Home Shows", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-TcX-lO0okkrwTxDq_uQUWasze5uzR4sA8x8OKCitfg3IHSsM")
		
	Add_Dir( 
		name="Business Ideas", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp4mVmAWP42z5JEq7WgGFOI09TpuELOZAzdDBcnt9xQkHIFTE")
	
	Add_Dir( 
		name="Money Saving and Life Hacks", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLWBUIcP5lBtfqjVkl4jOsOZu_bnc3La5JHoVbLiZNUIpmVFZC")
	
	Add_Dir( 
		name="Worship and Inspiration", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScF3VUCTqy0qrfanSbxZJkpc2R-j5XoqX9C7a2LdzHnZZnr90u")
	
	Add_Dir( 
		name="Day Time and Late Night Talk", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtWXXeqpuKF11tjEL6Xh-F4SInobXWSHk5-xX_RoORsQDN2zwD")
	
	Add_Dir( 
		name="Marvel and DC", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYd3E1LrhTnIjm_7NrzRAYDwhUkRcpqWfN3wssQsIaxeMoOUvS")
	
	Add_Dir( 
		name="Sports Frenzy", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_04-30-52/photo_2018-04-10_04-30-52.jpg")
	
	Add_Dir( 
		name="Water World", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_04-19-33/photo_2018-04-10_04-19-33.jpg")
			
	Add_Dir( 
		name="Crazy Karaoke", url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_04-15-33/photo_2018-04-10_04-15-33.jpg")

	Add_Dir( 
		name="Karaoke fever", url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_03-15-01/photo_2018-04-10_03-15-01.jpg")
		
	Add_Dir( 
		name="Car-e-oke Carpool", url=BASE+YOUTUBE_CHANNEL_ID_13+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3i5dQ52v9rtsxF0208su4UVxnN1uyVrF9ucYdlm-rwTsx9MKU")
		
	Add_Dir( 
		name="Music Express", url=BASE+YOUTUBE_CHANNEL_ID_14+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSL4XYsZolacaZjGFRvcufqQ83d1qFRjTKw5vKyCCDt_qe5IXdBkQ")
		
	Add_Dir(
		name="Gamers corner", url=BASE+YOUTUBE_CHANNEL_ID_15+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_03-36-06/photo_2018-04-10_03-36-06.jpg")
	
	Add_Dir( 
		name="Cartoons and anime", url=BASE+YOUTUBE_CHANNEL_ID_16+"/", folder=True,
		icon="https://archive.org/download/IMG20171022172819/IMG_20171022_172819.png")

	Add_Dir( 
		name="Armed Forces", url=BASE+YOUTUBE_CHANNEL_ID_17+"/", folder=True,
		icon="https://archive.org/download/IMG20171022131950/IMG_20171022_131950.png")

	Add_Dir( 
		name="Car Addicts", url=BASE+YOUTUBE_CHANNEL_ID_18+"/", folder=True,
		icon="https://archive.org/download/IMG20171022124735/IMG_20171022_124735.png")

	Add_Dir( 
		name="Out at Sea", url=BASE+YOUTUBE_CHANNEL_ID_19+"/", folder=True,
		icon="https://ia601507.us.archive.org/14/items/IMG20171122165036598/IMG_20171122_165036_598.png")

	Add_Dir( 
		name="Pyro Maniacs", url=BASE+YOUTUBE_CHANNEL_ID_20+"/", folder=True,
		icon="https://archive.org/download/IMG20171122163643205_201711/IMG_20171122_163643_205.png")

	Add_Dir( 
		name="Yummys", url=BASE+YOUTUBE_CHANNEL_ID_21+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_04-09-33/photo_2018-04-10_04-09-33.jpg")

	Add_Dir( 
		name="Trailer city", url=BASE+YOUTUBE_CHANNEL_ID_22+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_00-52-48/photo_2018-04-10_00-52-48.jpg")                                                                     

	Add_Dir( 	
		name="Documentaries", url=BASE+YOUTUBE_CHANNEL_ID_23+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_00-38-46/photo_2018-04-10_00-38-46.jpg")                          

	Add_Dir( 
		name="Blast from the past", url=BASE+YOUTUBE_CHANNEL_ID_24+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_03-31-07/photo_2018-04-10_03-31-07.jpg")
	
	Add_Dir(	
		name="Blessed movies", url=BASE+YOUTUBE_CHANNEL_ID_25+"/", folder=True,
		icon="https://archive.org/download/photo_2018-04-10_04-04-55/photo_2018-04-10_04-04-55.jpg")
		
    # Added by MuadDib
	Add_Dir( 
        name="Search", url='plugin://plugin.video.polaris?mode=search', folder=False,
        icon="http://www.clker.com/cliparts/f/c/d/7/1349200701375202527Search%20Icon.svg.hi.png")		

@route(mode='koding_settings')
def Koding_Settings():
	Open_Settings()

def Simple_Dialog(title,msg):
	OK_Dialog(title, msg)
	
# Added by MuadDib
@route(mode='search')
def Playlist_Search():
    search_term = Keyboard(default='', heading='Search Titles')
    if len(search_term) > 0:
        perform_search(search_term, PLAYLISTS)
    else:
        pass	

if __name__ == "__main__":
	Run(default='main_menu')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))
