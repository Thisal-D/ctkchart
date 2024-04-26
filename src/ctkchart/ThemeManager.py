import customtkinter as ctk
import time
from typing import List, Tuple, Any, Union
import threading


class ThemeManager:
    running_state = False
    child_objects: List = []
    theme: str = "-"

    @staticmethod
    def get_color_by_theme(color_s: Union[Tuple[str, str], str]) -> str:
        if type(color_s) is tuple:
            if ThemeManager.theme == "Light":
                return color_s[0]
            else:
                return color_s[1]
        else:
            return color_s

    @staticmethod
    def theme_tracker() -> None:
        while True:
            if ctk.get_appearance_mode() != ThemeManager.theme:
                ThemeManager.theme = ctk.get_appearance_mode()
                for child_object in ThemeManager.child_objects:
                    try:
                        child_object._CTkLineChart__configure_theme_mode()
                    except:
                        try:
                            ThemeManager.child_objects.remove(child_object)
                        except:
                            pass
            time.sleep(1)

    @staticmethod
    def run():
        running_state = True
        threading.Thread(target=ThemeManager.theme_tracker).start()

    @staticmethod
    def bind_widget(widget: Any) -> None:
        ThemeManager.child_objects.append(widget)

    @staticmethod
    def unbind_widget(widget: Any) -> None:
        try:
            ThemeManager.child_objects.remove(widget)
        except:
            pass