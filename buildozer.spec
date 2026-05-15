[app]

# (str) Title of your application
title = PhishGuard

# (str) Package name
package.name = phishguard

# (str) Package domain (needed for android packaging)
package.domain = org.arvin.security

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# GitHub Actions এ স্ট্যাবিলিটির জন্য kivy ভার্সন ফিক্স করা হয়েছে
requirements = python3,kivy==2.2.1,requests,urllib3,certifi,pyjnius,openssl

# (str) Supported orientations
orientation = portrait

# -----------------------------------------------------------------------------
# Android specific configuration
# -----------------------------------------------------------------------------

# (list) Permissions
# Phishing detection এবং SMS monitoring এর জন্য প্রয়োজনীয় পারমিশন
android.permissions = INTERNET, READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, FOREGROUND_SERVICE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
# GitHub Actions এর জন্য 25b সবচেয়ে স্টেবল
android.ndk = 25b

# (bool) Use the private directory for python files
android.private_storage = True

# (list) Services to run in the background
# আপনার monitor_service.py ফাইলটিকে এখানে রেজিস্টার করা হয়েছে
android.services = monitor:monitor_service.py

# (list) Intent filters
android.manifest.intent_filters = [ {"name": "android.service.notification.NotificationListenerService", "actions": ["android.service.notification.NotificationListenerService"]} ]

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup
android.allow_backup = True

# (str) python-for-android branch to use
p4a.branch = master

# -----------------------------------------------------------------------------
# Buildozer configurations
# -----------------------------------------------------------------------------

[buildozer]

# (int) Log level (2 = debug, বিস্তারিত এরর দেখার জন্য এটি জরুরি)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
