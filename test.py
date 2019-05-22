import os
import time


print(os.getcwd())

print(os.listdir("/home"))
print(os.listdir(os.getcwd()))


f=os.open("ddd/bbb")

f.write(time.time())
f.write("\n")
f.close()


print(os.open("ddd/bbb").read())
