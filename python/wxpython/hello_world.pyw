import wx
# pip install wxpython

app = wx.App()

frame = wx.Frame(parent=None, title='Hello wxPython')
frame.Show()

app.MainLoop()