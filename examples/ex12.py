import ctkchart
import customtkinter as ctk


tk = ctk.CTk()
tk.configure(bg="#ffffff")
tk.geometry("600+300")

chart = ctkchart.CTkLineChart(master=tk, x_axis_values=tuple([x for x in range(2018,2026,1)]),
                          y_axis_values=(-100, 100), bg_color=("#eeeeee", "#191919"),fg_color=("#eeeeee", "#191919") , axis_color=("#909090", "#2C2C2C")
                          
                          )

chart.pack()

line = ctkchart.CTkLine(master=chart, size=3, style="dashed", style_type=(10,2))
line2 = ctkchart.CTkLine(master=chart, size=3, style="dashed", style_type=(6,20))
line3 = ctkchart.CTkLine(master=chart, size=3, style="dotted", style_type=(6,3))
line4 = ctkchart.CTkLine(master=chart, size=3, style="dotted", style_type=(3,6))



import random

chart.show_data(line=line, data=[90]*10)
chart.show_data(line=line2, data=[40]*10)
chart.show_data(line=line3, data=[0]*10)
chart.show_data(line=line4, data=[-40]*10)
 

tk.mainloop()