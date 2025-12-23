import shutil
import webbrowser
import os
import time
os.system('git clone https://github.com/moaad77/gemi_js_py.git')
os.chdir('gemi_js_py')

webbrowser.open('index.html')
os.chdir('..')
time.sleep(16)
shutil.rmtree('gemi_js_py')

