# -*- coding: utf-8 -*-


# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Hammer Time 
# Author: Code by Gracie Platlisting bu Doggmatic71

import os           
import xbmc         
import xbmcaddon    
import xbmcplugin   


from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

debug        = Addon_Setting(setting='debug')       
addon_id     = xbmcaddon.Addon().getAddonInfo('id') 


BASE  = "plugin://plugin.video.youtube/playlist/"

YOUTUBE_CHANNEL_ID_1 = "PL5gS9e_RDcYwnvZwxeTk8xgAEZlGjCuq3"
YOUTUBE_CHANNEL_ID_2 = "PL5gS9e_RDcYxPxmLdydv6DfdXkElYSFt0" 
YOUTUBE_CHANNEL_ID_3 = "PL5gS9e_RDcYzLUKTGWsC-JrKlEgxaL6Qn" 
YOUTUBE_CHANNEL_ID_4 = "PL5gS9e_RDcYzkQoy-OsYunaQh7UdEoFSF" 	
YOUTUBE_CHANNEL_ID_5 = "PL5gS9e_RDcYzayw7E0HCpjODy2V_lPLjM" 
YOUTUBE_CHANNEL_ID_6 = "PL5gS9e_RDcYzxWv_UZ8k2zzis_lstLp1L" 	
YOUTUBE_CHANNEL_ID_7 = "PL5gS9e_RDcYyE1loewXcBs6YhITMH8VLh" 	
YOUTUBE_CHANNEL_ID_8 = "PL5gS9e_RDcYykNjGcm0dMdTdjii0Ms6NH" 	
YOUTUBE_CHANNEL_ID_9 = "PL5gS9e_RDcYyoJ6AGFexB8mVwO20kSIFD" 	
YOUTUBE_CHANNEL_ID_10 = "PL5gS9e_RDcYye76gn1Ag1QxgBm6UXxrLm" 	
YOUTUBE_CHANNEL_ID_11 = "PL5gS9e_RDcYwdXCoN32wzYkVEbAGNvW9i" 	
YOUTUBE_CHANNEL_ID_12 = "PL5gS9e_RDcYwdH_KlTmkENPnXgNM3KMQn" 
YOUTUBE_CHANNEL_ID_13 = "PL5gS9e_RDcYxkWiTlqi57SmUpqig24NdT" 	
YOUTUBE_CHANNEL_ID_14 = "PL5gS9e_RDcYzCNMu8j27LhYjS4qGGzgFX" 	
YOUTUBE_CHANNEL_ID_15 = "PL5gS9e_RDcYwFA1Sg2O1RMpqXOYANjMqQ" 	
YOUTUBE_CHANNEL_ID_16 = "PL5gS9e_RDcYzdAe24GTTEWZSLNZt9xVfU"

@route(mode='main_menu')
def Main_Menu():
	Add_Dir( 
        name="Outdoor Games DIY", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="http://img.youtube.com/vi/iZOsDhXCJiM/maxresdefault.jpg")
		
	Add_Dir( 
        name="Automotive Tips", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="http://img.youtube.com/vi/u9Y_Wf3mCm8/maxresdefault.jpg")
	
	Add_Dir( 
        name="Natural Disaster Tips", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="http://img.youtube.com/vi/-OzViYab2No/maxresdefault.jpg")
		
	Add_Dir( 
        name="Plumbing DIY", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="http://img.youtube.com/vi/gdibSnViLJA/maxresdefault.jpg")
	
	Add_Dir( 
        name="Electrical DIY", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="http://img.youtube.com/vi/VLKTHMdHJN8/maxresdefault.jpg")
	
	Add_Dir( 
        name="Appliance Maintenance", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="http://img.youtube.com/vi/6jV6zSP75tA/maxresdefault.jpg")
	
	Add_Dir( 
        name="Garden DIY", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="http://img.youtube.com/vi/bX8vi9gOibk/maxresdefault.jpg")
	
	Add_Dir( 
        name="Laundry Room Makeover", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="http://img.youtube.com/vi/kqw03Z8YJO8/maxresdefault.jpg")
	
	Add_Dir( 
        name="Solar DIY", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="http://img.youtube.com/vi/w4qcoEXYqK0/maxresdefault.jpg")
	
	Add_Dir( 
        name="Outdoor Living", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="http://img.youtube.com/vi/rqdfEYaWJaM/maxresdefault.jpg")
	
	Add_Dir( 
        name="Picture Hanging", url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
        icon="http://img.youtube.com/vi/VTLPKdzgpA4/maxresdefault.jpg")
	
	Add_Dir( 
        name="Living Room Makeover", url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,
        icon="http://img.youtube.com/vi/T9WFqR9FCEg/maxresdefault.jpg")
	
	Add_Dir( 
        name="Bedroom Makeover", url=BASE+YOUTUBE_CHANNEL_ID_13+"/", folder=True,
        icon="http://img.youtube.com/vi/SyGf_SfEKVM/maxresdefault.jpg")
	
	Add_Dir( 
        name="Bathroom Makeover", url=BASE+YOUTUBE_CHANNEL_ID_14+"/", folder=True,
        icon="http://img.youtube.com/vi/yrsCC3ErrhI/maxresdefault.jpg")
	
	Add_Dir( 
        name="Kitchen Makeover", url=BASE+YOUTUBE_CHANNEL_ID_15+"/", folder=True,
        icon="http://img.youtube.com/vi/yhNj6HkdFRY/maxresdefault.jpg")
	
	Add_Dir( 
        name="Space Saving DIY", url=BASE+YOUTUBE_CHANNEL_ID_16+"/", folder=True,
        icon="http://img.youtube.com/vi/VshBBHxbTyQ/maxresdefault.jpg")
		
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