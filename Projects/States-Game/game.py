import wx, pandas, random, time

class Game:

    def __init__(self):
        self.button_counter = 0
        self.states_list = []

        # These are just for fun coords for the button
        self.button_x = 150
        self.button_y = 10

        # Get data from CSV and convert to a dict
        self.data = pandas.read_csv("50_states.csv").to_dict()

        # Setup Frame/Panel
        self.app = wx.App()
        self.frame = wx.Frame(None, title="Enter all the states", size=(700, 600))
        self.panel = wx.Panel(self.frame)

        # Setup Image
        self.image = wx.Bitmap("blank_states_img.gif")

        # Create a text box
        self.text_box = wx.TextCtrl(self.panel, size=(230, 30), pos=(230, 510), style=wx.TE_PROCESS_ENTER)
        self.text_box.Bind(wx.EVT_TEXT_ENTER, self.on_enter)

        # Create score lable
        self.score_label = wx.StaticText(self.panel, label="Score: 0/50", pos=(110, 517))

        # Create a button
        self.button = wx.Button(self.panel, label="Ok", pos=(480, 507))
        self.button.Bind(wx.EVT_BUTTON, self.on_click)

        self.display_image("", pos_x=300, pos_y=400)

    def display_image(self, text, pos_x, pos_y):
        self.device_control = wx.MemoryDC(self.image)
        self.device_control.DrawText(text, pos_x, pos_y)
        del self.device_control
        control = wx.StaticBitmap(self.panel, -1, self.image)

    def on_click(self, event):
        button_text = ["I don't do anything. Just hit enter, good luck with your game.",
                       "Maybe you didn't hear me. I Don't have a function. You don't need to click me.",
                       "You will have a better experience with the enter key. Now stop bothering me."]
        angry_text = ["I warned you!!!!", "Why didn't you listen?!", "HAHAHAHAH!!!!", "Try to play now"]
        
        if self.button_counter > 2:
             for x in range(200):
                random_x = random.randint(0, 700)
                random_y = random.randint(0, 600)
                random_list_num = random.randint(0, 3)       
                self.display_image(angry_text[random_list_num], pos_x=random_x, pos_y=random_y)
        else:
            self.display_image(button_text[self.button_counter], self.button_x, self.button_y)
            self.button_y += 15
            self.button_counter += 1

    def on_enter(self, event):
        text_input = self.text_box.GetValue().lower()
        x_cord = 0
        y_cord = 0
        
        # Enumerate to get the x, y keys from the dictionary
        for index, state in enumerate(self.data['state']):

            if self.data['state'][state].lower() == text_input:
                x_cord = self.data['x'][index]
                y_cord = self.data['y'][index]
                text = self.data['state'][state]

                if self.data['state'][state] not in self.states_list:
                    self.states_list.append(self.data['state'][state])
                    self.text_box.Clear()
                    self.display_image(text, pos_x = x_cord, pos_y = y_cord)
                    self.update_score()

    def update_score(self):
        self.score_label.SetLabel(f"Score: {len(self.states_list)}/50")

    def run(self):
        self.frame.Show()
        self.app.MainLoop()
    
app = Game()
app.run()