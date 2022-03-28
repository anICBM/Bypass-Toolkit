import wx
import wx.aui
import sys

sys.path.insert(1, 'tools/')

import browser
import youtube
import wallpaper

class mainframe(wx.Frame):
    """frame"""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)

        self.notebook = wx.Notebook(self)
        self.notebook.AddPage(browser.htmlPanel(self.notebook), "browser")
        self.notebook.AddPage(youtube.youtubeDownload(self.notebook), "youtube")
        self.notebook.AddPage(wallpaper.wallpaper(self.notebook), "wallpaper")

        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    mainframe(None, 'toolkit')
    app.MainLoop()