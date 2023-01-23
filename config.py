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


def compile():
    lines = JenTex.get_input(
        "latex_input",
    )
    latex.build_pdf(lines)


JenTex.add_frame(
    name="left",
    row=0,
    col=0,
)

JenTex.add_frame(
    name="right",
    row=0,
    col=1,
)

JenTex.add_input(
    name="latex_input",
    width=100,
    height=100,
    frame="left",
)

JenTex.add_button(
    text="Compile",
    callback=compile,
    locx=1,
    locy=1
)

JenTex.add_button(
    text="Save",
    callback=save,
)
