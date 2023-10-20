import os

#use basename to get filename or the leaf folder instead of using split on path.
#the paths don't even need to exist.

print(os.path.basename('/tmp/dir1'))
print(os.path.basename('/tmp/dir1/heythere.txt'))


#use dirname for getting the path excluding the leaf file/directory.

print(os.path.dirname('/tmp/dir1'))
print(os.path.dirname('/tmp/dir1/heythere.txt'))

#check if path exists using exists

print(os.path.exists('/tmp/dir1/heythere.txt'))

#check if object is file/directory

path = os.path.expanduser('~')

print(os.path.isdir(path))
print(os.path.isfile(path))

#split file name and ext
newpath = os.path.join(path, 'heythere.txt')
print(os.path.splitext(os.path.basename(newpath)))