echo Added by test-install script > "%PREFIX%\test_install_sentinel.txt"
SetLocal EnableDelayedExpansion

set PREFIX=C:\ProgramData\imswitchuc2
echo %PREFIX%

REM Download the driver file
echo Downloading driver file and install ImSwitch...

echo "%PREFIX%\Scripts\activate.bat"

call "%PREFIX%\Scripts\activate.bat"
python "%PREFIX%\install.py"

@ECHO ON
call "%PREFIX%\Scripts\activate.bat
conda info || exit 1
conda config --show-sources || exit 1
conda config --show --json | python -c "import sys, json; info = json.loads(sys.stdin.read()); assert 'conda-forge' in info['channels'], info
python %$PREFIX/%install.py"