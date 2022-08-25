import wx
import wx.html2
import urllib.parse
import urllib.request
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

class htmlPanel(wx.Panel):
    """html panel"""
    def __init__(self, frame):
        self.htmlVal = ''
        wx.Panel.__init__(self, frame)

        self.searchBar = wx.TextCtrl(self)
        self.searchButton = wx.Button(self, wx.ID_ANY, "search")

        self.topSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.topSizer.Add(self.searchBar, 1)
        self.topSizer.Add(self.searchButton, 0)
        self.mainSizer.Add(self.topSizer, 0, wx.EXPAND)
        try:
            self.html = wx.html2.WebView.New(self, backend = wx.html2.WebViewBackendEdge)
            self.mainSizer.Add(self.html, 1, wx.EXPAND)
        except:
            self.html = wx.html2.WebView.New(self)
            self.mainSizer.Add(self.html, 1, wx.EXPAND)

        self.SetSizer(self.mainSizer)
        self.SetAutoLayout(1)

        self.Bind(wx.EVT_BUTTON, self.onSearch, self.searchButton)

        self.html.LoadURL("file://" + os.path.join(os.getcwd(), 'homepage.html'))

        self.Show()

    def onSearch(self, event):
        self.search(self.searchBar.GetValue())
    
    def search(self, urlName):
        # Urlencode the URL
        url = urllib.parse.quote_plus(urlName) 
        if(urlName != ''):
            query = "https://api.scraperbox.com/scrape"
            query += "?token=%s" % "your key"
            query += "&url=%s" % url

            # Call the API.
            request = urllib.request.Request(query)
            raw_response = urllib.request.urlopen(request).read()
            html = raw_response.decode("utf-8")
            print(html)
    
            with open('cache.html', 'wb') as out:
                out.write(html.encode("utf-8"))
                
                self.load('file://' + os.path.join(os.getcwd(), 'cache.html'))

    def load(self, page):
        self.html.LoadURL(page)
        file = open(page.replace('file://', ''), 'r')
        self.htmlVal = file.read()
        file.close()

if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None, title="browser")
    pannel = htmlPanel(frame)
    frame.Show()
    app.MainLoop()
