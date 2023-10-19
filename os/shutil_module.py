import shutil


path = '/home/pyninja/dir'


#the os module's rmdir command cann't remove the  non empty dir which shutil can.
shutil.rmtree(path)
