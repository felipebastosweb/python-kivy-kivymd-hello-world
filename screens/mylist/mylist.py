from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import TwoLineListItem

class MyListScreen(MDScreen):
    # constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('screens/mylist/mylist.kv')
    # screen render
    def build(self):
        return self.screen
    
    def on_start(self):
        for i in range(20):
            self.screen.ids.md_list.add_widget(
                TwoLineListItem(text=f"Title {i}", secondary_text=f"Secundary title"
                )
            )
