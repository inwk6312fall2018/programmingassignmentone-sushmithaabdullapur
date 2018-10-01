#my first attempt
myfile=open("running-config.cfg")
for line in myfile:
  line =line.strip()
  line=line.split()
  if (line[0]=='interface'):
    mylist_intname.append(line[1])
print(mylist_intname)

