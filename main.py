from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class HackerApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1) # خلفية سوداء
        self.title = "KING SAQR HACKER V1"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # العنوان بحقوقك
        header = Label(text="[color=00ff00]KING SAQR SYSTEM[/color]", 
                      markup=True, font_size='30sp', size_hint_y=None, height=100)
        layout.add_widget(header)

        # أزرار الاختراق كما في الصور
        btn_phone = Button(text="اختراق عبر رقم الهاتف", background_color=(0, 1, 0, 1))
        btn_phone.bind(on_press=lambda x: print("Phone Hack Started..."))
        layout.add_widget(btn_phone)

        btn_email = Button(text="اختراق عبر الإيميل", background_color=(0, 0.8, 0, 1))
        layout.add_widget(btn_email)

        btn_user = Button(text="اختراق اليوزر (Username)", background_color=(0, 0.6, 0, 1))
        layout.add_widget(btn_user)

        # لوحة حقوق سفلية
        footer = Label(text="ALL RIGHTS RESERVED TO KING SAQR", font_size='12sp', color=(0, 1, 0, 0.5))
        layout.add_widget(footer)
        
        return layout

HackerApp().run()
