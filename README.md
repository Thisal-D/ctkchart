<div id="top">

### 🌟 Like what you see? Give us a star! 🚀 Thanks a bunch! 😄

## ***# If you're using tkinter, I recommend checking out <a href="https://github.com/Thisal-D/tkchart"> tkchart </a>.***

### <a href="#contributing">Contributing to ctkchart</a>

<div align="center">

<img src="https://drive.google.com/thumbnail?id=1f4Q2dA64iJGUVWpAZsl0q6Mq0NVkGCDR&sz=w900">

<img src="https://drive.google.com/thumbnail?id=1Iy0H33x3J9tHh_FMTUV2zRITUk1xFrfB&sz=w180">

</div>

### <li>ctkchart Library is a Python library that simplifies the process of creating line charts in customtkinter GUI applications.</li>

## Examples

<a href="https://github.com/Thisal-D/ctkchart/blob/main/Tests/Main%20-%20Test.py"> Tests/Main - Test.py </a>

https://github.com/Thisal-D/ctkchart/assets/93121062/8cdec09a-d5c1-458c-8575-39b0fbe4f21f

https://github.com/Thisal-D/ctkchart/assets/93121062/05d01144-ad3e-4d7c-aa61-df79acf2e1c7

https://github.com/Thisal-D/ctkchart/assets/93121062/6fb3cba4-909b-46bc-a259-17db5279a1e1

## ctkchart - 0.0.2

### You need to install & import package first
* installation
    * ``` 
        pip install ctkchart 
        ```

* importing
    * ```
        import ctkchart
        ```

## objects
* CTkLineChart 
* CTkLine 

## To display data using CTkLineChart you need to do 3 main tasks
1. Creating a CTkLineChart
2. Creating a CTkLine
3. Display of data
<br>

# 1 . Creating a CTkLineChart
 
```
linechart = ctkchart.CTkLineChart()
```
- ##  Attributes & Types & Values
    ## Master Configuration
    - master : ``tkinter | customtkinter (Frame | Canvas | Tk)``

    ## Dimensions 
    - width : ``int``
    - height : ``int``
    - axis_size : ``int``
    - x_space : ``int``
    - y_space : ``int``
    - line_width : ``int | str``
        - "auto"
        - 10
    - pointer_size : ``int``

    ## Value Configuration
    - x_axis_section_count : ``int``
    - y_axis_section_count : ``int``
    - x_axis_label_count : ``int``
    - y_axis_label_count : ``int``
    - x_axis_display_values_indices : ``tuple[int, ...]``
    - x_axis_data : ``any``
    - y_axis_data : ``any``
    - x_axis_values : ``tuple[any, ...]`` 
        - ("2020 Year", "2021 Year", "2022 Year", "2023 Year", "2024 Year")
        - (0.1, 0.2, 0.3, 0.4, 0.5)
    - y_axis_values : ``tuple[int | float, int | float]``
        - (0 ,1000)
        - (-1000, 1000)
    - y_axis_precision : ``int``
    - pointing_values_precision : ``int``
    - ~~y_axis_max_value~~ : <span style="color:red; font-weight:bold">Deprecated</span>

    ## Color Configuration
    - bg_color : ``tuple[str, str] | str``
    - fg_color : ``tuple[str, str] | str``
    - axis_color : ``tuple[str, str] | str``
    - x_axis_font_color : ``tuple[str, str] | str``
        - ("#ffffff", "#000000")
        - ("white", "black")
        - "white"
        - "#ffffff"
    - y_axis_font_color : ``tuple[str, str] | str``
    - x_axis_data_font_color : ``tuple[str, str] | str``
    - y_axis_data_font_color : ``tuple[str, str] | str``
    - y_axis_section_color : ``tuple[str, str] | str``
    - x_axis_section_color : ``tuple[str, str] | str``
    - pointer_color : ``tuple[str, str] | str``
    - ~~section_color~~ : <span style="color:red; font-weight:bold">Deprecated</span>
    
    ## Font Configuration
    - data_font_style : ``tuple[str, int, str]``
        - ("arial", 10, "bold")
        - ("arial", 20, "normal")
    - axis_font_style : ``tuple``

    ## Style Configuration
    - x_axis_data_position : ``str``
        - "top"
        - "side"
    - y_axis_data_position : ``str``
    - x_axis_section_style : ``str``
        - "normal"
        - "dashed"
    - y_axis_section_style : ``str``
    - x_axis_section_style_type : ``tuple[int, int]``
        - (50, 10)
        - (10, 10)
    - y_axis_section_style_type : ``tuple[int, int]``

    ## Data Retrieval Configuration
    - pointing_callback_function : ``function``
        - function_name(*args)
        - function_name(x: any, y: list)
    - pointer_state : ``str``
        - "enabled"
        - "disabled"
    - pointer_lock : ``str``
        - "enabled"
        - "disabled"
    
    ## Recent Changes
    -  ~~y_axis_max_value : ``int | float``~~ <span style="color:red; font-weight:bold">Deprecated</span>
        - replaced with y_axis_values : ``tuple[int | float, int | float]``

            **_The y_axis_values parameter is a tuple where the value at index 0 represents the starting value of the Y-axis, and the value at index 1 represents the ending value of the Y-axis._**

    - ~~section_color : ``tuple[str, str] | str``~~ <span style="color:red; font-weight:bold">Deprecated</span>
        - replaced with x_axis_section_color : ``tuple[str, str] | str``
        - replaced with y_axis_section_color : ``tuple[str, str] | str``

