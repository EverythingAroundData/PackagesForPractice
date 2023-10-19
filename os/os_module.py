import os

print(os.getcwd())
print('\n')
print(os.listdir('.'))
print('\n')

os.chdir('/home/linuxgeek/PythonProjects/EverythingAroundData/Repos/PackagesForPractice/PackagesForPractice')

print(os.getcwd())
print(os.listdir())

#Get all the files in root along with file size
for root, directory, file in os.walk(os.getcwd()):
    for f in file:
        file = root+'/'+f
        file_size = os.stat(file).st_size/(1024*1024)
        print('Filesize of '+str(file)+' is '+str(file_size)+' MB')

#get particular file
for root, directory, file in os.walk(os.getcwd()):
    for f in file:
        if '.csv' in f:
            print(f)


#sets environment variables
os.environ['LinuxUserProfile']='/home/linuxgeek'

#both environ.get and getenv gives same results
print(os.environ.get('LinuxUserProfile'))
print(os.getenv('LinuxUserProfile'))
