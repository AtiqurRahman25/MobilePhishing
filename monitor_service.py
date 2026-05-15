import time
import requests
from jnius import autoclass

# অ্যান্ড্রয়েড ক্লাসগুলো লোড করা
Context = autoclass('android.content.Context')
PythonService = autoclass('org.kivy.android.PythonService')

def start_monitoring():
    # আপনার Ngrok URL এখানে দিন
    SERVER_URL = "https://desecrate-elf-snack.ngrok-free.dev/predict"
    
    print("Background Monitoring Started...")
    while True:
        # এখানে আপনার এসএমএস লিসেনিং লজিক রান হবে
        # ডেমোর জন্য আমরা একটি লুপ চালাচ্ছি
        time.sleep(10)

if __name__ == '__main__':
    start_monitoring()
