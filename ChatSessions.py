import re
class ChatSession:


    def __init__(self, file_name):
        #path="C:/Users/512677/AppData/Local/Programs/Python/Python310/WORKPSPACE/KianChee_Seng_FinalProj_27Dec2021/"
        #self.filename = path + file_name
        self.filename = open(file_name, "r")
        self.numLines = 0
        self.TagsList = []
        self.MembersList = []
        self.TimesList = []
        self.UserSysList = []
        self.UniqueMembersList = []
        self.UniqueTagsList = []
        self.MessageList = []
        self.li=[]
        self.Msgs=[]

        records = self.filename.readlines()
        for lines in records:
            self.numLines +=1
            tags = re.findall('^T\S', lines)
            self.TagsList.extend(tags)
            self.li = re.split ('\s', lines)
            self.TimesList.append(self.li[1])
            self.MembersList.append(self.li[2])
            self.UserSysList.append(self.li[3])
            if self.li[0] not in self.UniqueTagsList:
                self.UniqueTagsList.append(self.li[0])
            if self.li[2] not in self.UniqueMembersList:
                self.UniqueMembersList.append(self.li[2])
            self.Msgs = re.findall ('^.*[:*]\s (\S.*)', lines)
            self.MessageList.extend(self.Msgs)
        self.filename.close
                
    def GetNumLines(self):             
        return self.numLines            
            
    def GetTagsList(self):
        return self.TagsList
    
    def GetTimesList(self):
        return self.TimesList
    
    def GetMembersList(self):
        return self.MembersList
    
    def GetUserSysList(self):
        return self.UserSysList
    
    def GetUniqueMembersList(self):
        return self.UniqueMembersList
    
    def GetUniqueTagsList(self):
        return self.UniqueTagsList
    
    def GetMessageList(self):
        return self.MessageList

    def GetLi(self):             
        return self.li

    def GetMsgs(self):
        return self.Msgs


