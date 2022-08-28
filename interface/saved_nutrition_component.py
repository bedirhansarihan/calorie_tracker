import tkinter as tk
import typing
from interface.styling import *
from nutrition import Nutrition

class SavedNutrition(tk.Frame):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.widgets = dict()
        self.saved_food_data = dict()

        self._headers = ["Food","Amount (g)",  "Carbohydrate", "Protein", "Fat", "Calories"]


        self._headers_frame = tk.Frame(self, bg=BG_COLOR)
        for idx, h in enumerate(self._headers):
            label = tk.Label(self._headers_frame, text=h.capitalize(), bg=BG_COLOR,
                              fg=FG_COLOR, font=GLOBAL_FONT, width= 12)
            label.grid(row=1, column=idx)

        self._headers_frame.pack(side=tk.TOP, anchor="nw")

        self.table_frame = tk.Frame(self, bg=BG_COLOR)
        self.table_frame.pack(side=tk.TOP)


        self._params = [
            {"code_name": "food_name", "widget": tk.Label, "header": "Food Name"},
            {"code_name": "amount", "widget": tk.Label, "header": "Amount (g)"},
            {"code_name": "carbonhydrate", "widget": tk.Label, "header": "Carbohydrate"},
            {"code_name": "protein", "widget": tk.Label, "header": "Protein"},
            {"code_name": "fat", "widget": tk.Label, "header": "Fat"},
            {"code_name": "calories", "widget": tk.Label, "header": "Calories"},
        ]

        self._body_index = 0


    def update_table(self):




        for f_obj in self.saved_food_data:

            b_index = self.saved_food_data[f_obj]['index']

            if not self.saved_food_data[f_obj]['Displayed']:

                print("xx")
                # food_name
                self.widgets['food_name'][b_index] = tk.Label(self.table_frame,
                                                                                      text=f_obj.food_name,
                                                                                      bg=BG_COLOR, fg=FG_COLOR,
                                                                                      font=GLOBAL_FONT,
                                                                                      width=30, bd=1, relief=tk.FLAT)
                self.widgets['food_name'][b_index].grid(row=b_index, column=0, padx=2)

                # amount
                self.widgets['amount'][b_index] = tk.Label(self.table_frame,
                                                                                   text=f_obj.amount, bg=BG_COLOR,
                                                                                   fg=FG_COLOR, font=GLOBAL_FONT,
                                                                                   width=10, bd=1, relief=tk.FLAT)
                self.widgets['amount'][b_index].grid(row=b_index, column=1, padx=2)

                # carbonhydrate
                self.widgets['carbonhydrate'][b_index] = tk.Label(
                    self.table_frame, text=f_obj.carbonhydrate,
                    bg=BG_COLOR,
                    fg=FG_COLOR, font=GLOBAL_FONT,
                    width=10, bd=1, relief=tk.FLAT)
                self.widgets['carbonhydrate'][b_index].grid(row=b_index, column=2, padx=2)

                # protein
                self.widgets['protein'][b_index] = tk.Label(self.table_frame,
                                                                                    text=f_obj.protein, bg=BG_COLOR,
                                                                                    fg=FG_COLOR, font=GLOBAL_FONT,
                                                                                    width=10, bd=1, relief=tk.FLAT)
                self.widgets['protein'][b_index].grid(row=b_index, column=3, padx=2)

                # fat
                self.widgets['fat'][b_index] = tk.Label(self.table_frame,
                                                                                text=f_obj.fat, bg=BG_COLOR,
                                                                                fg=FG_COLOR, font=GLOBAL_FONT,
                                                                                width=10, bd=1, relief=tk.FLAT)
                self.widgets['fat'][b_index].grid(row=b_index, column=4, padx=2)

                # calories
                self.widgets['calories'][b_index] = tk.Label(self.table_frame,
                                                                                     text=f_obj.calories,
                                                                                     bg=BG_COLOR,
                                                                                     fg=FG_COLOR, font=GLOBAL_FONT,
                                                                                     width=10, bd=1, relief=tk.FLAT)
                self.widgets['calories'][b_index].grid(row=b_index, column=5, padx=2)

                self.saved_food_data[f_obj]['Displayed'] = True
                b_index += 1