"""
Mavzu: Python tashqi kutubxonasi. Pypi.org
Muallif: Uktam Turgunov
Sana: 2025-07-01
Mavzu: wxPython moduli

📚 Asosiy tushunchalar
   Termin	                Tavsif
🔷 wx.App	                Ilova (dastur) konteyneri, GUI ishga tushiradi.
🔷 wx.Frame	              Asosiy oyna (Window).
🔷 wx.Panel	              Oynaning ichidagi ishchi panel.
🔷 wx.Button	            Tugma vidjeti.
🔷 wx.TextCtrl	          Matn kiritish qutisi.
🔷 wx.StaticText	        Fiksatsiyalangan matn ko‘rsatish.
🔷 wx.CheckBox	          Belgilash qutisi.
🔷 wx.RadioButton	        Radio tugma.
🔷 wx.ComboBox	          Tanlash uchun drop-down ro‘yxat.
🔷 wx.ListBox	            Ro‘yxat oynasi.
🔷 wx.Slider	            Slider (suriluvchi o‘lchov).
"""


# Misollar
import wx

# 📝 1: Salom, Oyna!


def example_1():
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Salom, wxPython!")
    frame.Show()
    app.MainLoop()

# 📝 2: Tugmali oyna


class Example2(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Tugmali oyna')
        panel = wx.Panel(self)
        button = wx.Button(panel, label='Meni bos!', pos=(100, 50))
        button.Bind(wx.EVT_BUTTON, self.on_click)

    def on_click(self, event):
        wx.MessageBox("Tugma bosildi!", "Xabar", wx.OK | wx.ICON_INFORMATION)


def example_2():
    app = wx.App(False)
    frame = Example2()
    frame.Show()
    app.MainLoop()

# 📝 3: Matn kiritish va chiqarish


class Example3(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Matn kiritish')
        panel = wx.Panel(self)

        wx.StaticText(panel, label="Ismingiz:", pos=(10, 10))
        self.text_ctrl = wx.TextCtrl(panel, pos=(80, 10))

        button = wx.Button(panel, label='Ko‘rsat', pos=(80, 40))
        button.Bind(wx.EVT_BUTTON, self.on_click)

    def on_click(self, event):
        name = self.text_ctrl.GetValue()
        wx.MessageBox(f"Salom, {name}!", "Xabar", wx.OK | wx.ICON_INFORMATION)


def example_3():
    app = wx.App(False)
    frame = Example3()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    print("wxPython misollari:")
    print("1 - Salom, Oyna")
    print("2 - Tugmali oyna")
    print("3 - Matn kiritish va chiqarish")
    choice = input("Qaysi misolni ishga tushiraylik (1/2/3)? ")

    if choice == "1":
        example_1()
    elif choice == "2":
        example_2()
    elif choice == "3":
        example_3()
    else:
        print("Noto‘g‘ri tanlov!")


'''
🎨 Foydali vidjetlar:

Vidjet	          Tavsif
---------------------------
wx.Button	        Tugma
wx.TextCtrl	      Matn kiritish qutisi
wx.StaticText	    Fiksatsiyalangan matn
wx.CheckBox	      Belgilash oynasi
wx.RadioButton	  Radio tugmalar
wx.ComboBox	      Drop-down ro‘yxat
wx.ListBox	      List qutisi
wx.Slider	        Slider
'''

'''
📒 Qisqa maslahatlar:
🔹 Dastur doim wx.App() va MainLoop() bilan ishlaydi.
🔹 Oyna ichida barcha elementlar wx.Panel ustida joylashadi.
🔹 Har bir vidjetni Bind bilan hodisaga (event) bog‘lang.

🚀 Mashq uchun g‘oyalar:
✅ Foydalanuvchidan 2 son so‘rab, ularni qo‘shib natijani chiqaradigan kalkulyator oynasi.
✅ Rang tanlash oynasi (wx.ColourDialog).
✅ Fayl tanlash oynasi (wx.FileDialog).


'''

# 4: CheckBox va RadioButton


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="CheckBox & RadioButton")
        panel = wx.Panel(self)

        self.cb = wx.CheckBox(panel, label="Roziman", pos=(10, 10))
        self.rb1 = wx.RadioButton(panel, label="Variant 1", pos=(10, 40))
        self.rb2 = wx.RadioButton(panel, label="Variant 2", pos=(10, 70))

        button = wx.Button(panel, label="Tekshir", pos=(10, 100))
        button.Bind(wx.EVT_BUTTON, self.on_click)

    def on_click(self, event):
        msg = ""
        if self.cb.GetValue():
            msg += "CheckBox: belgilangan\n"
        if self.rb1.GetValue():
            msg += "Radio: Variant 1\n"
        elif self.rb2.GetValue():
            msg += "Radio: Variant 2\n"
        wx.MessageBox(msg)


app = wx.App(False)
frame = MyFrame()
frame.Show()
app.MainLoop()

# 5: Fayl ochish dialogi


app = wx.App(False)
frame = wx.Frame(None, title="Fayl tanlash")
dlg = wx.FileDialog(frame, "Fayl tanlang", wildcard="Barcha fayllar (*.*)|*.*")
if dlg.ShowModal() == wx.ID_OK:
    path = dlg.GetPath()
    wx.MessageBox(f"Siz tanlagan fayl:\n{path}")
dlg.Destroy()
frame.Destroy()

# 6: Rang tanlash dialogi


app = wx.App(False)
frame = wx.Frame(None, title="Rang tanlash")
dlg = wx.ColourDialog(frame)
if dlg.ShowModal() == wx.ID_OK:
    color = dlg.GetColourData().GetColour()
    wx.MessageBox(f"Tanlangan rang: {color}")
dlg.Destroy()
frame.Destroy()
