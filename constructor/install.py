import os
import shutil
import urllib.request
import zipfile
import subprocess
import requests
import os
import tempfile

path_variable = os.environ.get('PREFIX')

#path_variable = os.path.join(tempfile.gettempdir(),"ImSwitchUC2")
#path_variable = os.path.join("C:\\Users\\diederichbenedict\\Downloads")
#path_variable = "C:\\ProgramData\\imswitchuc
# 2"d
try:
    os.mkdir(path_variable)
except:
    pass
print("Path: "+path_variable)    
os.chdir(path_variable)
try:
    
    # Download the driver file
    print("Downloading driver file...")
    urllib.request.urlretrieve("https://www.silabs.com/documents/public/software/CP210x_Universal_Windows_Driver.zip", os.path.join(path_variable,"driver_file.zip"))

    # Extract the driver file
    print("Extracting driver file...")
    with zipfile.ZipFile("driver_file.zip", "r") as zip_ref:
        zip_ref.extractall("driver")

    # Install the driver
    print("Installing driver...")
    subprocess.call(["pnputil", "-i", "-a", "driver\silabser.inf"])

    # Cleanup downloaded files
    print("Cleaning up...")
    os.remove("driver_file.zip")
    shutil.rmtree("driver")

except Exception as e:
    print("Driver could not be downloaded: ")
    print(e)

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

    ZIP_FILE = "latest.zip"

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
    command = [os.path.join(path_variable, "python.exe"), "-m", "pip", "install", "-e", ".", "--user"]

    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the output
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    # Check the exit code
    if result.returncode == 0:
        print("Command executed successfully")
    else:
        print(f"Command exited with code {result.returncode}")

    print("Installation completed successfully.")

except Exception as e:
    print("Installation of ImSwitch not succesful.")
    print(e)