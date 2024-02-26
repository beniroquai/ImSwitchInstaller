import os
import requests
import urllib.request
import zipfile
import subprocess
import time

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

# If INSTALL_DIR already exists, rename it with a timestamp
if os.path.exists(INSTALL_DIR):
    os.rename(INSTALL_DIR, f"{INSTALL_DIR}_old_{int(time.time())}")

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
INSTALL_PATH=os.path.join(os.getcwd(), mDir)

# Install the package using pip
print("Installing the package...")
os.chdir(INSTALL_PATH)
command = ["pip", "install", "-e", ".", "--no-cache-dir", "--force-reinstall", "--user"]

# Start the subprocess
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

# Print each line of output as it is produced
for line in iter(process.stdout.readline, ''):
    print(line, end='')

# Wait for the subprocess to finish
process.stdout.close()
process.wait()

print("Installation completed successfully.")
