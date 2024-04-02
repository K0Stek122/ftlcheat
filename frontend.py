#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu

import main as ftl

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "pygubu_ui.ui"


class FtlcheatFrontend:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: ttk.Frame = builder.get_object("main_frame", master)

        self.val: tk.IntVar = None
        self.invincibility_var: tk.IntVar = None
        self.superweapons_var: tk.IntVar = None
        self.var_infinite_drones: tk.IntVar = None
        builder.import_variables(self)

        builder.connect_callbacks(self)

        root.title("FTLCheat")

    def run(self):
        self.mainwindow.mainloop()

    def e_set_scrap(self):
        ftl.set_scrap(self.val.get())

    def e_set_hull(self):
        ftl.set_hull(self.val.get())

    def e_set_fuel(self):
        ftl.set_fuel(self.val.get())

    def e_set_missiles(self):
        ftl.set_missiles(self.val.get())

    def e_heal_crew(self):
        try:
            for i in range(0x0, ftl.get_crew_count() * 0x4, 0x4):
                ftl.set_health(ftl.get_entity_at(i), 100.0)
        except:
            pass

    def e_kill_enemy(self):
        try:
            for i in range(ftl.get_crew_count(), 0xC8):
                ftl.set_health(ftl.get_entity_at(i), 0.0)
        except:
            pass
    
    def e_invincibility(self):
        while self.invincibility_var.get() == 1:
            ftl.set_hull(30)
            root.update()

    def e_superweapons(self):
        while self.superweapons_var.get() == 1:
            try:
                for i in range(0, 4):
                    ftl.set_weapon_status(ftl.get_weapon_at(i), 1)
            except:
                pass
            root.update()
    
    def e_infinite_drones(self):
        if self.var_infinite_drones.get() == 1:
            ftl.disable_drone_part_subtract_instr()
        else:
            ftl.enable_drone_part_subtract_instr()

if __name__ == "__main__":
    root = tk.Tk()
    app = FtlcheatFrontend(root)
    app.run()

