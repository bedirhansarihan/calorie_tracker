import tkinter as tk
from tkinter.messagebox import askquestion
import logging
import json

from interface.client_data_component import *
from interface.nutrition_component import *
from interface.styling import *

class Root(tk.Tk):


    def __init__(self):
        super().__init__()
        self.title("Calculate Calories")


        self._base_frame= tk.Frame(self, bg=BG_COLOR)
        self._base_frame.pack(side=tk.LEFT)

        self._nutrition_frame = NutritionEditor(self._base_frame, bg= BG_COLOR)
        self._nutrition_frame.pack(side= tk.TOP, pady=15)

        self._client_data_frame = ClientData(self._base_frame, bg=BG_COLOR)
        self._client_data_frame.pack(side=tk.TOP, pady=15)
