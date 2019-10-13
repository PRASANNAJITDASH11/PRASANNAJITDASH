#!/bin/bash
$sudo raspi-config
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
# =============================================================================
# No, unfortunately not. You must recompile ffmpeg to add enable additional libraries. Below is the script I build to compile ffmpeg with alsa, fdk-aac, and libx264 support. It will install ffmpeg in your home folder inside a "ffmpeg" folder, so you'll need to call it specifically from there unless you add it to your path. I recommend uninstalling your current ffmpeg before using my script.
# Btw, I am able to stream directly to YouTube now without any issues. I use an external USB sound card and the PiCam v2 and stream a 1920x1080@25fps video stream with a 192kbps stereo audio stream mixed in. It works great!
# =============================================================================
#Any way to add alsa support to ffmpeg without recompiling?
#Quote,Sun Feb 11, 2018 6:56 pm,Hi! I have ffmpeg compiled and running based on these instructions. My USB mini mic is known-working, because:
#Get some required libraries and header files for x264 and OMX--player
#Get some required libraries and header files for x264 and OMX--player
$arecord -D plughw:1,0 -d 3.0 test.wav && aplay test.wav
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
#results in sound coming out of my earphones, as expected. But when I attempt to feed in sound from a USB mini mic via:
$sudo ffmpeg -f alsa -i hw:1 -t 30 out.wav
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
#I get the error
#Unknown input format: 'alsa'
#Based on this StackExchange answer, it looks like I may not have had alsa support configured when I compiled ffmpeg.
#On my machine, grep alsa configure returns:
#Code: Select all
#Get some required libraries and header files for x264 and OMX--player
$sudo apt-get install libasound2-dev libvpx. libx264. libomxil-bellagio-dev -y
$sudo apt-get install libasound2-dev --disable-alsa
$sudo apt disp-upgrade
$sudo apt-get dist-upgrade
$ sudo apt-get upgrade
 #--disable-alsa       #    disable ALSA support [autodetect]
$sudo apt-get install    alsa
$sudo nano alsa_indev_deps="alsa"
$sudo nano alsa_outdev_deps="alsa"
#enabled alsa && check_pkg_config alsa alsa "alsa/asoundlib.h" snd_pcm_htimestamp || check_lib alsa alsa/asoundlib.h snd_pcm_htimestamp -lasound
#I tried sudo apt-get install libasound2-dev after the fact, but that doesn't fix the problem.
#Is there a way to "install" support in ffmpeg for alsa without recompiling ffmpeg from scratch?
#Thanks!then use 
$sudo apt disp-upgrade
$sudo apt-get dist-upgrade
$ sudo apt-get upgrade
#Get FFMPEG source code
cd ~
git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
cd ffmpeg
mkdir dependencies
cd dependencies/
mkdir output
cd ~
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
#Compile libx264
git clone http://git.videolan.org/git/x264.git
cd x264/
./configure --enable-static --prefix=/home/pi/ffmpeg/dependencies/output/
make -j4
make install
cd ~
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
#Compile ALSA
# =============================================================================
# $wget ftp://ftp.alsa-project.org/pub/lib/alsa ... .1.tar.bz2
# $tar xjf alsa-lib-1.1.1.tar.bz2
# $cd alsa-lib-1.1.1/
# $./configure --prefix=/home/pi/ffmpeg/dependencies/output
# $make -j4
# $make install
# $cd ~
# =============================================================================
#Compile ALSA
$wget ftp://ftp.alsa-project.org/pub/lib/alsa ... .1.tar.bz2
$tar xjf alsa-lib-1.1.1.tar.bz2
$cd alsa-lib-1.1.1/
$./configure --prefix=/home/pi/ffmpeg/dependencies/output
$make -j4
$make install
$cd ~
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
#Compile FDK-AAC
sudo apt-get install pkg-config autoconf automake libtool -y
git clone https://github.com/mstorsjo/fdk-aac.git
cd fdk-aac
./autogen.sh
./configure --enable-shared --enable-static
make -j4
sudo make install
sudo ldconfig
cd ~
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
#Compile FFMPEG
cd ffmpeg
./configure --prefix=/home/pi/ffmpeg/dependencies/output --enable-gpl --enable-libx264 --enable-nonfree --enable-libfdk_aac --enable-omx --enable-omx-rpi --extra-cflags="-I/home/pi/ffmpeg/dependencies/output/include" --extra-ldflags="-L/home/pi/ffmpeg/dependencies/output/lib" --extra-libs="-lx264 -lpthread -lm -ldl"
make -j4
make install
cd ~ 
cd ffmpeg
./ffmpeg -re -thread_queue_size 512 -rtsp_transport tcp -i "rtsp://anonymous:password@192.168.1.10:554" -f concat -safe 0 -i playlist.txt -vcodec copy -acodec copy -t 01:47:02 -f flv "your-youtube-streaming-key"
#Hi! I have ffmpeg compiled and running based on these instructions. My USB mini mic is known-working, because:
$arecord -D plughw:1,0 -d 3.0 test.wav && aplay test.wav
#results in sound coming out of my earphones, as expected. But when I attempt to feed in sound from a USB mini mic via:
$sudo ffmpeg -f alsa -i hw:1 -t 30 out.wav --disable-alsa
#I get the error Unknown input format: 'alsa'
#it looks like I may not have had alsa support configured when I compiled ffmpeg.
#On my machine, grep alsa configure returns:
#Code: Select all
#
#  --disable-alsa           disable ALSA support [autodetect]
#    alsa
#alsa_indev_deps="alsa"
#alsa_outdev_deps="alsa"
#enabled alsa && check_pkg_config alsa alsa "alsa/asoundlib.h" snd_pcm_htimestamp ||
#    check_lib alsa alsa/asoundlib.h snd_pcm_htimestamp -lasound
#    
#I tried sudo apt-get install libasound2-dev after the fact, but that doesn't fix the problem.
#
#Is there a way to "install" support in ffmpeg for alsa without recompiling ffmpeg from scratch?
#
#Thanks!

