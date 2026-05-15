from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from android import PythonService

class PhishGuardApp(App):
    def build(self):
        # ব্যাকগ্রাউন্ড সার্ভিস স্টার্ট করা
        service = PythonService('PhishGuard', 'monitor')
        service.start('service arguments')
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="PhishGuard Active", font_size='30sp'))
        layout.add_widget(Label(text="Monitoring SMS & Notifications..."))
        return layout

if __name__ == '__main__':
    PhishGuardApp().run()
