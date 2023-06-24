echo Added by test-install script > "%PREFIX%\test_install_sentinel.txt"
SetLocal EnableDelayedExpansion


REM Download the driver file
echo Downloading driver file and install ImSwitch...


call "%PREFIX%\Scripts\activate.bat"
python "%PREFIX%\install.py"

