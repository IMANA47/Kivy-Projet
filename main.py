from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy_reloader.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class MainWidget(Widget):
    pass

class AnchorLayoutExemple(BoxLayout):
    pass

class BoxLayoutExemple(BoxLayout):
    pass
""" code pour mettre les layouts
 def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Moi")
        b2 = Button(text="Toi")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(Button(text="Bienvenue sur AI"))
"""

class LeLabApp(App):
        # ÉTAPE CLÉ : On dit au reloader quels fichiers surveiller
    autoreload_files = ["LeLab.kv"] 

    def build(self):
        # On force le nettoyage du cache de Kivy avant de recharger
        Builder.unload_file("LeLab.kv")
        return Builder.load_file("LeLab.kv")
if __name__ == "__main__":
    LeLabApp().run()