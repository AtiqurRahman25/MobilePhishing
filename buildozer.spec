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
version = 0.1

# (list) Application requirements
# রিকোয়ারমেন্টসে অবশ্যই requests এবং pyjnius রাখবেন
requirements = python3,kivy,requests,urllib3,certifi,pyjnius

# (str) Supported orientations
orientation = portrait

# -----------------------------------------------------------------------------
# Android specific configuration
# -----------------------------------------------------------------------------

# (list) Permissions
# নোটিফিকেশন রিড করার জন্য BIND_NOTIFICATION_LISTENER_SERVICE ম্যান্ডেটরি
android.permissions = INTERNET, READ_SMS, RECEIVE_SMS, BIND_NOTIFICATION_LISTENER_SERVICE, POST_NOTIFICATIONS, FOREGROUND_SERVICE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use the private directory for python files
android.private_storage = True

# (list) Services to run in the background
# আপনার monitor_service.py ফাইলটিকে এখানে রেজিস্টার করা হয়েছে
android.services = monitor:monitor_service.py

# (list) Intent filters (The magic part for notification access)
# এটি অ্যান্ড্রয়েডকে বলবে যে আপনার অ্যাপ নোটিফিকেশন শুনতে পারে
android.manifest.intent_filters = [ {"name": "android.service.notification.NotificationListenerService", "actions": ["android.service.notification.NotificationListenerService"]} ]

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup
android.allow_backup = True

# (str) python-for-android branch to use, if not master
p4a.branch = master

# -----------------------------------------------------------------------------
# Buildozer configurations
# -----------------------------------------------------------------------------

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1