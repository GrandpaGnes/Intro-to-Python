from ChatSessions import ChatSession

sessionObj = ChatSession('iphone_07_18-1.annot')

NumLine = sessionObj.GetNumLines()
Tags = sessionObj.GetTagsList()
times = sessionObj.GetTimesList()
members = sessionObj.GetMembersList()
usersys = sessionObj.GetUserSysList()
Uniqmem = sessionObj.GetUniqueMembersList()
Uniqtag = sessionObj.GetUniqueTagsList()
msgs = sessionObj.GetMessageList()
#lis = sessionObj.GetLi()
#mes = sessionObj.GetMsgs()

print(NumLine)
print(Tags)
print(times)
print(members)
print(usersys)
print(Uniqmem)
print(Uniqtag)
print(msgs)
#print(lis)
#print(mes)