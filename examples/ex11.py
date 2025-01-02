import ctkchart
import customtkinter as ctk


tk = ctk.CTk()
tk.configure(bg="#ffffff")
tk.geometry("600+300")

chart = ctkchart.CTkLineChart(master=tk, x_axis_values=tuple([x for x in range(2018,2026,1)]),
                          y_axis_values=(-100, 100), bg_color=("#eeeeee", "#191919"),fg_color=("#eeeeee", "#191919") , axis_color=("#909090", "#2C2C2C")
                          
                          )

chart.pack()

line = ctkchart.CTkLine(master=chart, size=3, style="dashed", style_type=(20,10))
line2 = ctkchart.CTkLine(master=chart, size=3, style="normal", style_type=(20,10))
line3 = ctkchart.CTkLine(master=chart, size=3, style="dotted", style_type=(8,10))


import random

chart.show_data(line=line3, data=[-30]*10)
chart.show_data(line=line, data=[20]*10)
chart.show_data(line=line2, data=[80]*10)
 

tk.mainloop()