import wx
from concurrent import futures
import requests
import os, subprocess



thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)

PROTON_GE_DIRECTORY = os.path.expanduser("~/.steam/root/compatibilitytools.d/")
PROTON_GE_RELEASES = ("https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases")

path_exist = os.path.isdir(PROTON_GE_DIRECTORY)

if (path_exist == False):
    os.mkdir(PROTON_GE_DIRECTORY)

class Main:

    def __init__(self):

        self.installed_proton_list = []        
        self.missing_proton_list = []
        self.missing_proton_index_list = []
        self.filename = ""
        self.selected = 0

        self.response = requests.get(PROTON_GE_RELEASES).json()

        self.app = wx.App()
        self.frame = wx.Frame(
            None,
            title = "Proton-GE Manager",
            size = (700, 600),
            style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER)
        )
        self.panel = wx.Panel(self.frame)


        # Installed 
        self.installed_staticbox = wx.StaticBox(self.frame, label="Installed", pos=(93, 20), size=(250, 300))
        self.installed_proton = wx.ListBox(self.installed_staticbox, size=(250, 200), choices=self.installed_proton_list)
        self.delete_button = wx.Button(self.installed_staticbox, pos=(85, 230), size=(80, 40), label="Delete")
        self.delete_button.Bind(wx.EVT_BUTTON, self.remove)

        #Not Installed
        self.missing_staticbox = wx.StaticBox(self.frame, label="Missing", pos=(353, 20), size=(250, 300))
        self.missing_proton = wx.ListBox(self.missing_staticbox, size=(250, 200), choices=self.missing_proton_list)
        self.download_button = wx.Button(self.missing_staticbox, label="Install", pos=(85, 230), size=(80,40))
        self.download_button.Bind(wx.EVT_BUTTON, self.on_install)

        # Status
        self.status_staticbox = wx.StaticBox(self.frame, label="Status", pos=(93, 330), size=(510, 150))
        self.status_text = wx.TextCtrl(self.status_staticbox, size=(510, 150), style=wx.TE_MULTILINE|wx.TE_READONLY)

        self.update_listbox()

    def update_listbox(self):
        self.missing_proton_index_list = []
        self.missing_proton_list = []
        self.installed_proton_list = []

        self.installed_proton_list = os.listdir(PROTON_GE_DIRECTORY)
        self.installed_proton_list.sort(reverse=True)

        for i in range(10):
            if self.response[i]["tag_name"] not in self.installed_proton_list:
                self.missing_proton_list.append(self.response[i]["tag_name"])
                self.missing_proton_index_list.append(i)

        self.missing_proton.Clear()
        self.missing_proton.Append(self.missing_proton_list)
        self.installed_proton.Clear()
        self.installed_proton.Append(self.installed_proton_list)

    def on_install(self, event):
        self.download_button.Disable()
        self.selected = self.missing_proton.GetSelection()
        self.filename = self.missing_proton_list[self.selected] + ".tar.gz"
        self.update_status(f"Downloading {self.filename}")
        thread_pool_executor.submit(self.download)   

    def download(self):
        download_url = self.response[self.missing_proton_index_list[self.selected]]["assets"][1]["browser_download_url"]
        file = requests.get(download_url, stream=True)

        with open(self.filename, 'wb') as downloaded_file:
            for chunk in file.iter_content(chunk_size=1024):
                downloaded_file.write(chunk)
        
        wx.CallAfter(self.after_download)

    def after_download(self):
        self.update_status("Download complete...")
        self.update_status(f"Installing to {PROTON_GE_DIRECTORY}")

        thread_pool_executor.submit(self.extract)

    def extract(self):
        subprocess.run(["tar", "-xf", self.filename, "-C", PROTON_GE_DIRECTORY])
        wx.CallAfter(self.cleanup)

    def cleanup(self):
        self.update_status("Installation complete...")
        self.update_status(f"Removing {self.filename}")
        subprocess.run(["rm", self.filename])
        self.update_status("Done")

        self.update_listbox()

        self.download_button.Enable()

    def update_status(self, text):
        self.status_text.AppendText(text + '\n')

    def remove(self, event):
        self.delete_button.Disable()
        selected = self.installed_proton.GetSelection()
        filename = self.installed_proton_list[selected] 
        self.update_status(f"Removing {filename}")
        subprocess.run(["rm", "-rf", PROTON_GE_DIRECTORY + filename])
        self.update_status(f"{filename} removed")

        self.update_listbox()

        self.delete_button.Enable()

    def run(self):
        self.frame.Show()
        self.app.MainLoop()

if __name__ == "__main__":
    app = Main()
    app.run()

    