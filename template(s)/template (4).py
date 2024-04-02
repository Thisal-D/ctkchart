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
                        size=1,
                        style="dashed",
                        style_type=(10,5),
                        point_highlight="enabled",)
                        #fill="enabled")



data = [x for x in range(-100,100)]
def loop():
    chart.show_data(line=line, data=[0, -80, -40, 100, 0, 80, 50, -50, -10,80,50,100])


loop()

root.mainloop()