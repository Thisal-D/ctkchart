## v2.1.4

- ### New Method Added to CTkLineChart Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `get_line_area` | Get the are of specific line                               | line: `ctkchart.CTkLine` | ``float`` | 
    | `get_lines_area`   | Get the are of all lines                                   | -                    | ``float`` | 

## v2.1.3

- ### New Method Added to CTkLineChart Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `destroy`        | Destroy the line chart, along with its lines               | -              | `None`      |

- ### New Method Added to CTkLine Object
    | Method Name      | Description                                                | Parameters     | Return Type |
    |------------------|------------------------------------------------------------|----------------|-------------|
    | `destroy`        | Destroy the line                                           | -              | `None`      |

## v2.1.2

- ### New Method Added to CTkLine Object

    | Method Name      | Description                                    | Parameters                              | Return Type |
    |------------------|------------------------------------------------|------------------------------------------|-------------|
    | `cget`           | Get the value of the specified parameter      | `attribute_name: str \| "__all__"`       | `any`       |
    | `set_visible`    | Change the visibility of the line             | `state: bool`                            | `None`      |
    | `get_visibility` | Get the visibility of the line                | -                                        | `bool`      |

- ### New Methods Added to CTkLineChart Object

    | Method Name            | Description                                    | Parameters                                       | Return Type |
    |------------------------|------------------------------------------------|--------------------------------------------------|-------------|
    | `set_lines_visibility` | Change the visibility of all the lines        | `state: bool`                                   | `None`      |
    | `set_line_visibility`  | Change the visibility of a specific line      | `line: ctkchart.CTkLine`<br>`state: bool`       | `None`      |
    | `get_line_visibility`  | Get the visibility of a specific line         | `line: ctkchart.CTkLine`                        | `bool`      |
    | `cget`        | Get the value of the specified parameter| `attribute_name: str \| "__all__"`       | `any`       |
    | `place_info`  | Get info about place                    | `attribute_name: str \| "__all__"`       | `any`       |
    | `pack_info`   | Get info about pack                     | `attribute_name: str \| "__all__"`       | `any`       |
    | `grid_info`   | Get info about grid                     | `attribute_name: str \| "__all__"`       | `any`       |

- ### Removed Methods in CTkLineChart

    | Method Name | Description          | Parameters                                   | Return Type |
    |-------------|----------------------|----------------------------------------------|-------------|
    | hide_all    | Hide all the lines   | state:  ``bool``                             | None        |
    | hide        | hide a specific line | line:  ``ctkchart.CTkLine``<br> state:  ``bool`` | None        |
