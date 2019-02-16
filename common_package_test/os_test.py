import os

print(os.getcwd())
print(os.listdir())

os.chdir("../package01")
print(os.getcwd())

if not os.path.exists(os.getcwd()+os.sep+"lijing.haha"):
    print(os.mkdir("lijing.haha"))
    

print(os.getenv("PATH"))

print(os.pardir)
print(os.curdir)
print(os.name)
print(os.fspath)