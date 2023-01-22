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

        self._widgets: dict[str, tk.Widget] = {}
        self._buttons: dict[str, tk.Button] = {}
        self._inputs: dict[str, tk.Text] = {}
        self._frames: dict[str, tk.Frame] = {}
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
    def inputs(self):
        return self._inputs

    @property
    def frames(self):
        return self._frames

    def add_frame(self, name: str, row, col, bg_color="GREEN"):
        f = tk.Frame(self.app, bg=bg_color)
        self.frames[f"{name}"] = f

    def add_button(self, text: str, callback: Callable, frame=""):
        assert isinstance(callback, Callable)
        f = self.app if not frame else self.frames[frame]
        b = tk.Button(
            f,
            text=text,
            command=callback,
        )
        self.widgets[f"{text} button"] = b
        self.buttons[f"{text}"] = b

    def add_input(self, name, width, height, frame=""):
        f = self.app if not frame else self.frames[frame]
        tb = tk.Text(
            f,
            width=width,
            height=height,
        )
        self.inputs[name] = tb
        self.widgets[f"{name} input"] = tb

    def setup_widgets(self):
        for w in self.widgets.values():
            w.pack()
        for n, f in self.frames.items():
            if n == "left":
                f.pack(side=tk.LEFT)
            elif n == "right":
                f.pack(side=tk.RIGHT)

    def get_input(self, name: str):
        return self.inputs[f"{name}"].get(
            "1.0",
            tk.END,
        )

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
