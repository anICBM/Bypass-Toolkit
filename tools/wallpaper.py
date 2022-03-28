import wx
import ctypes
import os

class wallpaper(wx.Panel):
    """change wallpaper"""
    def __init__(self, frame):
         
        wx.Panel.__init__(self, frame)

        self.entry = wx.TextCtrl(self)
        self.open = wx.Button(self, wx.ID_OPEN, "Open")
        self.change = wx.Button(self, wx.ID_OK, "Change wallpaper")

        self.img = wx.Image("default.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.static = wx.StaticBitmap(self, bitmap=self.img)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.entrySizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.entrySizer.Add(self.entry, 1, wx.EXPAND)
        self.entrySizer.Add(self.open, 0, wx.EXPAND)
        self.entrySizer.Add(self.change, 0, wx.EXPAND)
        self.mainSizer.Add(self.entrySizer, 0, wx.EXPAND)
        self.mainSizer.Add(self.static, 0, wx.EXPAND)

        self.SetSizer(self.mainSizer)
        self.SetAutoLayout(1)

        self.Bind(wx.EVT_TEXT, self.onChange, self.entry)
        self.Bind(wx.EVT_BUTTON, self.onSetDesktop, self.change)
        self.Bind(wx.EVT_BUTTON, self.onOpen, self.open)

        self.Show()

    def onChange(self, event):
        text = self.entry.GetValue() 
        if(os.path.exists(text) and '.' in text):
            temp = wx.Image(text, wx.BITMAP_TYPE_ANY)
            temp = temp.Scale(1000, 1000).ConvertToBitmap()
            self.static.SetBitmap(temp)

    def onSetDesktop(self, event):
        text = self.entry.GetValue()
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, text, 0)
        except:
            print('oof')
 
    def onOpen(self, event):
        self.dirName = ''
        openBox = wx.FileDialog(self, 'choose a file', self.dirName, "", "*.*", wx.FD_OPEN)
        if openBox.ShowModal() == wx.ID_OK:
            self.fileName = openBox.GetFilename()
            self.dirName = openBox.GetDirectory()
            f = os.path.join(self.dirName, self.fileName)
            self.entry.SetValue(f)
        openBox.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None)
    pannel = wallpaper(frame)
    frame.Show()
    app.MainLoop()