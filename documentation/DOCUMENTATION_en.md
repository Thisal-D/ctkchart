<div id="top">

[![Chinese](https://img.shields.io/badge/Language-中文-red)](DOCUMENTATION_zh.md)

</div> 

---

<div id="howtouse"> 

<a href="#howtouse">**Usage Guide**</a> | <a href="#example">**Examples**</a> | <a href="#parameter_explanation">**Parameter Explanation**</a> | <a href="../CHANGES_en.md">**Whats New ?**</a> 

### Importing & Installation 
* Installation 
    ``` 
    pip install ctkchart 
    ``` 

* Importing 
    ``` python
    import ctkchart 
    ``` 
---
<div id="parameter_img"> 

### Parameter Overview 

<div align="center"> 

<picture> 
<source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1J4XKj5-cVWxUTeS7zHkJvewOmISLVU6Y&sz=w2500"> 
<img src="https://drive.google.com/thumbnail?id=1CqZ2NZsJrrLKUgyzyVgoEREQuuai6Yha&sz=w2500"> 
</picture> 

</div> 
</div> 

---

### To display data using ctkchart you need to do 3 main tasks 
1. <a href="#create-line-chart">**Creating a Line Chart**</a> 
2. <a href="#create-line">**Creating a Line**</a> 
3. <a href="#display-data">**Display of data**</a> 

---

<div id="create-line-chart"> 

## 1 . Creating a LineChart 
<a href="#create-line">**Creating a Line**</a> | <a href="#display-data">**Display of data**</a> 

``` python
linechart = ctkchart.CTkLineChart() 
``` 

### Parameters

| Parameter                                       | Required / Optional | Description                                | Types                           | Example Value(s)                    | 
|-------------------------------------------------|---------------------|--------------------------------------------|---------------------------------|-------------------------------------| 
| master                                          | ***Required***      | Master Widget for LineChart                | ``widget``                      | widget                              | 
| [y_axis_values](#x_y_axis_values)               | ***Required***      | Minimum and maximum values for y-axis      | ``tuple[int \| float]``         | (-1000, 1000), ...                  | 
| [x_axis_values](#x_y_axis_values)               | ***Required***      | Values for x-axis                          | ``tuple[any]``                  | (1, 2, 3, 4, 5), ...                | 
| width                                           | ***Optional***      | Width of the chart                         | ``int``                         | 300, ...                            | 
| height                                          | ***Optional***      | Height of the chart                        | ``int``                         | 100, ...                            | 
| [axis_size](#parameter_img)                     | ***Optional***      | Size of the axis                           | ``int``                         | 1<=                                 | 
| [axis_color](#parameter_img)                    | ***Optional***      | Color of the axis                          | ``tuple[str, str]`` \| ``str``  | ("#FF0000", "#00FF00"), ...         | 
| [bg_color](#parameter_img)                      | ***Optional***      | Background color of the chart              | ``tuple[str, str]`` \| ``str``  | ("#FF0000", "#00FF00"), ...         | 
| [fg_color](#parameter_img)                      | ***Optional***      | Foreground color of the chart              | ``tuple[str, str]`` \| ``str``  | ("#FF0000", "#00FF00"), ...         | 
| [data_font_style](#x_y_data)                    | ***Optional***      | Font style for data labels                 | ``tuple[str, int, str]``        | ("arial", 9, "bold"), ...           | 
| [axis_font_style](#x_y_font_style)              | ***Optional***      | Font style for axis labels                 | ``tuple[str, int, str]``        | ("arial", 8, "normal"), ...         | 
| [x_axis_data](#x_y_data)                        | ***Optional***      | Data label for x-axis                      | ``str``                         | "X", ...                            | 
| [y_axis_data](#x_y_data)                        | ***Optional***      | Value for y-axi data label                 | ``any``                         | "Y", ...                            | 
| [x_axis_data_font_color](#x_y_data)             | ***Optional***      | Font color for x-axis data label           | ``tuple[str, str]`` \| ``str``  | ("#FF0000", "#00FF00"), ...         | 
| [y_axis_data_font_color](#x_y_data)             | ***Optional***      | Font color for y-axis data label           | ``tuple[str, str]`` \| ``str``  | ("#FF0000", "#00FF00"), ...         | 
| [x_axis_data_position](#data_position)          | ***Optional***      | Position of x-axis data label              | ``str`` ("top", "side")         | "top"                               | 
| [y_axis_data_position](#data_position)          | ***Optional***      | Position of y-axis data label              | ``str`` ("top", "side")         | "top"                               | 
| [x_axis_section_count](#x_y_section)            | ***Optional***      | Number of sections on the x-axis           | ``int``                         | 0<=                                 | 
| [y_axis_section_count](#x_y_section)            | ***Optional***      | Number of sections on the y-axis           | ``int``                         | 0<=                                 | 
| [x_axis_label_count](#x_y_label_count)          | ***Optional***      | Number of x-axis labels                    | ``int``                         | 0<=                                 | 
| [y_axis_label_count](#x_y_label_count)          | ***Optional***      | Number of y-axis labels                    | ``int``                         | 1<=                                 | 
| [x_axis_font_color](#x_y_font_style)            | ***Optional***      | Font color for x-axis labels               | ``tuple[str, str]`` \| ``str``  | ("#FF0000", "#00FF00"), ...         | 
| [y_axis_font_color](#x_y_font_style)            | ***Optional***      | Font color for y-axis labels               | ``tuple[str, str]`` \| ``str``  | ("#FF0000", "#00FF00"), ...         | 
| [x_axis_section_style](#x_y_section_style)      | ***Optional***      | Style of sections on the x-axis            | ``str`` ("normal", "dashed")    | "normal"                            | 
| [y_axis_section_style](#x_y_section_style)      | ***Optional***      | Style of sections on the y-axis            | ``str`` ("normal", "dashed")    | "normal"                            | 
| [x_axis_section_style_type](#x_y_section_style) | ***Optional***      | Style type for sections on the x-axis      | ``tuple[int, int]``             | (100, 50), ...                      | 
| [y_axis_section_style_type](#x_y_section_style) | ***Optional***      | Style type for sections on the y-axis      | ``tuple[int, int]``             | (100, 50)                           | 
| [x_axis_section_color](#x_y_section)            | ***Optional***      | Color of sections on the x-axis            | ``tuple[str, str]`` \| ``str``  | ("#FF0000", "#00FF00"), ...         | 
| [y_axis_section_color](#x_y_section)            | ***Optional***      | Color of sections on the y-axis            | ``tuple[str, str]`` \| ``str``  | ("#FF0000", "#00FF00"), ...         | 
| [y_axis_precision](#y_precision)                | ***Optional***      | Precision for y-axis values                | ``int``                         | 0<=                                 | 
| [x_axis_display_values_indices](#indices_view)  | ***Optional***      | Indices of values to display on the x-axis | ``tuple[int, ...]``             | (0, 1, 2, 3, 4, 5), ...             | 
| [x_axis_point_spacing](#x_axis_point_spacing)   | ***Optional***      | Width of lines                             | ``int`` \| ``str`` "auto"       | "auto" <br> 1<=                     | 
| [x_space](#parameter_img)                       | ***Optional***      | Space between x-axis and chart area        | ``int``                         | 0<=                                 | 
| [y_space](#parameter_img)                       | ***Optional***      | Space between y-axis and chart area        | ``int``                         | 0<=                                 | 
| pointer_state                                   | ***Optional***      | State of the pointer                       | ``str`` ("enabled", "disabled") | "disabled"                          | 
| pointing_callback_function                      | ***Optional***      | Callback function for pointer              | ``callable``                    | function(*args) <br> function(x, y) | 
| pointer_color                                   | ***Optional***      | Color of the pointer                       | ``tuple[str, str]`` \| ``str``  | ("#FF0000", "#00FF00"), ...         | 
| pointing_values_precision                       | ***Optional***      | Precision for pointing values              | ``int``                         | 0<=                                 | 
| pointer_lock                                    | ***Optional***      | State of pointer lock                      | ``str`` ("enabled", "disabled") | "enabled"                           | 
| pointer_size                                    | ***Optional***      | Size of the pointer                        | ``int``                         | 1<=                                 | 


---

### Methods 

| Method                     | Description                              | Supported / Required Parameters                                                                                                  | Return Type | 
|----------------------------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------| 
| configure                  | Change LineChart attributes              | All attributes except for master                                                                                                 | ``None``    | 
| [show_data](#display-data) | Display data                             | data: ``list``<br> line: ``ctkchart.CTkLine``                                                                                    | ``None``    | 
| place                      | Place LineChart                          | x: ``int``<br>y: ``int``<br>rely: ``float or int``<br>relx: ``float or int``<br>anchor: ``str``                                  | ``None``    | 
| pack                       | Pack LineChart                           | pady: ``int``<br>padx: ``int``<br> before: ``widget``<br> after: ``widget``<br>side: ``str``<br>anchor: ``str``                  | ``None``    | 
| grid                       | Grid LineChart                           | column: ``int``<br>columnspan: ``int``<br>padx: ``int``<br>pady: ``int``<br> row: ``int``<br>rowspan: ``int``<br>sticky: ``str`` | ``None``    | 
| place_forget               | Place forget the chart                   | -                                                                                                                                | ``None``    | 
| pack_forget                | Pack forget the chart                    | -                                                                                                                                | ``None``    | 
| grid_forget                | Grid forget the chart                    | -                                                                                                                                | ``None``    | 
| set_lines_visibility       | Change the visibility of all the lines   | state: ``bool``                                                                                                                  | ``None``    | 
| set_line_visibility        | Change the visibility of a specific line | line: ``ctkchart.CTkLine``<br> state: ``bool``                                                                                   | ``None``    | 
| get_line_visibility        | Get the visibility of a specific line    | line: ``ctkchart.CTkLine``                                                                                                       | ``bool``    | 
| reset                      | Reset line chart                         | -                                                                                                                                | ``None``    | 
| cget                       | Get the value of the specified parameter | attribute_name: ``str`` \| "\_\_all\_\_"                                                                                         | ``any``     | 
| place_info                 | Get info about place                     | attribute_name: ``str`` \| "\_\_all\_\_"                                                                                         | ``any``     | 
| pack_info                  | Get info about pack                      | attribute_name: ``str`` \| "\_\_all\_\_"                                                                                         | ``any``     | 
| grid_info                  | Get info about grid                      | attribute_name: ``str`` \| "\_\_all\_\_"                                                                                         | ``any``     | 
| get_line_area               | Get the are of specific line            | line: `ctkchart.CTkLine`        | ``float``    | 
| get_lines_area               | Get the are of all lines               | -                           | ``float``    | 
| destroy                    | Destroy the chart                        | -                           | ``None``    | 
| clear_data  | Clears the data for all lines within the chart, ensuring that only the most recent visible data points are retained. If the total data points exceed the maximum visible points, the older data is removed from each line's data. This method ensures that the chart displays only the relevant portion of data based on the maximum visible range.                                                           | -              | ``None``    |  
| get_lines_data              | Retrieves data points for all lines within a specified range with an optional step value. | start: `int` <br> end: `int` <br> step: `int` | `Dict[ctkchart.CTkLine, Tuple[int]]` |  
get_line_data               | Retrieves data points for a specific line within a specified range and step. | line: `ctkchart.CTkLine` <br> start: `int` <br> end: `int`<br> step: `int` | `Tuple[int \| float]` |  
| get_x_axis_visible_point_count | Retrieves the maximum number of data points that can be visible along the X-axis. | -                                       | `int` |  
| get_lines_visible_data      | Retrieves currently visible data points for all lines based on the maximum data length and visible points. | -                                       | `Dict[ctkchart.CTkLine, Tuple[int \| float]]` |  
| get_line_visible_data       | Retrieves currently visible data points for a specific line. | line: `ctkchart.CTkLine`                          | `Tuple[int \| float]` |  

</div> 

---

<div id="create-line"> 

## 2 . Creating a Line 

<a href="#create-line-chart">**Creating a LineChart**</a> | <a href="#display-data">**Display of data**</a> 

``` python
line = ctkchart.CTkLine() 
``` 

### Parameters 

| Parameter Name                            | Required / Optional | Description                    | Types                                  | Example Value(s) | 
|-------------------------------------------|---------------------|--------------------------------|----------------------------------------|------------------| 
| master                                    | Required            | Master of the line             | ``ctkchart.CTkLine``                   | LineChart obj    | 
| [color](#line_color_size)                 | Optional            | Color of the line              | ``tuple[str, str]`` \| ``str``         | "#768df1"        | 
| [size](#line_color_size)                  | Optional            | Size of the line               | ``int``                                | 1<=              | 
| [style](#line_style)                      | Optional            | Style of the line              | ``str`` ("normal", "dashed", "dotted") | "normal"         | 
| [style_type](#line_style_type)            | Optional            | Style type for the line        | ``tuple[int, int]``                    | (10, 5),...      | 
| [point_highlight](#point_highlight)     | Optional            | State of point highlighting    | ``str`` ("enabled", "disabled")        | "disabled"       | 
| [point_highlight_size](#point_highlight)  | Optional            | Size of the highlighted point  | ``int``                                | 1<=              | 
| [point_highlight_color](#point_highlight) | Optional            | Color of the highlighted point | ``tuple[str, str]`` \| ``str``         | "#768df1"        | 
| [fill](#fill)                             | Optional            | State of filling               | ``str`` ("enabled", "disabled")        | "disabled"       | 
| [fill_color](#fill)                       | Optional            | Color of the fill              | ``tuple[str, str]`` \| ``str``         | "#5d6db6"        | 


---

### Methods 

| Method         | Description                              | Supported Parameters                       | Return Type | 
|----------------|------------------------------------------|--------------------------------------------|-------------| 
| configure      | Change LineChart attributes              | All attributes except for master           | ``None``    | 
| cget           | Get the value of the specified parameter | attribute_name: ``str`` \| "\_\_all\_\_"   | ``any``     | 
| reset          | reset line object                        | -                                          | ``None``    | 
| set_visible    | change the visibility of the line        | state: ``bool``                            | ``None``    | 
| get_visibility | get the visibility of the line           | -                                          | ``bool``    | 
| clear_data     | Clears the data for a specific line, ensuring that only the most recent visible data points are retained. If the line's data exceeds the maximum visible points, the older data is trimmed. This method allows each line to independently clean its data, ensuring it remains within the visible range.                                                           | -              | ``None``    | 
| destroy        | Destroy the line                         | -                                          | ``None``    | 
| get_data                   | Retrieves data points from a specified range with an optional step value. If no parameters are given, it returns all available data. | start: `int` <br> end: `int` <br> step: `int` | `Tuple[int \| float]` |  
| get_current_visible_data    | Returns the currently visible data points based on the maximum data length across all lines and the maximum number of visible points. | -                   | `Tuple[int \| float]` |  
| get_x_axis_visible_point_count | Retrieves the maximum number of data points that can be visible along the X-axis. | -                   | `int` |  

</div> 

---

<div id="display-data"> 

## 3 . Display of Data 

<a href="#create-line-chart">**Creating a LineChart**</a> | <a href="#create-line">**Creating a Line**</a> 

``` python
import tkinter as tk 
import ctkchart 
import random 

#root 
root = tk.Tk() 
root.configure(bg="#151515") 

#creating a chart 
chart = ctkchart.CTkLineChart(
    master=root, 
    x_axis_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 
    y_axis_values = (-100,100)
) 
chart.pack() 

#creating a line 
line = ctkchart.CTkLine(master=chart) 

data = [x for x in range(-100,101)] #values -100 to 100 
#dipslay data (random) 
def loop(): 
    chart.show_data(line=line, data=random.choices(data, k=1)) 
    root.after(500, loop) 
loop() 

root.mainloop() 
``` 

<div align="center"> 

https://github.com/Thisal-D/tkchart/assets/93121062/64440c23-63e6-4093-b027-21b00a6f5518 

</div> 

---

</div> 


<div id="parameter_explanation"> 

<a href="#top">**Back to the Top**</a> | <a href="#howtouse">**Usage Guide**</a> | <a href="#example">**Examples**</a> | <a href="../CHANGES_en.md">**Whats New ?**</a> 

## Parameter Explanation 

<div id="x_y_axis_values"> 

### CTkLineChart 

- #### y_axis_values 
    y_axis_values is a tuple that containing two numeric values for the y-axis. The first value (index 0) represents the starting value of the y-axis, and the second value (index 1) represents the end value of the y-axis. This tuple defines the range of values displayed along the y-axis on chart. 

- #### x_axis_values 
    x_axis_values is a collection of values that can include any data type. These values are assigned to the x-axis, starting from index 0 and continuing to the last index of the x_axis_values tuple. Each value in the tuple corresponds to a point along the x-axis in chart. 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1GBmf8GaiQG_zJbsYBqfAW7jYgGh7oKCr&sz=w950"> 
    <img src="https://drive.google.com/thumbnail?id=1UbyQEKDYhZjUI9VttKerpSVc6hZoEfi8&sz=w950" > 
    </picture> 

    ``` python
    chart = ctkchart.CTkLineChart(
        master=any_widget
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100) 
    ) 
    ``` 
---
</div> 

<div id="x_y_data"> 

- #### x_axis_data 
    refers to the value type displayed in the x-axis of a chart. 
    **Note: "X" is the default value.** 

- #### y_axis_data 
    refers to the value type displayed in the y-axis of a chart. 
    **Note: "Y" is the default value.** 

- #### x_axis_data_font_color 
    refers to the font color applied to the label representing the data type on x-axis of a chart. 

- #### y_axis_data_font_color 
    refers to the font color applied to the label representing the data type on y-axis of a chart. 

- #### data_font_style 
    refers to the font style applied to the labels representing the data types on both the x-axis and y-axis of a chart. 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1-F7IvqoT0Cl73_F2hvf9Gnbi9gM0I9cN&sz=w1000"> 
    <img src="https://drive.google.com/thumbnail?id=1m2kBnDRycSviMXO3uTHIzL6Y7S7u1rsC&sz=w1000" > 
    </picture> 

    ``` python
    chart = ctkchart.CTkLineChart(
        master=any_widget, 
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        y_axis_data="Y data" , 
        x_axis_data="X data", 
        x_axis_data_font_color="#ff0000", 
        y_axis_data_font_color="#00ff00", 
        data_font_style=("arial", 15, "underline") 
    ) 
    ``` 

---

</div> 

<div id="x_y_label_count"> 

- #### x_axis_label_count 
    When you have a set of x-axis labels, such as years from 2018 to 2025, normally all these labels are shown. But sometimes you might want to show only a few of them for better clarity. <br> 
    For instance, if you set the x_axis_label_count to 4, it means you want to display only 4 labels instead of all 8. So, the chart will automatically skip some labels to fit your specified count. <br> 
    **Note: len(<a href="#x_y_axis_values">x_axis_values</a>) is the default value.**<br> 
    In other words, adjusting the x_axis_label_count allows you to control how many labels appear on the x-axis, making your visualization cleaner and easier to understand. 
    <br> 
    - **if there are 9 labels you can limit it to : 3, 1, 0.** 
    - **if there are 20 labels you can limit it to : 10, 5, 4, 2, 1, 0.** 
    - **if there are 15 labels you can limit it to : 5, 3, 1, 0.** 

    ##### In some cases, using the x_axis_label_count parameter might not be sufficient for your needs. In such situations, you can utilize the <a href="#indices_view">x_axis_display_values_indices</a> parameter to precisely control which values are displayed on the x-axis. 

- #### y_axis_label_count 
    By default, if you set the y-axis values to range from -100 to 100, only the extreme values (-100 and 100) will be displayed on the y-axis. However, you have the option to adjust the number of labels displayed using the y_axis_label_count parameter.<br> 
    For example, if you set y_axis_label_count to 3, the system will divide the y-axis range (-100 to 100) into equal intervals and display labels at those intervals. So, for this case, with a label count of 3, you might see labels at -100, 0, and 100.<br> 
    In summary, adjusting the y_axis_label_count parameter allows you to control the number of labels displayed on the y-axis, providing flexibility in customizing the visualization based on your preferences and requirements. 


    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1mecucNsfolJPIAiGU4oX2idc_-tc2yPB&sz=w1000"> 
    <img src="https://drive.google.com/thumbnail?id=1mHgbpbaWQeQE-ykFwIizd_vIdLVSXc5w&sz=w1000" > 
    </picture> 

    ``` python
    chart = ctkchart.CTkLineChart(
        master=any_widget, 
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        x_axis_label_count=4, 
        y_axis_label_count=10, 
    ) 
    ``` 
    
---

</div> 

<div id="indices_view"> 

- #### x_axis_display_values_indices 

    Let's say you have a set of x-axis values representing years from 2018 to 2025: (2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025). Normally, all these values would be displayed on the x-axis.<br> 
    However, there might be cases where you only want to display specific years rather than all of them. In such situations, you can use the x_axis_display_values_indices parameter to control which values are shown on the x-axis.<br> 
    For example, if you only want to display the years 2019, 2022, and 2025, you can specify their indices in the x_axis_display_values_indices parameter. So, if the index of 2919 is 1, 2022 is 4, and 2025 is 7 (assuming 0-based indexing), you would set x_axis_display_values_indices to (1, 4, 7).<br> 
    This way, by setting the indices of the values you want to display, you have precise control over which values appear on the x-axis in your visualization, allowing you to tailor it according to your specific requirements. 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=122KUh1KoOSXx3Eb7U_QINSkdKvgoEiJ_&sz=w800"> 
    <img src="https://drive.google.com/thumbnail?id=1gN_DhzFPzs-7LTG7-EfeZzjisWDTFYSn&sz=w800" > 
    </picture> 

    ``` python
    chart = ctkchart.CTkLineChart(
        master=any_widget, 
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        x_axis_display_values_indices=(1, 4, 7)
    ) 
    ``` 

---

</div> 

<div id="data_position"> 

- #### x_axis_data_position 
    The x_axis_data_position parameter determines the position of the x data label. It has two 
    
    supported values: 
    - "top"
    - "side" 

    **Note: "top" is the default position** 

- #### y_axis_data_position 
    The y_axis_data_position parameter determines the position of the x data label. It has two 
    
    supported values: 
    - "top"
    - "side" 

    **Note: "top" is the default position**

    Choosing between "top" and "side" determines whether the data labels are placed horizontally above the data points or vertically beside them, respectively. This parameter allows you to customize the layout of your chart according to your preferences and available space. 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=15QCDaKjOQP83AeqaWuoFxiAbL8XCW4bg&sz=w950"> 
    <img src="https://drive.google.com/thumbnail?id=18W70YdLf8f6n1K69GhKP_Es69JF-Va3L&sz=w950" > 
    </picture> 

    ``` python
    chart = ctkchart.CTkLineChart(
        master=any_widget, 
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        x_axis_data_position="side", 
        y_axis_data_position="top" 
    ) 
    ``` 

---

</div> 

<div id="y_precision"> 

- #### y_axis_precision 

    The y_axis_precision parameter controls the number of decimal places displayed for the values on the y-axis.<br> 
    **Note: 1 is the deafault precion**<br> 
    For example: 
    - If you set y_axis_precision to 0, the values on the y-axis will be displayed as whole numbers.<br> 
    - If you set y_axis_precision to 1, the values on the y-axis will be displayed with one decimal place.<br> 
    - If you set y_axis_precision to 2, the values on the y-axis will be displayed with two decimal places. 
    <br> 

    And so on : 
    - **Adjusting the y_axis_precision parameter allows you to control the level of precision for the y-axis values in your chart. This parameter is particularly useful when dealing with data that requires specific precision or when you want to improve the readability of the chart by reducing the number of decimal places displayed.** 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=10j8-iuQ4URQcHNKX3f-eCqxW8Sl0Dn9i&sz=w950"> 
    <img src="https://drive.google.com/thumbnail?id=1B6e3yf6cPBuQvqpoleIR8syR0_WLmB1x&sz=w950" > 
    </picture> 

    ``` python
    chart = ctkchart.CTkLineChart(
        master=any_widget, 
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        y_axis_label_count=12, 
        y_axis_precision=4, 
    ) 
    ``` 

---

</div> 

<div id="x_y_font_style"> 

- #### axis_font_style 
    refers to font style of the x and y axis values 

- #### x_axis_font_color 
    refers to color of x axis values 

- #### y_axis_font_color 
    refers to color of y axis values 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1qFDqT8Vb9sxAozyKuNyEj7YWDo-wDzZv&sz=w950"> 
    <img src="https://drive.google.com/thumbnail?id=19kfPmQxP9AuDNJuFlM2F3YrDhuF3OnAs&sz=w950" > 
    </picture> 

    ``` python
    chart = ctkchart.CTkLineChart(
        master=any_widget, 
        x_axis_values=(2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025), 
        y_axis_values=(-100, 100), 
        x_axis_font_color="#00FF00", 
        y_axis_font_color="#FF0000", 
        axis_font_style=("arial", 13, "bold") 
    ) 
    ``` 

---

</div> 

<div id="x_y_section"> 

<div id="x_axis_section_count"> 

- #### x_axis_section_count 
    The x_axis_section_count parameter defines the number of sections or intervals into which the x-axis range will be divided in a chart.<br> 
    **Here's a clearer breakdown :** 
    - Let's say you have a range of values on the x-axis, such as years from 2018 to 2025. By default, this range might be represented as a continuous line without any specific sections or intervals marked. 
    - However, if you set x_axis_section_count to a value, such as 8, it means you want to divide this x-axis range into equally spaced sections or intervals. Each section will represent a subset of the total x-axis range. 
    - Adjusting the x_axis_section_count parameter allows you to control the granularity of the x-axis in your chart, making it easier for viewers to interpret the data and identify trends within specific intervals. 

</div> 

- #### y_axis_section_count 
    The y_axis_section_count parameter defines the number of sections or intervals into which the y-axis range will be divided in a chart.<br> 
    **refer : <a href="#x_axis_section_count">x_axis_section_count**</a> for more... 

- #### x_axis_section_color 
    refers to color of y axis sections 

- #### y_axis_section_color 
    refers to color of x axis sections 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=11h3KM6OhL2rzRQijHSU4damLgN3_EeWN&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1GoduMuhlvwayY55QvjEwjwrk8np-8ULL&sz=w1050" > 
    </picture> 

    ``` python
    chart = ctkchart.CTkLineChart(
        master=any_widget, 
        x_axis_section_count=8, 
        y_axis_section_count=5, 
        x_axis_section_color="#2C2C2C", 
        y_axis_section_color="#2C2C2C" 
    ) 
    ``` 

---

</div> 

<div id="x_y_section_style"> 

<div id="x_section_style"> 

- #### x_axis_section_style 
    x_axis_section_style parameter allows you to define the visual style of the sections along the x-axis in a chart. 

    - Supported styles: 
        - "dashed": When you set x_axis_section_style to "dashed", the sections along the x-axis are displayed using dashed lines. 
        - "normal": Conversely, when x_axis_section_style is set to "normal", the sections along the x-axis are displayed using solid lines.<br><br> 

    **Note: "normal" is default style.** 

</div> 

- #### y_axis_section_style 
    working same as x_axis_section_style, 
    refer <a href="#x_section_style"> x_axis_section_style </a> for more 

<div id="x_section_style_type"> 

- #### x_axis_section_style_type 
    The x_axis_section_style_type parameter is a tuple that contains two integer values, specifying the style of the dashes used when the x_axis_section_style is set to "dashed".<br> 
    For example:<br> 
    - If you set x_axis_section_style_type to (20, 10), it means : 
        - The width of each dash is 20 pixels. 
        - The spacing between dashes is 10 pixels.
        <br>

    These values determine the visual appearance of the dashed lines or markers used to represent the sections along the x-axis. Adjusting these values allows you to customize the appearance of the dashed sections according to your preferences or the requirements of your visualization. 

</div> 

- #### y_axis_section_style_type 
    working same as x_axis_section_style_type, 
    refer <a href="#x_section_style_type"> x_axis_section_style_type </a> for more 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1TJjAsXkcEk84DPZxUMn_kH10Pc0Yc3PH&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1SOieJLRtMLbIqgqlt-ATRAYRSuOwbrEK&sz=w1050" > 
    </picture> 

    ``` python
    chart = ctkchart.CTkLineChart(
        master=any_widget, 
        x_axis_section_count=8, 
        y_axis_section_count=5, 
        x_axis_section_style="dashed", 
        x_axis_section_style_type=(20,10), 
        y_axis_section_style="dashed", 
        y_axis_section_style_type=(20,10), 
    ) 
    ``` 

---

</div> 

<div id="x_axis_point_spacing"> 

- #### x_axis_point_spacing 
    The x_axis_point_spacing parameter allows your to manually set the spacing between points on the x-axis, typically measured in pixels. However, if you do not manually set this parameter, it is automatically calculated based on the length of x_axis_values.<br> 
    **Note: "auto" is the default value.** 
    <br> 

    - after configure specific value to x_axis_point_spacing, you can reset value by configure it as "auto" for set default value. 
    <br> 
        ```  python
        chart.configure(x_axis_point_spacing = "auto") 
        ``` 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=11oRyaQRFOFFbFTQH6lSsZiLdbLUndweY&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1YZeyRNvsgUKZuLfr8NbqdlKFMWAL9EMf&sz=w720" > 
    </picture> 

    ``` python
    chart = ctkchart.CTkLineChart(
        master=any_widget, 
        x_axis_point_spacing="auto" 
    ) 
    ``` 
    
    The x_axis_point_spacing parameter is automatically calculated based on the length of the x_axis_values tuple. This means that the spacing between points on the x-axis is determined by dividing the width of the chart by the length of the x_axis_values list. 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1LC0SkXUmKS9N5mx52GE2_ZoafRObrtNv&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1SJvjLOJrfMRcnAwEaPm_yveIhu3gbFS6&sz=w720" > 
    </picture> 

    When you set the x_axis_point_spacing parameter to a specific value, such as 40, it means that you have manually specified the spacing between points on the x-axis to be 40 units (e.g., pixels). In this case, the chart will use the user-defined spacing of 40 units between each point on the x-axis, regardless of the length of the x_axis_values tuple. 

    ``` python
    chart = ctkchart.CTkLineChart(
        master=any_widget, 
        x_axis_point_spacing=40 
    ) 
    ``` 

---

</div> 

### CTkLine 

<div id="line_color_size"> 

- #### color 
    refers to color of line. 

- #### size 
    refers to size(thickness) of line.<br> 
    **Note: 1 is the deafault size** 
    <br> 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1pAa1fA9Xp63VB-aCvcoHLyY_Hpa-oRfq&sz=w720"> 
    <img src="https://drive.google.com/thumbnail?id=1iFTyIyVJ2C1HhbaYHOyVx9H_F1UHCW8l&sz=w720" > 
    </picture> 

    ``` python
    line = ctkchart.CTkLine(
        master=chart, 
        color="#30ACC7", 
        size=5 
    ) 
    ``` 

</div> 

<div id="line_style"> 

- #### style 
    style parameter allows you to define the visual style of the line. 
    <br> 
    - supported styles: 
        - "dashed": When you set style to "dashed", the line is displayed as dashed line. 
        - "dotted": When you set style to "dotted", the line is displayed as dotted line. 
        - "normal": When you set style to "normal", the line is displayed as solid line.
        <br> 
    **Note: "normal" is the default style.** 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1JmL02oCW0iWuXcCMBYlwqs4zlk37ptqp&sz=w1050"> 
    <img src="https://drive.google.com/thumbnail?id=1FRATeOC2GRsv4l5nchVopvtUSmUqR-hW&sz=w1050" > 
    </picture> 

    ``` python
    line = ctkchart.CTkLine(
        master=chart, 
        line_style="dashed" 
    ) 
    ```
    
---

</div> 

<div id="line_style_type"> 

- #### style_type 
    The style_type parameter is a tuple that contains two integer values, specifying the style of the dashes and dots used when the style is set to "dashed" or "dotted". 

    For example: 
    - If you set style_type to (20, 10), it means: 
        - The width of each dash or size of each dot is 20 pixels. 
        - The spacing between dashes or dots is 10 pixels. 

    **Note: In the "dotted" style, the size parameter is irrelevant as the dots are of fixed size determined by the style_type tuple.**<br> 
    **Note: In the "normal" style, the style_type parameter is do nothing.** 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1V3bEduu9-5IZDJR6ONxep2SIKBe_gYGp&sz=w720"> 
    <img src="https://drive.google.com/thumbnail?id=1AK70nKWqZ04frfx90YB6wqzYjEmQoZqF&sz=w720" > 
    </picture> 

    ``` python
    line = ctkchart.CTkLine(
        master=chart, 
        line_style="dashed", 
        line_style_type=(10,2) 
    ) 
    ``` 

---

</div> 

<div id="point_highlight"> 

- #### point_highlight 
    The point_highlight parameter is used to control point highlight, enabling or disabling it. 
    <br> 
    - Supported values: 
        - "enabled": Enable point highlight. 
        - "disabled": Disable point highlight. 

- #### point_highlight_size 
    The point_highlight_size is used to set size of the highlight. 

- #### point_highlight_color 
    The point_highlight_color used to control color of highlight. 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1HJHapDIDYKstmGKekFHEA4-xxw5Ez-Vi&sz=w1000"> 
    <img src="https://drive.google.com/thumbnail?id=1WmHPyqtt6W1DQVtmM0beYE6S800x_Hfh&sz=w1000" > 
    </picture> 

    ``` python
    line = ctkchart.CTkLine(
        master=chart, 
        point_highlight="enabled", 
        point_highlight_color="#80CCFF", 
        point_highlight_size=8 
    ) 
    ``` 

---

</div> 

<div id="fill"> 

- #### fill 
    The fill parameter is utilized to control whether line fill is enabled or disabled. 
    <br> 
    - Supported Values: 
        - "enabled": Enable line fill. 
        - "disabled": Disable line fill. 

- #### fill_color 
    The fill_color parameter is used to specify the color for the fill. 

    <picture> 
    <source media="(prefers-color-scheme: dark)" srcset="https://drive.google.com/thumbnail?id=1j7tjTNZSqr7frhbuUPpc_gktl_7Fp7cg&sz=w950"> 
    <img src="https://drive.google.com/thumbnail?id=1Un5x0Aetoq0LUE6piGPjsCoJt1mpjxCE&sz=w950" > 
    </picture> 

    ``` python
    line = ctkchart.CTkLine(
        master=chart, 
        fill="enabled", 
        fill_color="#5D6DB6" 
    ) 
    ``` 

---

</div> 

</div> 

<div id="theme_change"> 

## Dynamic Color Change 

***For every parameter that involves color in ctkchart, you can provide either***: 

- A single string representing the color. 
- A tuple of two strings where the first string represents the color for the light theme and the second string represents the color for the dark theme. 

</div> 

---

<div id="example"> 

<a href="#top">**Back to the Top**</a> | <a href="#howtouse">**Usage Guide**</a> | <a href="#parameter_explanation">**Parameter Explanation**</a> | <a href="../CHANGES_en.md">**Whats New ?**</a> 

## [Examples](https://github.com/Thisal-D/ctkchart/tree/main/template(s))

<div align="center"> 

<img src="https://drive.google.com/thumbnail?id=1PoDTZqd2SZG7mNVBJgmpVBHGLaG-vH7K&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1BhX8vEuLFysgFh8jyfWuWX-bYLb_qqfS&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1rA4Fe9fog7ny841IBnJNedScY936EoQT&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1-BOYqyb8ixX2VbpseDkJOpKBABnGAJZf&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1AknbWhYCDYZ03M--zKaJhNcCoTOyhL9K&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=17flH38q_0Z9S3Gep20dqZi-tCUO79L62&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1EK8GKI-_E9pkQwgLdywWMm9uqJoEl_FO&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1ex0cdh_Ml4duZ8taYOB04rsX8CLl88i9&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1ghuhCoz7srDme8_2b3DFUfxnxVsd8-hP&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1WFunUzibiEopRqZjaJD9DLsoln9YAa8B&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1NwTavf0nuUAjR0qJfIzo3dfBoNKSsQ8S&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1oMUERN5WDApzRlnNul00VUrbd-Ty7fPW&sz=w720" style="width: 50%"> 

<img src="https://drive.google.com/thumbnail?id=1hgssGvZLUGkZ_knFtcf82f-TS7seeHZm&sz=w720" style="width: 50%"><img src="https://drive.google.com/thumbnail?id=1JsI0L4BmbyPGihnnZ2s3mpYOcmkpIaJU&sz=w720" style="width: 50%"> 

</div> 

</div> 

---

## Links 

**PyPi.org** : <a href="https://pypi.org/project/ctkchart" target="_blank" ><i>ctkchart</i></a> 

**GitHub.com** : <a href="https://github.com/Thisal-D/ctkchart" target="_blank" ><i>ctkchart</i></a> 