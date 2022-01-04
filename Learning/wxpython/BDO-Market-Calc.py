
import wx

class Main:

    def __init__(self):

        # ----------Set Attributes---------- #

        self.tax = .35
        self.value_pack = .30
        self.market_benefit = .05
        self.total_bonus = .005
        self.family_fame = [".5%", "1%", "1.5%"]
        self.family_bonus = .005

        # ----------Create Window/Frame/Panel---------- #

        self.app = wx.App()
        self.frame = wx.Frame(None, title="Black Desert Market Calculator", size=(700, 400),
                              style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        self.panel = wx.Panel(self.frame)

        # ----------Create Textbox---------- #
        self.entry = wx.TextCtrl(self.panel, size=(400, 40), pos=(40, 150))

        # ----------Create Button and Bindings---------- #
        self.button = wx.Button(self.panel, label="Calculate", pos=(500, 150))
        self.button.Bind(wx.EVT_BUTTON, self.on_click)

        # ----------Create Labels---------- #
        self.amount = wx.StaticText(self.panel, label="", pos=(10, 10))
        self.total_bonus_label = wx.StaticText(self.panel, label="Total Bonus: 0.5%", pos=(40, 300))
        self.family_fame_label = wx.StaticText(self.panel, label="Family Fame", pos=(500, 250))

        # ----------Create Checkboxes---------- #
        self.value_check = wx.CheckBox(self.panel, label="Value Pack", pos=(40, 250))
        self.value_check.Bind(wx.EVT_CHECKBOX, self.on_value_check)
        
        self.market_check = wx.CheckBox(self.panel, label="Market Benefit", pos=(250, 250))
        self.market_check.Bind(wx.EVT_CHECKBOX, self.on_market_check)

        # ----------Create Combobox---------- #
        self.family_box = wx.ComboBox(self.panel, choices=self.family_fame, pos=(520, 300))
        self.family_box.Bind(wx.EVT_COMBOBOX, self.on_family_select)

    # ----------Methods---------- #
    
    # ----------Market Benefit Checkbox---------- #

    def on_family_select(self, event):
        choice = self.family_box.GetValue()
        self.total_bonus -= self.family_bonus
        if choice == ".5%":
            self.family_bonus = .005
        elif choice == "1%":
            self.family_bonus = .01
        elif choice =="1.5%":
            self.family_bonus = .015
        
        self.total_bonus += self.family_bonus

        bonus = round(self.total_bonus * 100, 1)
        self.total_bonus_label.SetLabel(f"Total Bonus: {str(bonus)}%")


    # ----------Market Benefit Checkbox---------- # 
    def on_market_check(self, event):
        box = event.GetEventObject()
        setting = box.GetValue()
        if setting:
            self.total_bonus += self.market_benefit
        else:
            self.total_bonus -= self.market_benefit
        bonus = round(self.total_bonus * 100, 1)
        self.total_bonus_label.SetLabel(f"Total bonus: {str(bonus)}%")
   

    # ----------Value Pack Checkbox---------- #
    def on_value_check(self, event):
        box = event.GetEventObject()
        setting = box.GetValue()
        if setting:
            self.total_bonus += self.value_pack
        else:
            self.total_bonus -= self.value_pack
        bonus = round(self.total_bonus * 100, 1)
        self.total_bonus_label.SetLabel(f"Total bonus: {str(bonus)}%")


    # ----------Button Click Event---------- #
    def on_click(self, event):
        num = self.entry.GetValue()
        num = num.replace(",", "")
        num = float(num)
        taxed_num = float(num) * self.tax
        num -= taxed_num
        bonus = float(num) * self.total_bonus
        total = round(float(num) + bonus)
        total_ = "{:,}".format(total)

        self.amount.SetLabel(str(total_))


    def run(self):
        self.frame.Show()
        self.app.MainLoop()


app = Main()
app.run()
