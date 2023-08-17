from SocialMedia.Instagram import Instagram
from Folder import ProjectFolders

folder = ProjectFolders()
listNewImages = folder.getNewImages()
bot = Instagram(username, password)

bot.login()

listImages = folder.groupImages(listNewImages)

for tempImages in listImages:
    print("Uploading " + str(len(tempImages)) + " image(s): ", tempImages)

    #check for number of items
    if len(tempImages) > 1:
        print("Uploading an album: ", tempImages)
        bot.uploadPhotos(tempImages, "test")
        
        #move images
        for oldPath in tempImages:
            newPath = folder.replaceFolder(tempImages[0], "NewImages", "UsedImages")
            folder.moveFile(oldPath, newPath)

    else:
        print("Uploading a photo: ", tempImages)
        bot.uploadPhoto(tempImages[0], "test")

        #move image
        newPath = folder.replaceFolder(tempImages[0], "NewImages", "UsedImages")
        folder.moveFile(tempImages[0], newPath)
    





    


