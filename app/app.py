import tkinter as tk
from typing import Callable


class App:
    def __init__(
            self,
            name: str,
            width: int,
            height: int,
            min_height: int = 300,
            max_height: int = 600,
            min_width: int = 500,
            max_width: int = 1000,
    ):
        self.name = name
        self.width = width
        self.height = height
        self.min_height = min_height
        self.max_height = max_height
        self.min_width = min_width
        self.max_width = max_width

        self._widgets: list[tk.Widget] = []
        self._buttons: list[tk.Button] = []
        self._entries: list[tk.Entry] = []
        self._frames: list[tk.Frame] = []
        self._app = tk.Tk()

    @property
    def app(self):
        return self._app

    @property
    def geometry(self) -> str:
        return f"{self.width}x{self.height}"

    @property
    def widgets(self):
        return self._widgets

    @property
    def buttons(self):
        return self._buttons

    @property
    def entries(self):
        return self._entries

    @property
    def frames(self):
        return self._entries

    def add_frame(self):
        return

    def add_button(self, text: str, callback: Callable):
        assert isinstance(callback, Callable)
        b = tk.Button(
            self.app,
            text=text,
            command=callback,
        )
        self.widgets.append(b)
        self.buttons.append(b)

    def setup_widgets(self):
        for w in self.widgets:
            w.pack()

    def config(self):
        self.app.title(self.name)
        self.app.geometry(self.geometry)

        self.app.minsize(
            height=self.min_height,
            width=self.min_width,
        )

        self.app.maxsize(
            height=self.max_height,
            width=self.max_width,
        )
        self.setup_widgets()

    def run(self):
        self.config()
        self.app.mainloop()
