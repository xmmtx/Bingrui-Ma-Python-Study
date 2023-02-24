str1='dksdfjghdfaeussdkjdcijiawUudisdkuydzskuhchdukjzuidxrkjfdxukysrdmjxcymdrxxymdsfydfcmdsfydfymxmfdsmysugbyuyjbsgyumsnsyunvyusvyumnyncuynumscvyumymactyuncstytsbsyttytrctnvnctyt rtcbbtmbmcebmcbtcrbcbmrbcsbycrbctbcrbcsrbcrb cbcbtcrbrcbrctcyrbyrybcztsycbtymbcsrzytycrtyzcrbczryybmrmtcrycbycrbrcybctryctctctrtrctyrtggfhhgbbcnndhhyqoprpoudjhjfhhjedjjfjmmvnnbbvnmmmxmmmsmmznnxjjsjhhrfrytyuuydudjsdkikidejjujdujj'
list1=[]
for x in str1:
    list1.append(x)
n=len(list1)
for i in range(n):
    if i in range(n):
        if list1[i]=='z':
            
    else:
        nn=ord(list1[i])
        list1[i]=chr(nn+1)
print(str1)
str2=''.join(list1)
print(str2)