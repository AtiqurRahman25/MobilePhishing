from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.network.urlrequest import UrlRequest
import json

# আপনার Ngrok URL (প্রতিবার Ngrok চালু করলে এটি আপডেট করতে হবে)
SERVER_URL = "https://desecrate-elf-snack.ngrok-free.dev/predict"

class PhishGuardUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)
        
        self.add_widget(Label(text="PhishGuard: Forensic Interceptor", font_size='20sp', bold=True))
        
        self.status_label = Label(text="System: Idle", color=(1, 1, 1, 1))
        self.add_widget(self.status_label)
        
        self.add_widget(Label(text="Enable Real-Time Monitoring"))
        self.monitor_switch = Switch(active=False)
        self.monitor_switch.bind(active=self.on_switch_active)
        self.add_widget(self.monitor_switch)

    def on_switch_active(self, instance, value):
        if value:
            self.status_label.text = "System: Monitoring Active"
            self.status_label.color = (0, 1, 0, 1)
            # এখানে অ্যান্ড্রয়েড সার্ভিস স্টার্ট করার লজিক আসবে
        else:
            self.status_label.text = "System: Idle"
            self.status_label.color = (1, 1, 1, 1)

    # এই ফাংশনটি নোটিফিকেশন লিসেনার থেকে কল হবে
    def send_to_server(self, message_text):
        headers = {'Content-type': 'application/json'}
        params = json.dumps({'message': message_text})
        UrlRequest(SERVER_URL, on_success=self.on_prediction, req_body=params, req_headers=headers)

    def on_prediction(self, req, result):
        label = result.get("status")
        prob = result.get("probability")
        self.status_label.text = f"Threat Detected: {label} ({prob*100}%)"
        if label == "Malicious":
            self.status_label.color = (1, 0, 0, 1)

class PhishGuardApp(App):
    def build(self):
        return PhishGuardUI()

if __name__ == '__main__':
    PhishGuardApp().run()