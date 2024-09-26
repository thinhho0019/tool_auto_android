class ButtonStyle:
    BUTTON_SEARCH = "QPushButton {margin-top:10px;margin-bottom:5px;background-color:rgb(193, 208, 181);color:black;border:1px solid;height:30px;border-radius:8px;}"
    BUTTON_MENU = "QPushButton {margin-top:2px;margin-bottom:5px;background-color:rgb(193, 208, 181);color:black;border:1px solid;height:30px;border-radius:8px;}"
    BUTTON_CLICKED = "QPushButton {margin-top:2px;margin-bottom:5px;background-color:black;color:white;border:1px solid white;height:30px;border-radius:8px;}"
    HOVER_EFFECT_BUTTON = """
                QPushButton:hover {
                    background-color: rgb(110, 204, 175);
                    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);
                    color:white;
                    border:1px solid white
                }
                """