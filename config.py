from app.app import App

JenTex = App(
    name="JenTex",
    width=800,
    height=500,
)


def save_button():
    print("save button pressed")


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

JenTex.add_button(
    text="save",
    callback=save_button,
    frame="right",
)
