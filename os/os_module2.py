import os

for env in os.environ:
    print(env,'->', os.getenv(env))

print(os.environ.get('HOME')) 
print(os.getenv('HOME'))    


#join paths using path.join
filetobecreated = os.path.join(os.path.expanduser('~'),'heythere.txt')

with open(filetobecreated, 'a') as f:
    f.write('This is some random text. Testing os.path.join')

for obj in os.listdir(os.path.expanduser('~')):
    print(obj)
