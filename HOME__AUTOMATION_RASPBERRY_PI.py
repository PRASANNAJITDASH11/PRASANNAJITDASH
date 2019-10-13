# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:19:08 2019

@author: user
"""

# =============================================================================
# Hello reader, I’m glad you are here. Welcome to another code showdown. In this post, I’m going to tell you about home automation with Raspberry Pi, Python, VueJS+CSS+HTML and an Arduino relay module.
# First of all, let’s describe the goals of each requisite:
# Raspberry Pi -> will serve as a host to our Control API and our Web page. Those 40 GPIO (General Purpose Input Output) will come handy connecting relays and sensors.
# Arduino Relay Module -> will turn on/off a house electrical device, such as lamps, coffee machines, tvs, etc. It will connect directly to Raspberry’s GPIO.
# Python -> will work as a server (using Flask) providing an API to control the GPIO and a file host, to send our HTML interface.
# VueJS+CSS+HTML -> we will create a VueJS instance to send/receive data to our Python API utilizing axios. And of course, update our picture to show that if your device is either on or off.
# 
# =============================================================================

#With everything on hand, let’s get started. First, you will want to install some dependencies. To help you, here is the command.
$ sudo pip3 install flask RPi.GPIO
# =============================================================================
# Note that I’m running Python 3, with pip3 (python package manager). If you prefer working with Python 2, use only pip instead of pip3. To read/write to GPIO you may need to be root, so be sure to install it as a super user.
# Web Server with Flask
# As this API does not need to be high performance and scalable, we can simply use the built-in server host with Flask. Take a look at the following code and pay attention to the comments as they will explain a lot.
# =============================================================================

# =============================================================================
# Static files
# As we make use of VueJS, we will need to serve the source file (vue.js) aside with axios.js to assure that our application will work without internet connection. With everything on hand, let’s get started. First, you will want to install some dependencies. To help you, here is the command.
# =============================================================================
$ sudo pip3 install flask RPi.GPIO
# =============================================================================
# Note that I’m running Python 3, with pip3 (python package manager). If you prefer working with Python 2, use only pip instead of pip3. To read/write to GPIO you may need to be root, so be sure to install it as a super user.
# Web Server with Flask
# As this API does not need to be high performance and scalable, we can simply use the built-in server host with Flask. Take a look at the following code and pay attention to the comments as they will explain a lot.
# 
# =============================================================================
# =============================================================================
# Run after reboot
# Well, every time that I reboot my system, will it need a manual intervention to start the web server?
# Actually, this can be automated with crontab, that will help us to run our server upon reboot and make sure that everything is running. Of course, if you encounter some issue, just reboot it and it will automatically be brought up to life.
# To edit the Rasberry’s cron schedule, just run
# =============================================================================
$ sudo crontab -e
# =============================================================================
# If is the first time that you are editing it, you will be asked which text editor you would like to use. I personally prefer nano over vi, as I find it more user friendly.
# Upon editing, just add the following line at the end of the file:
# =============================================================================
@reboot sudo python3 /home/pi/control.py &
# =============================================================================
# If you are using nano, just type CTRL + X, press ‘y’ and save it.
# Full code on:
# PythonLamp
# Simple Home Automation-Python + Relay Module (RPi) With everything on hand, let's get started. First, you will want to install some dependencies. To help you, here is the command. 
# =============================================================================

$ sudo pip3 install flask RPi.GPIO
# =============================================================================
# Note that I'm running Python 3, with pip3 (python package manager). If you prefer working with Python 2, use only pip instead of pip3. To read/write to GPIO you may need to be root, so be sure to install it as a super user.
# =============================================================================

# =============================================================================
# Web Server with Flask
# As this API does not need to be high performance and scalable, we can simply use the built-in server host with Flask. Take a look at the following code and pay attention to the comments as they will explain a lot.
# Run after reboot
# Well, every time that I reboot my system, will it need a manual intervention to start the web server?  Actually, this can be automated with crontab, that will help us to run our server upon reboot and make sure that everything is running. Of course, if you encounter some issue, just reboot it and it will automatically be brought up to life. To edit the Rasberry's cron schedule, just run 
# 
# =============================================================================
$ sudocrontab -e
#If is the first time that you are editing it, you will be asked which text editor you would like to use. I personally prefer nano over vi, as I find it more user friendly. Upon editing, just add the following line at the end of the file:

@reboot sudo python3 /home/pi/control.py &
# =============================================================================
# If you are using nano, just type CTRL + X, press 'y' and save it.
# PythonLamp
# Simple Home Automation-Python + Relay Module (RPi) With everything on hand, let's get started. First, you will want to install some dependencies. To help you, here is the command. 
# =============================================================================

$ sudo pip3 install flask RPi.GPIO
# =============================================================================
# Note that I'm running Python 3, with pip3 (python package manager). If you prefer working with Python 2, use only pip instead of pip3. To read/write to GPIO you may need to be root, so be sure to install it as a super user.
# Web Server with Flask
# As this API does not need to be high performance and scalable, we can simply use the built-in server host with Flask. Take a look at the following code and pay attention to the comments as they will explain a lot.
# 
# =============================================================================
# =============================================================================
# Run after reboot
# Well, every time that I reboot my system, will it need a manual intervention to start the web server?  Actually, this can be automated with crontab, that will help us to run our server upon reboot and make sure that everything is running. Of course, if you encounter some issue, just reboot it and it will automatically be brought up to life. To edit the Rasberry's cron schedule, just run 
# 
# =============================================================================
$ sudocrontab -e
# =============================================================================
# If is the first time that you are editing it, you will be asked which text editor you would like to use. I personally prefer nano over vi, as I find it more user friendly. Upon editing, just add the following line at the end of the file:
# 
# =============================================================================
@reboot sudo python3 /home/pi/control.py &
# =============================================================================
# If you are using nano, just type CTRL + X, press 'y' and save it.    
# =============================================================================
