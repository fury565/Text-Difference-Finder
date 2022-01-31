import codecs
file1=codecs.open("orig.txt",'r',"utf-8")
file2=codecs.open("test.txt",'r',"utf-8")
s1=file1.readline()
s2=file2.readline()
line1=1
line2=1
while(s1!="" and s2!=""):
    if(s1==s2):
        print(str(line1)+" = "+str(line2))
        s1=file1.readline()
        s2=file2.readline()
        line1+=1
        line2+=1
    else:
        print(s1+" Failed "+s2)
        s2=file2.readline()
        line2+=1

