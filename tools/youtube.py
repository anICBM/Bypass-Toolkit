import wx
import requests
import json

class youtubeDownload(wx.Panel):
    """"youtube downloader"""
    def __init__(self, frame):

        wx.Panel.__init__(self, frame)

        self.out = wx.TextCtrl(self, style = wx.TE_MULTILINE | wx.TE_READONLY)

        self.searchBar = wx.TextCtrl(self)
        self.searchButton = wx.Button(self, wx.ID_ANY, "search")

        self.topSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.topSizer.Add(self.searchBar, 1)
        self.topSizer.Add(self.searchButton, 0)
        self.mainSizer.Add(self.topSizer, 0, wx.EXPAND)
        self.mainSizer.Add(self.out, 1, wx.EXPAND)
        self.SetSizer(self.mainSizer)
        self.SetAutoLayout(1)

        self.Bind(wx.EVT_BUTTON, self.onSearch, self.searchButton)

        self.Show()

    def search(self, id):

        url = "https://youtube-downloader9.p.rapidapi.com/CiGnubZC5cs/videoandaudio"

        headers = {
            'x-rapidapi-host': "youtube-downloader9.p.rapidapi.com",
            'x-rapidapi-key': "your key"
            }

        response = requests.request("GET", url, headers=headers)

        converted = json.loads(response.content)
        self.out.SetValue(converted[0]['url'] + '\n\n' + self.out.GetValue()) 

    def onSearch(self, event):
        self.search(self.searchBar.GetValue())

if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None, title="youtube")
    pannel = youtubeDownload(frame)
    frame.Show()
    app.MainLoop()
