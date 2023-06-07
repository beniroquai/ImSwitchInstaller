/**
 * This file is loaded via the <script> tag in the index.html file and will
 * be executed in the renderer process for that window. No Node.js APIs are
 * available in this process because `nodeIntegration` is turned off and
 * `contextIsolation` is turned on. Use the contextBridge API in `preload.js`
 * to expose Node.js functionality from the main process.
 */


/*
  const file = fs.createWriteStream(MINICONDA_FILE);
  https.get(MINICONDA_URL, response => {
    response.pipe(file);
    file.on('finish', () => {
      file.close();
      console.log(`Downloaded ${MINICONDA_FILE}`);
    });
  }).on('error', error => {
    fs.unlink(MINICONDA_FILE);
    console.error(`Error downloading ${MINICONDA_FILE}: ${error.message}`);
  });
  */
// Add an event listener to the download button
const downloadButton = document.getElementById('download-button');
downloadButton.addEventListener('click', downloadMiniconda);
