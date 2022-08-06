from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('codemy16_Popup.kv')

class MyLayout(Widget):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)


class MyPopup(Popup):
    # @staticmethod
    def run_function(self):
        print('Button pressed')


class AwesomeApp(App):
    def build(self):
        self.my_popup = MyPopup()
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()