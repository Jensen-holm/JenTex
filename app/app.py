import tkinter as tk


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

        self._app = tk.Tk()

    @property
    def app(self):
        return self._app

    @property
    def geometry(self) -> str:
        return f"{self.width}x{self.height}"

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

    def run(self):
        self.config()
        self.app.mainloop()
