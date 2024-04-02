import customtkinter as ctk
import ctkchart
import random

#root
root = ctk.CTk()
root.geometry("700x400+500+300")
#creating a chart
chart = ctkchart.CTkLineChart(master=root,
                          width=1700,
                          height=800,
                          axis_size=5,
                          x_axis_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                          y_axis_values = (-1000,1000),
                          y_axis_label_count=10,
                         
                          x_axis_section_color=("#aaaaaa","#555555"),
                          y_axis_section_color=("#aaaaaa","#555555"),

                          y_axis_font_color=("#454545", "#aaaaaa"),
                          x_axis_font_color=("#454545", "#aaaaaa"),
                          data_font_style=("arial", 17, "bold"),
                          axis_font_style=("arial", 13, "bold"),
                          x_axis_data_font_color=("#505050","#efefef"),
                          y_axis_data_font_color=("#505050","#efefef"),
                          
                          y_space=20,
                          x_space=20,
                          )         
chart.pack(pady=40)

#creating a line
line1 = ctkchart.CTkLine(master=chart,
                    size=3,
                    style="normal",
                
                    fill="enabled",
                    point_highlight="enabled",
                    point_highlight_size=15,
                   )




data = [x for x in range(-1000,1000)]
#dipslay data (random)
def loop():
    chart.show_data(line=line1, data=random.choices(data, k=1))
    root.after(500, loop)
loop()

root.mainloop()