from app.app import App
import latex

from tkinter import filedialog

JenTex = App(
    name="JenTex",
    width=800,
    height=500,
)


def save_file(f_name: str, data):
    with open(f_name, "w") as f:
        f.write(data)


def save():
    try:
        code = JenTex.get_input("latex_input")
        output = latex.build_pdf(code)
    except:
        print("error compiling code")
        return

    directory = filedialog.askdirectory(
        initialdir="/",
        title="Save JenTex"
    )
    name = "doc"
    save_file(
        f_name=f"{directory}/{name}.tex",
        data=code
    )
    output.save_to(f"{directory}/{name}.pdf")


def build():
    """
    Builds a temporary file and
    displays it inside of its own
    tkinter window for live preview editing
    :return:
    """
    code = JenTex.get_input("latex_input")
    doc = latex.build_pdf("temp.pdf")


JenTex.add_input(
    name="latex_input",
    width=100,
    height=100,
)

JenTex.add_button(
    text="Preview",
    callback=compile,
    locx=10,
    locy=10
)

JenTex.add_button(
    text="Save",
    callback=save,
    locx=10,
    locy=10,
)
