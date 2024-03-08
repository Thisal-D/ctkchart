import ctkchart
import customtkinter as ctk
from random import choices

root = ctk.CTk()

chart = ctkchart.CTkLineChart(master=root, pointer_state="enabled", width=900, x_axis_values=tuple([x for x in range(20)]),
                             pointer_lock="enabled", pointer_size=1) 
chart.pack()

line = ctkchart.CTkLine(master=chart)

chart.show_data(line=line, data=[0,1,2,3,4,5,6,7,8,9,10])

def loop():
    chart.show_data(line=line, data=tuple(choices((range(0,11)),k=1)))
    root.after(1000, loop)

loop()

ctk.CTkButton(master=root ,text="Dark", command=lambda:ctk.set_appearance_mode("dark")).pack(pady=10)
ctk.CTkButton(master=root ,text="Light", command=lambda:ctk.set_appearance_mode("light")).pack()

root.mainloop()
