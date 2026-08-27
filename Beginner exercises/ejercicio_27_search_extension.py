# find the extension or the archive https://docs.python.org/3/library/os.path.html#os.path.splitext
import os

cwd1=os.path.abspath('../sample.txt')
print(cwd1)
cwd=os.path.basename('../sample.txt')
print(cwd)
extension = os.path.splitext(cwd)
print(extension[1])
