import tkinter as tk
import typing
from interface.styling import *


class ClientData(tk.Frame):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




        self.body_widgets = dict()  # Dictionary of dictionaries, contains all the references to the widgets in the table
        self._headers = ["Food","Amount (g)",  "Carbohydrate", "Protein", "Fat", "Calories"]
        self._table_frame = tk.Frame(self, bg=BG_COLOR)
        self._table_frame.pack(side=tk.TOP)

        self._headers_frame = tk.Frame(self._table_frame, bg=BG_COLOR)


        for idx, h in enumerate(self._headers):
            label = tk.Label(self._headers_frame, text=h.capitalize(), bg=BG_COLOR,
                              fg=FG_COLOR, font=GLOBAL_FONT, width= 12)
            label.grid(row=1, column=idx)

        self._headers_frame.pack(side=tk.TOP, anchor="nw")

        for h in self._headers:
            self.body_widgets[h] = dict()

        self._body_index = 0
