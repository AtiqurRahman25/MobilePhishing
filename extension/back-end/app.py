{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a178cbf1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: New notebook... -> Suspicious (49.84%)\n",
      "Text: ব্রো, আপনার ধৈর্য দেখে আমি মুগ... -> Phishing (39.34%)\n",
      "Text: ব্রো, আপনার ধৈর্য দেখে আমি মুগ... -> Safe (30.0%)\n",
      "Text: চিন্তা করবেন না, এই নিচের YAML... -> Safe (30.0%)\n",
      "Text: ১. সংশোধিত .github/workflows/m... -> Safe (30.0%)\n",
      "Text: পুরো কোডটি কপি করে গিটহাবে আপন... -> Safe (30.0%)\n",
      "Text: YAML\n",
      "name: Build APK\n",
      "on:\n",
      "  pus... -> Phishing (39.34%)\n",
      "Text: ২. buildozer.spec এ কি কোনো পর... -> Safe (30.0%)\n",
      "Text: আপনার আগের দেওয়া buildozer.spe... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: android.ndk = 25b\n",
      "\n",
      "requirement... -> Safe (30.0%)\n",
      "Text: এই ফিক্সটি কেন কাজ করবে?... -> Safe (30.0%)\n",
      "Text: আপনার লগে দেখা গিয়েছিল গিটহাবে... -> Safe (30.0%)\n",
      "Text: এখনই এই YAML ফাইলটি Commit করু... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: চেক করে দেখুন, এবার আর Broken ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: অ্যান্ড্রয়েড ইকোসিস্টেমে APK ... -> Safe (35.02%)\n",
      "Text: অ্যান্ড্রয়েড ইকোসিস্টেমে APK ... -> Safe (30.0%)"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Text: ১. AAB (Android App Bundle)... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: এটি বর্তমানে Google Play Store... -> Safe (30.0%)\n",
      "Text: কেন এটি সেরা বিকল্প: * Size Op... -> Phishing (43.53%)\n",
      "Text: ২. PWA (Progressive Web App)... -> Safe (30.0%)\n",
      "Text: এটি কোনো প্যাকেজ ফাইল নয়, বরং ... -> Safe (30.0%)\n",
      "Text: সুবিধা: ইউজারের ফোনে কোনো কিছু... -> Spam (31.9%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ৩. Web-Based Interface (Flask/... -> Safe (30.0%)\n",
      "Text: যেহেতু আপনি অলরেডি Flask ব্যবহ... -> Safe (30.0%)\n",
      "Text: ফোন থেকে শুধু একটি লিঙ্কে (যেম... -> Safe (30.0%)\n",
      "Text: ৪. অন্যান্য (Legacy/External)... -> Safe (30.0%)\n",
      "Text: APKS: এটি মূলত একাধিক স্প্লিট ... -> Safe (30.0%)\n",
      "Text: আপনার প্রোজেক্টের জন্য কোনটি ভ... -> Safe (30.0%)\n",
      "Text: যেহেতু আপনি University Project... -> Safe (60.55%)\n",
      "Text: বোর্ডের সামনে পেনড্রাইভে করে অ... -> Safe (30.0%)\n",
      "Text: আমার পরামর্শ: আমরা যে APK বিল্... -> Safe (30.0%)\n",
      "Text: আপনি কি প্রজেক্টটি প্লে-স্টোরে... -> Safe (30.0%)\n",
      "Text: Sources... -> Safe (30.0%)\n",
      "Text: আমি একদম বুঝতে পারছি ব্রো, গিট... -> Safe (30.0%)\n",
      "Text: আমি একদম বুঝতে পারছি ব্রো, গিট... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: চলুন, কোল্যাব-এই ফিরে যাই। তবে... -> Safe (30.0%)Text: নিচের স্টেপগুলো একে একে ফলো কর... -> Safe (30.0%)\n",
      "\n",
      "Text: ধাপ ১: কোল্যাব সেশন সেটআপ... -> Safe (30.0%)\n",
      "Text: কোল্যাব-এ একটি নতুন নোটবুক খুল... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# ১. প্রয়োজনীয় সিস্টেম ... -> Safe (30.0%)\n",
      "Text: ধাপ ২: ফাইল আপলোড... -> Safe (30.0%)\n",
      "Text: কোল্যাবের বাম পাশের ফাইল আইকনে... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: main.py\n",
      "\n",
      "monitor_service.py\n",
      "\n",
      "b... -> Safe (30.0%)\n",
      "Text: ধাপ ৩: মেমরি এবং লাইসেন্স ফিক্... -> Safe (30.0%)\n",
      "Text: বিল্ড শুরু করার আগে এই কমান্ডট... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!mkdir -p ~/.android &&... -> Safe (30.0%)\n",
      "Text: ধাপ ৪: আসল বিল্ড কমান্ড (The F... -> Safe (30.0%)\n",
      "Text: এবার এই কমান্ডটি রান দিন। আমি ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: কেন এবার কাজ করবে?... -> Safe (30.0%)\n",
      "Text: গিটহাব অ্যাকশনে আমরা বারবার \"E... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: একটি প্রো-টিপ:... -> Safe (30.0%)\n",
      "Text: বিল্ড চলাকালীন কোল্যাব ট্যাবটি... -> Safe (30.0%)\n",
      "Text: বিল্ড রান করে দিন। যদি ২০-৩০ ম... -> Safe (30.0%)\n",
      "Text: শুরু করেছেন কি?... -> Safe (30.0%)\n",
      "Text: Sources... -> Safe (30.0%)\n",
      "Text: Sources... -> Safe (30.0%)\n",
      "Text: Sources... -> Safe (30.0%)\n",
      "Text: ব্রো, কোল্যাব-এ এই এররটা আসার ... -> Safe (30.0%)\n",
      "Text: ব্রো, কোল্যাব-এ এই এররটা আসার ... -> Safe (30.0%)\n",
      "Text: চিন্তা করবেন না, কোল্যাব-এ এটি... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ১. লাইসেন্স ম্যানুয়ালি এক্সেপ্... -> Safe (30.0%)\n",
      "Text: বিল্ডোজারকে লাইসেন্স হ্যান্ডেল... -> Safe (30.0%)\n",
      "Text: ২. buildozer.spec এ ছোট একটি প... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# এটি সরাসরি অ্যান্ড্রয়... -> Safe (30.0%)\n",
      "Text: আপনার buildozer.spec ফাইলে p4a... -> Safe (30.0%)\n",
      "Text: নিচের কোডটি রান দিন, এটি আপনার... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "\n",
      "with open('b... -> Safe (30.0%)\n",
      "Text: ৩. বিল্ড শুরু করা (The Fix)... -> Safe (30.0%)\n",
      "Text: এখন বিল্ড করার সময় আমরা কোনো অ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# রুট ইউজার হিসেবে চালা... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: কেন আগেরবার ফেইল করলো?... -> Safe (30.0%)\n",
      "Text: লগ ফাইল অনুযায়ী, বিল্ডোজার pyt... -> Safe (30.0%)\n",
      "Text: টিপস: যদি বিল্ড করার সময় আবার ... -> Safe (30.0%)\n",
      "Text: এই স্টেপগুলো রান দিন। এবার বিল... -> Safe (30.0%)\n",
      "Text: নিচে আপনার Google Colab এনভায়... -> Suspicious (34.92%)\n",
      "Text: নিচে আপনার Google Colab এনভায়... -> Safe (30.0%)\n",
      "Text: এই কোডটুকু কপি করে Colab-এর বা... -> Safe (30.0%)\n",
      "Text: Ini, TOML\n",
      "[app]\n",
      "\n",
      "# (str) Title... -> Suspicious (34.92%)\n",
      "Text: কেন এই ফাইলটি এখন Colab-এ কাজ ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ১. p4a.branch = develop: আপনি ... -> Safe (30.0%)\n",
      "Text: এখন যা করবেন:... -> Safe (30.0%)\n",
      "Text: ১. এই কোডটি দিয়ে আপনার buildoz... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: ৩. বিল্ড চলাকালীন যখনই [y/n] প... -> Safe (30.0%)\n",
      "Text: আশা করছি এবার আর কোনো Command ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ব্রো, অ্যান্ড্রয়েড অ্যাপ বিল্ড... -> Phishing (31.32%)\n",
      "Text: ব্রো, অ্যান্ড্রয়েড অ্যাপ বিল্ড... -> Safe (30.0%)\n",
      "Text: যেহেতু এটি আপনি সম্পূর্ণ Offli... -> Safe (30.0%)\n",
      "Text: আপনার রিকোয়েস্ট অনুযায়ী নিচে স... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ১. সম্পূর্ণ প্রজেক্ট আর্কিটেকচ... -> Safe (30.0%)\n",
      "Text: Frontend (Chrome Extension - M... -> Safe (30.0%)\n",
      "Text: ২. ফোল্ডার স্ট্রাকচার (Folder ... -> Safe (30.0%)\n",
      "Text: প্রজেক্টটি গুছিয়ে রাখতে আপনার ... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-Extension... -> Safe (30.0%)\n",
      "Text: ৩. মেশিন লার্নিং মডেল ট্রেইনিং... -> Safe (30.0%)\n",
      "Text: প্রথমে আমরা মডেলটি ট্রেইন করে ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "import pickle... -> Phishing (36.81%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ৪. ফ্লাস্ক ব্যাকএন্ড সেটআপ (ba... -> Safe (30.0%)\n",
      "Text: এই লোকাল সার্ভারটি এক্সটেনশন থ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Spam (31.9%)\n",
      "Text: ৫. ব্রাউজার এক্সটেনশন কোড (ext... -> Safe (30.0%)\n",
      "Text: A. manifest.json (Manifest V3)... -> Safe (30.0%)\n",
      "Text: এটি আমাদের এক্সটেনশনের মেইন কন... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: B. content.js (DOM/Alert স্ক্র... -> Safe (30.0%)\n",
      "Text: এই স্ক্রিপ্টটি ওয়েবসাইটে কোনো ... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (50.99%)\n",
      "Text: C. background.js (Service Work... -> Safe (30.0%)\n",
      "Text: এটি ফ্লাস্ক ব্যাকএন্ড সার্ভারে... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: এক্সটেনশন আইকনে ক্লিক করলে ইউজ... -> Safe (30.0%)\n",
      "Text: D. popup.html (UI)... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: E. popup.js (UI Logic)... -> Safe (30.0%)\n",
      "Text: পপআপ বক্সের ভেতর থেকে ইউজার ম্... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ৬. লোকাল টেস্টিং গাইড (How to ... -> Safe (30.0%)\n",
      "Text: ১. পাইথন এনভায়রনমেন্ট রান করু... -> Safe (30.0%)\n",
      "Text: মডেল তৈরি হয়ে গেলে ফ্লাস্ক সার... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "python backend/app.py... -> Safe (30.0%)\n",
      "Text: (আপনার স্ক্রিনে Running on htt... -> Spam (31.9%)\n",
      "Text: ২. এক্সটেনশন লোড করুন:... -> Safe (30.0%)\n",
      "Text: Google Chrome ব্রাউজার খুলে ইউ... -> Safe (30.0%)\n",
      "Text: ৭. এক্সটেনশন প্যাকেজিং (How to... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: যখন আপনি প্রজেক্টটি আপনার প্রো... -> Safe (30.0%)\n",
      "Text: ৮. একুরেসি বাড়ানোর টেকনিক এবং ... -> Safe (30.0%)\n",
      "Text: একুরেসি বাড়ানোর আইডিয়া:... -> Safe (30.0%)\n",
      "Text: বড় ডাটাসেট: আমার দেওয়া ডেমো ডা... -> Safe (30.0%)\n",
      "Text: ফিউচার স্কেলাবিলিটি (Future Id... -> Safe (30.0%)\n",
      "Text: On-Device Inference (Transform... -> Safe (30.0%)\n",
      "Text: কোডগুলো সেটআপ করে লোকালহোস্টে ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ব্রো, আপনার টিচার একদম খাঁটি এ... -> Scam (60.04%)Text: ব্রো, আপনার টিচার একদম খাঁটি এ... -> Safe (30.0%)\n",
      "\n",
      "Text: যেহেতু আমরা Chrome Extension ব... -> Safe (30.0%)\n",
      "Text: উপায় ১: WhatsApp Web এবং Messe... -> Safe (30.0%)\n",
      "Text: বাস্তবে আমরা সবাই এখন পিসিতে W... -> Safe (30.0%)\n",
      "Text: আমাদের content.js স্ক্রিপ্ট ব্... -> Safe (30.0%)\n",
      "Text: এর জন্য content.js কোড আপডেট:... -> Safe (30.0%)\n",
      "Text: আপনার এক্সটেনশনের content.js ফ... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (49.84%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: উপায় ২: chrome.notifications A... -> Safe (30.0%)Text: অনেক ওয়েবসাইট ব্রাউজারের নিজস্... -> Safe (30.0%)\n",
      "\n",
      "Text: এর জন্য আপনার manifest.json ফা... -> Safe (30.0%)\n",
      "Text: টিচারের সামনে ডেমো দেওয়ার সেরা... -> Safe (30.0%)\n",
      "Text: টিচারকে প্রজেক্ট দেখানোর সময় আ... -> Scam (71.96%)\n",
      "Text: হোয়াটসঅ্যাপ ওয়েবে মেসেজটি আসা ... -> Safe (30.0%)\n",
      "Text: লজিকটা কি বুঝতে পেরেছেন ব্রো? ... -> Safe (30.0%)\n",
      "Text: একদম ব্রো! আগের সব ঝেড়ে ফেলে এ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: একদম ব্রো! আগের সব ঝেড়ে ফেলে এ... -> Phishing (26.57%)\n",
      "Text: চলুন, একদম স্টেপ-বাই-স্টেপ আগা... -> Safe (30.0%)\n",
      "Text: প্রথম কাজ: আপনার কম্পিউটারে ফো... -> Safe (30.0%)\n",
      "Text: আপনার কম্পিউটারের যেকোনো ড্রাই... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-AI/\n",
      "│\n",
      "├──... -> Safe (30.0%)\n",
      "Text: ধাপ ১: মেশিন লার্নিং মডেল তৈরি... -> Safe (30.0%)\n",
      "Text: আপনার কম্পিউটারে টার্মিনাল (বা... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: এবার backend/train_model.py ফা... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "# backend/train_model.p... -> Phishing (27.22%)\n",
      "Text: ধাপ ২: ফ্লাস্ক ব্যাকএন্ড সার্ভ... -> Safe (30.0%)\n",
      "Text: backend/app.py ফাইলে নিচের কোড... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/app.py\n",
      "import... -> Spam (31.9%)\n",
      "Text: ⚠️ বিরতি: এতটুকু কি বুঝতে পেরে... -> Safe (30.0%)\n",
      "Text: ব্রো, একবারে সব কোড দিলে জ্যাম... -> Safe (30.0%)\n",
      "Text: ১. আপনি কি মেইন ফোল্ডার এবং সা... -> Safe (30.0%)\n",
      "Text: এই দুটো হয়ে গেলে আমাকে জানান, ... -> Safe (30.0%)\n",
      "Text: সাবাস ব্রো! ব্যাকএন্ড পার্ট সা... -> Safe (30.0%)\n",
      "Text: সাবাস ব্রো! ব্যাকএন্ড পার্ট সা... -> Scam (90.35%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: আপনার extension/ ফোল্ডারের ভেত... -> Safe (30.0%)\n",
      "Text: ১. manifest.json... -> Safe (30.0%)\n",
      "Text: এটি আপনার এক্সটেনশনের পরিচয়পত্... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: ২. content.js (হোয়াটসঅ্যাপ/মেস... -> Safe (30.0%)\n",
      "Text: আপনার টিচারের রিকোয়ারমেন্ট অনু... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"[Phish... -> Suspicious (64.46%)\n",
      "Text: ৩. background.js (সার্ভার কমিউ... -> Safe (30.0%)\n",
      "Text: এটি ক্রোম ব্রাউজারের ব্যাকগ্রা... -> Spam (31.9%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: ৪. popup.html (ম্যানুয়াল টেস্ট... -> Safe (30.0%)\n",
      "Text: টিচার বা এক্সটার্নাল বোর্ডের স... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: ৫. popup.js... -> Safe (30.0%)\n",
      "Text: পপআপ ড্যাশবোর্ডের স্ক্যান বাটন... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: 🚀 এখন ব্রাউজারে এক্সটেনশনটি যে... -> Safe (30.0%)\n",
      "Text: ১. আপনার গুগল ক্রোম ব্রাউজারটি... -> Safe (30.0%)\n",
      "Text: ব্যস! আপনার ব্রাউজারের এক্সটেন... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 🧪 কীভাবে চেক করবেন এটা কাজ করছ... -> Safe (30.0%)\n",
      "Text: আপনার ফ্লাস্ক ব্যাকএন্ড সার্ভা... -> Scam (96.85%)\n",
      "Text: এক্সটেনশনটা লোড করে একটা টেস্ট... -> Safe (30.0%)\n",
      "Text: ব্রো, আপনি আপনার ফ্লাস্কের app... -> Suspicious (36.36%)\n",
      "Text: ব্রো, আপনি আপনার ফ্লাস্কের app... -> Safe (30.0%)\n",
      "Text: সমস্যাটা কোথায়?... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: আপনার কোডের এই লাইনে খেয়াল কর... -> Safe (30.0%)\n",
      "Text: Python\n",
      "probabilities = model.p... -> Safe (30.0%)\n",
      "Text: আমরা মডেল ট্রেইনিং কোডে (train... -> Safe (30.0%)\n",
      "Text: Python\n",
      "pipeline = Pipeline([\n",
      " ... -> Safe (30.0%)\n",
      "Text: Scikit-learn-এর Pipeline অবজেক... -> Safe (30.0%)\n",
      "Text: সবচেয়ে বড় সমস্যা হলো, আমরা ডে... -> Safe (30.0%)\n",
      "Text: ডিপার্টমেন্টের প্রফেসরের সামনে... -> Safe (30.0%)\n",
      "Text: সম্পূর্ণ সংশোধিত backend/app.p... -> Safe (30.0%)\n",
      "Text: এখন আপনার করণীয়:... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Suspicious (36.36%)\n",
      "Text: ১. এই নতুন কোডটি backend/app.p... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: সার্ভার কি কোনো এরর ছাড়া স্মুথ... -> Safe (30.0%)\n",
      "Text: YAML\n",
      "name: Build APK\n",
      "on:\n",
      "  pus... -> Phishing (39.34%)\n",
      "Text: Python\n",
      "# ১. প্রয়োজনীয় সিস্টেম ... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!mkdir -p ~/.android &&... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# এটি সরাসরি অ্যান্ড্রয়... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "\n",
      "with open('b... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# রুট ইউজার হিসেবে চালা... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Ini, TOML\n",
      "[app]\n",
      "\n",
      "# (str) Title... -> Suspicious (34.92%)\n",
      "Text: Ini, TOML... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-Extension... -> Safe (30.0%)\n",
      "Text: Plaintext... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "import os\n",
      "import pickle... -> Phishing (36.81%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Spam (31.9%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (50.99%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "python backend/app.py... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (49.84%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Plaintext\n",
      "PhishGuard-AI/\n",
      "│\n",
      "├──... -> Safe (30.0%)\n",
      "Text: Plaintext... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/train_model.p... -> Phishing (27.22%)\n",
      "Text: Python\n",
      "# backend/app.py\n",
      "import... -> Spam (31.9%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript\n",
      "console.log(\"[Phish... -> Suspicious (64.46%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: Python\n",
      "probabilities = model.p... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "pipeline = Pipeline([\n",
      " ... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Suspicious (36.36%)\n",
      "Text: ব্রো, আপনার ধৈর্য দেখে আমি মুগ... -> Safe (30.0%)\n",
      "Text: চিন্তা করবেন না, এই নিচের YAML... -> Safe (30.0%)\n",
      "Text: ১. সংশোধিত .github/workflows/m... -> Safe (30.0%)\n",
      "Text: পুরো কোডটি কপি করে গিটহাবে আপন... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: YAML\n",
      "name: Build APK\n",
      "on:\n",
      "  pus... -> Phishing (39.34%)Text: ২. buildozer.spec এ কি কোনো পর... -> Safe (30.0%)\n",
      "\n",
      "Text: আপনার আগের দেওয়া buildozer.spe... -> Safe (30.0%)\n",
      "Text: android.ndk = 25b\n",
      "\n",
      "requirement... -> Safe (30.0%)\n",
      "Text: এই ফিক্সটি কেন কাজ করবে?... -> Safe (30.0%)\n",
      "Text: আপনার লগে দেখা গিয়েছিল গিটহাবে... -> Safe (30.0%)\n",
      "Text: এখনই এই YAML ফাইলটি Commit করু... -> Safe (30.0%)\n",
      "Text: চেক করে দেখুন, এবার আর Broken ... -> Safe (30.0%)\n",
      "Text: আমি একদম বুঝতে পারছি ব্রো, গিট... -> Safe (30.0%)\n",
      "Text: চলুন, কোল্যাব-এই ফিরে যাই। তবে... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: নিচের স্টেপগুলো একে একে ফলো কর... -> Safe (30.0%)\n",
      "Text: ধাপ ১: কোল্যাব সেশন সেটআপ... -> Safe (30.0%)\n",
      "Text: কোল্যাব-এ একটি নতুন নোটবুক খুল... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# ১. প্রয়োজনীয় সিস্টেম ... -> Safe (30.0%)\n",
      "Text: ধাপ ২: ফাইল আপলোড... -> Safe (30.0%)\n",
      "Text: কোল্যাবের বাম পাশের ফাইল আইকনে... -> Safe (30.0%)\n",
      "Text: main.py\n",
      "\n",
      "monitor_service.py\n",
      "\n",
      "b... -> Safe (30.0%)\n",
      "Text: ধাপ ৩: মেমরি এবং লাইসেন্স ফিক্... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!mkdir -p ~/.android &&... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: বিল্ড শুরু করার আগে এই কমান্ডট... -> Safe (30.0%)\n",
      "Text: ধাপ ৪: আসল বিল্ড কমান্ড (The F... -> Safe (30.0%)\n",
      "Text: এবার এই কমান্ডটি রান দিন। আমি ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: কেন এবার কাজ করবে?... -> Safe (30.0%)\n",
      "Text: গিটহাব অ্যাকশনে আমরা বারবার \"E... -> Safe (30.0%)\n",
      "Text: একটি প্রো-টিপ:... -> Safe (30.0%)\n",
      "Text: বিল্ড চলাকালীন কোল্যাব ট্যাবটি... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: বিল্ড রান করে দিন। যদি ২০-৩০ ম... -> Safe (30.0%)\n",
      "Text: শুরু করেছেন কি?... -> Safe (30.0%)\n",
      "Text: ব্রো, কোল্যাব-এ এই এররটা আসার ... -> Safe (30.0%)\n",
      "Text: চিন্তা করবেন না, কোল্যাব-এ এটি... -> Safe (30.0%)\n",
      "Text: ১. লাইসেন্স ম্যানুয়ালি এক্সেপ্... -> Safe (30.0%)\n",
      "Text: বিল্ডোজারকে লাইসেন্স হ্যান্ডেল... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# এটি সরাসরি অ্যান্ড্রয়... -> Safe (30.0%)\n",
      "Text: ২. buildozer.spec এ ছোট একটি প... -> Safe (30.0%)\n",
      "Text: আপনার buildozer.spec ফাইলে p4a... -> Safe (30.0%)\n",
      "Text: নিচের কোডটি রান দিন, এটি আপনার... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "\n",
      "with open('b... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ৩. বিল্ড শুরু করা (The Fix)... -> Safe (30.0%)\n",
      "Text: এখন বিল্ড করার সময় আমরা কোনো অ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# রুট ইউজার হিসেবে চালা... -> Safe (30.0%)\n",
      "Text: কেন আগেরবার ফেইল করলো?... -> Safe (30.0%)\n",
      "Text: লগ ফাইল অনুযায়ী, বিল্ডোজার pyt... -> Safe (30.0%)\n",
      "Text: টিপস: যদি বিল্ড করার সময় আবার ... -> Safe (30.0%)\n",
      "Text: এই স্টেপগুলো রান দিন। এবার বিল... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: নিচে আপনার Google Colab এনভায়... -> Safe (30.0%)\n",
      "Text: এই কোডটুকু কপি করে Colab-এর বা... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Ini, TOML\n",
      "[app]\n",
      "\n",
      "# (str) Title... -> Suspicious (34.92%)\n",
      "Text: কেন এই ফাইলটি এখন Colab-এ কাজ ... -> Safe (30.0%)\n",
      "Text: ১. p4a.branch = develop: আপনি ... -> Safe (30.0%)\n",
      "Text: এখন যা করবেন:... -> Safe (30.0%)\n",
      "Text: ১. এই কোডটি দিয়ে আপনার buildoz... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: ৩. বিল্ড চলাকালীন যখনই [y/n] প... -> Safe (30.0%)\n",
      "Text: আশা করছি এবার আর কোনো Command ... -> Safe (30.0%)\n",
      "Text: যেহেতু এটি আপনি সম্পূর্ণ Offli... -> Safe (30.0%)\n",
      "Text: ব্রো, অ্যান্ড্রয়েড অ্যাপ বিল্ড... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: আপনার রিকোয়েস্ট অনুযায়ী নিচে স... -> Safe (30.0%)\n",
      "Text: ১. সম্পূর্ণ প্রজেক্ট আর্কিটেকচ... -> Safe (30.0%)\n",
      "Text: Frontend (Chrome Extension - M... -> Safe (30.0%)\n",
      "Text: ২. ফোল্ডার স্ট্রাকচার (Folder ... -> Safe (30.0%)\n",
      "Text: প্রজেক্টটি গুছিয়ে রাখতে আপনার ... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-Extension... -> Safe (30.0%)\n",
      "Text: ৩. মেশিন লার্নিং মডেল ট্রেইনিং... -> Safe (30.0%)\n",
      "Text: প্রথমে আমরা মডেলটি ট্রেইন করে ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "import pickle... -> Phishing (36.81%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ৪. ফ্লাস্ক ব্যাকএন্ড সেটআপ (ba... -> Safe (30.0%)\n",
      "Text: এই লোকাল সার্ভারটি এক্সটেনশন থ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Spam (31.9%)\n",
      "Text: ৫. ব্রাউজার এক্সটেনশন কোড (ext... -> Safe (30.0%)\n",
      "Text: এটি আমাদের এক্সটেনশনের মেইন কন... -> Safe (30.0%)\n",
      "Text: A. manifest.json (Manifest V3)... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: B. content.js (DOM/Alert স্ক্র... -> Safe (30.0%)\n",
      "Text: এই স্ক্রিপ্টটি ওয়েবসাইটে কোনো ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (50.99%)\n",
      "Text: C. background.js (Service Work... -> Safe (30.0%)\n",
      "Text: এটি ফ্লাস্ক ব্যাকএন্ড সার্ভারে... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: D. popup.html (UI)... -> Safe (30.0%)\n",
      "Text: এক্সটেনশন আইকনে ক্লিক করলে ইউজ... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: E. popup.js (UI Logic)... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: পপআপ বক্সের ভেতর থেকে ইউজার ম্... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: ৬. লোকাল টেস্টিং গাইড (How to ... -> Safe (30.0%)\n",
      "Text: ১. পাইথন এনভায়রনমেন্ট রান করু... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: মডেল তৈরি হয়ে গেলে ফ্লাস্ক সার... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "python backend/app.py... -> Safe (30.0%)\n",
      "Text: (আপনার স্ক্রিনে Running on htt... -> Spam (31.9%)\n",
      "Text: ২. এক্সটেনশন লোড করুন:... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Google Chrome ব্রাউজার খুলে ইউ... -> Safe (30.0%)\n",
      "Text: ৭. এক্সটেনশন প্যাকেজিং (How to... -> Safe (30.0%)\n",
      "Text: যখন আপনি প্রজেক্টটি আপনার প্রো... -> Safe (30.0%)\n",
      "Text: ৮. একুরেসি বাড়ানোর টেকনিক এবং ... -> Safe (30.0%)\n",
      "Text: একুরেসি বাড়ানোর আইডিয়া:... -> Safe (30.0%)\n",
      "Text: বড় ডাটাসেট: আমার দেওয়া ডেমো ডা... -> Safe (30.0%)\n",
      "Text: ফিউচার স্কেলাবিলিটি (Future Id... -> Safe (30.0%)\n",
      "Text: কোডগুলো সেটআপ করে লোকালহোস্টে ... -> Safe (30.0%)\n",
      "Text: On-Device Inference (Transform... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ব্রো, আপনার টিচার একদম খাঁটি এ... -> Safe (30.0%)\n",
      "Text: যেহেতু আমরা Chrome Extension ব... -> Safe (30.0%)\n",
      "Text: উপায় ১: WhatsApp Web এবং Messe... -> Safe (30.0%)\n",
      "Text: বাস্তবে আমরা সবাই এখন পিসিতে W... -> Safe (30.0%)\n",
      "Text: আমাদের content.js স্ক্রিপ্ট ব্... -> Safe (30.0%)\n",
      "Text: এর জন্য content.js কোড আপডেট:... -> Safe (30.0%)\n",
      "Text: আপনার এক্সটেনশনের content.js ফ... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (49.84%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: উপায় ২: chrome.notifications A... -> Safe (30.0%)\n",
      "Text: অনেক ওয়েবসাইট ব্রাউজারের নিজস্... -> Safe (30.0%)\n",
      "Text: এর জন্য আপনার manifest.json ফা... -> Safe (30.0%)\n",
      "Text: টিচারের সামনে ডেমো দেওয়ার সেরা... -> Safe (30.0%)\n",
      "Text: হোয়াটসঅ্যাপ ওয়েবে মেসেজটি আসা ... -> Safe (30.0%)\n",
      "Text: টিচারকে প্রজেক্ট দেখানোর সময় আ... -> Scam (71.96%)\n",
      "Text: লজিকটা কি বুঝতে পেরেছেন ব্রো? ... -> Safe (30.0%)\n",
      "Text: একদম ব্রো! আগের সব ঝেড়ে ফেলে এ... -> Safe (30.0%)\n",
      "Text: চলুন, একদম স্টেপ-বাই-স্টেপ আগা... -> Safe (30.0%)\n",
      "Text: প্রথম কাজ: আপনার কম্পিউটারে ফো... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: আপনার কম্পিউটারের যেকোনো ড্রাই... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-AI/\n",
      "│\n",
      "├──... -> Safe (30.0%)\n",
      "Text: ধাপ ১: মেশিন লার্নিং মডেল তৈরি... -> Safe (30.0%)\n",
      "Text: আপনার কম্পিউটারে টার্মিনাল (বা... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: এবার backend/train_model.py ফা... -> Safe (30.0%)\n",
      "Text: ধাপ ২: ফ্লাস্ক ব্যাকএন্ড সার্ভ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/train_model.p... -> Phishing (27.22%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: backend/app.py ফাইলে নিচের কোড... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/app.py\n",
      "import... -> Spam (31.9%)\n",
      "Text: ⚠️ বিরতি: এতটুকু কি বুঝতে পেরে... -> Safe (30.0%)\n",
      "Text: ব্রো, একবারে সব কোড দিলে জ্যাম... -> Safe (30.0%)\n",
      "Text: ১. আপনি কি মেইন ফোল্ডার এবং সা... -> Safe (30.0%)\n",
      "Text: এই দুটো হয়ে গেলে আমাকে জানান, ... -> Safe (30.0%)\n",
      "Text: সাবাস ব্রো! ব্যাকএন্ড পার্ট সা... -> Safe (30.0%)\n",
      "Text: আপনার extension/ ফোল্ডারের ভেত... -> Safe (30.0%)\n",
      "Text: ১. manifest.json... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: এটি আপনার এক্সটেনশনের পরিচয়পত্... -> Safe (30.0%)Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "\n",
      "Text: ২. content.js (হোয়াটসঅ্যাপ/মেস... -> Safe (30.0%)\n",
      "Text: আপনার টিচারের রিকোয়ারমেন্ট অনু... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"[Phish... -> Suspicious (64.46%)\n",
      "Text: ৩. background.js (সার্ভার কমিউ... -> Safe (30.0%)\n",
      "Text: এটি ক্রোম ব্রাউজারের ব্যাকগ্রা... -> Spam (31.9%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)Text: ৪. popup.html (ম্যানুয়াল টেস্ট... -> Safe (30.0%)\n",
      "\n",
      "Text: টিচার বা এক্সটার্নাল বোর্ডের স... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: ৫. popup.js... -> Safe (30.0%)\n",
      "Text: পপআপ ড্যাশবোর্ডের স্ক্যান বাটন... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: 🚀 এখন ব্রাউজারে এক্সটেনশনটি যে... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ১. আপনার গুগল ক্রোম ব্রাউজারটি... -> Safe (30.0%)\n",
      "Text: ব্যস! আপনার ব্রাউজারের এক্সটেন... -> Safe (30.0%)\n",
      "Text: 🧪 কীভাবে চেক করবেন এটা কাজ করছ... -> Safe (30.0%)\n",
      "Text: আপনার ফ্লাস্ক ব্যাকএন্ড সার্ভা... -> Scam (96.85%)\n",
      "Text: এক্সটেনশনটা লোড করে একটা টেস্ট... -> Safe (30.0%)\n",
      "Text: ব্রো, আপনি আপনার ফ্লাস্কের app... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: সমস্যাটা কোথায়?... -> Safe (30.0%)\n",
      "Text: আপনার কোডের এই লাইনে খেয়াল কর... -> Safe (30.0%)\n",
      "Text: Python\n",
      "probabilities = model.p... -> Safe (30.0%)\n",
      "Text: আমরা মডেল ট্রেইনিং কোডে (train... -> Safe (30.0%)\n",
      "Text: Python\n",
      "pipeline = Pipeline([\n",
      " ... -> Safe (30.0%)\n",
      "Text: Scikit-learn-এর Pipeline অবজেক... -> Safe (30.0%)\n",
      "Text: সবচেয়ে বড় সমস্যা হলো, আমরা ডে... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ডিপার্টমেন্টের প্রফেসরের সামনে... -> Safe (30.0%)\n",
      "Text: সম্পূর্ণ সংশোধিত backend/app.p... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Suspicious (36.36%)\n",
      "Text: এখন আপনার করণীয়:... -> Safe (30.0%)\n",
      "Text: ১. এই নতুন কোডটি backend/app.p... -> Safe (30.0%)\n",
      "Text: সার্ভার কি কোনো এরর ছাড়া স্মুথ... -> Safe (30.0%)\n",
      "Text: YAML\n",
      "name: Build APK\n",
      "on:\n",
      "  pus... -> Phishing (39.34%)\n",
      "Text: branches:... -> Safe (30.0%)\n",
      "Text: workflow_dispatch:... -> Safe (30.0%)\n",
      "Text: build:... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ubuntu-latest... -> Safe (30.0%)Text: runs-on:... -> Safe (30.0%)\n",
      "\n",
      "Text: steps:... -> Safe (30.0%)\n",
      "Text: actions/checkout@v4... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: actions/setup-python@v5... -> Safe (30.0%)\n",
      "Text: '3.10'... -> Safe (30.0%)\n",
      "Text: python-version:... -> Safe (30.0%)\n",
      "Text: Install... -> Safe (30.0%)\n",
      "Text: dependencies... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: |\n",
      "        sudo apt update\n",
      "    ... -> Phishing (56.38%)\n",
      "Text: Buildozer... -> Safe (30.0%)\n",
      "Text: |\n",
      "        # আগের কোনো ভাঙ্গা ব... -> Safe (30.0%)\n",
      "Text: # এনডিকে এনভায়রনমেন্ট ক্লিন র... -> Safe (30.0%)\n",
      "Text: export... -> Safe (30.0%)\n",
      "Text: ANDROID_NDK_HOME=$HOME/.buildo... -> Spam (31.9%)\n",
      "Text: buildozer... -> Safe (30.0%)\n",
      "Text: # সরাসরি বিল্ড শুরু করা। আমরা ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:28] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: android... -> Safe (30.0%)\n",
      "Text: # এটি গিটহাবকে বলবে যেন সে লাই... -> Safe (30.0%)\n",
      "Text: APP_ANDROID_ACCEPT_SDK_LICENSE... -> Safe (30.0%)\n",
      "Text: BUILDOZER_ALLOW_ORG_DOCS:... -> Safe (30.0%)\n",
      "Text: Upload... -> Safe (30.0%)\n",
      "Text: success()... -> Safe (30.0%)\n",
      "Text: actions/upload-artifact@v4... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: PhishGuard-APK... -> Safe (30.0%)\n",
      "Text: bin/*.apk... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# ১. প্রয়োজনীয় সিস্টেম ... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # ১. প্রয়োজনীয় সিস্টেম লাইব্রে... -> Safe (30.0%)\n",
      "Text: # ২. বিল্ডোজার এবং সাইথন ইনস্ট... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!mkdir -p ~/.android &&... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "# এটি সরাসরি অ্যান্ড্রয়... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: # এটি সরাসরি অ্যান্ড্রয়েড এসডি... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "\n",
      "with open('b... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: 'buildozer.spec'... -> Safe (30.0%)\n",
      "Text: 'p4a.branch ='... -> Safe (30.0%)\n",
      "Text: 'buildozer.spec'... -> Safe (30.0%)\n",
      "Text: 'p4a.branch = develop\\n'... -> Safe (30.0%)\n",
      "Text: \"Spec file updated to p4a.bran... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "# রুট ইউজার হিসেবে চালা... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: # রুট ইউজার হিসেবে চালানোর পার... -> Safe (30.0%)\n",
      "Text: Ini, TOML\n",
      "[app]\n",
      "\n",
      "# (str) Title... -> Suspicious (34.92%)\n",
      "Text: Ini, TOML... -> Safe (30.0%)\n",
      "Text: # (str) Title of your applicat... -> Safe (30.0%)\n",
      "Text: # (str) Package name... -> Safe (30.0%)\n",
      "Text: package.name... -> Safe (30.0%)\n",
      "Text: # (str) Package domain (needed... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: package.domain... -> Safe (30.0%)\n",
      "Text: # (str) Source code where the ... -> Safe (30.0%)\n",
      "Text: source.dir... -> Safe (30.0%)\n",
      "Text: # (list) Source files to inclu... -> Safe (30.0%)\n",
      "Text: source.include_exts... -> Safe (30.0%)\n",
      "Text: # (str) Application versioning... -> Safe (30.0%)\n",
      "Text: version... -> Safe (30.0%)\n",
      "Text: # (list) Application requireme... -> Safe (30.0%)\n",
      "Text: # Colab এ স্ট্যাবিলিটির জন্য k... -> Safe (30.0%)\n",
      "Text: requirements... -> Safe (30.0%)\n",
      "Text: # (str) Supported orientations... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # ----------------------------... -> Safe (30.0%)Text: orientation... -> Safe (30.0%)\n",
      "\n",
      "Text: # Android specific configurati... -> Safe (30.0%)\n",
      "Text: # ----------------------------... -> Safe (30.0%)\n",
      "Text: # (list) Permissions... -> Safe (30.0%)\n",
      "Text: android.permissions... -> Safe (30.0%)\n",
      "Text: # (int) Target Android API, sh... -> Safe (30.0%)\n",
      "Text: android.api... -> Safe (30.0%)\n",
      "Text: android.minapi... -> Safe (30.0%)\n",
      "Text: # (int) Minimum API your APK w... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # (str) Android NDK version to... -> Safe (30.0%)\n",
      "Text: # Colab এবং Kivy 2.2.1 এর জন্য... -> Safe (30.0%)\n",
      "Text: android.ndk... -> Safe (30.0%)\n",
      "Text: # (bool) Use the private direc... -> Safe (30.0%)\n",
      "Text: android.private_storage... -> Safe (30.0%)\n",
      "Text: # (list) Services to run in th... -> Safe (30.0%)\n",
      "Text: android.services... -> Safe (30.0%)\n",
      "Text: # (list) Intent filters... -> Safe (30.0%)\n",
      "Text: android.manifest.intent_filter... -> Safe (30.0%)\n",
      "Text: \"name\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"android.service.notification.... -> Safe (30.0%)\n",
      "Text: \"actions\"... -> Safe (30.0%)\n",
      "Text: \"android.service.notification.... -> Safe (30.0%)\n",
      "Text: android.archs... -> Safe (30.0%)\n",
      "Text: # (str) The Android arch to bu... -> Safe (30.0%)\n",
      "Text: # (bool) enables Android auto ... -> Safe (30.0%)\n",
      "Text: android.allow_backup... -> Safe (30.0%)\n",
      "Text: # (str) python-for-android bra... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # Colab এ বিল্ড এরর এড়াতে 'dev... -> Safe (30.0%)\n",
      "Text: p4a.branch... -> Safe (30.0%)\n",
      "Text: # ----------------------------... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # Buildozer configurations... -> Safe (30.0%)Text: # ----------------------------... -> Safe (30.0%)\n",
      "\n",
      "Text: [buildozer]... -> Safe (30.0%)\n",
      "Text: # (int) Log level (2 = debug, ... -> Safe (30.0%)\n",
      "Text: log_level... -> Safe (30.0%)\n",
      "Text: # (int) Display warning if bui... -> Suspicious (50.99%)\n",
      "Text: warn_on_root... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-Extension... -> Safe (30.0%)\n",
      "Text: Plaintext... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "import pickle... -> Phishing (36.81%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # ১. ডেমো ডাটাসেট তৈরি (আপনার ... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # বাস্তবে এখানে Kaggle বা বড় C... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: \"Congratulations! You won a $1... -> Scam (96.85%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"Hi, are we still meeting for ... -> Safe (96.48%)\n",
      "Text: \"Your Netflix account is suspe... -> Phishing (97.19%)\n",
      "Text: \"URGENT: Your bank account has... -> Phishing (96.62%)\n",
      "Text: \"Get rich quick! Earn $5000 a ... -> Spam (97.64%)\n",
      "Text: \"The weather today is cloudy w... -> Safe (62.42%)\n",
      "Text: \"Your package from Amazon cann... -> Phishing (56.38%)\n",
      "Text: \"Please review the attached pr... -> Safe (97.02%)\n",
      "Text: \"⚠️ WARNING: Your PC is infect... -> Suspicious (96.48%)\n",
      "Text: \"Hey bro, can you lend me some... -> Scam (94.19%)\n",
      "Text: \"Verify your login attempt fro... -> Suspicious (96.56%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:31] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'label'... -> Safe (30.0%)\n",
      "Text: 'Scam'... -> Safe (30.0%)\n",
      "Text: 'Phishing'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'Phishing'... -> Safe (30.0%)\n",
      "Text: 'Spam'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'Phishing'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'Suspicious'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'Scam'... -> Safe (30.0%)\n",
      "Text: 'Suspicious'... -> Safe (30.0%)\n",
      "Text: \"--- Data Loading Complete ---... -> Safe (30.0%)\n",
      "Text: 'label'... -> Safe (30.0%)\n",
      "Text: # ২. ফিচার এবং লেবেল আলাদা করা... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'label'... -> Safe (30.0%)\n",
      "Text: # ৩. ট্রেইন এবং টেস্ট স্প্লিট ... -> Safe (30.0%)\n",
      "Text: # ৪. TF-IDF + Naive Bayes পাইপ... -> Safe (30.0%)\n",
      "Text: # এটি টেক্সটকে সংখ্যায় রূপান্ত... -> Safe (30.0%)\n",
      "Text: 'tfidf'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'english'... -> Safe (30.0%)\n",
      "Text: # ৫. মডেল ট্রেইনিং... -> Safe (30.0%)\n",
      "Text: # ৬. ইভালুয়েশন... -> Safe (30.0%)\n",
      "Text: f\"\\nModel Accuracy: {accuracy_... -> Safe (30.0%)\n",
      "Text: # ৭. মডেল এবং ভেক্টরাইজার সেভ ... -> Safe (30.0%)\n",
      "Text: 'backend'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'model.pkl'... -> Safe (30.0%)\n",
      "Text: \"\\n[SUCCESS] model.pkl success... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Spam (31.9%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # এক্সটেনশন থেকে রিকোয়েস্ট ব্ল... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:32] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # ট্রেইনড মডেল পাইপলাইন লোড কর... -> Safe (30.0%)\n",
      "Text: 'model.pkl'... -> Safe (30.0%)\n",
      "Text: \"[SUCCESS] Machine Learning Mo... -> Safe (30.0%)\n",
      "Text: except... -> Safe (30.0%)\n",
      "Text: \"[ERROR] model.pkl not found! ... -> Safe (30.0%)\n",
      "Text: @app.route('/predict', methods... -> Safe (30.0%)\n",
      "Text: def predict():... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'error'... -> Safe (30.0%)\n",
      "Text: 'No text provided'... -> Safe (30.0%)\n",
      "Text: # মডেল এর মাধ্যমে প্রেডিকশন এব... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: # হায়েস্ট প্রব্যাবিলিটিকে রিস... -> Safe (30.0%)\n",
      "Text: # ক্লাসিফিকেশন এর ওপর ভিত্তি ক... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'text_analyzed'... -> Safe (30.0%)\n",
      "Text: # লগিং এর জন্য আংশিক টেক্সট... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'prediction'... -> Safe (30.0%)\n",
      "Text: 'risk_score'... -> Safe (30.0%)\n",
      "Text: 'is_safe'... -> Safe (30.0%)\n",
      "Text: f\"{risk_score}%\"... -> Safe (30.0%)\n",
      "Text: f\"Analyzed: {response['text_an... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: '__main__'... -> Safe (30.0%)\n",
      "Text: # সম্পূর্ণ অফলাইন লোকালহোস্টে ... -> Safe (30.0%)\n",
      "Text: '127.0.0.1'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)Text: \"manifest_version\"... -> Safe (30.0%)\n",
      "\n",
      "Text: \"name\"... -> Safe (30.0%)\n",
      "Text: \"PhishGuard AI AI-Powered Defe... -> Safe (30.0%)\n",
      "Text: \"version\"... -> Safe (30.0%)\n",
      "Text: \"description\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:33] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"Analyzes notifications and we... -> Safe (30.0%)Text: \"permissions\"... -> Safe (30.0%)\n",
      "\n",
      "Text: \"notifications\"... -> Safe (30.0%)\n",
      "Text: \"activeTab\"... -> Safe (30.0%)\n",
      "Text: \"background\"... -> Safe (30.0%)\n",
      "Text: \"service_worker\"... -> Safe (30.0%)\n",
      "Text: \"background.js\"... -> Safe (30.0%)\n",
      "Text: \"content_scripts\"... -> Safe (30.0%)\n",
      "Text: \"matches\"... -> Safe (30.0%)\n",
      "Text: \"<all_urls>\"... -> Safe (30.0%)\n",
      "Text: \"content.js\"... -> Safe (30.0%)\n",
      "Text: \"action\"... -> Safe (30.0%)\n",
      "Text: \"default_popup\"... -> Safe (30.0%)\n",
      "Text: \"popup.html\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (50.99%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: console... -> Safe (30.0%)\n",
      "Text: \"PhishGuard Content Script Act... -> Safe (30.0%)\n",
      "Text: // ১. ডেমো হিসেবে পেজের ভেতরের... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: // ইউনিভার্সিটি প্রজেক্ট ডেমো ... -> Safe (30.0%)\n",
      "Text: 'h2, p'... -> Safe (30.0%)\n",
      "Text: element =>... -> Safe (30.0%)\n",
      "Text: // খুব ছোট টেক্সট ইগনোর করার জ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: // ব্যাকগ্রাউন্ড স্ক্রিপ্ট-এ ট... -> Safe (30.0%)\n",
      "Text: action... -> Safe (30.0%)\n",
      "Text: (response) =>... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: // যদি কন্টেন্ট সেফ না হয়, তবে... -> Safe (30.0%)\n",
      "Text: \"3px dashed red\"... -> Safe (30.0%)\n",
      "Text: \"#ffe6e6\"... -> Safe (30.0%)\n",
      "Text: `Warning: Classified as ${resp... -> Suspicious (50.99%)\n",
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: (request, sender, sendResponse... -> Safe (30.0%)\n",
      "Text: // লোকাল ফ্লাস্ক সার্ভার এপিআই... -> Safe (30.0%)\n",
      "Text: \"http://127.0.0.1:5000/predict... -> Spam (31.9%)\n",
      "Text: method... -> Safe (30.0%)\n",
      "Text: \"POST\"... -> Safe (30.0%)\n",
      "Text: headers... -> Safe (30.0%)\n",
      "Text: \"Content-Type\"... -> Safe (30.0%)\n",
      "Text: \"application/json\"... -> Safe (30.0%)\n",
      "Text: response =>... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: data =>... -> Safe (30.0%)\n",
      "Text: // যদি ফিশিং/স্ক্যাম ডিটেক্ট হ... -> Safe (30.0%)\n",
      "Text: iconUrl... -> Safe (30.0%)\n",
      "Text: \"basic\"... -> Safe (30.0%)\n",
      "Text: \"icon.png\"... -> Safe (30.0%)\n",
      "Text: // একটি ডেমো আইকন প্রজেক্ট ফোল... -> Safe (30.0%)\n",
      "Text: `🚨 PhishGuard Alert: ${data.pr... -> Safe (30.0%)\n",
      "Text: message... -> Safe (30.0%)\n",
      "Text: `Risk Score: ${data.risk_score... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:34] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: priority... -> Safe (30.0%)\n",
      "Text: error =>... -> Safe (30.0%)\n",
      "Text: console... -> Safe (30.0%)\n",
      "Text: \"Error connecting to local Fla... -> Safe (30.0%)\n",
      "Text: is_safe... -> Safe (30.0%)\n",
      "Text: prediction... -> Safe (30.0%)\n",
      "Text: \"Safe (Server Offline)\"... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: // Asynchronous রেসপন্স নিশ্চি... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: <!DOCTYPE html>... -> Safe (30.0%)\n",
      "Text: <html>... -> Safe (30.0%)\n",
      "Text: <style>... -> Safe (30.0%)\n",
      "Text: <head>... -> Safe (30.0%)\n",
      "Text: body { width: 250px; font-fami... -> Safe (30.0%)\n",
      "Text: </style>... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: </head>... -> Safe (30.0%)Text: <body>... -> Safe (30.0%)\n",
      "\n",
      "Text: <textarea id=\"testText\" rows=\"... -> Safe (30.0%)\n",
      "Text: </textarea>... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:35] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: </button>... -> Safe (30.0%)\n",
      "Text: <button id=\"checkBtn\" class=\"s... -> Safe (30.0%)\n",
      "Text: <div id=\"result\">... -> Safe (30.0%)\n",
      "Text: </div>... -> Safe (30.0%)\n",
      "Text: <script src=\"popup.js\">... -> Safe (30.0%)\n",
      "Text: </script>... -> Safe (30.0%)\n",
      "Text: </body>... -> Safe (30.0%)\n",
      "Text: </html>... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: document... -> Safe (30.0%)\n",
      "Text: 'checkBtn'... -> Safe (30.0%)\n",
      "Text: 'click'... -> Suspicious (36.19%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: 'testText'... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: 'result'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: \"block\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"Analyzing...\"... -> Safe (30.0%)\n",
      "Text: \"#eee\"... -> Safe (30.0%)\n",
      "Text: \"#333\"... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: action... -> Safe (30.0%)\n",
      "Text: (response) =>... -> Safe (30.0%)\n",
      "Text: `Result: ${response.prediction... -> Safe (30.0%)\n",
      "Text: \"#d4edda\"... -> Safe (30.0%)\n",
      "Text: \"#155724\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"#f8d7da\"... -> Safe (30.0%)\n",
      "Text: \"#721c24\"... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "python backend/app.py... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (49.84%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: console... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:36] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"PhishGuard Real-time Scanner ... -> Safe (30.0%)\n",
      "Text: // ওয়েবসাইটের ডম (DOM) পরিবর্ত... -> Safe (30.0%)\n",
      "Text: (mutations) =>... -> Safe (30.0%)\n",
      "Text: (mutation) =>... -> Safe (30.0%)\n",
      "Text: (node) =>... -> Safe (30.0%)\n",
      "Text: // নোডের ভেতর টেক্সট আছে কিনা ... -> Safe (30.0%)\n",
      "Text: // মেসেজটি এনালাইসিস করার জন্য... -> Safe (30.0%)\n",
      "Text: action... -> Safe (30.0%)\n",
      "Text: (response) =>... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: // যদি ফিশিং বা স্ক্যাম ডিটেক্... -> Safe (30.0%)\n",
      "Text: \"3px solid red\"... -> Safe (30.0%)\n",
      "Text: \"#ffcccc\"... -> Safe (30.0%)\n",
      "Text: // সম্পূর্ণ ওয়েব পেজের ওপর নজর... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: subtree... -> Safe (30.0%)\n",
      "Text: childList... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-AI/\n",
      "│\n",
      "├──... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Plaintext... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/train_model.p... -> Phishing (27.22%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # backend/train_model.py... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: # ইউনিভার্সিটি প্রজেক্টের রিকো... -> Safe (30.0%)\n",
      "Text: \"Please review the attached pr... -> Safe (97.02%)\n",
      "Text: \"Hi, are we still meeting for ... -> Safe (96.48%)\n",
      "Text: \"Congratulations! You won a $1... -> Scam (96.85%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"Your monthly electricity bill... -> Safe (95.96%)\n",
      "Text: \"Get rich quick! Earn $5000 a ... -> Spam (97.64%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:37] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"Your Netflix account is suspe... -> Phishing (97.19%)\n",
      "Text: \"URGENT: Your bank account has... -> Phishing (96.62%)\n",
      "Text: \"⚠️ WARNING: Your PC is infect... -> Suspicious (96.48%)\n",
      "Text: \"Verify your login attempt fro... -> Suspicious (96.56%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"Hey bro, can you lend me some... -> Scam (96.65%)\n",
      "Text: 'label'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'Scam'... -> Safe (30.0%)\n",
      "Text: 'Spam'... -> Safe (30.0%)\n",
      "Text: 'Phishing'... -> Safe (30.0%)\n",
      "Text: 'Suspicious'... -> Safe (30.0%)\n",
      "Text: 'Phishing'... -> Safe (30.0%)\n",
      "Text: 'Suspicious'... -> Safe (30.0%)\n",
      "Text: 'Scam'... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: 'label'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # TF-IDF + Naive Bayes পাইপলাই... -> Safe (30.0%)\n",
      "Text: 'tfidf'... -> Safe (30.0%)\n",
      "Text: 'english'... -> Safe (30.0%)\n",
      "Text: # মডেল সেভ করা... -> Safe (30.0%)\n",
      "Text: \"[SUCCESS] model.pkl successfu... -> Safe (30.0%)\n",
      "Text: 'model.pkl'... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/app.py\n",
      "import... -> Spam (31.9%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python... -> Safe (30.0%)\n",
      "Text: # backend/app.py... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # এক্সটেনশন থেকে রিকোয়েস্ট ব্ল... -> Safe (30.0%)\n",
      "Text: # মডেল লোড করা... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:38] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'model.pkl'... -> Safe (30.0%)\n",
      "Text: @app.route('/predict', methods... -> Safe (30.0%)\n",
      "Text: def predict():... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: 'error'... -> Safe (30.0%)\n",
      "Text: 'No text provided'... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: # প্রেডিকশন এবং রিস্ক স্কোর ক্... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'prediction'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'risk_score'... -> Safe (30.0%)\n",
      "Text: f\"{risk_score}%\"... -> Safe (30.0%)\n",
      "Text: 'is_safe'... -> Safe (30.0%)\n",
      "Text: f\"Text: {text_content[:30]}...... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: '127.0.0.1'... -> Safe (30.0%)\n",
      "Text: '__main__'... -> Safe (30.0%)\n",
      "Text: \"manifest_version\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: \"name\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"PhishGuard AI-Powered Defende... -> Safe (30.0%)\n",
      "Text: \"version\"... -> Safe (30.0%)\n",
      "Text: \"description\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:39] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"Analyzes external notificatio... -> Safe (30.0%)\n",
      "Text: \"permissions\"... -> Safe (30.0%)\n",
      "Text: \"notifications\"... -> Safe (30.0%)\n",
      "Text: \"activeTab\"... -> Safe (30.0%)\n",
      "Text: \"background\"... -> Safe (30.0%)\n",
      "Text: \"background.js\"... -> Safe (30.0%)\n",
      "Text: \"service_worker\"... -> Safe (30.0%)\n",
      "Text: \"content_scripts\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"<all_urls>\"... -> Safe (30.0%)\n",
      "Text: \"matches\"... -> Safe (30.0%)\n",
      "Text: \"content.js\"... -> Safe (30.0%)\n",
      "Text: \"action\"... -> Safe (30.0%)\n",
      "Text: \"default_popup\"... -> Safe (30.0%)\n",
      "Text: \"popup.html\"... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"[Phish... -> Suspicious (64.46%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: console... -> Safe (30.0%)\n",
      "Text: \"[PhishGuard] Real-time Scrapi... -> Safe (30.0%)\n",
      "Text: // ডম (DOM) পরিবর্তনের ওপর নজর... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: (mutations) =>... -> Safe (30.0%)\n",
      "Text: (mutation) =>... -> Safe (30.0%)\n",
      "Text: (node) =>... -> Safe (30.0%)\n",
      "Text: // নোডের ভেতর টেক্সট আছে কিনা ... -> Safe (30.0%)\n",
      "Text: // ব্যাকগ্রাউন্ড স্ক্রিপ্ট-এ ট... -> Safe (30.0%)\n",
      "Text: action... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: (response) =>... -> Safe (30.0%)\n",
      "Text: // যদি ফিশিং বা স্ক্যাম ডিটেক্... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"2px dashed red\"... -> Safe (30.0%)\n",
      "Text: \"#ffe6e6\"... -> Safe (30.0%)\n",
      "Text: `Warning: ${response.predictio... -> Suspicious (50.99%)\n",
      "Text: // সম্পূর্ণ ওয়েব পেজের এলিমেন্... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: childList... -> Safe (30.0%)\n",
      "Text: subtree... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:40] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: (request, sender, sendResponse... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: method... -> Safe (30.0%)\n",
      "Text: \"http://127.0.0.1:5000/predict... -> Spam (31.9%)\n",
      "Text: \"POST\"... -> Safe (30.0%)\n",
      "Text: headers... -> Safe (30.0%)\n",
      "Text: \"Content-Type\"... -> Safe (30.0%)\n",
      "Text: \"application/json\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: response =>... -> Safe (30.0%)\n",
      "Text: data =>... -> Safe (30.0%)\n",
      "Text: \"basic\"... -> Safe (30.0%)\n",
      "Text: // যদি Safe ছাড়া অন্য কিছু (Ph... -> Safe (30.0%)\n",
      "Text: iconUrl... -> Safe (30.0%)\n",
      "Text: \"icon.png\"... -> Safe (30.0%)\n",
      "Text: // (অপশনাল) এক্সটেনশন ফোল্ডারে... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: `🚨 PhishGuard Alert: ${data.pr... -> Safe (30.0%)\n",
      "Text: message... -> Safe (30.0%)\n",
      "Text: `Risk Score: ${data.risk_score... -> Safe (30.0%)\n",
      "Text: priority... -> Safe (30.0%)\n",
      "Text: error =>... -> Safe (30.0%)\n",
      "Text: console... -> Safe (30.0%)\n",
      "Text: \"Flask server offline or error... -> Safe (30.0%)\n",
      "Text: is_safe... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: prediction... -> Safe (30.0%)\n",
      "Text: \"Safe\"... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: // Asynchronous রেসপন্স হ্যান্... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: <!DOCTYPE html>... -> Safe (30.0%)\n",
      "Text: <html>... -> Safe (30.0%)\n",
      "Text: <head>... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: <style>... -> Safe (30.0%)\n",
      "Text: body { width: 280px; font-fami... -> Safe (30.0%)\n",
      "Text: </head>... -> Safe (30.0%)\n",
      "Text: </style>... -> Safe (30.0%)\n",
      "Text: <body>... -> Safe (30.0%)\n",
      "Text: <textarea id=\"testText\" rows=\"... -> Safe (30.0%)\n",
      "Text: </textarea>... -> Safe (30.0%)\n",
      "Text: <button id=\"checkBtn\">... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: </button>... -> Safe (30.0%)\n",
      "Text: <div id=\"result\">... -> Safe (30.0%)\n",
      "Text: </div>... -> Safe (30.0%)\n",
      "Text: <script src=\"popup.js\">... -> Safe (30.0%)\n",
      "Text: </script>... -> Safe (30.0%)\n",
      "Text: </body>... -> Safe (30.0%)\n",
      "Text: </html>... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'checkBtn'... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: 'click'... -> Suspicious (36.19%)\n",
      "Text: 'testText'... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: 'result'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"block\"... -> Safe (30.0%)\n",
      "Text: \"Analyzing Content...\"... -> Safe (30.0%)\n",
      "Text: \"#f1f1f1\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"#333\"... -> Safe (30.0%)\n",
      "Text: action... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: (response) =>... -> Safe (30.0%)\n",
      "Text: `Classification: ${response.pr... -> Safe (30.0%)\n",
      "Text: \"#d4edda\"... -> Safe (30.0%)\n",
      "Text: \"#155724\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:42] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"#f8d7da\"... -> Safe (30.0%)\n",
      "Text: \"#721c24\"... -> Safe (30.0%)\n",
      "Text: Python\n",
      "probabilities = model.p... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "pipeline = Pipeline([\n",
      " ... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: 'tfidf'... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Suspicious (36.36%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # এক্সটেনশন থেকে রিকোয়েস্ট ব্... -> Safe (30.0%)\n",
      "Text: # মডেল লোড করা... -> Safe (30.0%)\n",
      "Text: 'model.pkl'... -> Safe (30.0%)\n",
      "Text: except... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"[SUCCESS] Machine Learning Mo... -> Safe (30.0%)\n",
      "Text: \"[ERROR] model.pkl ফাইলটি পাওয়... -> Safe (30.0%)\n",
      "Text: @app.route('/predict', methods... -> Safe (30.0%)\n",
      "Text: def predict():... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: 'error'... -> Safe (30.0%)\n",
      "Text: 'No text provided'... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: hasattr... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'trim'... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: 'prediction'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'risk_score'... -> Safe (30.0%)\n",
      "Text: 'is_safe'... -> Safe (30.0%)\n",
      "Text: # ১. টেক্সট ক্লাসিফাই করা (Saf... -> Safe (30.0%)\n",
      "Text: # ২. পাইপলাইনের ভেতর থেকে সেফল... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # backend/app.py... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:43] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: import pickle... -> Safe (30.0%)\n",
      "Text: import numpy as np... -> Safe (30.0%)\n",
      "Text: from flask import Flask, reque... -> Safe (30.0%)\n",
      "Text: from flask_cors import CORS... -> Safe (30.0%)\n",
      "Text: app = Flask(__name__)... -> Safe (30.0%)\n",
      "Text: CORS(app)  # এক্সটেনশন থেকে রি... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # মডেল লোড করা... -> Safe (30.0%)Text: with open('model.pkl', 'rb') a... -> Safe (30.0%)\n",
      "\n",
      "Text: model = pickle.load(f)... -> Safe (30.0%)\n",
      "Text: @app.route('/predict', methods... -> Safe (30.0%)\n",
      "Text: def predict():... -> Safe (30.0%)\n",
      "Text: data = request.get_json()... -> Safe (30.0%)\n",
      "Text: if not data or 'text' not in d... -> Safe (30.0%)\n",
      "Text: return jsonify({'error': 'No t... -> Safe (30.0%)\n",
      "Text: text_content = data['text']... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # প্রেডিকশন এবং রিস্ক স্কোর ক্... -> Safe (30.0%)\n",
      "Text: prediction = model.predict([te... -> Safe (30.0%)\n",
      "Text: probabilities = model.predict_... -> Safe (30.0%)\n",
      "Text: risk_score = round(float(np.ma... -> Safe (30.0%)\n",
      "Text: is_safe = True if prediction =... -> Safe (30.0%)\n",
      "Text: 'prediction': prediction,... -> Safe (30.0%)\n",
      "Text: response = {... -> Safe (30.0%)\n",
      "Text: 'risk_score': f\"{risk_score}%\"... -> Safe (30.0%)\n",
      "Text: 'is_safe': is_safe... -> Safe (30.0%)\n",
      "Text: print(f\"Text: {text_content[:3... -> Safe (30.0%)\n",
      "Text: return jsonify(response)... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: if __name__ == '__main__':... -> Safe (30.0%)\n",
      "Text: app.run(host='127.0.0.1', port... -> Spam (31.9%)\n",
      "Text: import pickle... -> Safe (30.0%)\n",
      "Text: import numpy as np... -> Safe (30.0%)\n",
      "Text: from flask import Flask, reque... -> Safe (30.0%)\n",
      "Text: from flask_cors import CORS... -> Safe (30.0%)\n",
      "Text: app = Flask(__name__)... -> Safe (30.0%)\n",
      "Text: CORS(app)  # এক্সটেনশন থেকে রি... -> Safe (30.0%)\n",
      "Text: # মডেল লোড করা... -> Safe (30.0%)\n",
      "Text: with open('model.pkl', 'rb') a... -> Safe (30.0%)\n",
      "Text: model = pickle.load(f)... -> Safe (30.0%)\n",
      "Text: @app.route('/predict', methods... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:44] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: def predict():... -> Safe (30.0%)\n",
      "Text: data = request.get_json()... -> Safe (30.0%)\n",
      "Text: if not data or 'text' not in d... -> Safe (30.0%)\n",
      "Text: return jsonify({'error': 'No t... -> Safe (30.0%)\n",
      "Text: text_content = data['text']... -> Safe (30.0%)\n",
      "Text: # প্রেডিকশন এবং রিস্ক স্কোর ক্... -> Safe (30.0%)\n",
      "Text: prediction = model.predict([te... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: probabilities = model.predict_... -> Safe (30.0%)\n",
      "Text: * Serving Flask app '__main__'... -> Suspicious (36.36%)\n",
      "Text: * Serving Flask app '__main__'... -> Safe (30.0%)\n",
      "Text: An exception has occurred, use... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: WARNING: This is a development... -> Suspicious (36.36%)Text: http://127.0.0.1:5000... -> Spam (31.9%)\n",
      "\n",
      "Text: An exception has occurred, use... -> Safe (30.0%)\n",
      "Text: * Debug mode: on... -> Safe (30.0%)\n",
      "Text: SystemExit... -> Safe (30.0%)\n",
      "Text: WARNING: This is a development... -> Suspicious (50.99%)\n",
      "Text: An exception has occurred, use... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: ব্রো, আপনি আপনার ফ্লাস্কের app... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: আপনার কোডের এই লাইনে খেয়াল কর... -> Safe (30.0%)\n",
      "Text: সমস্যাটা কোথায়?... -> Safe (30.0%)\n",
      "Text: Python\n",
      "probabilities = model.p... -> Safe (30.0%)\n",
      "Text: আমরা মডেল ট্রেইনিং কোডে (train... -> Safe (30.0%)\n",
      "Text: Python\n",
      "pipeline = Pipeline([\n",
      " ... -> Safe (30.0%)\n",
      "Text: Scikit-learn-এর Pipeline অবজেক... -> Safe (30.0%)\n",
      "Text: সবচেয়ে বড় সমস্যা হলো, আমরা ডে... -> Safe (30.0%)\n",
      "Text: ডিপার্টমেন্টের প্রফেসরের সামনে... -> Safe (30.0%)\n",
      "Text: সম্পূর্ণ সংশোধিত backend/app.p... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Suspicious (36.36%)\n",
      "Text: এখন আপনার করণীয়:... -> Safe (30.0%)\n",
      "Text: ১. এই নতুন কোডটি backend/app.p... -> Safe (30.0%)\n",
      "Text: সার্ভার কি কোনো এরর ছাড়া স্মুথ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:45] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: * Serving Flask app '__main__'... -> Safe (30.0%)\n",
      "Text: * Debug mode: on... -> Safe (30.0%)\n",
      "Text: WARNING: This is a development... -> Suspicious (50.99%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: An exception has occurred, use... -> Safe (30.0%)\n",
      "Text: Python\n",
      "probabilities = model.p... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "pipeline = Pipeline([\n",
      " ... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Suspicious (36.36%)\n",
      "Text: 'tfidf'... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # এক্সটেনশন থেকে রিকোয়েস্ট ব্... -> Safe (30.0%)\n",
      "Text: # মডেল লোড করা... -> Safe (30.0%)\n",
      "Text: 'model.pkl'... -> Safe (30.0%)\n",
      "Text: \"[SUCCESS] Machine Learning Mo... -> Safe (30.0%)\n",
      "Text: except... -> Safe (30.0%)\n",
      "Text: \"[ERROR] model.pkl ফাইলটি পাওয়... -> Safe (30.0%)\n",
      "Text: @app.route('/predict', methods... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: def predict():... -> Safe (30.0%)Text: return... -> Safe (30.0%)\n",
      "\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: 'error'... -> Safe (30.0%)\n",
      "Text: 'No text provided'... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: hasattr... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:46] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'trim'... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: 'prediction'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'risk_score'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'is_safe'... -> Safe (30.0%)\n",
      "Text: # ১. টেক্সট ক্লাসিফাই করা (Saf... -> Safe (30.0%)\n",
      "Text: # ২. পাইপলাইনের ভেতর থেকে সেফল... -> Safe (30.0%)\n",
      "Text: # ৩. হায়েস্ট প্রব্যাবিলিটি নি... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: except... -> Safe (30.0%)\n",
      "Text: # কোনো কারণে প্রব্যাবিলিটি ফেই... -> Safe (30.0%)\n",
      "Text: f\"[Warning] Probability calcul... -> Suspicious (50.99%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: * Serving Flask app '__main__'... -> Safe (30.0%)\n",
      "Text: * Debug mode: on... -> Safe (30.0%)\n",
      "Text: যেহেতু আমরা জুপিটার নোটবুক বা ... -> Safe (30.0%)\n",
      "Text: আপনার backend/app.py ফাইলের এক... -> Safe (30.0%)\n",
      "Text: Pythonif __name__ == '__main__... -> Spam (31.9%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:47] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:48] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:48] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:48] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Pythonif __name__ == '__main__... -> Spam (31.9%)\n",
      "Text: উইন্ডোজে এই... -> Safe (30.0%)\n",
      "Text: ব্রো, উইন্ডোজে এই SystemExit: ... -> Safe (30.0%)\n",
      "Text: যেহেতু আমরা জুপিটার নোটবুক বা ... -> Safe (30.0%)\n",
      "Text: আপনার backend/app.py ফাইলের এক... -> Safe (30.0%)\n",
      "Text: Python\n",
      "if __name__ == '__main_... -> Spam (31.9%)\n",
      "Text: ⚠️ যদি আগের কোনো হ্যাং হওয়া প্... -> Safe (30.0%)\n",
      "Text: অনেক সময় আগের ফেইল হওয়া রানটি ... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "Taskkill /IM python.exe /... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:47:48] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:48] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:48] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:48] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:47:48] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: (অথবা আপনি চাইলে পোর্টের ঝামেল... -> Safe (30.0%)\n",
      "Text: আশা করছি এবার আর কোনো SystemEx... -> Safe (30.0%)\n",
      "Text: এবার ফাইলটি সেভ করে আবার রান দ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "if __name__ == '__main_... -> Spam (31.9%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:03] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Conversation with Gemini... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: New chat\n",
      "My stuff\n",
      "Chats\n",
      "Build ... -> Safe (54.86%)Text: My stuff\n",
      "Chats\n",
      "Build Offline P... -> Safe (70.34%)\n",
      "\n",
      "Text: New chat... -> Suspicious (49.84%)\n",
      "Text: New chat... -> Suspicious (49.84%)\n",
      "Text: New chat... -> Suspicious (49.84%)\n",
      "Text: New chat... -> Suspicious (49.84%)\n",
      "Text: My stuff... -> Safe (30.0%)\n",
      "Text: Chats\n",
      "Build Offline Phishing D... -> Safe (70.34%)\n",
      "Text: Settings & help... -> Scam (48.54%)\n",
      "Text: Settings & help... -> Scam (48.54%)\n",
      "Text: Settings & help... -> Scam (48.54%)\n",
      "Text: Settings & help... -> Scam (48.54%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:04] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:05] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Gemini is AI and can make mist... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:07] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:07] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:07] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Gemini... -> Safe (30.0%)\n",
      "Text: Gemini... -> Safe (30.0%)\n",
      "Text: Gemini... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:07] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:07] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:07] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:07] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:07] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Upgrade... -> Safe (30.0%)\n",
      "Text: Build Offline Phishing Detecto... -> Safe (30.0%)\n",
      "Text: Build Offline Phishing Detecto... -> Safe (30.0%)\n",
      "Text: Build Offline Phishing Detecto... -> Safe (30.0%)\n",
      "Text: Upgrade... -> Safe (30.0%)\n",
      "Text: Upgrade... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:07] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: You said\n",
      "\n",
      "what is the alternat... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "what is the alternat... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "what is the alternat... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "what is the alternat... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "what is the alternat... -> Safe (30.0%)\n",
      "Text: what is the alternative of apk... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "bro i am fed up, let... -> Scam (48.54%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: You said\n",
      "\n",
      "bro i am fed up, let... -> Scam (48.54%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "bro i am fed up, let... -> Scam (48.54%)\n",
      "Text: You said\n",
      "\n",
      "bro i am fed up, let... -> Scam (48.54%)\n",
      "Text: You said\n",
      "\n",
      "bro i am fed up, let... -> Scam (48.54%)\n",
      "Text: bro i am fed up, lets' go to c... -> Scam (48.54%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "Buildozer is running... -> Suspicious (43.38%)\n",
      "Text: You said\n",
      "\n",
      "Buildozer is running... -> Suspicious (43.38%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "Buildozer is running... -> Suspicious (43.38%)\n",
      "Text: You said\n",
      "\n",
      "Buildozer is running... -> Suspicious (43.38%)\n",
      "Text: You said\n",
      "\n",
      "Buildozer is running... -> Suspicious (43.38%)\n",
      "Text: Buildozer is running as root!T... -> Safe (30.0%)\n",
      "Text: Are you sure you want to conti... -> Phishing (43.53%)\n",
      "Text: * master 58d21141 [origin/mast... -> Safe (30.0%)\n",
      "Text: [WARNING]: prerequisites.py is... -> Suspicious (50.99%)\n",
      "Text: [WARNING]: Please report any i... -> Safe (39.63%)\n",
      "Text: [WARNING]: prerequisites.py is... -> Suspicious (50.99%)\n",
      "Text: [WARNING]: Please report any i... -> Safe (39.63%)\n",
      "Text: usage: toolchain.py [-h] [-v]... -> Safe (30.0%)\n",
      "Text: {recommendations,recipes,boots... -> Suspicious (50.99%)\n",
      "Text: A packaging tool for turning P... -> Safe (30.0%)\n",
      "Text: positional arguments:... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:08] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: {recommendations,recipes,boots... -> Suspicious (50.99%)\n",
      "Text: The command to run... -> Safe (30.0%)\n",
      "Text: recommendations List recommend... -> Safe (30.0%)\n",
      "Text: recipes List the available rec... -> Safe (30.0%)\n",
      "Text: bootstraps List the available ... -> Safe (30.0%)\n",
      "Text: clean_all (clean-all)... -> Safe (30.0%)\n",
      "Text: Delete all builds, dists and c... -> Safe (30.0%)\n",
      "Text: clean_dists (clean-dists)... -> Safe (30.0%)\n",
      "Text: Delete all dists... -> Safe (30.0%)\n",
      "Text: clean_bootstrap_builds (clean-... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Delete all bootstrap builds... -> Safe (30.0%)\n",
      "Text: clean_builds (clean-builds)... -> Safe (30.0%)\n",
      "Text: Delete all builds... -> Safe (30.0%)\n",
      "Text: clean Delete build components.... -> Safe (30.0%)\n",
      "Text: clean_recipe_build (clean-reci... -> Safe (30.0%)\n",
      "Text: Delete the build components of... -> Safe (30.0%)\n",
      "Text: default this will also delete ... -> Safe (30.0%)\n",
      "Text: clean_download_cache (clean-do... -> Suspicious (50.99%)\n",
      "Text: Delete cached downloads for re... -> Safe (30.0%)\n",
      "Text: export_dist (export-dist)... -> Safe (30.0%)\n",
      "Text: aar Build an AAR... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Copy the named dist to the giv... -> Safe (30.0%)\n",
      "Text: apk Build an APK... -> Safe (30.0%)\n",
      "Text: aab Build an AAB... -> Safe (30.0%)\n",
      "Text: create Compile a set of requir... -> Safe (30.0%)\n",
      "Text: archs List the available targe... -> Safe (30.0%)\n",
      "Text: distributions (dists)... -> Safe (30.0%)\n",
      "Text: List the currently available (... -> Safe (30.0%)\n",
      "Text: delete_dist (delete-dist)... -> Safe (30.0%)\n",
      "Text: Delete a compiled dist... -> Safe (30.0%)\n",
      "Text: sdk_tools (sdk-tools)... -> Safe (30.0%)\n",
      "Text: Run the given binary from the ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: adb Run adb from the given SDK... -> Safe (30.0%)\n",
      "Text: logcat Run logcat from the giv... -> Safe (30.0%)\n",
      "Text: build_status (build-status)... -> Safe (30.0%)\n",
      "Text: Print some debug information a... -> Safe (30.0%)\n",
      "Text: components... -> Safe (30.0%)\n",
      "Text: options:... -> Safe (30.0%)\n",
      "Text: -h, --help show this help mess... -> Scam (48.54%)\n",
      "Text: -v, --version show program's v... -> Spam (31.9%)\n",
      "Text: '--tunnel_background_save_url=... -> Phishing (43.53%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: '--tunnel_background_save_dela... -> Safe (30.0%)\n",
      "Text: '--tunnel_periodic_background_... -> Safe (30.0%)\n",
      "Text: '--enable_output_coalescing=tr... -> Safe (60.55%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "give me buildozer.sp... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "give me buildozer.sp... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "give me buildozer.sp... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "give me buildozer.sp... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "give me buildozer.sp... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:09] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: give me buildozer.spec again... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "I want to build an A... -> Safe (49.59%)\n",
      "Text: You said\n",
      "\n",
      "I want to build an A... -> Safe (49.59%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "I want to build an A... -> Safe (49.59%)\n",
      "Text: You said\n",
      "\n",
      "I want to build an A... -> Safe (49.59%)\n",
      "Text: You said\n",
      "\n",
      "I want to build an A... -> Safe (49.59%)\n",
      "Text: I want to build an AI-powered ... -> Safe (60.55%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Project Idea:... -> Safe (60.55%)\n",
      "Text: The extension will analyze bro... -> Safe (30.0%)\n",
      "Text: Main Goal:... -> Safe (30.0%)\n",
      "Text: Detect phishing, spam, scam, a... -> Safe (30.0%)\n",
      "Text: * Safe... -> Safe (30.0%)\n",
      "Text: * Spam... -> Safe (30.0%)\n",
      "Text: * Scam... -> Safe (30.0%)\n",
      "Text: * Phishing... -> Safe (30.0%)\n",
      "Text: * Suspicious... -> Safe (30.0%)\n",
      "Text: Expected Workflow:... -> Safe (30.0%)\n",
      "Text: 1. A browser notification or s... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 2. The browser extension captu... -> Safe (30.0%)\n",
      "Text: 3. The text is sent to a local... -> Safe (30.0%)\n",
      "Text: 4. The ML model analyzes the t... -> Safe (30.0%)\n",
      "Text: 5. The model returns a predict... -> Safe (30.0%)\n",
      "Text: 6. The extension then:... -> Safe (30.0%)\n",
      "Text: * Shows a warning popup for un... -> Suspicious (50.99%)\n",
      "Text: * Or allows safe notifications... -> Safe (30.0%)\n",
      "Text: Technical Requirements:... -> Safe (30.0%)\n",
      "Text: * Browser Extension using Java... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: * Chrome Extension Manifest V3... -> Safe (30.0%)\n",
      "Text: * Python backend using Flask... -> Safe (30.0%)\n",
      "Text: * Machine Learning using Sciki... -> Safe (30.0%)\n",
      "Text: * Spam/phishing detection usin... -> Safe (30.0%)\n",
      "Text: * Completely free and offline ... -> Safe (30.0%)\n",
      "Text: * No paid APIs... -> Safe (30.0%)\n",
      "Text: Machine Learning Goals:... -> Safe (30.0%)\n",
      "Text: * Train a text classification ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: * Use datasets related to spam... -> Safe (30.0%)\n",
      "Text: * Beginner-friendly models pre... -> Safe (30.0%)\n",
      "Text: * Naive Bayes... -> Safe (30.0%)\n",
      "Text: * Logistic Regression... -> Safe (30.0%)\n",
      "Text: Suggested Architecture:... -> Safe (30.0%)\n",
      "Text: Browser Extension... -> Safe (30.0%)\n",
      "Text: → Captures notification text... -> Safe (30.0%)\n",
      "Text: → Sends text to Flask API... -> Safe (30.0%)\n",
      "Text: → ML model predicts SAFE/UNSAF... -> Safe (30.0%)\n",
      "Text: → Extension displays result... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:10] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Features I want:... -> Safe (30.0%)Text: * Real-time notification analy... -> Safe (30.0%)\n",
      "\n",
      "Text: * Popup warnings... -> Safe (30.0%)\n",
      "Text: * Risk scoring... -> Safe (30.0%)\n",
      "Text: * Offline/local inference... -> Safe (30.0%)\n",
      "Text: * User privacy protection... -> Safe (30.0%)\n",
      "Text: * Lightweight performance... -> Safe (30.0%)\n",
      "Text: Please help me with:... -> Scam (48.54%)\n",
      "Text: 1. Full project architecture... -> Safe (60.55%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 2. Folder structure... -> Safe (30.0%)\n",
      "Text: 3. Browser extension code... -> Safe (30.0%)\n",
      "Text: 4. Flask backend setup... -> Safe (30.0%)\n",
      "Text: 5. ML model training code... -> Safe (30.0%)\n",
      "Text: 6. Communication between exten... -> Safe (30.0%)\n",
      "Text: 7. How to test locally... -> Safe (30.0%)\n",
      "Text: 8. How to package the extensio... -> Safe (30.0%)\n",
      "Text: 9. Suggestions for improving a... -> Safe (30.0%)\n",
      "Text: 10. Future scalability ideas... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: I want beginner-friendly step-... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "amar teachre bolechi... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "amar teachre bolechi... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "amar teachre bolechi... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "amar teachre bolechi... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "amar teachre bolechi... -> Safe (30.0%)\n",
      "Text: amar teachre bolechilo bahirer... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: You said\n",
      "\n",
      "okay then, ager shob... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "okay then, ager shob... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "okay then, ager shob... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "okay then, ager shob... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "okay then, ager shob... -> Safe (30.0%)\n",
      "Text: okay then, ager shob kichu baa... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "hae done\n",
      "\n",
      "Gemini sai... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "hae done... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: You said\n",
      "\n",
      "hae done... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "hae done... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "hae done... -> Safe (30.0%)\n",
      "Text: hae done... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "# backend/app.py\n",
      "\n",
      "im... -> Spam (31.9%)\n",
      "Text: You said\n",
      "\n",
      "# backend/app.py\n",
      "\n",
      "im... -> Spam (31.9%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:11] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "# backend/app.py\n",
      "\n",
      "im... -> Spam (31.9%)\n",
      "Text: You said\n",
      "\n",
      "# backend/app.py\n",
      "\n",
      "im... -> Spam (31.9%)\n",
      "Text: You said\n",
      "\n",
      "# backend/app.py\n",
      "\n",
      "im... -> Spam (31.9%)\n",
      "Text: # backend/app.py... -> Safe (30.0%)\n",
      "Text: import pickle... -> Safe (30.0%)\n",
      "Text: import numpy as np... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: from flask import Flask, reque... -> Safe (30.0%)\n",
      "Text: from flask_cors import CORS... -> Safe (30.0%)\n",
      "Text: app = Flask(__name__)... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # মডেল লোড করা... -> Safe (30.0%)\n",
      "Text: CORS(app)  # এক্সটেনশন থেকে রি... -> Safe (30.0%)\n",
      "Text: model = pickle.load(f)... -> Safe (30.0%)\n",
      "Text: with open('model.pkl', 'rb') a... -> Safe (30.0%)\n",
      "Text: @app.route('/predict', methods... -> Safe (30.0%)\n",
      "Text: def predict():... -> Safe (30.0%)\n",
      "Text: data = request.get_json()... -> Safe (30.0%)\n",
      "Text: if not data or 'text' not in d... -> Safe (30.0%)\n",
      "Text: text_content = data['text']... -> Safe (30.0%)\n",
      "Text: return jsonify({'error': 'No t... -> Safe (30.0%)\n",
      "Text: # প্রেডিকশন এবং রিস্ক স্কোর ক্... -> Safe (30.0%)\n",
      "Text: prediction = model.predict([te... -> Safe (30.0%)\n",
      "Text: probabilities = model.predict_... -> Safe (30.0%)\n",
      "Text: risk_score = round(float(np.ma... -> Safe (30.0%)\n",
      "Text: is_safe = True if prediction =... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: response = {... -> Safe (30.0%)\n",
      "Text: 'prediction': prediction,... -> Safe (30.0%)\n",
      "Text: 'risk_score': f\"{risk_score}%\"... -> Safe (30.0%)\n",
      "Text: 'is_safe': is_safe... -> Safe (30.0%)\n",
      "Text: print(f\"Text: {text_content[:3... -> Safe (30.0%)\n",
      "Text: return jsonify(response)... -> Safe (30.0%)\n",
      "Text: if __name__ == '__main__':... -> Safe (30.0%)\n",
      "Text: app.run(host='127.0.0.1', port... -> Spam (31.9%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:12] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: You said\n",
      "\n",
      "* Serving Flask app ... -> Suspicious (50.99%)\n",
      "Text: * Serving Flask app '__main__'... -> Safe (30.0%)\n",
      "Text: * Debug mode: on... -> Safe (30.0%)\n",
      "Text: WARNING: This is a development... -> Suspicious (50.99%)\n",
      "Text: An exception has occurred, use... -> Safe (30.0%)\n",
      "Text: Gemini said... -> Safe (30.0%)\n",
      "Text: Notebooks\n",
      "New notebook... -> Suspicious (49.84%)\n",
      "Text: Notebooks... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Notebooks... -> Safe (30.0%)\n",
      "Text: Notebooks... -> Safe (30.0%)\n",
      "Text: New notebook... -> Suspicious (49.84%)\n",
      "Text: New notebook... -> Suspicious (49.84%)\n",
      "Text: New notebook... -> Suspicious (49.84%)\n",
      "Text: অ্যান্ড্রয়েড ইকোসিস্টেমে APK ... -> Safe (35.02%)\n",
      "Text: অ্যান্ড্রয়েড ইকোসিস্টেমে APK ... -> Safe (30.0%)\n",
      "Text: ১. AAB (Android App Bundle)... -> Safe (30.0%)\n",
      "Text: এটি বর্তমানে Google Play Store... -> Safe (30.0%)\n",
      "Text: কেন এটি সেরা বিকল্প: * Size Op... -> Phishing (43.53%)\n",
      "Text: ২. PWA (Progressive Web App)... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: এটি কোনো প্যাকেজ ফাইল নয়, বরং ... -> Safe (30.0%)\n",
      "Text: সুবিধা: ইউজারের ফোনে কোনো কিছু... -> Spam (31.9%)\n",
      "Text: ৩. Web-Based Interface (Flask/... -> Safe (30.0%)\n",
      "Text: যেহেতু আপনি অলরেডি Flask ব্যবহ... -> Safe (30.0%)\n",
      "Text: ফোন থেকে শুধু একটি লিঙ্কে (যেম... -> Safe (30.0%)\n",
      "Text: ৪. অন্যান্য (Legacy/External)... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: APKS: এটি মূলত একাধিক স্প্লিট ... -> Safe (30.0%)\n",
      "Text: আপনার প্রোজেক্টের জন্য কোনটি ভ... -> Safe (30.0%)\n",
      "Text: যেহেতু আপনি University Project... -> Safe (60.55%)\n",
      "Text: বোর্ডের সামনে পেনড্রাইভে করে অ... -> Safe (30.0%)\n",
      "Text: আমার পরামর্শ: আমরা যে APK বিল্... -> Safe (30.0%)\n",
      "Text: আপনি কি প্রজেক্টটি প্লে-স্টোরে... -> Safe (30.0%)\n",
      "Text: Sources... -> Safe (30.0%)\n",
      "Text: আমি একদম বুঝতে পারছি ব্রো, গিট... -> Safe (30.0%)\n",
      "Text: আমি একদম বুঝতে পারছি ব্রো, গিট... -> Safe (30.0%)\n",
      "Text: চলুন, কোল্যাব-এই ফিরে যাই। তবে... -> Safe (30.0%)\n",
      "Text: নিচের স্টেপগুলো একে একে ফলো কর... -> Safe (30.0%)\n",
      "Text: ধাপ ১: কোল্যাব সেশন সেটআপ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:13] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: কোল্যাব-এ একটি নতুন নোটবুক খুল... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# ১. প্রয়োজনীয় সিস্টেম ... -> Safe (30.0%)\n",
      "Text: ধাপ ২: ফাইল আপলোড... -> Safe (30.0%)\n",
      "Text: কোল্যাবের বাম পাশের ফাইল আইকনে... -> Safe (30.0%)\n",
      "Text: main.py\n",
      "\n",
      "monitor_service.py\n",
      "\n",
      "b... -> Safe (30.0%)\n",
      "Text: ধাপ ৩: মেমরি এবং লাইসেন্স ফিক্... -> Safe (30.0%)\n",
      "Text: বিল্ড শুরু করার আগে এই কমান্ডট... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!mkdir -p ~/.android &&... -> Safe (30.0%)\n",
      "Text: ধাপ ৪: আসল বিল্ড কমান্ড (The F... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: এবার এই কমান্ডটি রান দিন। আমি ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: কেন এবার কাজ করবে?... -> Safe (30.0%)\n",
      "Text: গিটহাব অ্যাকশনে আমরা বারবার \"E... -> Safe (30.0%)\n",
      "Text: একটি প্রো-টিপ:... -> Safe (30.0%)\n",
      "Text: বিল্ড চলাকালীন কোল্যাব ট্যাবটি... -> Safe (30.0%)\n",
      "Text: বিল্ড রান করে দিন। যদি ২০-৩০ ম... -> Safe (30.0%)\n",
      "Text: শুরু করেছেন কি?... -> Safe (30.0%)\n",
      "Text: Sources... -> Safe (30.0%)\n",
      "Text: Sources... -> Safe (30.0%)\n",
      "Text: Sources... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ব্রো, কোল্যাব-এ এই এররটা আসার ... -> Safe (30.0%)\n",
      "Text: ব্রো, কোল্যাব-এ এই এররটা আসার ... -> Safe (30.0%)\n",
      "Text: চিন্তা করবেন না, কোল্যাব-এ এটি... -> Safe (30.0%)\n",
      "Text: ১. লাইসেন্স ম্যানুয়ালি এক্সেপ্... -> Safe (30.0%)\n",
      "Text: বিল্ডোজারকে লাইসেন্স হ্যান্ডেল... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# এটি সরাসরি অ্যান্ড্রয়... -> Safe (30.0%)\n",
      "Text: ২. buildozer.spec এ ছোট একটি প... -> Safe (30.0%)\n",
      "Text: আপনার buildozer.spec ফাইলে p4a... -> Safe (30.0%)\n",
      "Text: নিচের কোডটি রান দিন, এটি আপনার... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "import os\n",
      "\n",
      "with open('b... -> Safe (30.0%)\n",
      "Text: ৩. বিল্ড শুরু করা (The Fix)... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# রুট ইউজার হিসেবে চালা... -> Safe (30.0%)\n",
      "Text: এখন বিল্ড করার সময় আমরা কোনো অ... -> Safe (30.0%)\n",
      "Text: কেন আগেরবার ফেইল করলো?... -> Safe (30.0%)\n",
      "Text: লগ ফাইল অনুযায়ী, বিল্ডোজার pyt... -> Safe (30.0%)\n",
      "Text: টিপস: যদি বিল্ড করার সময় আবার ... -> Safe (30.0%)\n",
      "Text: এই স্টেপগুলো রান দিন। এবার বিল... -> Safe (30.0%)\n",
      "Text: নিচে আপনার Google Colab এনভায়... -> Suspicious (34.92%)\n",
      "Text: নিচে আপনার Google Colab এনভায়... -> Safe (30.0%)\n",
      "Text: এই কোডটুকু কপি করে Colab-এর বা... -> Safe (30.0%)\n",
      "Text: Ini, TOML\n",
      "[app]\n",
      "\n",
      "# (str) Title... -> Suspicious (34.92%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: কেন এই ফাইলটি এখন Colab-এ কাজ ... -> Safe (30.0%)\n",
      "Text: ১. p4a.branch = develop: আপনি ... -> Safe (30.0%)\n",
      "Text: এখন যা করবেন:... -> Safe (30.0%)\n",
      "Text: ১. এই কোডটি দিয়ে আপনার buildoz... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ৩. বিল্ড চলাকালীন যখনই [y/n] প... -> Safe (30.0%)\n",
      "Text: আশা করছি এবার আর কোনো Command ... -> Safe (30.0%)\n",
      "Text: ব্রো, অ্যান্ড্রয়েড অ্যাপ বিল্ড... -> Phishing (31.32%)\n",
      "Text: ব্রো, অ্যান্ড্রয়েড অ্যাপ বিল্ড... -> Safe (30.0%)\n",
      "Text: যেহেতু এটি আপনি সম্পূর্ণ Offli... -> Safe (30.0%)\n",
      "Text: আপনার রিকোয়েস্ট অনুযায়ী নিচে স... -> Safe (30.0%)\n",
      "Text: ১. সম্পূর্ণ প্রজেক্ট আর্কিটেকচ... -> Safe (30.0%)\n",
      "Text: Frontend (Chrome Extension - M... -> Safe (30.0%)\n",
      "Text: ২. ফোল্ডার স্ট্রাকচার (Folder ... -> Safe (30.0%)\n",
      "Text: প্রজেক্টটি গুছিয়ে রাখতে আপনার ... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-Extension... -> Safe (30.0%)\n",
      "Text: ৩. মেশিন লার্নিং মডেল ট্রেইনিং... -> Safe (30.0%)\n",
      "Text: প্রথমে আমরা মডেলটি ট্রেইন করে ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "import pickle... -> Phishing (36.81%)\n",
      "Text: ৪. ফ্লাস্ক ব্যাকএন্ড সেটআপ (ba... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:14] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: এই লোকাল সার্ভারটি এক্সটেনশন থ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Spam (31.9%)\n",
      "Text: ৫. ব্রাউজার এক্সটেনশন কোড (ext... -> Safe (30.0%)\n",
      "Text: A. manifest.json (Manifest V3)... -> Safe (30.0%)\n",
      "Text: এটি আমাদের এক্সটেনশনের মেইন কন... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: B. content.js (DOM/Alert স্ক্র... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: এই স্ক্রিপ্টটি ওয়েবসাইটে কোনো ... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (50.99%)\n",
      "Text: C. background.js (Service Work... -> Safe (30.0%)\n",
      "Text: এটি ফ্লাস্ক ব্যাকএন্ড সার্ভারে... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: D. popup.html (UI)... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: এক্সটেনশন আইকনে ক্লিক করলে ইউজ... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: E. popup.js (UI Logic)... -> Safe (30.0%)\n",
      "Text: পপআপ বক্সের ভেতর থেকে ইউজার ম্... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: ৬. লোকাল টেস্টিং গাইড (How to ... -> Safe (30.0%)\n",
      "Text: ১. পাইথন এনভায়রনমেন্ট রান করু... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: মডেল তৈরি হয়ে গেলে ফ্লাস্ক সার... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "python backend/app.py... -> Safe (30.0%)\n",
      "Text: (আপনার স্ক্রিনে Running on htt... -> Spam (31.9%)\n",
      "Text: ২. এক্সটেনশন লোড করুন:... -> Safe (30.0%)\n",
      "Text: Google Chrome ব্রাউজার খুলে ইউ... -> Safe (30.0%)\n",
      "Text: ৭. এক্সটেনশন প্যাকেজিং (How to... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: যখন আপনি প্রজেক্টটি আপনার প্রো... -> Safe (30.0%)Text: ৮. একুরেসি বাড়ানোর টেকনিক এবং ... -> Safe (30.0%)\n",
      "\n",
      "Text: একুরেসি বাড়ানোর আইডিয়া:... -> Safe (30.0%)\n",
      "Text: বড় ডাটাসেট: আমার দেওয়া ডেমো ডা... -> Safe (30.0%)\n",
      "Text: ফিউচার স্কেলাবিলিটি (Future Id... -> Safe (30.0%)\n",
      "Text: On-Device Inference (Transform... -> Safe (30.0%)\n",
      "Text: কোডগুলো সেটআপ করে লোকালহোস্টে ... -> Safe (30.0%)\n",
      "Text: ব্রো, আপনার টিচার একদম খাঁটি এ... -> Scam (60.04%)\n",
      "Text: ব্রো, আপনার টিচার একদম খাঁটি এ... -> Safe (30.0%)\n",
      "Text: যেহেতু আমরা Chrome Extension ব... -> Safe (30.0%)\n",
      "Text: উপায় ১: WhatsApp Web এবং Messe... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:15] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: বাস্তবে আমরা সবাই এখন পিসিতে W... -> Safe (30.0%)\n",
      "Text: আমাদের content.js স্ক্রিপ্ট ব্... -> Safe (30.0%)\n",
      "Text: এর জন্য content.js কোড আপডেট:... -> Safe (30.0%)\n",
      "Text: আপনার এক্সটেনশনের content.js ফ... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (49.84%)\n",
      "Text: উপায় ২: chrome.notifications A... -> Safe (30.0%)\n",
      "Text: অনেক ওয়েবসাইট ব্রাউজারের নিজস্... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: এর জন্য আপনার manifest.json ফা... -> Safe (30.0%)\n",
      "Text: টিচারের সামনে ডেমো দেওয়ার সেরা... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: টিচারকে প্রজেক্ট দেখানোর সময় আ... -> Scam (71.96%)\n",
      "Text: একদম ব্রো! আগের সব ঝেড়ে ফেলে এ... -> Safe (30.0%)\n",
      "Text: হোয়াটসঅ্যাপ ওয়েবে মেসেজটি আসা ... -> Safe (30.0%)\n",
      "Text: লজিকটা কি বুঝতে পেরেছেন ব্রো? ... -> Safe (30.0%)\n",
      "Text: একদম ব্রো! আগের সব ঝেড়ে ফেলে এ... -> Phishing (26.57%)\n",
      "Text: চলুন, একদম স্টেপ-বাই-স্টেপ আগা... -> Safe (30.0%)\n",
      "Text: প্রথম কাজ: আপনার কম্পিউটারে ফো... -> Safe (30.0%)\n",
      "Text: আপনার কম্পিউটারের যেকোনো ড্রাই... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-AI/\n",
      "│\n",
      "├──... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ধাপ ১: মেশিন লার্নিং মডেল তৈরি... -> Safe (30.0%)\n",
      "Text: আপনার কম্পিউটারে টার্মিনাল (বা... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: এবার backend/train_model.py ফা... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/train_model.p... -> Phishing (27.22%)\n",
      "Text: ধাপ ২: ফ্লাস্ক ব্যাকএন্ড সার্ভ... -> Safe (30.0%)\n",
      "Text: backend/app.py ফাইলে নিচের কোড... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/app.py\n",
      "import... -> Spam (31.9%)\n",
      "Text: ⚠️ বিরতি: এতটুকু কি বুঝতে পেরে... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:16] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ব্রো, একবারে সব কোড দিলে জ্যাম... -> Safe (30.0%)\n",
      "Text: ১. আপনি কি মেইন ফোল্ডার এবং সা... -> Safe (30.0%)\n",
      "Text: এই দুটো হয়ে গেলে আমাকে জানান, ... -> Safe (30.0%)\n",
      "Text: সাবাস ব্রো! ব্যাকএন্ড পার্ট সা... -> Scam (90.35%)\n",
      "Text: সাবাস ব্রো! ব্যাকএন্ড পার্ট সা... -> Safe (30.0%)\n",
      "Text: আপনার extension/ ফোল্ডারের ভেত... -> Safe (30.0%)\n",
      "Text: ১. manifest.json... -> Safe (30.0%)\n",
      "Text: এটি আপনার এক্সটেনশনের পরিচয়পত্... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: ২. content.js (হোয়াটসঅ্যাপ/মেস... -> Safe (30.0%)\n",
      "Text: আপনার টিচারের রিকোয়ারমেন্ট অনু... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript\n",
      "console.log(\"[Phish... -> Suspicious (64.46%)\n",
      "Text: ৩. background.js (সার্ভার কমিউ... -> Safe (30.0%)\n",
      "Text: এটি ক্রোম ব্রাউজারের ব্যাকগ্রা... -> Spam (31.9%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)Text: ৪. popup.html (ম্যানুয়াল টেস্ট... -> Safe (30.0%)\n",
      "\n",
      "Text: টিচার বা এক্সটার্নাল বোর্ডের স... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: ৫. popup.js... -> Safe (30.0%)\n",
      "Text: পপআপ ড্যাশবোর্ডের স্ক্যান বাটন... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: 🚀 এখন ব্রাউজারে এক্সটেনশনটি যে... -> Safe (30.0%)\n",
      "Text: ১. আপনার গুগল ক্রোম ব্রাউজারটি... -> Safe (30.0%)\n",
      "Text: ব্যস! আপনার ব্রাউজারের এক্সটেন... -> Safe (30.0%)\n",
      "Text: 🧪 কীভাবে চেক করবেন এটা কাজ করছ... -> Safe (30.0%)\n",
      "Text: আপনার ফ্লাস্ক ব্যাকএন্ড সার্ভা... -> Scam (96.85%)\n",
      "Text: এক্সটেনশনটা লোড করে একটা টেস্ট... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ব্রো, আপনি আপনার ফ্লাস্কের app... -> Suspicious (36.36%)\n",
      "Text: ব্রো, আপনি আপনার ফ্লাস্কের app... -> Safe (30.0%)\n",
      "Text: সমস্যাটা কোথায়?... -> Safe (30.0%)\n",
      "Text: আপনার কোডের এই লাইনে খেয়াল কর... -> Safe (30.0%)\n",
      "Text: Python\n",
      "probabilities = model.p... -> Safe (30.0%)\n",
      "Text: আমরা মডেল ট্রেইনিং কোডে (train... -> Safe (30.0%)\n",
      "Text: Python\n",
      "pipeline = Pipeline([\n",
      " ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:17] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Scikit-learn-এর Pipeline অবজেক... -> Safe (30.0%)\n",
      "Text: সবচেয়ে বড় সমস্যা হলো, আমরা ডে... -> Safe (30.0%)\n",
      "Text: ডিপার্টমেন্টের প্রফেসরের সামনে... -> Safe (30.0%)\n",
      "Text: সম্পূর্ণ সংশোধিত backend/app.p... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Suspicious (36.36%)\n",
      "Text: এখন আপনার করণীয়:... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ১. এই নতুন কোডটি backend/app.p... -> Safe (30.0%)\n",
      "Text: সার্ভার কি কোনো এরর ছাড়া স্মুথ... -> Safe (30.0%)\n",
      "Text: ব্রো, উইন্ডোজে এই SystemExit: ... -> Spam (31.9%)\n",
      "Text: ব্রো, উইন্ডোজে এই SystemExit: ... -> Safe (30.0%)\n",
      "Text: যেহেতু আমরা জুপিটার নোটবুক বা ... -> Safe (30.0%)\n",
      "Text: আপনার backend/app.py ফাইলের এক... -> Safe (30.0%)\n",
      "Text: Python\n",
      "if __name__ == '__main_... -> Spam (31.9%)\n",
      "Text: ⚠️ যদি আগের কোনো হ্যাং হওয়া প্... -> Safe (30.0%)\n",
      "Text: অনেক সময় আগের ফেইল হওয়া রানটি ... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "Taskkill /IM python.exe /... -> Safe (30.0%)\n",
      "Text: (অথবা আপনি চাইলে পোর্টের ঝামেল... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: এবার ফাইলটি সেভ করে আবার রান দ... -> Safe (30.0%)\n",
      "Text: আশা করছি এবার আর কোনো SystemEx... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# ১. প্রয়োজনীয় সিস্টেম ... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!mkdir -p ~/.android &&... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# এটি সরাসরি অ্যান্ড্রয়... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "\n",
      "with open('b... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# রুট ইউজার হিসেবে চালা... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Ini, TOML\n",
      "[app]\n",
      "\n",
      "# (str) Title... -> Suspicious (34.92%)\n",
      "Text: Ini, TOML... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-Extension... -> Safe (30.0%)\n",
      "Text: Plaintext... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "import pickle... -> Phishing (36.81%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Spam (31.9%)\n",
      "Text: Python... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (50.99%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "python backend/app.py... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (49.84%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-AI/\n",
      "│\n",
      "├──... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:18] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Plaintext... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/train_model.p... -> Phishing (27.22%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/app.py\n",
      "import... -> Spam (31.9%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"[Phish... -> Suspicious (64.46%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "probabilities = model.p... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "pipeline = Pipeline([\n",
      " ... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Suspicious (36.36%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "if __name__ == '__main_... -> Spam (31.9%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "Taskkill /IM python.exe /... -> Safe (30.0%)\n",
      "Text: আমি একদম বুঝতে পারছি ব্রো, গিট... -> Safe (30.0%)\n",
      "Text: চলুন, কোল্যাব-এই ফিরে যাই। তবে... -> Safe (30.0%)\n",
      "Text: নিচের স্টেপগুলো একে একে ফলো কর... -> Safe (30.0%)\n",
      "Text: ধাপ ১: কোল্যাব সেশন সেটআপ... -> Safe (30.0%)\n",
      "Text: কোল্যাব-এ একটি নতুন নোটবুক খুল... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "# ১. প্রয়োজনীয় সিস্টেম ... -> Safe (30.0%)\n",
      "Text: ধাপ ২: ফাইল আপলোড... -> Safe (30.0%)\n",
      "Text: কোল্যাবের বাম পাশের ফাইল আইকনে... -> Safe (30.0%)\n",
      "Text: main.py\n",
      "\n",
      "monitor_service.py\n",
      "\n",
      "b... -> Safe (30.0%)\n",
      "Text: ধাপ ৩: মেমরি এবং লাইসেন্স ফিক্... -> Safe (30.0%)\n",
      "Text: বিল্ড শুরু করার আগে এই কমান্ডট... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!mkdir -p ~/.android &&... -> Safe (30.0%)\n",
      "Text: ধাপ ৪: আসল বিল্ড কমান্ড (The F... -> Safe (30.0%)\n",
      "Text: এবার এই কমান্ডটি রান দিন। আমি ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: কেন এবার কাজ করবে?... -> Safe (30.0%)\n",
      "Text: গিটহাব অ্যাকশনে আমরা বারবার \"E... -> Safe (30.0%)\n",
      "Text: একটি প্রো-টিপ:... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: বিল্ড চলাকালীন কোল্যাব ট্যাবটি... -> Safe (30.0%)\n",
      "Text: বিল্ড রান করে দিন। যদি ২০-৩০ ম... -> Safe (30.0%)\n",
      "Text: শুরু করেছেন কি?... -> Safe (30.0%)\n",
      "Text: ব্রো, কোল্যাব-এ এই এররটা আসার ... -> Safe (30.0%)\n",
      "Text: চিন্তা করবেন না, কোল্যাব-এ এটি... -> Safe (30.0%)\n",
      "Text: ১. লাইসেন্স ম্যানুয়ালি এক্সেপ্... -> Safe (30.0%)\n",
      "Text: বিল্ডোজারকে লাইসেন্স হ্যান্ডেল... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# এটি সরাসরি অ্যান্ড্রয়... -> Safe (30.0%)\n",
      "Text: ২. buildozer.spec এ ছোট একটি প... -> Safe (30.0%)\n",
      "Text: আপনার buildozer.spec ফাইলে p4a... -> Safe (30.0%)\n",
      "Text: নিচের কোডটি রান দিন, এটি আপনার... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "\n",
      "with open('b... -> Safe (30.0%)\n",
      "Text: ৩. বিল্ড শুরু করা (The Fix)... -> Safe (30.0%)\n",
      "Text: এখন বিল্ড করার সময় আমরা কোনো অ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "# রুট ইউজার হিসেবে চালা... -> Safe (30.0%)\n",
      "Text: কেন আগেরবার ফেইল করলো?... -> Safe (30.0%)\n",
      "Text: লগ ফাইল অনুযায়ী, বিল্ডোজার pyt... -> Safe (30.0%)\n",
      "Text: টিপস: যদি বিল্ড করার সময় আবার ... -> Safe (30.0%)\n",
      "Text: এই স্টেপগুলো রান দিন। এবার বিল... -> Safe (30.0%)\n",
      "Text: নিচে আপনার Google Colab এনভায়... -> Safe (30.0%)\n",
      "Text: এই কোডটুকু কপি করে Colab-এর বা... -> Safe (30.0%)\n",
      "Text: Ini, TOML\n",
      "[app]\n",
      "\n",
      "# (str) Title... -> Suspicious (34.92%)\n",
      "Text: কেন এই ফাইলটি এখন Colab-এ কাজ ... -> Safe (30.0%)\n",
      "Text: ১. p4a.branch = develop: আপনি ... -> Safe (30.0%)\n",
      "Text: এখন যা করবেন:... -> Safe (30.0%)\n",
      "Text: ১. এই কোডটি দিয়ে আপনার buildoz... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:19] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: ৩. বিল্ড চলাকালীন যখনই [y/n] প... -> Safe (30.0%)\n",
      "Text: আশা করছি এবার আর কোনো Command ... -> Safe (30.0%)\n",
      "Text: ব্রো, অ্যান্ড্রয়েড অ্যাপ বিল্ড... -> Safe (30.0%)\n",
      "Text: যেহেতু এটি আপনি সম্পূর্ণ Offli... -> Safe (30.0%)\n",
      "Text: আপনার রিকোয়েস্ট অনুযায়ী নিচে স... -> Safe (30.0%)\n",
      "Text: ১. সম্পূর্ণ প্রজেক্ট আর্কিটেকচ... -> Safe (30.0%)\n",
      "Text: Frontend (Chrome Extension - M... -> Safe (30.0%)\n",
      "Text: ২. ফোল্ডার স্ট্রাকচার (Folder ... -> Safe (30.0%)\n",
      "Text: প্রজেক্টটি গুছিয়ে রাখতে আপনার ... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-Extension... -> Safe (30.0%)\n",
      "Text: ৩. মেশিন লার্নিং মডেল ট্রেইনিং... -> Safe (30.0%)\n",
      "Text: প্রথমে আমরা মডেলটি ট্রেইন করে ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "import os\n",
      "import pickle... -> Phishing (36.81%)\n",
      "Text: ৪. ফ্লাস্ক ব্যাকএন্ড সেটআপ (ba... -> Safe (30.0%)\n",
      "Text: এই লোকাল সার্ভারটি এক্সটেনশন থ... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Spam (31.9%)\n",
      "Text: ৫. ব্রাউজার এক্সটেনশন কোড (ext... -> Safe (30.0%)\n",
      "Text: A. manifest.json (Manifest V3)... -> Safe (30.0%)\n",
      "Text: এটি আমাদের এক্সটেনশনের মেইন কন... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: B. content.js (DOM/Alert স্ক্র... -> Safe (30.0%)\n",
      "Text: এই স্ক্রিপ্টটি ওয়েবসাইটে কোনো ... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (50.99%)\n",
      "Text: C. background.js (Service Work... -> Safe (30.0%)\n",
      "Text: এটি ফ্লাস্ক ব্যাকএন্ড সার্ভারে... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: D. popup.html (UI)... -> Safe (30.0%)\n",
      "Text: এক্সটেনশন আইকনে ক্লিক করলে ইউজ... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: E. popup.js (UI Logic)... -> Safe (30.0%)\n",
      "Text: পপআপ বক্সের ভেতর থেকে ইউজার ম্... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: ৬. লোকাল টেস্টিং গাইড (How to ... -> Safe (30.0%)\n",
      "Text: ১. পাইথন এনভায়রনমেন্ট রান করু... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: মডেল তৈরি হয়ে গেলে ফ্লাস্ক সার... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "python backend/app.py... -> Safe (30.0%)\n",
      "Text: (আপনার স্ক্রিনে Running on htt... -> Spam (31.9%)\n",
      "Text: ২. এক্সটেনশন লোড করুন:... -> Safe (30.0%)\n",
      "Text: Google Chrome ব্রাউজার খুলে ইউ... -> Safe (30.0%)\n",
      "Text: ৭. এক্সটেনশন প্যাকেজিং (How to... -> Safe (30.0%)\n",
      "Text: যখন আপনি প্রজেক্টটি আপনার প্রো... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:20] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: ৮. একুরেসি বাড়ানোর টেকনিক এবং ... -> Safe (30.0%)\n",
      "Text: একুরেসি বাড়ানোর আইডিয়া:... -> Safe (30.0%)\n",
      "Text: বড় ডাটাসেট: আমার দেওয়া ডেমো ডা... -> Safe (30.0%)\n",
      "Text: ফিউচার স্কেলাবিলিটি (Future Id... -> Safe (30.0%)\n",
      "Text: On-Device Inference (Transform... -> Safe (30.0%)\n",
      "Text: কোডগুলো সেটআপ করে লোকালহোস্টে ... -> Safe (30.0%)\n",
      "Text: ব্রো, আপনার টিচার একদম খাঁটি এ... -> Safe (30.0%)\n",
      "Text: যেহেতু আমরা Chrome Extension ব... -> Safe (30.0%)\n",
      "Text: উপায় ১: WhatsApp Web এবং Messe... -> Safe (30.0%)\n",
      "Text: বাস্তবে আমরা সবাই এখন পিসিতে W... -> Safe (30.0%)\n",
      "Text: আমাদের content.js স্ক্রিপ্ট ব্... -> Safe (30.0%)\n",
      "Text: এর জন্য content.js কোড আপডেট:... -> Safe (30.0%)\n",
      "Text: আপনার এক্সটেনশনের content.js ফ... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (49.84%)\n",
      "Text: উপায় ২: chrome.notifications A... -> Safe (30.0%)\n",
      "Text: এর জন্য আপনার manifest.json ফা... -> Safe (30.0%)\n",
      "Text: অনেক ওয়েবসাইট ব্রাউজারের নিজস্... -> Safe (30.0%)\n",
      "Text: টিচারের সামনে ডেমো দেওয়ার সেরা... -> Safe (30.0%)\n",
      "Text: টিচারকে প্রজেক্ট দেখানোর সময় আ... -> Scam (71.96%)\n",
      "Text: হোয়াটসঅ্যাপ ওয়েবে মেসেজটি আসা ... -> Safe (30.0%)\n",
      "Text: লজিকটা কি বুঝতে পেরেছেন ব্রো? ... -> Safe (30.0%)\n",
      "Text: একদম ব্রো! আগের সব ঝেড়ে ফেলে এ... -> Safe (30.0%)\n",
      "Text: চলুন, একদম স্টেপ-বাই-স্টেপ আগা... -> Safe (30.0%)\n",
      "Text: প্রথম কাজ: আপনার কম্পিউটারে ফো... -> Safe (30.0%)\n",
      "Text: আপনার কম্পিউটারের যেকোনো ড্রাই... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-AI/\n",
      "│\n",
      "├──... -> Safe (30.0%)\n",
      "Text: ধাপ ১: মেশিন লার্নিং মডেল তৈরি... -> Safe (30.0%)\n",
      "Text: আপনার কম্পিউটারে টার্মিনাল (বা... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: এবার backend/train_model.py ফা... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/train_model.p... -> Phishing (27.22%)\n",
      "Text: ধাপ ২: ফ্লাস্ক ব্যাকএন্ড সার্ভ... -> Safe (30.0%)\n",
      "Text: backend/app.py ফাইলে নিচের কোড... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/app.py\n",
      "import... -> Spam (31.9%)\n",
      "Text: ⚠️ বিরতি: এতটুকু কি বুঝতে পেরে... -> Safe (30.0%)\n",
      "Text: ব্রো, একবারে সব কোড দিলে জ্যাম... -> Safe (30.0%)\n",
      "Text: এই দুটো হয়ে গেলে আমাকে জানান, ... -> Safe (30.0%)\n",
      "Text: ১. আপনি কি মেইন ফোল্ডার এবং সা... -> Safe (30.0%)\n",
      "Text: সাবাস ব্রো! ব্যাকএন্ড পার্ট সা... -> Safe (30.0%)\n",
      "Text: আপনার extension/ ফোল্ডারের ভেত... -> Safe (30.0%)\n",
      "Text: এটি আপনার এক্সটেনশনের পরিচয়পত্... -> Safe (30.0%)\n",
      "Text: ১. manifest.json... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: ২. content.js (হোয়াটসঅ্যাপ/মেস... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: আপনার টিচারের রিকোয়ারমেন্ট অনু... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"[Phish... -> Suspicious (64.46%)\n",
      "Text: ৩. background.js (সার্ভার কমিউ... -> Safe (30.0%)\n",
      "Text: এটি ক্রোম ব্রাউজারের ব্যাকগ্রা... -> Spam (31.9%)\n",
      "Text: ৪. popup.html (ম্যানুয়াল টেস্ট... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: টিচার বা এক্সটার্নাল বোর্ডের স... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: ৫. popup.js... -> Safe (30.0%)\n",
      "Text: পপআপ ড্যাশবোর্ডের স্ক্যান বাটন... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: 🚀 এখন ব্রাউজারে এক্সটেনশনটি যে... -> Safe (30.0%)\n",
      "Text: ১. আপনার গুগল ক্রোম ব্রাউজারটি... -> Safe (30.0%)\n",
      "Text: ব্যস! আপনার ব্রাউজারের এক্সটেন... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 🧪 কীভাবে চেক করবেন এটা কাজ করছ... -> Safe (30.0%)\n",
      "Text: আপনার ফ্লাস্ক ব্যাকএন্ড সার্ভা... -> Scam (96.85%)\n",
      "Text: এক্সটেনশনটা লোড করে একটা টেস্ট... -> Safe (30.0%)\n",
      "Text: ব্রো, আপনি আপনার ফ্লাস্কের app... -> Safe (30.0%)\n",
      "Text: সমস্যাটা কোথায়?... -> Safe (30.0%)\n",
      "Text: আপনার কোডের এই লাইনে খেয়াল কর... -> Safe (30.0%)\n",
      "Text: Python\n",
      "probabilities = model.p... -> Safe (30.0%)\n",
      "Text: আমরা মডেল ট্রেইনিং কোডে (train... -> Safe (30.0%)\n",
      "Text: Python\n",
      "pipeline = Pipeline([\n",
      " ... -> Safe (30.0%)\n",
      "Text: Scikit-learn-এর Pipeline অবজেক... -> Safe (30.0%)\n",
      "Text: সবচেয়ে বড় সমস্যা হলো, আমরা ডে... -> Safe (30.0%)\n",
      "Text: ডিপার্টমেন্টের প্রফেসরের সামনে... -> Safe (30.0%)\n",
      "Text: সম্পূর্ণ সংশোধিত backend/app.p... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Suspicious (36.36%)\n",
      "Text: এখন আপনার করণীয়:... -> Safe (30.0%)\n",
      "Text: ১. এই নতুন কোডটি backend/app.p... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:21] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: সার্ভার কি কোনো এরর ছাড়া স্মুথ... -> Safe (30.0%)\n",
      "Text: ব্রো, উইন্ডোজে এই SystemExit: ... -> Safe (30.0%)\n",
      "Text: যেহেতু আমরা জুপিটার নোটবুক বা ... -> Safe (30.0%)\n",
      "Text: আপনার backend/app.py ফাইলের এক... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python\n",
      "if __name__ == '__main_... -> Spam (31.9%)\n",
      "Text: অনেক সময় আগের ফেইল হওয়া রানটি ... -> Safe (30.0%)\n",
      "Text: ⚠️ যদি আগের কোনো হ্যাং হওয়া প্... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "Taskkill /IM python.exe /... -> Safe (30.0%)\n",
      "Text: (অথবা আপনি চাইলে পোর্টের ঝামেল... -> Safe (30.0%)\n",
      "Text: এবার ফাইলটি সেভ করে আবার রান দ... -> Safe (30.0%)\n",
      "Text: আশা করছি এবার আর কোনো SystemEx... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# ১. প্রয়োজনীয় সিস্টেম ... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: # ১. প্রয়োজনীয় সিস্টেম লাইব্রে... -> Safe (30.0%)\n",
      "Text: # ২. বিল্ডোজার এবং সাইথন ইনস্ট... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!mkdir -p ~/.android &&... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# এটি সরাসরি অ্যান্ড্রয়... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python... -> Safe (30.0%)\n",
      "Text: # এটি সরাসরি অ্যান্ড্রয়েড এসডি... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "\n",
      "with open('b... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: 'buildozer.spec'... -> Safe (30.0%)\n",
      "Text: 'buildozer.spec'... -> Safe (30.0%)\n",
      "Text: 'p4a.branch ='... -> Safe (30.0%)\n",
      "Text: 'p4a.branch = develop\\n'... -> Safe (30.0%)\n",
      "Text: \"Spec file updated to p4a.bran... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# রুট ইউজার হিসেবে চালা... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: # রুট ইউজার হিসেবে চালানোর পার... -> Safe (30.0%)\n",
      "Text: Ini, TOML\n",
      "[app]\n",
      "\n",
      "# (str) Title... -> Suspicious (34.92%)\n",
      "Text: Ini, TOML... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # (str) Title of your applicat... -> Safe (30.0%)Text: # (str) Package name... -> Safe (30.0%)\n",
      "\n",
      "Text: package.name... -> Safe (30.0%)\n",
      "Text: # (str) Package domain (needed... -> Safe (30.0%)\n",
      "Text: package.domain... -> Safe (30.0%)\n",
      "Text: # (str) Source code where the ... -> Safe (30.0%)\n",
      "Text: source.dir... -> Safe (30.0%)\n",
      "Text: # (list) Source files to inclu... -> Safe (30.0%)\n",
      "Text: source.include_exts... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # (str) Application versioning... -> Safe (30.0%)\n",
      "Text: version... -> Safe (30.0%)\n",
      "Text: # (list) Application requireme... -> Safe (30.0%)\n",
      "Text: # Colab এ স্ট্যাবিলিটির জন্য k... -> Safe (30.0%)\n",
      "Text: requirements... -> Safe (30.0%)\n",
      "Text: # (str) Supported orientations... -> Safe (30.0%)\n",
      "Text: orientation... -> Safe (30.0%)\n",
      "Text: # ----------------------------... -> Safe (30.0%)\n",
      "Text: # Android specific configurati... -> Safe (30.0%)\n",
      "Text: # ----------------------------... -> Safe (30.0%)\n",
      "Text: # (list) Permissions... -> Safe (30.0%)\n",
      "Text: android.permissions... -> Safe (30.0%)\n",
      "Text: # (int) Target Android API, sh... -> Safe (30.0%)\n",
      "Text: android.api... -> Safe (30.0%)\n",
      "Text: # (int) Minimum API your APK w... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:22] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: android.minapi... -> Safe (30.0%)\n",
      "Text: # (str) Android NDK version to... -> Safe (30.0%)\n",
      "Text: # Colab এবং Kivy 2.2.1 এর জন্য... -> Safe (30.0%)\n",
      "Text: android.ndk... -> Safe (30.0%)\n",
      "Text: # (bool) Use the private direc... -> Safe (30.0%)\n",
      "Text: android.private_storage... -> Safe (30.0%)\n",
      "Text: # (list) Services to run in th... -> Safe (30.0%)\n",
      "Text: android.services... -> Safe (30.0%)\n",
      "Text: # (list) Intent filters... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: android.manifest.intent_filter... -> Safe (30.0%)\n",
      "Text: \"name\"... -> Safe (30.0%)\n",
      "Text: \"android.service.notification.... -> Safe (30.0%)\n",
      "Text: \"actions\"... -> Safe (30.0%)\n",
      "Text: \"android.service.notification.... -> Safe (30.0%)\n",
      "Text: # (str) The Android arch to bu... -> Safe (30.0%)\n",
      "Text: android.archs... -> Safe (30.0%)\n",
      "Text: # (bool) enables Android auto ... -> Safe (30.0%)\n",
      "Text: android.allow_backup... -> Safe (30.0%)\n",
      "Text: # (str) python-for-android bra... -> Safe (30.0%)\n",
      "Text: # Colab এ বিল্ড এরর এড়াতে 'dev... -> Safe (30.0%)\n",
      "Text: p4a.branch... -> Safe (30.0%)\n",
      "Text: # ----------------------------... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: # Buildozer configurations... -> Safe (30.0%)\n",
      "Text: # ----------------------------... -> Safe (30.0%)\n",
      "Text: [buildozer]... -> Safe (30.0%)\n",
      "Text: # (int) Log level (2 = debug, ... -> Safe (30.0%)\n",
      "Text: log_level... -> Safe (30.0%)\n",
      "Text: # (int) Display warning if bui... -> Suspicious (50.99%)\n",
      "Text: warn_on_root... -> Safe (30.0%)\n",
      "Text: Python\n",
      "!buildozer -v android d... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-Extension... -> Safe (30.0%)\n",
      "Text: Plaintext... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import os\n",
      "import pickle... -> Phishing (36.81%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: Python... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:23] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # ১. ডেমো ডাটাসেট তৈরি (আপনার ... -> Safe (30.0%)\n",
      "Text: # বাস্তবে এখানে Kaggle বা বড় C... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: \"Congratulations! You won a $1... -> Scam (96.85%)\n",
      "Text: \"Your Netflix account is suspe... -> Phishing (97.19%)\n",
      "Text: \"Hi, are we still meeting for ... -> Safe (96.48%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"URGENT: Your bank account has... -> Phishing (96.62%)\n",
      "Text: \"Get rich quick! Earn $5000 a ... -> Spam (97.64%)\n",
      "Text: \"The weather today is cloudy w... -> Safe (62.42%)\n",
      "Text: \"Your package from Amazon cann... -> Phishing (56.38%)\n",
      "Text: \"Please review the attached pr... -> Safe (97.02%)\n",
      "Text: \"⚠️ WARNING: Your PC is infect... -> Suspicious (96.48%)\n",
      "Text: \"Hey bro, can you lend me some... -> Scam (94.19%)\n",
      "Text: \"Verify your login attempt fro... -> Suspicious (96.56%)\n",
      "Text: 'Phishing'... -> Safe (30.0%)\n",
      "Text: 'Scam'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'label'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'Phishing'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'Spam'... -> Safe (30.0%)\n",
      "Text: 'Phishing'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'Suspicious'... -> Safe (30.0%)\n",
      "Text: 'Scam'... -> Safe (30.0%)\n",
      "Text: 'Suspicious'... -> Safe (30.0%)\n",
      "Text: \"--- Data Loading Complete ---... -> Safe (30.0%)\n",
      "Text: 'label'... -> Safe (30.0%)\n",
      "Text: # ২. ফিচার এবং লেবেল আলাদা করা... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'label'... -> Safe (30.0%)Text: 'text'... -> Safe (30.0%)\n",
      "\n",
      "Text: # ৩. ট্রেইন এবং টেস্ট স্প্লিট ... -> Safe (30.0%)\n",
      "Text: # ৪. TF-IDF + Naive Bayes পাইপ... -> Safe (30.0%)\n",
      "Text: # এটি টেক্সটকে সংখ্যায় রূপান্ত... -> Safe (30.0%)\n",
      "Text: 'tfidf'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:24] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'english'... -> Safe (30.0%)\n",
      "Text: # ৫. মডেল ট্রেইনিং... -> Safe (30.0%)\n",
      "Text: # ৬. ইভালুয়েশন... -> Safe (30.0%)\n",
      "Text: f\"\\nModel Accuracy: {accuracy_... -> Safe (30.0%)\n",
      "Text: # ৭. মডেল এবং ভেক্টরাইজার সেভ ... -> Safe (30.0%)\n",
      "Text: 'backend'... -> Safe (30.0%)\n",
      "Text: 'model.pkl'... -> Safe (30.0%)\n",
      "Text: \"\\n[SUCCESS] model.pkl success... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Spam (31.9%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # এক্সটেনশন থেকে রিকোয়েস্ট ব্ল... -> Safe (30.0%)\n",
      "Text: # ট্রেইনড মডেল পাইপলাইন লোড কর... -> Safe (30.0%)\n",
      "Text: 'model.pkl'... -> Safe (30.0%)\n",
      "Text: \"[SUCCESS] Machine Learning Mo... -> Safe (30.0%)\n",
      "Text: except... -> Safe (30.0%)\n",
      "Text: \"[ERROR] model.pkl not found! ... -> Safe (30.0%)\n",
      "Text: @app.route('/predict', methods... -> Safe (30.0%)\n",
      "Text: def predict():... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: 'error'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'No text provided'... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: # মডেল এর মাধ্যমে প্রেডিকশন এব... -> Safe (30.0%)\n",
      "Text: # হায়েস্ট প্রব্যাবিলিটিকে রিস... -> Safe (30.0%)\n",
      "Text: # ক্লাসিফিকেশন এর ওপর ভিত্তি ক... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'text_analyzed'... -> Safe (30.0%)\n",
      "Text: # লগিং এর জন্য আংশিক টেক্সট... -> Safe (30.0%)\n",
      "Text: 'prediction'... -> Safe (30.0%)\n",
      "Text: 'risk_score'... -> Safe (30.0%)\n",
      "Text: f\"{risk_score}%\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'is_safe'... -> Safe (30.0%)Text: f\"Analyzed: {response['text_an... -> Safe (30.0%)\n",
      "\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: '__main__'... -> Safe (30.0%)\n",
      "Text: # সম্পূর্ণ অফলাইন লোকালহোস্টে ... -> Safe (30.0%)\n",
      "Text: '127.0.0.1'... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: \"manifest_version\"... -> Safe (30.0%)\n",
      "Text: \"name\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"PhishGuard AI AI-Powered Defe... -> Safe (30.0%)\n",
      "Text: \"version\"... -> Safe (30.0%)\n",
      "Text: \"description\"... -> Safe (30.0%)\n",
      "Text: \"Analyzes notifications and we... -> Safe (30.0%)\n",
      "Text: \"permissions\"... -> Safe (30.0%)\n",
      "Text: \"notifications\"... -> Safe (30.0%)\n",
      "Text: \"activeTab\"... -> Safe (30.0%)\n",
      "Text: \"background\"... -> Safe (30.0%)\n",
      "Text: \"service_worker\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:25] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"background.js\"... -> Safe (30.0%)\n",
      "Text: \"content_scripts\"... -> Safe (30.0%)\n",
      "Text: \"matches\"... -> Safe (30.0%)\n",
      "Text: \"<all_urls>\"... -> Safe (30.0%)\n",
      "Text: \"content.js\"... -> Safe (30.0%)\n",
      "Text: \"action\"... -> Safe (30.0%)\n",
      "Text: \"default_popup\"... -> Safe (30.0%)\n",
      "Text: \"popup.html\"... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (50.99%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: console... -> Safe (30.0%)\n",
      "Text: \"PhishGuard Content Script Act... -> Safe (30.0%)\n",
      "Text: // ১. ডেমো হিসেবে পেজের ভেতরের... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: // ইউনিভার্সিটি প্রজেক্ট ডেমো ... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: 'h2, p'... -> Safe (30.0%)\n",
      "Text: element =>... -> Safe (30.0%)\n",
      "Text: // খুব ছোট টেক্সট ইগনোর করার জ... -> Safe (30.0%)\n",
      "Text: // ব্যাকগ্রাউন্ড স্ক্রিপ্ট-এ ট... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: action... -> Safe (30.0%)\n",
      "Text: (response) =>... -> Safe (30.0%)\n",
      "Text: // যদি কন্টেন্ট সেফ না হয়, তবে... -> Safe (30.0%)\n",
      "Text: \"3px dashed red\"... -> Safe (30.0%)\n",
      "Text: \"#ffe6e6\"... -> Safe (30.0%)\n",
      "Text: `Warning: Classified as ${resp... -> Suspicious (50.99%)\n",
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: (request, sender, sendResponse... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: // লোকাল ফ্লাস্ক সার্ভার এপিআই... -> Safe (30.0%)\n",
      "Text: \"http://127.0.0.1:5000/predict... -> Spam (31.9%)\n",
      "Text: method... -> Safe (30.0%)\n",
      "Text: \"POST\"... -> Safe (30.0%)\n",
      "Text: headers... -> Safe (30.0%)\n",
      "Text: \"Content-Type\"... -> Safe (30.0%)\n",
      "Text: \"application/json\"... -> Safe (30.0%)\n",
      "Text: response =>... -> Safe (30.0%)\n",
      "Text: data =>... -> Safe (30.0%)\n",
      "Text: // যদি ফিশিং/স্ক্যাম ডিটেক্ট হ... -> Safe (30.0%)\n",
      "Text: \"basic\"... -> Safe (30.0%)\n",
      "Text: iconUrl... -> Safe (30.0%)\n",
      "Text: \"icon.png\"... -> Safe (30.0%)\n",
      "Text: // একটি ডেমো আইকন প্রজেক্ট ফোল... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: `🚨 PhishGuard Alert: ${data.pr... -> Safe (30.0%)\n",
      "Text: message... -> Safe (30.0%)\n",
      "Text: `Risk Score: ${data.risk_score... -> Safe (30.0%)\n",
      "Text: priority... -> Safe (30.0%)\n",
      "Text: error =>... -> Safe (30.0%)\n",
      "Text: console... -> Safe (30.0%)\n",
      "Text: \"Error connecting to local Fla... -> Safe (30.0%)\n",
      "Text: is_safe... -> Safe (30.0%)\n",
      "Text: prediction... -> Safe (30.0%)\n",
      "Text: \"Safe (Server Offline)\"... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: // Asynchronous রেসপন্স নিশ্চি... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: <!DOCTYPE html>... -> Safe (30.0%)\n",
      "Text: <html>... -> Safe (30.0%)\n",
      "Text: <head>... -> Safe (30.0%)\n",
      "Text: <style>... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: body { width: 250px; font-fami... -> Safe (30.0%)\n",
      "Text: </style>... -> Safe (30.0%)\n",
      "Text: </head>... -> Safe (30.0%)\n",
      "Text: <body>... -> Safe (30.0%)\n",
      "Text: <textarea id=\"testText\" rows=\"... -> Safe (30.0%)\n",
      "Text: </textarea>... -> Safe (30.0%)\n",
      "Text: <button id=\"checkBtn\" class=\"s... -> Safe (30.0%)\n",
      "Text: </button>... -> Safe (30.0%)\n",
      "Text: <div id=\"result\">... -> Safe (30.0%)\n",
      "Text: </div>... -> Safe (30.0%)\n",
      "Text: <script src=\"popup.js\">... -> Safe (30.0%)\n",
      "Text: </script>... -> Safe (30.0%)\n",
      "Text: </body>... -> Safe (30.0%)\n",
      "Text: </html>... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:26] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'checkBtn'... -> Safe (30.0%)\n",
      "Text: 'click'... -> Suspicious (36.19%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: 'testText'... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: 'result'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: \"block\"... -> Safe (30.0%)\n",
      "Text: \"Analyzing...\"... -> Safe (30.0%)\n",
      "Text: \"#eee\"... -> Safe (30.0%)\n",
      "Text: \"#333\"... -> Safe (30.0%)\n",
      "Text: action... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: (response) =>... -> Safe (30.0%)\n",
      "Text: `Result: ${response.prediction... -> Safe (30.0%)\n",
      "Text: \"#d4edda\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"#155724\"... -> Safe (30.0%)\n",
      "Text: \"#f8d7da\"... -> Safe (30.0%)\n",
      "Text: \"#721c24\"... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "python backend/app.py... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"PhishG... -> Suspicious (49.84%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: console... -> Safe (30.0%)\n",
      "Text: \"PhishGuard Real-time Scanner ... -> Safe (30.0%)\n",
      "Text: // ওয়েবসাইটের ডম (DOM) পরিবর্ত... -> Safe (30.0%)\n",
      "Text: (mutations) =>... -> Safe (30.0%)\n",
      "Text: (mutation) =>... -> Safe (30.0%)\n",
      "Text: (node) =>... -> Safe (30.0%)\n",
      "Text: // নোডের ভেতর টেক্সট আছে কিনা ... -> Safe (30.0%)\n",
      "Text: // মেসেজটি এনালাইসিস করার জন্য... -> Safe (30.0%)\n",
      "Text: action... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: (response) =>... -> Safe (30.0%)\n",
      "Text: // যদি ফিশিং বা স্ক্যাম ডিটেক্... -> Safe (30.0%)\n",
      "Text: \"3px solid red\"... -> Safe (30.0%)\n",
      "Text: \"#ffcccc\"... -> Safe (30.0%)\n",
      "Text: // সম্পূর্ণ ওয়েব পেজের ওপর নজর... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: childList... -> Safe (30.0%)\n",
      "Text: subtree... -> Safe (30.0%)\n",
      "Text: Plaintext\n",
      "PhishGuard-AI/\n",
      "│\n",
      "├──... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "pip install flask flask-c... -> Safe (30.0%)\n",
      "Text: Plaintext... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/train_model.p... -> Phishing (27.22%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: # backend/train_model.py... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # ইউনিভার্সিটি প্রজেক্টের রিকো... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: \"Hi, are we still meeting for ... -> Safe (96.48%)\n",
      "Text: \"Please review the attached pr... -> Safe (97.02%)\n",
      "Text: \"Your monthly electricity bill... -> Safe (95.96%)\n",
      "Text: \"Congratulations! You won a $1... -> Scam (96.85%)\n",
      "Text: \"Get rich quick! Earn $5000 a ... -> Spam (97.64%)\n",
      "Text: \"Your Netflix account is suspe... -> Phishing (97.19%)\n",
      "Text: \"URGENT: Your bank account has... -> Phishing (96.62%)\n",
      "Text: \"⚠️ WARNING: Your PC is infect... -> Suspicious (96.48%)\n",
      "Text: \"Verify your login attempt fro... -> Suspicious (96.56%)\n",
      "Text: \"Hey bro, can you lend me some... -> Scam (96.65%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'label'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'Scam'... -> Safe (30.0%)\n",
      "Text: 'Spam'... -> Safe (30.0%)\n",
      "Text: 'Phishing'... -> Safe (30.0%)\n",
      "Text: 'Phishing'... -> Safe (30.0%)\n",
      "Text: 'Suspicious'... -> Safe (30.0%)\n",
      "Text: 'Suspicious'... -> Safe (30.0%)\n",
      "Text: 'Scam'... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: 'label'... -> Safe (30.0%)\n",
      "Text: # TF-IDF + Naive Bayes পাইপলাই... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:27] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'tfidf'... -> Safe (30.0%)\n",
      "Text: 'english'... -> Safe (30.0%)\n",
      "Text: # মডেল সেভ করা... -> Safe (30.0%)\n",
      "Text: 'model.pkl'... -> Safe (30.0%)\n",
      "Text: \"[SUCCESS] model.pkl successfu... -> Safe (30.0%)\n",
      "Text: Python\n",
      "# backend/app.py\n",
      "import... -> Spam (31.9%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: # backend/app.py... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # এক্সটেনশন থেকে রিকোয়েস্ট ব্ল... -> Safe (30.0%)\n",
      "Text: # মডেল লোড করা... -> Safe (30.0%)\n",
      "Text: 'model.pkl'... -> Safe (30.0%)\n",
      "Text: @app.route('/predict', methods... -> Safe (30.0%)\n",
      "Text: def predict():... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: 'error'... -> Safe (30.0%)\n",
      "Text: 'No text provided'... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: # প্রেডিকশন এবং রিস্ক স্কোর ক্... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'prediction'... -> Safe (30.0%)\n",
      "Text: 'risk_score'... -> Safe (30.0%)\n",
      "Text: f\"{risk_score}%\"... -> Safe (30.0%)\n",
      "Text: 'is_safe'... -> Safe (30.0%)\n",
      "Text: f\"Text: {text_content[:30]}...... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: '__main__'... -> Safe (30.0%)\n",
      "Text: '127.0.0.1'... -> Safe (30.0%)\n",
      "Text: JSON\n",
      "{\n",
      "  \"manifest_version\": 3... -> Safe (30.0%)\n",
      "Text: \"manifest_version\"... -> Safe (30.0%)\n",
      "Text: \"name\"... -> Safe (30.0%)\n",
      "Text: \"PhishGuard AI-Powered Defende... -> Safe (30.0%)\n",
      "Text: \"version\"... -> Safe (30.0%)\n",
      "Text: \"description\"... -> Safe (30.0%)\n",
      "Text: \"Analyzes external notificatio... -> Safe (30.0%)\n",
      "Text: \"permissions\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: \"notifications\"... -> Safe (30.0%)\n",
      "Text: \"activeTab\"... -> Safe (30.0%)\n",
      "Text: \"background\"... -> Safe (30.0%)\n",
      "Text: \"service_worker\"... -> Safe (30.0%)\n",
      "Text: \"background.js\"... -> Safe (30.0%)\n",
      "Text: \"content_scripts\"... -> Safe (30.0%)\n",
      "Text: \"matches\"... -> Safe (30.0%)\n",
      "Text: \"<all_urls>\"... -> Safe (30.0%)\n",
      "Text: \"content.js\"... -> Safe (30.0%)\n",
      "Text: \"action\"... -> Safe (30.0%)\n",
      "Text: \"default_popup\"... -> Safe (30.0%)\n",
      "Text: \"popup.html\"... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "console.log(\"[Phish... -> Suspicious (64.46%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: console... -> Safe (30.0%)\n",
      "Text: \"[PhishGuard] Real-time Scrapi... -> Safe (30.0%)\n",
      "Text: // ডম (DOM) পরিবর্তনের ওপর নজর... -> Safe (30.0%)\n",
      "Text: (mutations) =>... -> Safe (30.0%)\n",
      "Text: (mutation) =>... -> Safe (30.0%)\n",
      "Text: (node) =>... -> Safe (30.0%)\n",
      "Text: // নোডের ভেতর টেক্সট আছে কিনা ... -> Safe (30.0%)\n",
      "Text: // ব্যাকগ্রাউন্ড স্ক্রিপ্ট-এ ট... -> Safe (30.0%)\n",
      "Text: action... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: (response) =>... -> Safe (30.0%)\n",
      "Text: // যদি ফিশিং বা স্ক্যাম ডিটেক্... -> Safe (30.0%)\n",
      "Text: \"2px dashed red\"... -> Safe (30.0%)\n",
      "Text: \"#ffe6e6\"... -> Safe (30.0%)\n",
      "Text: `Warning: ${response.predictio... -> Suspicious (50.99%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:28] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: // সম্পূর্ণ ওয়েব পেজের এলিমেন্... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: childList... -> Safe (30.0%)\n",
      "Text: subtree... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "chrome.runtime.onMe... -> Spam (31.9%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n",
      "Text: (request, sender, sendResponse... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: \"http://127.0.0.1:5000/predict... -> Spam (31.9%)\n",
      "Text: method... -> Safe (30.0%)\n",
      "Text: \"POST\"... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: headers... -> Safe (30.0%)\n",
      "Text: \"Content-Type\"... -> Safe (30.0%)\n",
      "Text: \"application/json\"... -> Safe (30.0%)\n",
      "Text: response =>... -> Safe (30.0%)\n",
      "Text: data =>... -> Safe (30.0%)\n",
      "Text: // যদি Safe ছাড়া অন্য কিছু (Ph... -> Safe (30.0%)\n",
      "Text: \"basic\"... -> Safe (30.0%)\n",
      "Text: iconUrl... -> Safe (30.0%)\n",
      "Text: \"icon.png\"... -> Safe (30.0%)\n",
      "Text: // (অপশনাল) এক্সটেনশন ফোল্ডারে... -> Safe (30.0%)\n",
      "Text: `🚨 PhishGuard Alert: ${data.pr... -> Safe (30.0%)\n",
      "Text: message... -> Safe (30.0%)\n",
      "Text: `Risk Score: ${data.risk_score... -> Safe (30.0%)\n",
      "Text: priority... -> Safe (30.0%)\n",
      "Text: error =>... -> Safe (30.0%)\n",
      "Text: \"Flask server offline or error... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: console... -> Safe (30.0%)\n",
      "Text: is_safe... -> Safe (30.0%)\n",
      "Text: prediction... -> Safe (30.0%)\n",
      "Text: \"Safe\"... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: // Asynchronous রেসপন্স হ্যান্... -> Safe (30.0%)\n",
      "Text: HTML\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<h... -> Safe (30.0%)\n",
      "Text: <!DOCTYPE html>... -> Safe (30.0%)\n",
      "Text: <html>... -> Safe (30.0%)\n",
      "Text: <head>... -> Safe (30.0%)\n",
      "Text: <style>... -> Safe (30.0%)\n",
      "Text: body { width: 280px; font-fami... -> Safe (30.0%)\n",
      "Text: </style>... -> Safe (30.0%)\n",
      "Text: </head>... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: <body>... -> Safe (30.0%)\n",
      "Text: <textarea id=\"testText\" rows=\"... -> Safe (30.0%)\n",
      "Text: </textarea>... -> Safe (30.0%)\n",
      "Text: <button id=\"checkBtn\">... -> Safe (30.0%)\n",
      "Text: </button>... -> Safe (30.0%)\n",
      "Text: <div id=\"result\">... -> Safe (30.0%)\n",
      "Text: </div>... -> Safe (30.0%)\n",
      "Text: <script src=\"popup.js\">... -> Safe (30.0%)\n",
      "Text: </script>... -> Safe (30.0%)\n",
      "Text: </body>... -> Safe (30.0%)\n",
      "Text: </html>... -> Safe (30.0%)\n",
      "Text: JavaScript\n",
      "document.getElement... -> Suspicious (36.19%)\n",
      "Text: JavaScript... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: document... -> Safe (30.0%)\n",
      "Text: 'checkBtn'... -> Safe (30.0%)\n",
      "Text: 'click'... -> Suspicious (36.19%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: 'testText'... -> Safe (30.0%)\n",
      "Text: document... -> Safe (30.0%)\n",
      "Text: 'result'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: \"block\"... -> Safe (30.0%)\n",
      "Text: \"Analyzing Content...\"... -> Safe (30.0%)\n",
      "Text: \"#f1f1f1\"... -> Safe (30.0%)\n",
      "Text: \"#333\"... -> Safe (30.0%)\n",
      "Text: action... -> Safe (30.0%)\n",
      "Text: \"analyze_text\"... -> Safe (30.0%)\n",
      "Text: (response) =>... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:29] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: `Classification: ${response.pr... -> Safe (30.0%)\n",
      "Text: \"#d4edda\"... -> Safe (30.0%)\n",
      "Text: \"#155724\"... -> Safe (30.0%)\n",
      "Text: \"#f8d7da\"... -> Safe (30.0%)\n",
      "Text: \"#721c24\"... -> Safe (30.0%)\n",
      "Text: Python\n",
      "probabilities = model.p... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: Python\n",
      "pipeline = Pipeline([\n",
      " ... -> Safe (30.0%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: 'tfidf'... -> Safe (30.0%)\n",
      "Text: Python\n",
      "import pickle\n",
      "import nu... -> Suspicious (36.36%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: import... -> Safe (30.0%)\n",
      "Text: import... -> Safe (30.0%)\n",
      "Text: # এক্সটেনশন থেকে রিকোয়েস্ট ব্... -> Safe (30.0%)\n",
      "Text: # মডেল লোড করা... -> Safe (30.0%)\n",
      "Text: 'model.pkl'... -> Safe (30.0%)\n",
      "Text: \"[SUCCESS] Machine Learning Mo... -> Safe (30.0%)\n",
      "Text: except... -> Safe (30.0%)\n",
      "Text: \"[ERROR] model.pkl ফাইলটি পাওয়... -> Safe (30.0%)\n",
      "Text: @app.route('/predict', methods... -> Safe (30.0%)\n",
      "Text: def predict():... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: 'error'... -> Safe (30.0%)\n",
      "Text: 'No text provided'... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: hasattr... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'trim'... -> Safe (30.0%)\n",
      "Text: 'text'... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: 'prediction'... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'risk_score'... -> Safe (30.0%)\n",
      "Text: 'is_safe'... -> Safe (30.0%)\n",
      "Text: # ১. টেক্সট ক্লাসিফাই করা (Saf... -> Safe (30.0%)\n",
      "Text: # ২. পাইপলাইনের ভেতর থেকে সেফল... -> Safe (30.0%)\n",
      "Text: # ৩. হায়েস্ট প্রব্যাবিলিটি নি... -> Safe (30.0%)\n",
      "Text: except... -> Safe (30.0%)\n",
      "Text: # কোনো কারণে প্রব্যাবিলিটি ফেই... -> Safe (30.0%)\n",
      "Text: f\"[Warning] Probability calcul... -> Suspicious (50.99%)\n",
      "Text: # ডিফল্ট কনফিডেন্স... -> Safe (30.0%)\n",
      "Text: 'Safe'... -> Safe (30.0%)\n",
      "Text: 'prediction'... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: 'risk_score'... -> Safe (30.0%)\n",
      "Text: f\"{risk_score}%\"... -> Safe (30.0%)\n",
      "Text: 'is_safe'... -> Safe (30.0%)\n",
      "Text: # টার্মিনালে সুন্দর লগ দেখার জ... -> Safe (30.0%)\n",
      "Text: f\"Text Snippet: {text_content[... -> Safe (30.0%)\n",
      "Text: return... -> Safe (30.0%)\n",
      "Text: '__main__'... -> Safe (30.0%)\n",
      "Text: # ৫০০০ পোর্টে লোকালহোস্টে সার্... -> Safe (30.0%)\n",
      "Text: '127.0.0.1'... -> Safe (30.0%)\n",
      "Text: Python\n",
      "if __name__ == '__main_... -> Spam (31.9%)\n",
      "Text: Python... -> Safe (30.0%)\n",
      "Text: '__main__'... -> Safe (30.0%)\n",
      "Text: # উইন্ডোজে স্ট্যাবিলিটির জন্য ... -> Safe (30.0%)\n",
      "Text: '127.0.0.1'... -> Safe (30.0%)\n",
      "Text: Bash\n",
      "Taskkill /IM python.exe /... -> Safe (30.0%)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [16/May/2026 09:49:30] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "# backend/app.py\n",
    "import pickle\n",
    "import numpy as np\n",
    "from flask import Flask, request, jsonify\n",
    "from flask_cors import CORS\n",
    "\n",
    "app = Flask(__name__)\n",
    "CORS(app)\n",
    "\n",
    "with open('model.pkl', 'rb') as f:\n",
    "    model = pickle.load(f)\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    data = request.get_json()\n",
    "    if not data or 'text' not in data:\n",
    "        return jsonify({'error': 'No text provided'}), 400\n",
    "    \n",
    "    text_content = data['text']\n",
    " \n",
    "    prediction = model.predict([text_content])[0]\n",
    "    probabilities = model.predict_proba([text_content])[0]\n",
    "    risk_score = round(float(np.max(probabilities)) * 100, 2)\n",
    "    \n",
    "    is_safe = True if prediction == 'Safe' else False\n",
    "    \n",
    "    response = {\n",
    "        'prediction': prediction,\n",
    "        'risk_score': f\"{risk_score}%\",\n",
    "        'is_safe': is_safe\n",
    "    }\n",
    "    \n",
    "    print(f\"Text: {text_content[:30]}... -> {prediction} ({risk_score}%)\")\n",
    "    return jsonify(response)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
