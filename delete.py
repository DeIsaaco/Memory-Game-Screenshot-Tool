import os


i = 1
while i < 50:
    if os.path.exists(os.getcwd() + r'\Screenshots\screenshot_' + str(i) + r'.png'):
        os.remove(os.getcwd() + r'\Screenshots\screenshot_' + str(i) + r'.png')
    else:
        break
    i+=1