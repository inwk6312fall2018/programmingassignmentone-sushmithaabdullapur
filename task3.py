#opening the file in reading mode
fin=open("running-config.cfg","r")
#creating an empty lis1 and list2
list1=[]
list2=[]
for line in fin:
  line=line.strip()
  line=line.split()
 # print(line)
#by using  if condition checking wheather line consist of  accesslist.
  if line[0]== 'access-list':
#nested if and elif condition to verify line consist of global_access and fw-management_access_in 
    if line[1]=='global_access'
#if condition is true by using append method it will append the line to list1
       list1.append(line)
    elif line[1]=='fw-management_access_in':
#it will append to list2.
       list2.append(line)
  else:
    print(False)
#displaying list1 and list2
print(list1)
print(list2)
