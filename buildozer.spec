[app]
title = PhishGuard
package.name = phishguard
package.domain = org.arvin.security
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# রিকোয়ারমেন্টস আপডেট করা হয়েছে
requirements = python3,kivy==2.2.1,requests,urllib3,certifi,pyjnius,openssl

orientation = portrait
android.permissions = INTERNET, READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, FOREGROUND_SERVICE
android.api = 33
android.minapi = 21
# NDK ভার্সন অটোমেটিক হ্যান্ডেল করতে দিন
android.private_storage = True
android.services = monitor:monitor_service.py
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
