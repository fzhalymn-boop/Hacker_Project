from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

KV = '''
MDScreen:
    md_bg_color: 0, 0, 0, 1
    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "20dp"

        MDLabel:
            text: "TERMINAL EXPLOIT v9.0"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1
            font_style: "H4"
            bold: True

        MDTextField:
            id: target_num
            hint_text: "ENTER TARGET NUMBER"
            current_hint_text_color: 0, 1, 0, 1
            line_color_focus: 0, 1, 0, 1
            text_color_normal: 0, 1, 0, 1

        MDRaisedButton:
            text: "START INJECTION"
            md_bg_color: 1, 0, 0, 1
            pos_hint: {"center_x": .5}
            on_release: app.start_process()

        MDProgressBar:
            id: progress
            value: 0
            color: 0, 1, 0, 1

        MDLabel:
            id: status
            text: "STATUS: WAITING..."
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 1, 0, 1
'''

class HackerApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def start_process(self):
        if self.root.ids.target_num.text:
            self.root.ids.status.text = "INJECTING EXPLOIT..."
            Clock.schedule_interval(self.update_bar, 0.1)

    def update_bar(self, dt):
        if self.root.ids.progress.value < 100:
            self.root.ids.progress.value += 1
            return True
        else:
            self.root.ids.status.text = "ACCESS GRANTED"
            return False

if __name__ == "__main__":
    HackerApp().run()
