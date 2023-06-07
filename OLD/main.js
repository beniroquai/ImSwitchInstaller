const { app, BrowserWindow } = require('electron');
const path = require('path');

const os = require('os')
const HOME = os.homedir()
const InstallDir = path.join(HOME, "ImSwitchDownload")
const WorkspaceDir = path.join(HOME, "ImSwitchWorkspace")

const https = require('https');
const fs = require('fs');


let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({ width: 800, height: 600 });

  mainWindow.webContents.openDevTools()
  mainWindow.loadFile(path.join(__dirname, 'index.html'));

  mainWindow.on('closed', function () {
    mainWindow = null;
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow();
  }
});





const MINICONDA_URL = 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh';
const MINICONDA_FILE = 'Miniconda3-latest-Linux-x86_64.sh';

function downloadMiniconda() {
    return new Promise((resolve, reject)=>{
    fs.mkdirSync(InstallDir);
    const InstallerPath = path.join(InstallDir, 'Miniconda_Install.sh')
    download("https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh", InstallerPath)
    })
}

