import os
import time


print(os.getcwd())

print(os.listdir("/home"))
print(os.listdir(os.getcwd()))


f=open("ddd/bbb","w+")

f.write(time.time())
f.write("\n")
f.close()


print(open("ddd/bbb","r").read())