$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade

# =============================================================================
# You're welcome, I'm glad I could finally contribute something to the forums!
# I meant YouTube Live, their live streaming service where anyone with a YouTube account can stream live video from a device, usually a smartphone but it can be any device with a video camera that can output h264 video and stream it via RTMP. Facebook Live operates the same way.
# Here are my two command lines, which captures video using raspivid and pipes it into ffmpeg, with ffmpeg capturing audio using the alsa plugin (for which I had to recompile ffmpeg) and muxing the h264 video and AAC audio streams into the FLV format for YouTube and Facebook.
# For live streaming to YouTube:
# =============================================================================
$raspivid -o - -t 0 -w 1920 -h 1080 -fps 25 -b 300000000000000000 -rot 270 -g 50 -f | /home/pi/ffmpeg/ffmpeg -thread_queue_size 10240 -f h264 -r 25 -i - -itsoffset 5.3 -f alsa -thread_queue_size 10240 -ac 2 -i hw:1,0 -vcodec copy -acodec aac -ac 2 -ar 44100 -ab 192k -f flv rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY
$sudo apt-get install alsa -alsa_indev_deps="alsa" -alsa_outdev_deps="alsa"
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
# =============================================================================
# For live streaming to Facebook (requires quotation marks around the URL and stream key):
##############################################################################
$raspivid -o - -t 0 -w 1920 -h 1080 -fps 25 -b 300000000000000000 -rot 270 -g 50 -f | /home/pi/ffmpeg/ffmpeg -thread_queue_size 10240 -f h264 -r 25 -i - -itsoffset 5.3 -f alsa -thread_queue_size 10240 -ac 2 -i plughw:1,0 -vcodec copy -acodec aac -ac 2 -ar 44100 -ab 192k -f flv "rtmp://rtmp-api.facebook.com:80/rtmp/YOUR_STREAM_KEY"
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
##############################################################################
################################################################################
$raspivid -o - -t 0 -h 720 -w 1296 -fps 24 -b 600000000000000000 | ./ffmpeg -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -thread_queue_size 512 -i - -vcodec copy -acodec aac -ab 128k -g 50 -preset ultrafast -crf 32 -strict experimental -f flv rtmp://173.194.183.168/live2/<MY_YOUTUBE_KEY>
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
###################################################################################
#For live streaming to YouTube:
raspivid -o - -t 0 -w 1920 -h 1080 -fps 25 -b 300000000000000000 -rot 270 -g 50 -f | /home/pi/ffmpeg/ffmpeg -thread_queue_size 10240 -f h264 -r 25 -i - -itsoffset 5.3 -f alsa -thread_queue_size 10240 -ac 2 -i hw:1,0 -vcodec copy -acodec aac -ac 2 -ar 44100 -ab 192k -f flv rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
#For live streaming to Facebook (requires quotation marks around the URL and stream key):
raspivid -o - -t 0 -w 1920 -h 1080 -fps 25 -b 300000000000000000 -rot 270 -g 50 -f | /home/pi/ffmpeg/ffmpeg -thread_queue_size 10240 -f h264 -r 25 -i - -itsoffset 5.3 -f alsa -thread_queue_size 10240 -ac 2 -i plughw:1,0 -vcodec copy -acodec aac -ac 2 -ar 44100 -ab 192k -f flv "rtmp://rtmp-api.facebook.com:80/rtmp/YOUR_STREAM_KEY"
$ sudo apt-get update
$ sudo apt-get dist-upgrade
$ sudo apt-get upgrade
(Replace YOUR_STREAM_KEY with your own key provided by YouTube or Facebook)
# =============================================================================
# Assuming you use my suggested command line for streaming to YouTube (below), are you certain you're specifying the correct audio recording device? If you haven't disabled the onboard audio device you should have at least one recording device and two playback devices, all with different hardware IDs. In my case, I had to use -i hw:1,0, but you could try -i hw:0,0 or -i hw:1,1 or -i hw:0,1. You can run arecord -l to list your recording devices and aplay -l to list your playback devices.
# If you want to disable the onboard audio device (it's playback only and won't affect recording), use sudo nano /etc/modules to edit the modules file, put a hash sign before snd-bcm2835 to make it #snd-bcm2835, then reboot. aplay -l will then report only one playback device, the USB audio adapter. If you do this all audio input and output will use the USB device, which will be the default.
# You should also know that I stopped using my device because it became unreliable during real (not tests at home) use. In one of my previous posts I detailed how the "speed=" indicator would gradually decrease over time while streaming, to the point where it was no longer streaming fast enough to prevent the dreaded buffering problem in YouTube. It happened every time, no matter what settings I adjusted. I was able to prolong the time until failure by reducing the bitrate but even when I reduced it to a terrible, high-compression setting it still eventually failed. I had better luck on a higher bandwidth connection but I was never able to resolve this; hopefully you can. If you do please share your solution with us! 
# I'll look into the audio device settings again. I did figure out that sound is going through but the volume level is barely audible ( I only figured this out because I sneezed almost right into the mic while I was testing) so I know the signal is going through, just the level is now the issue. - I should pre-face that I just got started with programming so I'm trying to get up to speed as quick as I can and I do appreciate your help. 
# I did use your code to start the stream and that works great. I haven't tried long term stream yet but I found the frame rate over about 10 minutes seemed to drop to 1.01x. I'll see if that changes on longer streams. IF I can get to even an hour without issues, I can reset for my purposes every hour. it would be a pain but still would work. 
# now with that all said, have you found a better way to live stream to Youtube/facebook with Video and Audio?
# I'm thinking I may have to look at streaming to my laptop and then use OBS to send it out to Youtube from there. 
# thanks again for your input.
# So with realizing the fact that the sound is there but very quiet, I played around with ALSAMIXER and increased the line levels to top end of the white before it goes red. that helped to some degree. you can now hear the audio but still too low. need to boost it to about double to be acceptable for what I need. I'm wanting to live stream a Karate Tournament next week... ya, tall order, I know. I need to set up 3 of these to be running. 
# # I did find one suggestion on Stackexchanger: 
# "You could try increasing the thread_queue_size to something like 4096 or even higher. I've seen it as high as 12000. I had a similar problem with my stream lagging and this seemed to fix it."
# Here's the thread where I found that information:
# https://raspberrypi.stackexchange.com/q ... -over-time
# =============================================================================
#Re: Any way to add alsa support to ffmpeg without recompiling?
#So with realizing the fact that the sound is there but very quiet, I played around with ALSAMIXER and increased the line levels to top end of the white before it goes red. that helped to some degree. you can now hear the audio but still too low. need to boost it to about double to be acceptable for what I need. I'm wanting to live stream 
# =============================================================================
# If your Raspberry Pi 4 will not boot, it is possible that the SPI EEPROM has become corrupted.
# To check, remove the SD card, disconnect the device from power, then reconnect it. If the green LED does not flash, you will need to reprogram the EEPROM:
# 1.Download the bootloader
# 2.Extract it to an empty FAT-formatted SD card and insert it into your Raspberry Pi 4
# 3.Connect the power and wait for the green LED to flash quickly
# Notes:
# •The updated bootloader improves compatibility with HATs by changing the behaviour of HALT to keep the 3V3 pin powered (view the full bootloader release notes)
# •The previous bootloader remains available for download
# Raspberry Pi Desktop (for PC and Mac)
# Debian with Raspberry Pi Desktop is the Foundation’s operating system for PC and Mac. You can create a live disc, run it in a virtual machine, or even install it on your computer.
# Raspberry Pi Desktop
# Third Party Operating System Images
# Third-party operating system images for Raspberry Pi are also available:
# # =============================================================================
#Re: Any way to add alsa support to ffmpeg without recompiling?
# =============================================================================
# Also, if you're looking for rock-solid streaming I highly recommend OBS but I really wanted to create an all-in-one live streaming device based on a Raspberry Pi 3B. I was able to run it on a Windows 10 laptop with no issues whatsoever....it ran exactly like I wanted it to but that would be much more expensive if you need to have three cameras running at once.
# So I've been playing with the code and figured out that Youtube will continue the stream even if the stream from the RPi stops and starts again. If you restart within about 10 seconds then the stream will 
# continue in the same stream.
# So my work around is to generate a script to start the stream code for a period of say 15 min, have it stop and then restart the stream. The stream would have a 5-10 second pause every 15 min but when live-streaming an event over 8 hours, it'd be better than having the sound out of sync.
# # my issue is, I'm still new to this and have no idea how to write the code to make The RPi do that. I know it's not an ideal solution but for what I need (live-stream an amateur tournament) it would work fine. Any suggestions on how to write that into the code to constantly loop the code to start, run for 15 min, stop and then start again? 
# Any help you could provide would be greatly appreciated. 
# Thanks. 
# That is a great idea! If I hadn't had cellular bandwidth issues I could've implemented it as a workaround.
# recommend you configure your streaming command line to run for 15 minutes, and call it from within another bash script that will restart your YouTube streaming script whenever it finishes. This should continue indefinitely until you CTRL-C or power off the Raspberry Pi. You will need to replace -t 0 with -t 900000 in your command line to stop streaming after 15 minutes (900,000ms=15 minutes). My previous command line is in the example script below; replace it with whatever you have tailored to your needs.
# =============================================================================
# =============================================================================
# Here's my suggestion:
# =============================================================================
#Create the bash script you will invoke when you want to stream to YouTube:
$sudo nano 15min_stream_loop.sh

