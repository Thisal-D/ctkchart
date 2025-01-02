import ctkchart
import customtkinter as ctk




tk = ctk.CTk()
tk.configure(bg="#ffffff")
tk.geometry("600+300")

chart = ctkchart.CTkLineChart(master=tk, x_axis_values=tuple([x for x in range(2018,2026,1)]),
                          y_axis_values=(-100, 100), bg_color=("#eeeeee", "#191919"),fg_color=("#eeeeee", "#191919") , axis_color=("#909090", "#2C2C2C"),
                          #y_axis_data="Y data" , y_axis_data_font_color=("#00ff00", "#00ff00"), x_axis_data_font_color=("#ff0000", "#ff0000"),
                          #x_axis_data="X data",
                          #data_font_style=("arial", 15, "underline")
                          x_axis_font_color=("#ff0000", "#ff0000"),
                          y_axis_font_color=("#00ff00","#00ff00"),
                          axis_font_style=("arial",13,"bold")
                          )
chart.pack()

line = ctkchart.CTkLine(master=chart)

chart.show_data(line=line, data=[0,-100,10,90,-10,76,20,-54,100])

tk.mainloop()