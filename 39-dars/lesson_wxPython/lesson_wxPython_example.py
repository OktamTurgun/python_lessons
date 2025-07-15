# 📋 wxPython ishchi misol

import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='wxPython Darsi', size=(300, 200))
        panel = wx.Panel(self)

        # StaticText
        wx.StaticText(panel, label="Ismingiz:", pos=(10, 10))

        # TextCtrl
        self.text_ctrl = wx.TextCtrl(panel, pos=(80, 10))

        # Button
        button = wx.Button(panel, label='Ko‘rsat', pos=(80, 50))
        button.Bind(wx.EVT_BUTTON, self.on_click)

    def on_click(self, event):
        name = self.text_ctrl.GetValue()
        wx.MessageBox(f"Salom, {name}!", "Xabar", wx.OK | wx.ICON_INFORMATION)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
