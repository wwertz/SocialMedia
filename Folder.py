from pathlib import Path
import collections
import os


class ProjectFolders:
    def __init__(self):
        self.pathProject = Path().absolute()
        self.pathData = self.pathProject/'Data'
        self.pathNewImages = self.pathData/'NewImages'
        self.pathOldImages = self.pathData/'OldImages'

    def getNewImages(self):
        print('Getting images from ' + str(self.pathNewImages))

        listNewImages = list(self.pathNewImages.iterdir())
        print('The images in ' + str(self.pathNewImages) + ' are: ' + str(listNewImages))
        return listNewImages

    def groupImages(self, list):
        print('Grouping images: ', list)
        listReturn = []
        l = []
        
        #seperate and count paths
        for x in list:
            print('this is ', x)
            temp = Path(x).stem
            tempList = temp.split('_')
            l.insert(len(l), tempList[0])

            print(l)
        
        temp = collections.Counter(l)
        res = [[i] * j for i, j in temp.items()]

        print(res)

        #count and build paths
        for x in res:
            count = 1
            listx = []
            for temp in x:
                image = "\\" + temp + "_" + str(count) + ".jpg"
                tempPath = str(self.pathNewImages) + image
                listx.insert(len(listx),tempPath)
                count = count+1
            listReturn.insert(len(listReturn),listx)
        
        print(listReturn)
        return listReturn

    def moveFile(self, source, dest):
        print("Moving " + source + " to " + dest)
        os.rename(source, dest)

    def replaceFolder(source, target, new):
        print("Changing folder " + target + " from " + source + " to " + new)
        return source.replace(target, new)
        


        