#pip install instabot
#pip install instagrapi

from instabot import Bot
from instagrapi import Client

class Instagram:
    def __init__(self, username, password):
        self.bot = Client()
        self.username = username
        self.password = password

    def login(self):
        self.bot.login(self.username,self.password)
        #self.bot.login(username=self.username, password=self.password)

    def uploadPhoto(self, path_photo, caption):
        self.bot.photo_upload(path_photo, caption)

    def uploadPhotos(self, list_photos, caption):
        self.bot.album_upload(list_photos, caption)
