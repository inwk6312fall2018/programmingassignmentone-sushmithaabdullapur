#open the file in reading mode
fin = open("running-config.cfg","r")
#creating a config file to write mode
fout= open("config.txt","w")
for line in fin:
#by using for loop copying the  data to config file
  fout.write(line)
x=172
y=192
z=10
#creating the function for modifying the data
def  modify(fout):
  for line in fout:
    word=word.strip()
    word=word.split()
#by using if condition checking the expression is correct or not
    if word == x:
#replaceing the 172 by 10 by using replace method
      word=word.replace(x,z)
#replaceing the 172 by 10 by using replace method
    else word == y:
      word=word.replace(y,z)
file=open("config.txt",'r') 
modify(file)

