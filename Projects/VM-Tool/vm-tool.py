import wx
import os
import subprocess

class Main:

    def __init__(self):

        self.path = "/mnt/game2/vms/"
        self.iso_path = "/mnt/nas1/share/iso/"
        self.file_list = []
        self.vm_list = [""]
        self.iso_list = [""]
        self.cores = "1"
        self.selected_iso = ""
        self.selected_vm = ""
        self.mem_amount = "4"

    # --Create Window/Frame/Panel
        self.app = wx.App()
        self.frame = wx.Frame(None, title="VM-Tool", size = (777, 400), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        self.panel = wx.Panel(self.frame)

        self.get_vms()
        self.get_cores()
        
    # --Create VM Img--
        
        # Static Box
        self.img_create_box = wx.StaticBox(self.panel, size=(200, 180), label="Create VM", pos=(5, 5))

        # Create Button
        self.create_button = wx.Button(self.img_create_box, label="Create", pos=(55, 100))
        self.create_button.Bind(wx.EVT_BUTTON, self.create_vm)

        # TextBoxes
        self.img_size_textbox = wx.TextCtrl(self.img_create_box, size=(50, 30), pos=(5, 5))
        self.img_name_textbox = wx.TextCtrl(self.img_create_box, size=(130, 30), pos=(5, 40))

        # Labels
        self.size_label = wx.StaticText(self.img_create_box, label="GB", pos=(65, 10))
        self.name_label = wx.StaticText(self.img_create_box, label="Name", pos=(145,45))

    # --Show VM List--
        
        # Static Box
        self.vm_list_box = wx.StaticBox(self.panel, size=(550, 180), label="VMs", pos=(220, 5))

        # Combo Box
        self.vm_list_combo = wx.ComboBox(self.vm_list_box, choices=self.vm_list, pos=(5, 5))
        self.vm_list_combo.Bind(wx.EVT_COMBOBOX, self.on_vm_select)

        self.iso_list_combo = wx.ComboBox(self.vm_list_box, choices=self.iso_list, pos=(5, 50))
        self.iso_list_combo.Bind(wx.EVT_COMBOBOX, self.on_iso_select)

        # Buttons
        self.run_button = wx.Button(self.vm_list_box, label="Run", pos=(230, 100))
        self.run_button.Bind(wx.EVT_BUTTON, self.run_vm)

        self.delete_button = wx.Button(self.vm_list_box, label="Delete", pos=(130, 100))
        self.delete_button.Bind(wx.EVT_BUTTON, self.delete_vm)

    # -- Options 
        self.options_box = wx.StaticBox(self.panel, size=(765, 200), label="Options", pos=(5, 190))

        # Combo Box
        self.core_combo = wx.ComboBox(self.options_box, choices=self.cores_list, pos=(5, 5))
        self.core_combo.Bind(wx.EVT_COMBOBOX, self.on_core_select) 

        # Labels
        self.core_label = wx.StaticText(self.options_box, label="Cores", pos=(80, 10))
        self.memory_label = wx.StaticText(self.options_box, label="Ram(GB)", pos=(195, 10))
        self.launch_options_label_1 = wx.StaticText(self.options_box, label="", pos=(10, 100))
        self.launch_options_label_2 = wx.StaticText(self.options_box, label="", pos=(10, 120))
        self.launch_options_label_3 = wx.StaticText(self.options_box, label="", pos=(10, 140))


        # Text Entry
        self.memory_entry = wx.TextCtrl(self.options_box, size=(40, 30), pos=(150, 5))

        # Test Button
        self.test_button = wx.Button(self.options_box, label="Test", pos=(5, 50))
        self.test_button.Bind(wx.EVT_BUTTON, self._testclick)


        self.update_label()

    # Methods


    def get_cores(self):
        result = subprocess.run(["nproc"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        cores = int(result.stdout)
        self.cores_list = []

        for c in range(1, cores + 1):
            self.cores_list.append(str(c))

    def _testclick(self, event):
        self.mem_amount = self.memory_entry.GetValue()
        print(f"\n\nMemory: {self.mem_amount}")
        print(f"Cores: {self.cores}")
        print(f"ISO: {self.selected_iso}")
        print(f"VM: {self.selected_vm}")

    def run_vm(self, event):
        self.mem_amount = self.memory_entry.GetValue()

        if self.selected_iso == "":
            os.system("qemu-system-x86_64 -enable-kvm -serial none -drive file=" + self.path + self.selected_vm + " -m " + self.mem_amount + 
                      "G -cpu host -smp " + self.cores + " -vga virtio -display sdl,gl=on")
        else:
            os.system("qemu-system-x86_64 -enable-kvm -serial none -cdrom " + self.iso_path + self.selected_iso + " -drive file=" + 
                       self.path + self.selected_vm + " -m " + self.mem_amount + "G -cpu host -smp " + self.cores + " -vga virtio -display sdl,gl=on")

    def on_core_select(self, event):
        self.cores = self.core_combo.GetValue()
        self.update_label()

    def update_label(self):
        if self.selected_iso == "":
            self.launch_options_label_1.SetLabel("qemu-system-x86_64 -enable-kvm -serial none -drive file=" + self.path + self.selected_vm)  
            self.launch_options_label_2.SetLabel(" -m " + self.mem_amount + "G -cpu host -smp ") 
            self.launch_options_label_3.SetLabel(self.cores + " -vga virtio -display sdl,gl=on")
        else:
            self.launch_options_label_1.SetLabel("qemu-system-x86_64 -enable-kvm -serial none -cdrom ") 
            self.launch_options_label_2.SetLabel(self.iso_path + self.selected_iso + " -drive file=")  
            self.launch_options_label_3.SetLabel(self.path + self.selected_vm + " -m " + self.mem_amount + "G -cpu host -smp " + self.cores + " -vga virtio -display sdl,gl=on")

    def on_vm_select(self, event):
        self.selected_vm = self.vm_list_combo.GetValue()
        self.update_label()

    def on_iso_select(self, event):
        self.selected_iso = self.iso_list_combo.GetValue()
        self.update_label()

    def delete_vm(self, event):
        os.system("rm " + self.path + self.selected_vm)
        self.vm_list.remove(self.selected_vm)
        self.get_vms()
        self.vm_list_combo.SetItems(self.vm_list)

    def create_vm(self, event):
        img_name = self.img_name_textbox.GetValue()
        img_size = self.img_size_textbox.GetValue()

        subprocess.run(["qemu-img", "create", "-f", "qcow2", self.path + img_name + ".img", img_size + "G"])
        self.get_vms()
        self.vm_list_combo.SetItems(self.vm_list)

   
    def get_vms(self):
        vm_list = os.listdir(self.path)
        iso_list = os.listdir(self.iso_path)

        for vms in vm_list:
            if vms not in self.vm_list and "img" in vms:
                self.vm_list.append(vms)

        for iso in iso_list:
            if iso not in self.iso_list and "iso" in iso:
                self.iso_list.append(iso)

    def get_file(self):
        self.file_list = os.listdir(self.path)
        print(self.file_list)
        

    def run(self):
        self.frame.Show()
        self.app.MainLoop()


app = Main()
app.run()



    
