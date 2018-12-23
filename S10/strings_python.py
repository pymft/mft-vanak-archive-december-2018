text = """all work and no play makes Jack a dull boy!
all work and no play makes Jack a dull boy!all work and no play makes Jack a dull boy!
all work and no play makes Jack a dull boy!all work and no play makes Jack a dull boy!
all work and no play makes Jack a dull boy!all work and no play makes Jack a dull boy!
all work and no play makes Jack a dull boy!all work and no play makes Jack a dull boy!
all work and no play makes Jack a dull boy!"""

# split
# replace
#

start = 0
while True:
    start = text.find("Jack", start)
    if start == -1:
        break
    print (start)
    start += 1
