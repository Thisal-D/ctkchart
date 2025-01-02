import ctkchart
import customtkinter as ctk


tk = ctk.CTk()
tk.configure(bg="#ffffff")
tk.geometry("600+300")

chart = ctkchart.CTkLineChart(master=tk, x_axis_values=tuple([x for x in range(2018,2026,1)]),
                          y_axis_values=(-100, 100), bg_color=("#eeeeee", "#191919"),fg_color=("#eeeeee", "#191919") , axis_color=("#909090", "#2C2C2C")
                          
                          )

chart.pack()

line = ctkchart.CTkLine(master=chart, style="normal" ,point_highlight="enabled", point_highlight_color="#80ccff", point_highlight_size=8)



chart.show_data(line=line, data=[0,-100,10,90,-10,76,20,-54,100])

 

tk.mainloop()