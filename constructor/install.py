import os
import shutil
import urllib.request
import zipfile
import subprocess
import requests
import os
import tempfile
import ctypes, sys
import os
import pythoncom
from win32com.shell import shell, shellcon

path_variable = os.environ.get('PREFIX')

if path_variable is None:
    print("Adjusting path to tmp")
    path_variable = os.path.join(tempfile.gettempdir(),"ImSwitchUC2")
#path_variable = os.path.join("C:\\Users\\diederichbenedict\\Downloads")
#path_variable = "C:\\ProgramData\\imswitchuc
# 2"d

print("In the following we try to download ImSwitch from github and install it aloongside the necessary drivers. For this you need admin control. Please hit Enter to continue...")
input()
try:
    os.mkdir(path_variable)
except:
    pass
print("Path: "+path_variable)    
os.chdir(path_variable)
def run_as_admin(script_path):
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script_path, None, 1)

#run_as_admin(os.path.join(path_variable,"install_driver.py"))
run_as_admin(os.path.join("C:\\Users\\diederichbenedict\\Dropbox\\Dokumente\\Promotion\\PROJECTS\\ImSwitchInstaller\\constructor\\install_driver.py"))

try:
    # Set the download URL and file name
    # Specify the repository details
    owner = "openUC2"
    repo = "ImSwitch"

    # Make a request to the GitHub API to retrieve the latest commit information
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commit_info = response.json()[0]

    # Get the SHA of the latest commit
    commit_sha = commit_info["sha"]

    # Construct the download URL for the latest commit as a zip folder
    DOWNLOAD_URL = f"https://github.com/{owner}/{repo}/archive/{commit_sha}.zip"
    print("Download URL:", DOWNLOAD_URL)

    ZIP_FILE = "latestImSwitch.zip"

    # Set the installation directory
    INSTALL_DIR = "ImSwitch"

    # Download the latest release
    print("Downloading the latest release...")
    urllib.request.urlretrieve(DOWNLOAD_URL, ZIP_FILE)

    # Unzip the downloaded file
    print("Unzipping the release...")
    with zipfile.ZipFile(ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(INSTALL_DIR)
        
    
    print("changing into unzip directory:"+INSTALL_DIR)
    os.chdir(INSTALL_DIR)
    mDir = os.listdir(".")[0]
    print(mDir)
    INSTALL_PATH=os.path.join(path_variable,INSTALL_DIR,mDir)
    
    # Install the package using pip
    print("Installing the package...")
    os.chdir(INSTALL_PATH)
    #command = [os.path.join(path_variable, "python.exe"), "-m", "pip", "install", "-e", "."#]
    command = [os.path.join(path_variable, "Scripts", "pip3.exe"), "install", "-e", "."]

    # Execute the command
    #result = subprocess.run(command, capture_output=True, text=True)
    
    # Start the subprocess
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # Print each line of output as it is produced
    for line in iter(process.stdout.readline, ''):
        print(line, end='')

    # Wait for the subprocess to finish
    process.stdout.close()
    process.wait()

    # Print the output
    #print("STDOUT:", result.stdout)
    #print("STDERR:", result.stderr)

    # Check the exit code
    #if result.returncode == 0:
    #    print("Command executed successfully")
    #else:
    #    print(f"Command exited with code {result.returncode}")

    print("Installation completed successfully.")

except Exception as e:
    print("Installation of ImSwitch not succesful.")
    print(e)

# Cleanup downloaded files
print("Cleaning up...")
os.remove(os.path.join(path_variable,ZIP_FILE))

# Creating Icon/Shortcut on Desktop
shortcut_path = os.path.join(os.path.expanduser("~"), "Desktop", "ImSwitch.lnk")
icon_path = os.path.join(path_variable, "icon.ico")  # Replace with your icon path
target = os.path.join(path_variable, "python.exe"
args = "-m imswitch"

shortcut = pythoncom.CoCreateInstance(
    shell.CLSID_ShellLink,
    None,
    pythoncom.CLSCTX_INPROC_SERVER,
    shell.IID_IShellLink
)

shortcut.SetPath(target)
shortcut.SetArguments(args)
shortcut.SetIconLocation(icon_path, 0)

persist_file = shortcut.QueryInterface(pythoncom.IID_IPersistFile)
persist_file.Save(shortcut_path, 0)

print("Hit enter to continue.")
input()