- ##  Methods

    - ### configure : ``use to change CTkLineChart attributes``
        Support parameters
        - width 
        - height 
        - axis_size 
        - x_space 
        - y_space 
        - line_width 
        - pointer_size
        - x_axis_section_count 
        - y_axis_section_count 
        - x_axis_label_count
        - y_axis_label_count 
        - x_axis_display_values_indices 
        - x_axis_data 
        - y_axis_data 
        - x_axis_values 
        - y_axis_values 
        - y_axis_precision 
        - pointing_values_precision
        - bg_color 
        - fg_color
        - axis_color
        - x_axis_font_color 
        - y_axis_font_color 
        - x_axis_data_font_color 
        - y_axis_data_font_color
        - y_axis_section_color 
        - x_axis_section_color 
        - pointer_color
        - data_font_style 
        - axis_font_style
        - x_axis_data_position 
        - y_axis_data_position 
        - x_axis_section_style 
        - y_axis_section_style
        - x_axis_section_style_type 
        - y_axis_section_style_type 
        - pointing_callback_function
        - pointer_state 
        - pointer_lock 
        - ~~y_axis_max_value~~ : <span style="color:red; font-weight:bold">Removed</span>
        - ~~section_color~~ : <span style="color:red; font-weight:bold">Removed</span>
    
    - ### show_data : ``use to display data``
        Support parameters
        - data : ``list``
        - line : ``ctkchart.CTkLine``
       
    - ### place : ``use to place LineChart``
        Support parameters
        - x : ``int``
        - y : ``int``
        - rely : ``float | int``
        - relx : ``float | int``
        - anchor : ``str``
       
    - ### pack : ``use to pack LineChart``
        Support parameters
        - pady : ``int``
        - padx : ``int``
        - before : ``widget``
        - after : ``widget``
        - side : ``str``
        - anchor : ``str``
        
    - ### grid : ``use to grid LineChart``
        Support parameters
        - column : ``int``
        - columnspan : ``int``
        - padx : ``int``
        - pady : ``int``
        - row : ``int``
        - rowspan : ``int``
        - sticky : ``str``

    - ### place_forget : ``use to place forget the chart``
    - ### pack_forget : ``use to pack forget the chart``
    - ### grid_forget : ``use to grid forget the chart``
    - ### place_back : ``use to place chart in the old location after place forget``
    - ### pack_back : ``use to pack chart in the old location after pack forget``
    - ### grid_back : ``use to grid chart in the old location after grid forget``
    - ### hide_all : ``use to hide all the lines``
        Support parameters
        - state : ``bool``
        
    - ### hide : ``use to hide a specific line``
        Support parameters
        - line : ``ctkchart.CTkLine``
        - state : ``bool``
    - ### reset : ``use to reset chart``

 

# 2 . Creating a CTkLine

```
line = ctkchart.CTkLine()
```

- ##  Attributes & Types & Values
    - master : ``ctkchart.CTkLineChart``
    - color : ``tuple[str, str] | str``
        - ("#ffffff", "#000000")
        - ("white", "black")
        - "white"
        - "#ffffff"
    - size : ``int``
    - style : ``str``
        - "normal"
        - "dashed"
        - "dotted"
    - style_type : ``tuple[int, int]``
        - (5,10)
        - (10,5)
    - point_highlight: ``str``
        - "disabled"
        - "enabled"
    - point_highlight_size: ``int`` 
    - point_highlight_color: ``tuple[str, str] | str``


- ##  Methods
    - #### configure : ``use to change CTkLine attributes``
        Support parameters
        - size 
        - color 
        - style
        - style_type
        - point_highlight
        - point_highlight_size
        - point_highlight_color

```
line = ctkchart.CTkLine(master=linechart,
                color="lightblue",
                size=2,
                style="dashed",
                style_type=(4,10))

```


# 3 . Display of Data
```
import ctkchart
import customtkinter as ctk
from random import choices

root = ctk.CTk()

chart = ctkchart.CTkLineChart(master=root, pointer_state="enabled", width=900, x_axis_values=tuple([x for x in range(20)]),
                             pointer_lock="enabled", pointer_size=1)
                      
chart.place(x=10,y=10)

line = ctkchart.CTkLine(master=chart)

def loop():
    chart.show_data(line=line, data=(choices((range(0,11)),k=1)))
    root.after(1000, loop)
loop()


root.mainloop()
```


</div>

<br>
 
<div id="contributing">

### <a href="#top"> Go to top </a>

# Contributing to ctkchart

Thank you for considering contributing to ctkchart! Please follow these guidelines to contribute effectively.

## Getting Started

1. Fork the repository.
2. Clone your forked repository: `git clone https://github.com/Thisal-D/ctkchart.git`
3. Create a new branch for your changes: `git checkout -b feature-branch`

## Making Changes

1. Make your changes and ensure they follow the project's coding standards.
2. Test your changes locally.
3. Commit your changes: `git commit -m "Brief description of your changes"`

## Submitting Changes

1. Push your changes to your forked repository: `git push origin feature-branch`
2. Create a pull request on the main repository.

## Code of Conduct

Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) to maintain a respectful and inclusive community.

## Issues and Discussions

If you encounter issues or have questions, please check the [issue tracker](https://github.com/Thisal-D/ctkchart/issues) or start a discussion in the [GitHub Discussions](https://github.com/Thisal-D/ctkchart/discussions) section.

## License

By contributing, you agree that your contributions will be licensed under the project's [LICENSE](LICENSE).

Thank you for your contribution!

</div>


### go to PyPi
- # PyPi.org   :   <a href="https://pypi.org/project/ctkchart" target="_blank" ><i>ctkchart</i></a>

### go to GitHub
- # GitHub.com   :  <a href="https://github.com/Thisal-D/ctkchart" target="_blank" ><i>ctkchart</i></a>

