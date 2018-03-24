f = open("myfile.txt" , "w")
l = ["vaari\n" , "preeti\n" , "anchal\n"]
f.writelines(l)
f.close()

f = open("myfile.txt" , "r")
data1 = f.readlines()
f.seek(0) #jumps to 11th char and skips the 10 characters from the beginning
print(data1)
print(type(data1))
data2 = f.readlines()
print(data2)
f.close()

f = open("myfile.txt" , "a")
f.write("new content")
f.close()

with open("myfile.txt" , "w") as f:
    l1 = ["hellooo" , "bewdo"]
    f.writelines(l1)
    
