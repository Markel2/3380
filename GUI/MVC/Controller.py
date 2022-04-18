class Controller:
    def __init__(self, model, view, theHash):
        self.model = model
        self.view = view
        self.hash = theHash
        
        self.fileName = ""


    def SendFile(self):
        self.hash.startHash()

    def SetFile(self, filename):
        self.fileName = filename


    def GetFile(self):
        return self.fileName


    def GetMatch(self):
        if(self.hash.matcher):
            print("Match!")
        else:
            print("No Match!")
        
        return self.hash.matcher

    def sendback(self,file):
        self.hash.saveinfotofile(file)

    def writeInfo(self):
        self.hash.writeInfo()

    def getKey(self):
        return self.hash.getKey()
