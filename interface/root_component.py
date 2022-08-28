import time
import tkinter as tk
from tkinter.messagebox import askquestion
import logging
import json
import threading
from interface.saved_nutrition_component import *
from interface.nutrition_component import *
from interface.styling import *

class Root(tk.Tk):


    def __init__(self):
        super().__init__()
        self.title("Calorie Tracker")


        self._base_frame= tk.Frame(self, bg=BG_COLOR)
        self._base_frame.pack(side=tk.LEFT)

        self._nutrition_frame = NutritionEditor(self._base_frame, bg= BG_COLOR)
        self._nutrition_frame.pack(side= tk.TOP, pady=15)

        self._client_data_frame = SavedNutrition(self._base_frame, bg=BG_COLOR)
        self._client_data_frame.pack(side=tk.TOP, pady=15)

        x = threading.Thread(target=self._update)
        x.start()


    def _update(self):
        while True:
            time.sleep(1)
            try:

                self._client_data_frame.saved_food_data  = self._nutrition_frame.saved_food_data
                self._client_data_frame.update_table()

            except:

                pass





