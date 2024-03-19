import customtkinter as ctk
import ctkchart
import random

root = ctk.CTk()
root.geometry("600+300")
root.title("Line Chart")
chart = ctkchart.CTkLineChart(master=root,
                              y_axis_values = (-100,100),
                              x_axis_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                             
                              )
chart.pack()

line = ctkchart.CTkLine(master=chart,
                        size=2,
                        point_highlight="enabled",
                        style="dashed",
                        style_type=(20,5),
                        fill="disabled")

line2 = ctkchart.CTkLine(master=chart,
                         size=3,style="normal",
                         style_type=(15,7),
                         color=("#5dffb6","#5dffb6"),
                         fill="enabled",
                         fill_color = ("#5dffb6","#5dffb6")
                         )

data = [x for x in range(-100,100)]
def loop():
    chart.show_data(line=line, data=[0, -80, -40, 100, 0, 80, 50, -50, -10,80,50,100])
    chart.show_data(line=line2, data=[100, -10, -90, 40, -30, 40, 90,-90, -40,-100,40,0])
    
loop()

root.mainloop()