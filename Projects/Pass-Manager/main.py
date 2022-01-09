import wx
from random import choice, randint, shuffle

class AppFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Password Manager", 
        size=(500, 600), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = AppPanel(self)
        self.Show()


class AppPanel(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        self.image = wx.Image("logo.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.logo = wx.StaticBitmap(self, -1 ,self.image)

        # Create Label
        self.website_label = wx.StaticText(self, label="Website:")
        self.username_label = wx.StaticText(self, label="Email/Username:")
        self.password_label = wx.StaticText(self, label="Password:")

        # Text Box
        self.website_entry = wx.TextCtrl(self, size=(340, 35), value="Example.com")
        self.user_name_entry = wx.TextCtrl(self, size=(340, 35))
        self.password_entry = wx.TextCtrl(self, size=(170, 35))

        # Button
        self.generate_button = wx.Button(self, label="Generate Password")
        self.generate_button.Bind(wx.EVT_BUTTON, self.generate_password)
        self.add_button = wx.Button(self, label="Add")
        self.add_button.Bind(wx.EVT_BUTTON, self.save_password)

        # Sizers
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        logo_sizer = wx.BoxSizer(wx.HORIZONTAL)
        website_sizer = wx.BoxSizer(wx.HORIZONTAL)
        user_name_sizer = wx.BoxSizer()
        password_sizer = wx.BoxSizer()
        add_button_sizer = wx.BoxSizer()

        logo_sizer.Add(self.logo, 0, wx.CENTER, border=5)

        # Sizer for Website input
        website_sizer.Add(self.website_label, 0, wx.CENTER|wx.RIGHT, border=73)
        website_sizer.Add(self.website_entry, 0, wx.CENTER, border=5)

        # Sizer for Email/Username input
        user_name_sizer.Add(self.username_label, 0, wx.CENTER|wx.RIGHT, border=17)
        user_name_sizer.Add(self.user_name_entry, 0, wx.CENTER, border=5)

        # Sizer for password entry
        password_sizer.Add(self.password_label, 0, wx.CENTER|wx.RIGHT, border=63)
        password_sizer.Add(self.password_entry, 0, wx.CENTER|wx.RIGHT, border=10)
        password_sizer.Add(self.generate_button, 0, wx.CENTER|wx.RIGHT, border=10)

        #Sizer for add Button
        add_button_sizer.Add(self.add_button, 1, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, border=5)

        # Set main sizer
        main_sizer.Add(logo_sizer, 0, wx.ALL|wx.CENTER, border=40)
        main_sizer.Add(website_sizer, 0, wx.ALL|wx.LEFT, border=5)
        main_sizer.Add(user_name_sizer, 0, wx.ALL|wx.LEFT, border=5)
        main_sizer.Add(password_sizer, 0, wx.ALL|wx.LEFT, border=5)
        main_sizer.Add(add_button_sizer, 1, wx.BOTTOM|wx.EXPAND, border=115)

        self.SetSizer(main_sizer)


    # Methods
    def save_password(self, event):
        website = self.website_entry.GetValue()
        username = self.user_name_entry.GetValue()
        password = self.password_entry.GetValue()
        if website != "" and username != "" and password != "":
            self.website_entry.Clear()
            self.user_name_entry.Clear()
            self.password_entry.Clear()

            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")


    def generate_password(self, event):
        self.password_entry.Clear()
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
                'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '*', '+', '(', ')']

        password_letters = [choice(letters) for x in range(randint(8, 10))]
        password_numberes = [choice(numbers) for x in range(randint(2, 4))]
        password_symbols = [choice(symbols) for x in range(randint(2, 4))]
        password_list = password_letters + password_numberes + password_symbols
        shuffle(password_list)
        password = ''.join(password_list)
        self.password_entry.SetValue(password)



if __name__ == "__main__":
    app = wx.App()
    frame = AppFrame()
    app.MainLoop()
