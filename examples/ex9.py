import ctkchart
import customtkinter as ctk


tk = ctk.CTk()
tk.configure(bg="#ffffff")
tk.geometry("600+300")

chart = ctkchart.CTkLineChart(master=tk, x_axis_values=tuple([x for x in range(2018,2026,1)]),
                          y_axis_values=(-100, 100), bg_color=("#eeeeee", "#191919"),fg_color=("#eeeeee", "#191919") , axis_color=("#909090", "#2C2C2C"),
                            y_axis_section_color=("#aaaaaa","#2c2c2c"),
                            x_axis_section_color=("#aaaaaa","#2c2c2c"),
                            
                        
                          y_axis_label_count=5,
                          y_axis_section_count=5, 
                          x_axis_section_count=8,
                          x_axis_section_style = "dashed",
                          y_axis_section_style = "dashed",
                          
                          x_axis_section_style_type=(4,4),
                          y_axis_section_style_type=(4,4)
                          )

chart.pack()

line = ctkchart.CTkLine(master=chart)
import random

def loop():
  chart.show_data(line=line, data=random.choices([0,-100,10,90,-10,76,20,-54,100], k=1))
  tk.after(100,loop)
  
loop() 
tk.mainloop()