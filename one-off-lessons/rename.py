# https://youtu.be/ve2pmm5JqmI?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7


# be in dir of files  os.chdir # /Videos

# /Videos directory
# Earth - Our Solar System - #4.mp4
# Jupiter - Our Solar System - #6.mp4
# Mars - Our Solar System - #5.mp4
# Mercury - Our Solar System - #2.mp4
# Neptune - Our Solar System - #8.mp4
# Pluto - Our Solar System - #10.mp4
# Saturn - Our Solar System - #7.mp4
# The Sun - Our Solar System - #1.mp4
# Uranus - Our Solar System - #9.mp4
# Venus - Our Solar System - #3.mp4



# input         : 'Earth - Our Solar System - #4.mp4'
# desired format: '#4-Our Solar System-Earth.mp4'

for f in os.listdir():
  # split file extension
  filename, ext = os.path.splitext(f)    # ('Earth - Our Solar System - #4', '.mp4')

  # break apart individual pieces
  title, course, num = filename.split('-')    # title='Earth', course='Our Solar System', num='#4'

  # strip whitespace
  title  =  title.strip()
  course =  course.strip()

  # remove # sign & add padding to single numbers
  # zfill(NUM), NUM = number of values desired to add padding up to, if 2: 1 -> 01
  num =  num.strip()[1:].zfill(2)

  # save in new format
  new_filename = '{}-{}-{}{}'.format(num, course, title, ext) # '#4 - Our Solar System - Earth.mp4'

  os.rename(f, new_filename)
