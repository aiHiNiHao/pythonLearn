import shutil
import os

# shutil.move(os.pardir+os.sep+"package01"+os.sep+"lijing.haha", os.getcwd())
# shutil.copy2("lijing.haha", os.pardir+os.sep+"package01")

shutil.make_archive("ping", "zip", "lijing.haha")
shutil.unpack_archive("ping.zip", os.pardir+os.sep+"package01")