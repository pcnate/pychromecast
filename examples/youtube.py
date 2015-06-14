from __future__ import print_function
import time
import pychromecast
print( "\r\nGetting Devices" )
devices = pychromecast.get_chromecasts_as_dict().keys()
print( devices )

selectedDevice = list(devices)[0]
#selectedDevice = "Nate PC Right"
print( "\r\nUsing Device: "+selectedDevice )

exit()

cast = pychromecast.get_chromecast(friendly_name=selectedDevice)
print(cast.device)
print(cast.status)
mc = cast.media_controller
print(mc.status)
mc.stop()
time.sleep(5)
mc.pause()
time.sleep(5)
mc.play()
from pychromecast.controllers.youtube import YouTubeController
yt = YouTubeController()
cast.register_handler(yt)

#yt.play_video("Xw8XCxWWTDg")
#yt.play_video("Nr_5Y6JKPc0")
#yt.play_video("YiUdrIsqmyQ")
yt.play_video("O5RdMvgk8b0")