#Within this script enter:
#!/bin/bash
while true
do
raspivid -o - -t 900000 -w 1920 -h 1080 -fps 25 -b 3000000 -rot 270 -g 50 -f | /home/pi/ffmpeg/ffmpeg -hide_banner -thread_queue_size 10240 -f h264 -r 25 -i - -itsoffset 5.3 -f alsa -thread_queue_size 10240 -ac 2 -i hw:1,0 -vcodec copy -acodec aac -ac 2 -ar 44100 -ab 192k -f flv rtmp://a.rtmp.youtube.com/live2/INSERT-YOUR-STREAMING-KEY-HERE
sleep 1
done

#Make the bash script executable:
chmod +x 15min_stream_loop.sh

#Run it:
./15min_stream_loop.sh

# =============================================================================
# Now it should stream to YouTube for 15 minutes, wait 1 second, then begin streaming again for 15 minutes....again and again until you kill it. You can test it by reducing the streaming time to 2 minutes (-t 120000) to ensure it is restarting the stream as intended.
# davethemoneyman 
# Posts: 8
# Joined: Wed Mar 20, 2019 2:04 am
# Re: Any way to add alsa support to ffmpeg without recompiling?
# •	Quote 
# Wed Mar 27, 2019 3:59 am 
# tropho wrote: Now it should stream to YouTube for 15 minutes, wait 1 second, then begin streaming again for 15 minutes....again and again until you kill it. You can test it by reducing the streaming time to 2 minutes (-t 120000) to ensure it is restarting the stream as intended. 
# Unfortunately it seems the Sleep command seems to be crashing the feed. As I'm watching the terminal lines get to the 2 min mark nothing seems to happen. Then the Youtube feed goes into buffering mode but the Terminal screen just keeps going. The fps starts to drop quickly from what was becoming a stable 31 down to 24 in the next 15 seconds. Youtube just hangs in buffering mode. 
# 
# When I enter the original single line code in Terminal on it's own it runs fine hovering at about 30 fps for at least 2hrs, I always ended it by that time. what I found I can do is cancel the stream in Terminal. Close the Terminal, open another Terminal window and run the code again with only a delay in Youtube of the time it took to do that. Youtube takes about 20-30 seconds to determine if the feed is done and then will close the stream. so as long as I can do that in the 20-30 seconds, the YT Stream buffers for the time that I re-ran the code and then continues.
# 
# This code doesn't seem to re-set the Rpi feed. Is there a way to code a program to open Terminal, run the line for the feed and then close the terminal in 20 min and then do it all over again? I would think that would be possible but it's beyond my ability to code that. I appreciate your help on this. I'd buy you a beer it's a little tough to send via internet.  
# Display posts from previous:
#   Sort by    
# # 
# # 
# # (Replace YOUR_STREAM_KEY with your own key provided by YouTube or Facebook)
# 
# Some things to note:
# 1. There is about a 10-15 second delay between what is being recorded and when it shows up on YouTube/Facebook.
# 2. If ffmpeg is not compiled with alsa support there is no way to stream audio, so it would be a silent video. If you don't want or need audio, there is a way to substitute a "dummy" audio device, since YouTube will reject live stream feeds without sound.
# 3. The itsoffset value may need to be adjusted for your particular sound device; I did a bunch of testing with a microphone to get the audio/video sync just right, coming up with my value of 5.3. Without it set at all the audio would play 5 seconds BEFORE the video!
# 4. The thread_queue_size prevents ALSA buffer underruns. I had to use the large value of 10240 to stop buffer underruns, at the expense of adding a time delay to the stream. Nothing less than 10240 completely stopped the ALSA buffer underruns.
# 5. If you don't want to see any streaming statistics on your screen, add -nostats -loglevel 0 after ffmpeg. I like to see the information so I can see that stream is working or if there are problems.
# 6. Even though I use a 1920x1080 resolution, I limited the video bitrate to a conservative 3mbps (3000000) because anything more would eventually cause YouTube/Facebook to buffer and pause since it was just too much for my Pi3 (or perhaps my internet upload bandwidth) to keep up with. A 192k audio bitrate is good enough, and anything more just increases the overall bandwidth requirements with very little gain in quality.
# 7. I use a USB external sound device to capture audio, using the stereo line input. I used alsamixer to set my recording levels and which input I wanted to use. The microphone input can also be used but it's mono.
# 8. I wrote a couple of short scripts to allow me to use the 4 buttons on my Adafruit PiTFT screen for starting live streams (YouTube or Facebook), capturing video straight to the 128GB flash drive (no live stream), and properly shutting down.
# 9. My hardware: Raspberry Pi 3 Model B, Raspberry Pi Cam v2, 4GB Sandisk microSD card, Adafruit PiTFT 2.8" LCD screen with buttons (model 2298), USB external sound device (https://goo.gl/ALjiit), 20,000mAh battery pack (provides about 14 hours of recording time)
# 
# As you can imagine with #8 and #9, I built a small video camera that can live stream or capture video anywhere since it's battery powered. I need either public WiFi or my smartphone's hotspot to connect to the internet, but besides that it is self-contained. I screwed a tripod mount on the bottom of the case so it can be mounted on a tripod, and used right-angle cables and velcro to keep it all compact and secure. I have attached pictures so you can see what it looks like. It resembles an oversized GoPro video camera.
# 
# 
# If you have any questions or wonder how or why I did something feel free to ask. I have read many forums and experimented to figure out how to make this work for me, and I would enjoy giving back to other users looking to solve their own challenges.
# 
# 
# 
# =============================================================================
# =============================================================================
# Re: Any way to add alsa support to ffmpeg without recompiling?
# Quote
# Wed Apr 25, 2018 1:34 am
# 
# Tue Feb 27, 2018 12:35 am
# No, unfortunately not. You must recompile ffmpeg to add enable additional libraries. Below is the script I build to compile ffmpeg with alsa, fdk-aac, and libx264 support.
# Thanks! I don't know why I didn't see this earlier. I'll try this when I get back from my trip.
# 
# Thu Mar 01, 2018 2:31 pm
# 2. If ffmpeg is not compiled with alsa support there is no way to stream audio, so it would be a silent video. If you don't want or need audio, there is a way to substitute a "dummy" audio device, since YouTube will reject live stream feeds without sound.
# I had this same problem. Another solution is to download some royalty-free MP3 files provided by YouTube. Use scp to copy them to your pi, then make a text file containing their filenames, and use ffmpeg's "concat" filter to play them in series, e.g.:
# Code: Select all
# =============================================================================


