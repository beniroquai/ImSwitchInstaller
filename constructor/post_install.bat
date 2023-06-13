@echo off

REM Download the driver file
echo Downloading driver file...
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://www.silabs.com/documents/public/software/CP210x_Universal_Windows_Driver.zip', 'driver_file.zip')"

REM Extract the driver file
echo Extracting driver file...
powershell -Command "Expand-Archive -Path 'driver_file.zip' -DestinationPath 'driver' -Force"

REM Install the driver
echo Installing driver...
pnputil -i -a driver\silabser.inf

REM Cleanup downloaded files
echo Cleaning up...
del driver_file.zip
rd /s /q driver

conda activate "$PREFIX"

REM Set the download URL and file name
set "DOWNLOAD_URL=https://github.com/openUC2/ImSwitch/archive/refs/tags/v1.2.15.zip"
set "ZIP_FILE=latest.zip"

REM Set the installation directory
set "INSTALL_DIR=ImSwitch"

REM Download the latest release
echo Downloading the latest release...
curl -L -o "%ZIP_FILE%" "%DOWNLOAD_URL%"

REM Unzip the downloaded file
echo Unzipping the release...
powershell -Command "Expand-Archive -Path '%ZIP_FILE%' -DestinationPath '%INSTALL_DIR%' -Force"

REM Install the package using pip
echo Installing the package...
cd "%INSTALL_DIR%"
pip install -e . 

echo Installation completed successfully.

