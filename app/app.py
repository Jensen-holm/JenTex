import tkinter as tk


class App:
    def __init__(
            self,
            name: str,
            width: int,
            height: int,
    ):
        self.name = name
        self.width = width
        self.height = height

        self._app = tk.Tk(
            className=self.name,
        )

    @property
    def app(self):
        return self._app

    @property
    def geometry(self) -> str:
        return f"{self.width}x{self.height}"

    def config(self):
        self.app.geometry(self.geometry)

    def run(self):
        self.app.mainloop()
