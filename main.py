from kivy.app import App
from kivy.uix.widget import Widget
from kivy_reloader.app import App
from kivy.lang import Builder


class MainWidget(Widget):
    pass
class LeLabApp(App):
        # ÉTAPE CLÉ : On dit au reloader quels fichiers surveiller
    autoreload_files = ["LeLab.kv"] 

    def build(self):
        # On force le nettoyage du cache de Kivy avant de recharger
        Builder.unload_file("LeLab.kv")
        return Builder.load_file("LeLab.kv")
if __name__ == "__main__":
    LeLabApp().run()