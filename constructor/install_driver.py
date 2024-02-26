import os
import shutil
import urllib.request
import zipfile
import subprocess
import requests
import os
import tempfile

try:
    path_variable = os.environ.get('PREFIX')

    if path_variable is None:
        print("Adjusting path to tmp")
        path_variable = os.path.join(tempfile.gettempdir(),"ImSwitchUC2")
        print(path_variable)

    try:
        os.mkdir(path_variable)
    except:
        print("Could not creae folder")
        pass
    print("Path: "+path_variable)    
except Exception as e:
    print("Something went wrong: ")
    print(e)
try:
    
    import ctypes, sys

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if 1: #is_admin():
        # Code of your program here
        try:
            # Download the driver file
            print("Downloading driver file...")
            urllib.request.urlretrieve("https://www.silabs.com/documents/public/software/CP210x_Universal_Windows_Driver.zip", os.path.join(path_variable,"usbdriver_file.zip"))
        except Exception as e:
            print(e)
        # Extract the driver file
        print("Extracting driver file...")
        with zipfile.ZipFile(os.path.join(path_variable,"usbdriver_file.zip"), "r") as zip_ref:
            zip_ref.extractall("driver")

        # Install the driver
        print("Installing driver...")
        #subprocess.call(["pnputil", "-i", "-a", "driver\silabser.inf"])
       
        command = ["pnputil", "-i", "-a", "driver\silabser.inf"]

        # Start the subprocess
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # Print each line of output as it is produced
        for line in iter(process.stdout.readline, ''):
            print(line, end='')

        # Wait for the subprocess to finish
        process.stdout.close()
        process.wait()

        # Cleanup downloaded files
        print("Cleaning up...")
        os.remove( os.path.join(path_variable,"usbdriver_file.zip"))
        shutil.rmtree("driver")

        # wait a moment to continue 
        
except Exception as e:
    print("Driver could not be downloaded: ")
    print(e)
print("Please hit enter to continue")
input()