import os

print(os.getcwd())
print('\n')
print(os.listdir('.'))
print('\n')

os.chdir('/home/linuxgeek/PythonProjects')
#print(os.getcwd())

#for root, directory, file in os.walk(os.getcwd()):
#    print(root, directory, file)

for root, directory, file in os.walk(os.getcwd()):
    for f in file:
        file = root+'/'+f
        file_size = os.stat(file).st_size/(1024*1024)
        print('Filesize of '+str(file)+' is '+str(file_size)+' MB')

#help(os.environ)

