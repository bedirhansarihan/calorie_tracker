import tkinter as tk
import typing
from interface.styling import *
from database import *

class NutritionEditor(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.db = Database('food.db')

        self._commands_frame = tk.Frame(self, bg=BG_COLOR)
        self._commands_frame.pack(side=tk.TOP)

        self._table_frame = tk.Frame(self, bg=BG_COLOR)
        self._table_frame.pack(side=tk.TOP)

        self._add_button = tk.Button(self._commands_frame, text="Add Nutrition", font=GLOBAL_FONT,
                                     command= self.add_nutrition, bg=BG_COLOR_2, fg=FG_COLOR)
        self._add_button.pack(side=tk.TOP)

        self.body_widgets = dict()

        self._headers_frame = tk.Frame(self._table_frame, bg=BG_COLOR)

        self._base_params = [
            {"code_name": "food_name", "widget": tk.Entry,  "width": 10, "header": "Food Name"},
            {"code_name": "amount", "widget": tk.Entry, "width": 10, "header": "Amount (g)"},
            {"code_name": "search", "widget": tk.Button, "text": "Search",
             "bg": "darkred", "command": self._show_nutritions, "header": "", "width": 8},

        ]

        for h in self._base_params:
            self.body_widgets[h['code_name']] = dict()

        self._body_index = 1
    def add_nutrition(self):

        self._popup_window = tk.Toplevel(self)
        self._popup_window.wm_title("Add Food")
        self._popup_window.config(bg=BG_COLOR)
        self._popup_window.attributes("-topmost", "true")
        self._popup_window.grab_set()
        self._popup_window.geometry("1000x450")

        self._entry_frame = tk.Frame(self._popup_window, bg= BG_COLOR)
        self._entry_frame.pack(side= tk.TOP)

        self._result_frame = tk.Frame(self._popup_window, bg=BG_COLOR)
        self._result_frame.pack(side= tk.TOP)
        # For header
        for idx, h in enumerate(self._base_params):
            header = tk.Label(self._entry_frame, text=h['header'], bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT,
                              width=h['width'], bd=1, relief=tk.FLAT)
            header.grid(row=0, column=idx, padx=15)



        # For other widgets
        b_index = self._body_index
        for col, base_param in enumerate(self._base_params):
            code_name = base_param['code_name']

            if base_param['widget'] == tk.Entry:
                self.body_widgets[code_name]['widget'] = tk.Entry(self._entry_frame, justify=tk.CENTER,
                                                                 bg=BG_COLOR_2, fg=FG_COLOR,
                                                                     font=GLOBAL_FONT, bd=1, width=base_param['width'])
            elif base_param['widget'] == tk.Button:
                self.body_widgets[code_name]['widget'] = tk.Button(self._entry_frame, text=base_param['text'],
                                                                  bg=base_param['bg'], fg=FG_COLOR, font=GLOBAL_FONT,
                                                                  width=base_param['width'],
                                                                  command=lambda frozen_command=base_param[
                                                                      'command']: frozen_command(self.body_widgets['food_name']['widget'].get()))
            else:
                continue

            self.body_widgets[code_name]['widget'].grid(row=b_index, column=col, padx=2)




        #
        # #
        # validation_button = tk.Button(self._popup_window, text="Validate", bg=BG_COLOR_2, fg=FG_COLOR,
        #                               command=lambda: self._validate_parameters(b_index))
        # validation_button.grid(row=row_nb, column=0, columnspan=2)


    def _show_nutritions(self, food_name):
        b_index = 1

        food_data: typing.List[tuple] = self.db.get_data(food_name)  # (food_name, amount, carb, protein, fat, calories)
        self.label_widgets = {}

        self._params = [
                {"code_name": "food_name", "widget": tk.Label,  "header": "Food Name"},
                {"code_name": "amount", "widget": tk.Label, "header": "Amount (g)"},
                {"code_name": "carbonhydrate", "widget": tk.Label,  "header": "Carbohydrate"},
                {"code_name": "protein", "widget": tk.Label,  "header": "Protein"},
                {"code_name": "fat", "widget": tk.Label,  "header": "Fat"},
                {"code_name": "calories", "widget": tk.Label,  "header": "Calories"},


            ]

        for h in self._params:
            self.label_widgets[h['code_name']] = dict()


        # For header
        for idx, h in enumerate(self._params):
            header = tk.Label(self._result_frame, text=h['header'], bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT,
                              width= 15, bd=1, relief=tk.FLAT)
            header.grid(row=0, column=idx, padx=15)


        for f_tuple in food_data:

            # food_name
            self.label_widgets['food_name'][b_index] = tk.Label(self._result_frame, text= f_tuple[0], bg=BG_COLOR, fg=FG_COLOR, font=GLOBAL_FONT,
                              width= 30, bd=1, relief=tk.FLAT)
            self.label_widgets['food_name'][b_index].grid(row=b_index, column=0, padx=2)

            # amount
            self.label_widgets['amount'][b_index] = tk.Label(self._result_frame, text=f_tuple[1], bg=BG_COLOR,
                                                              fg=FG_COLOR, font=GLOBAL_FONT,
                                                              width=10,  bd=1, relief=tk.FLAT)
            self.label_widgets['amount'][b_index].grid(row=b_index, column=1, padx=2)

            # carbonhydrate
            self.label_widgets['carbonhydrate'][b_index] = tk.Label(self._result_frame, text=f_tuple[2], bg=BG_COLOR,
                                                              fg=FG_COLOR, font=GLOBAL_FONT,
                                                              width= 10, bd=1, relief=tk.FLAT)
            self.label_widgets['carbonhydrate'][b_index].grid(row=b_index, column=2, padx=2)

            # protein
            self.label_widgets['protein'][b_index] = tk.Label(self._result_frame, text=f_tuple[3], bg=BG_COLOR,
                                                              fg=FG_COLOR, font=GLOBAL_FONT,
                                                              width= 10, bd=1, relief=tk.FLAT)
            self.label_widgets['protein'][b_index].grid(row=b_index, column=3, padx=2)

            # fat
            self.label_widgets['fat'][b_index] = tk.Label(self._result_frame, text=f_tuple[4], bg=BG_COLOR,
                                                              fg=FG_COLOR, font=GLOBAL_FONT,
                                                              width=10, bd=1, relief=tk.FLAT)
            self.label_widgets['fat'][b_index].grid(row=b_index, column=4, padx=2)

            # calories
            self.label_widgets['calories'][b_index] = tk.Label(self._result_frame, text=f_tuple[5], bg=BG_COLOR,
                                                              fg=FG_COLOR, font=GLOBAL_FONT,
                                                              width=10, bd=1, relief=tk.FLAT)
            self.label_widgets['calories'][b_index].grid(row=b_index, column=5, padx=2)

            b_index += 1