# =============================================================================
# With "-acodec copy" the CPU usage is nearly 0% for the audio stream. The "-t 01:47:02" is just the length of my playlist (which I got by copying and pasting the titles and lengths from iTunes into Excel).
# In my case I'm running ffmpeg on a different Pi than the Pi that my camera is built around, but I intend to change that once I get ffmpeg compiled on the camera Pi.
# tropho
# =============================================================================
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:31:46 2019

@author: user
"""

# =============================================================================
# Setting up an Apache Web Server on a Raspberry Pi
# Apache is a popular web server application you can install on the Raspberry Pi to allow it to serve web pages.
# 
# On its own, Apache can serve HTML files over HTTP, and with additional modules can serve dynamic web pages using scripting languages such as PHP.
# 
# Install Apache
# First, update the available packages by typing the following command into the Terminal:
# =============================================================================

sudo apt-get update
#Then, install the apache2 package with this command:

sudo apt-get install apache2 -y
# =============================================================================
# Test the web server
# By default, Apache puts a test HTML file in the web folder. This default web page is served when you browse to http://localhost/ on the Pi itself, or http://192.168.1.10 (whatever the Pi's IP address is) from another computer on the network. To find the Pi's IP address, type hostname -I at the command line (or read more about finding your IP address).
# 
# Browse to the default web page either on the Pi or from another computer on the network and you should see the following:
# 
# Apache success message
# 
# This means you have Apache working!
# 
# Changing the default web page
# This default web page is just an HTML file on the filesystem. It is located at /var/www/html/index.html.
# 
# Navigate to this directory in a terminal window and have a look at what's inside:
# 
# =============================================================================
cd /var/www/html
ls -al
#This will show you:

total 12
drwxr-xr-x  2 root root 4096 Jan  8 01:29 .
drwxr-xr-x 12 root root 4096 Jan  8 01:28 ..
-rw-r--r--  1 root root  177 Jan  8 01:29 index.html
#This shows that by default there is one file in /var/www/html/ called index.htmland it is owned by the root user (as is the enclosing folder). In order to edit the file, you need to change its ownership to your own username. Change the owner of the file (the default pi user is assumed here) using sudo chown pi: index.html.

#You can now try editing this file and then refreshing the browser to see the web page change.
#
#Your own website
#If you know HTML you can put your own HTML files and other assets in this directory and serve them as a website on your local network.

# =============================================================================
# Additional - install PHP
# To allow your Apache server to process PHP files, you'll need to install the latest version of PHP and the PHP module for Apache. Type the following command to install these:
# 
# =============================================================================
sudo apt-get install php libapache2-mod-php -y
#Now remove the index.html file:

sudo rm index.html
#and create the file index.php:

sudo leafpad index.php
#Note: Leafpad is a graphical editor. Alternatively, use nano if you're restricted to the command line

#Put some PHP content in it:

<?php echo "hello world"; ?>
#Now save and refresh your browser. You should see "hello world". This is not dynamic but still served by PHP. Try something dynamic:

<?php echo date('Y-m-d H:i:s'); ?>
#or show your PHP info:

<?php phpinfo(); ?>
#Further - WordPress
#Now you have Apache and PHP installed you can progress to setting up a WordPress site on your Pi. Continue to WordPress usage.

sudo apt update
sudo apt upgrade
sudo apt update

sudo apt install apache2

sudo chown -R pi:www-data /var/www/html/
sudo chmod -R 770 /var/www/html/


#If you do not already have a GUI on your Raspbian, or you use SSH to connect to your Raspberry, you can use the following command:

wget -O check_apache.html http://127.0.0.1

# =============================================================================
# his command will save the HTML code of the page in the file “check_apache.html” in the current directory.
# So you only have to read the file with the command
# =============================================================================

cat ./check_apache.html

# =============================================================================
# If you see marked at a location in the code “It works! ” is that Apache is working.
# 
# Apache uses the directory “/var/www/html” as the root for your site. This means that when you call your Raspberry on port 80 (http), Apache looks for the file in “/var/www/html”.
# For example, if you call the address “http://127.0.0.1/example”, Apache will look for the “example” file in the “/var/www/html” directory.
# To add new files, sites, etc., you will need to add them to this directory.
# 
# You can now use your Raspberry to make a site in HTML, CSS and JavaScript, internally.
# However, you may want to quickly allow interactions between the site and the user. For example, to allow the user to register, etc. For this, you are going to need PHP.
# 
# =============================================================================
# =============================================================================
# What is PHP ?
# First of all, you should know that PHP is an interpreted language. And as in the case of servers, the acronym PHP can have several meanings. In fact, when we talk about PHP, we can talk about either the language or the interpreter.
# Here, when we talk about installing PHP, it means that we will install the interpreter, in order to use the language.
# 
# PHP (the language this time) is mainly used to make a site dynamic, that is to say that the user sends information to the server which returns the modified results according to this information. Conversely, a static site doesn’t adapt to information provided by a user. It’s saved as a file once for all, and will always deliver the same content.
# 
# PHP is free, and maintained by the PHP Foundation, as well as Zend Enterprise, and various other companies (it should be noted that Zend is also the author of the famous Zend PHP framework, widely used and recognized in the world of ” business).
# 
# It’s one of the most widely used programming languages, and it is even the most used for web programming, with about 79% market share.
# 
# Again, all the skills you can acquire, on the language, or on the installation and configuration of the interpreter, will always be useful. So we can only advise you to learn the PHP, which is really a wonderful language and too often underestimated.
# 
# =============================================================================
# =============================================================================
# How to install PHP
# We will again use the administrator to install PHP with the command line.
# =============================================================================

sudo apt install php php-mbstring


# =============================================================================
# Control if PHP is working
# To know if PHP is working properly, it’s not very complicated, and the method is quite similar to the one used for Apache.
# 
# You will first delete the file “index.html” in the directory “/var/www/html”.
# =============================================================================
#
sudo rm /var/www/html/index.html
##Then create an “index.php” file in this directory, with this command line
#
echo "<?php phpinfo ();?>" > /var/www/html/index.php
#From there, the operation is the same as for the Apache check. You try to access your page, and you should have a result close to this image (if you do not have an interface, use the same method as before, and look for the words “PHP Version”).

# =============================================================================
# A MySQL database for your server
# A DBMS what’s it ? Why MySQL ?
# Now that we have set up PHP, you will probably want to store information for use in your sites. For this purpose, databases are most often used.
# We will therefore set up a DBMS (Database Management System), namely MySQL.
# 
# MySQL is a free, powerful, massively used DBMS (about 56% market share of free DBMS). Here again, MySQL is so essential to development, whatever the language, that you must absolutely learn and master it, with this book for example.
# 
# How to install MySQL
# To do this, we will install mysql-server and php-mysql (which will serve as a link between php and mysql)
# 
# =============================================================================
sudo apt install mariadb-server php-mysql

sudo apt install phpmyadmin

sudo phpenmod mysqli
sudo /etc/init.d/apache2 restart

#Check that PHPMyAdmin is working properly
#To check that PHPMyAdmin works, you will simply try to access it, using the address of your Raspberry followed by /phpmyadmin. For example, locally it will be http://127.0.0.1/phpmyadmin
#
#If you still get an error, it could be because PHPMyAdmin has moved to another directory. In this case, try the command

sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin
#Now, we can access to PHPMyAdmin from Raspberry Pi’s browser, with the url : http://127.0.0.1/phpmyadmin
# =============================================================================
# super user25 August 2019 at 2 h 06 min
# Instead of installing mysql-server
# =============================================================================
sudo apt install mysql-server php-mysql
#you can install mariadb-server
sudo apt install mariadb-server php-mysql

#Once your connect to MySQL (or mariadb) to replace password with the password you want, I recommend to include “WITH GRANT OPTION”. You will thank me later…
#
DROP USER ‘root’@’localhost’;
CREATE USER ‘root’@’localhost’ IDENTIFIED BY ‘your_password’;
GRANT ALL PRIVILEGES ON *.* TO ‘root’@’localhost’ WITH GRANT OPTION;
#
#before exiting, you can verify your changes

FLUSH PRIVILEGES;
SHOW GRANTS FOR ‘root’@’localhost’;
