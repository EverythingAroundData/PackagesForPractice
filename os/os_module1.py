import os

os.getcwd()

#Creates child directories between paths using makedirs

path = os.path.expanduser('~')

newpath = path + '/dir/subdir/subdir1'

os.makedirs(newpath)

os.listdir(path)
