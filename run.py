import requests
import subprocess
import time
import os
from time import sleep

# Input your "Target"
channelName = 'USER'

contents = requests.get('https://www.twitch.tv/' + channelName).content.decode('utf-8')

refreshingalways = True
def checkStream():
    while refreshingalways == True:
        if 'isLiveBroadcast' in contents:
            # Return True if the Streamer is streaming
            print(channelName + " is now live") 
            time.sleep(1800)
            return True
        else:
            # Return False if the Streamer is not streaming
            print(channelName + " is not live")
            time.sleep(1800)
            return False

def startBot():
    # If checkStream() outputs True, meaning the Streamer is Streaming, then we will open a Chromium Browsers with just the Chat
    if checkStream() == True:
        with open (os.devnull, "w") as fp:
            url = "https://www.twitch.tv/popout/" + channelName + "/chat"
            # Creating and using the Process
            p = subprocess.Popen(["chromium-browser", url], stdout=fp, stderr=fp)
            # If the Streamer goes offline agian, we want to close the Chat again.
            if checkStream() == False:
                p.kill()
