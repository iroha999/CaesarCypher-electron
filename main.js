const { app, BrowserWindow } = require('electron')
const path = require('path')
const url = require('url')
const child_process = require('child_process')

let win

function createWindow () {
  win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    }
  })

  win.loadURL(url.format({
    pathname: 'localhost:5000',
    protocol: 'http:',
    slashes: true
  }))
}

app.on('ready', () => {
  child_process.spawn('python', ['app.py'])

  createWindow()

  win.on('closed', () => {
    win = null
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (win === null) {
    createWindow()
  }
})