AnchorLayoutExemple:
# MainWidget:

<AnchorLayoutExemple>:
    Button:
        text: "Moi"
        size_hint: .5, .5
        height: "60dp"
        # x, right, center_x
        # y, top, center_y
        pos_hint: { 'top': .5} 
    Button:
        text: "Toi"
#<BoxLayoutExemple>:
    orientation: "vertical"
    Button:
        text: "Moi"
        size_hint: .5, .5
        height: "60dp"
        # x, right, center_x
        # y, top, center_y
        pos_hint: { 'top': .5} 
    Button:
        text: "Toi"
    BoxLayout:
        orientation: "horizontal"
        Button:
            text: "A"
        Button:
            text: "B"
        Button:
            text: "C"

#<MainWidget>:
    canvas:
        Color:
            rgb: 5,4, 2
        Rectangle:
            pos: self.pos
            size: self.size
# affichage des boutons et du label
    Button:
        text: "Moi"
        size: "100dp", "50dp"
        pos: "100dp", "100dp"
        color: 1, 0, 0, 1
    Button:
        text: "Toi"
        size: "100dp", "50dp"
        pos: "300dp", "500dp"
        color: 0, 1, 0, 3
    Label:
        text: "Bienvenue sur AI"
        size: "100dp", "50dp"
        pos: "300dp", "300dp"
        color: 0, 0, 1, 1

