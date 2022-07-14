import sys
import time 
import random 

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 

from_dir=""
to_dir=""

dir_tree = {
      "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

#event handler class 
class FileMovementHandler(FileSystemEventHandler):

    def on_created(self,event):

        name ,extention=os.path.splitext(event.src_path)

        time.sleep(1)

        if extension in value:
            
            file_name = os.path.basename(event.src_path)
            print("downloaded" + file_name )

            path1 = from_dir + '/' + file_name
            path2 = to_dir + '/' + key
            path3 = to_dir + '/' + key + '/' + file_name

            if os.path.exists(path2):
                
                print("directory exist")
                print("Moving" + file_name + "....")
                shutil.move(path1,path3)
                time.sleep(1)

            else:

                print("making directory")
                os.makedirs(path2)
                print("Moving" + file_name + "....")
                shutil.move(path1,path3)
                time.sleep(1)


#Intialize event handler class            
event_handler = FileMovementHandler()

#initializing observer 
observer = Observer()

#schediling the observer 
observer.schedule(event_handler,from_dir,recursive = True)

#start the observer 
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except keyboardInterrupt:
    print("stopped")
    observer.stop()


