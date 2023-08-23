import requests
import subprocess
import time
import os

# Input your "Target"
channelName = 'USER'

# Twitch Chat URL
chat_url = f'https://www.twitch.tv/{channelName}/chat'

# Function to check if the stream is live
def checkStream():
    response = requests.get(chat_url)
    if response.status_code == 200:
        return True
    else:
        return False

def startBot():
    while True:
        if checkStream():
            print(f'{channelName} is now live')
                # TODO
        else:
            print(f'{channelName} is not live')
        time.sleep(300)  # Check every 5 minutes
if __name__ == "__main__":
    startBot()
    
