from app.app import App
import latex

JenTex = App(
    name="JenTex",
    width=800,
    height=500,
)


def compile_button():
    lines = JenTex.get_input(
        "latex_input",
    )
    with open("document.tex", "w") as f:
        f.write(lines)
    doc = latex.build_pdf(lines)
    doc.save_to("document.pdf")


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
    text="save",
    callback=compile_button,
    frame="right"
)
