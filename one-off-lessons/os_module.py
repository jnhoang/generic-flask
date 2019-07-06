# https://www.youtube.com/watch?v=tJxcKyFMTGo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=10

import os
from datetime import datetime
foo = os.listdir()
print(foo) # ['.git', '.gitignore', 'LICENSE', 'readme.MD', 'run.py']

# os.rename(original-filename, new-filename)


# stats
# modified_time = os.stat(filename).st_mtime
# print(datetime.fromtimestamp(mod_time)) # YYYY-MM-DD HH:MM:SS



# os.walk()
  # recursive, traverses the file tree top-down
  # generator, returns 3 tuples

# for dirpath, dirnames, filenames in os.walk(PATH):
#   print('current path: ', dirpath)    # /Users/coreyshafer/Desktop/
#   print('directories: ', dirnames)    # ['Demo-Folder', 'Module-OS', 'OS-Demo', 'Screenshots', 'Videos']
#   print('files: ', filenames)         # ['demo-txt']



# environment variables, os.environ
home_dir = os.environ.get('HOME')


# os.path.join()    # takes guesswork out of needing to add slash at the end of 1st variable or not
file_path = os.path.join(home_dir, 'test.txt', 'foo', 'bar')  # /Users/justinhoang/test.txt/foo/bar


funky_file = 'foobar.thing.us.txt'
print(os.path.splitext(funky_file)) # ('foobar.thing.us.txt', '.jpg')
print(funky_file.split('.'))        # ['foobar', 'thing', 'us', 'txt']
