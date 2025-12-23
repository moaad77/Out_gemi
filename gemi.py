import webbrowser
import os
import time
os.system('git clone https://github.com/moaad77/gemi_js_py.git')
os.chdir('gemi_js_py')
webbrowser.open('index.html')
#input('ENTER')
time.sleep(2)
os.remove('index.html')
os.chdir('..')
os.remove('gemi.py')





