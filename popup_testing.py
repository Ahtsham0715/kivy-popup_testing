from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
# from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('popup_testing.kv')

class MyLayout(Widget):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
    @staticmethod
    def btn():
        show_popup()

    # def label_overwrite( overwrite):
    #     print(f'text: {overwrite}')
    #     # self.ids.label_1.text = overwrite
    #     # self.ids['label_1'].text = str(overwrite)
    #     show = MyLayout()
    #     show.ids.label_1.text = overwrite
        

class P(FloatLayout):
    pass
    # def press_button(self):
    #     print('Button pressed')
    #     text = self.ids.input_1.text
    #     MyLayout.label_overwrite(text)
        # self.dismiss()

class MyApp(App):
    def build(self):
        return MyLayout()

def show_popup():
    show = P()
    popupWindow = Popup(title='PopupWindow', content=show, size_hint=(.6, .3), auto_dismiss=True)
    popupWindow.open()

if __name__ == '__main__':
    MyApp().run()
