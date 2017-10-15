#!/usr/bin/env python

import os
import subprocess
import sys

# Global variables
apps_dir = ("/Applications")
system_apps = os.popen("ls " + apps_dir + " | grep .app")
output_apps = "filtered_apps.txt"
output_versions = "apps_version.txt"
filtered_list = []
version_list = []

# Colors
class colors:
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	END = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

# Blacklist with OSX preinstalled apps. The script needs to skip these
blacklist = [
"/Applications/Battery Monitor.app"
"/Applications/DVD Player.app",
"/Applications/Siri.app",
"/Applications/QuickTime Player.app",
"/Applications/Chess.app",
"/Applications/Photo Booth.app",
"/Applications/Notes.app"
"/Applications/Image Capture.app",
"/Applications/iBooks.app",
"/Applications/iTunes.app/"
"/Applications/Numbers.app",
"/Applications/Preview.app",
"/Applications/Dashboard.app",
"/Applications/iMovie.app",
"/Applications/TextEdit.app",
"/Applications/Automator Loop Utility.app",
"/Applications/Mail.app",
"/Applications/Maps.app",
"/Applications/Safari.app",
"/Applications/Dictionary.app",
"/Applications/Contacts.app",
"/Applications/Time Machine.app",
"/Applications/Font Book.app",
"/Applications/FaceTime.app",
"/Applications/Keynote.app",
"/Applications/Mission Control.app",
"/Applications/Numbers.app",
"/Applications/Notes.app",
"/Applications/Pages.app",
"/Applications/Stickies.app",
"/Applications/Photos.app",
"/Applications/Messages.app",
"/Applications/Calculator.app",
"/Applications/iTunes.app",
"/Applications/Launchpad.app",
"/Applications/Reminders.app",
"/Applications/App Store.app",
"/Applications/Automator.app",
"/Applications/Calendar.app",
"/Applications/System Preferences.app"
]

def message(state, msg):
	if state == "success":
		print(colors.GREEN + msg + colors.END)
	elif state == "error":
		print(colors.WARNING + msg + colors.END)
	elif state == "warning":
		print(colors.WARNING + msg + colors.END)
	elif state == "header":
		print(colors.HEADER + msg + colors.END)
	elif state == "underline":
		print(colors.UNDERLINE + msg + colors.END)
	else:
		print(msg)

# 1. Checking if .app is in the list of OSX preinstalled apps.
# 2. Appeding the filelist to the corrected list if it's not in the blacklist.
# 3. Creating a textfile with the filtered apps.
def filtered_apps():
	global filtered_list
	try:
		for app in system_apps:
			if "/Applications/" + app.rstrip() in blacklist:
				#print(app.rstrip() + " is blacklisted!")
				pass
			else:
				filtered_list.append(app)
	except OSError, FileNotFoundError:
		message("error", "[+] Error...")

	return filtered_list
	print("")

# 1. Reading the output_apps file.
# 2. Checking the plist for 'CFBundleShortVersionString' aka application version. If no plist info is available it's left blank
# 3. Returning the version number if possible
def find_version():
	global version_list
	try:
		filtered_apps()
		for app in filtered_list:
			application = subprocess.Popen("plutil -p /Applications/"+app.rstrip()+"/Contents/Info.plist | awk '/CFBundleShortVersionString/ {print substr($3, 2, length($3)-2)}'", shell=True, stdout=subprocess.PIPE)
			number = app.rstrip()+" "+str(application.communicate()[0])
			if number not in version_list:
				version_list.append(number)
			else:
				pass
	except OSError, FileNotFoundError:
		message("error", "[+] Error...")

	return version_list
	print("")

def Main():
	message("header", '''
8b    d8    db     dP""b8        db    88""Yb 88""Yb 
88b  d88   dPYb   dP   `"       dPYb   88__dP 88__dP 
88YbdP88  dP__Yb  Yb           dP__Yb  88"""  88"""  
88 YY 88 dP""""Yb  YboodP     dP""""Yb 88     88     
                                                                                                     
   88   88 88""Yb 8888b.     db    888888 888888        
   88   88 88__dP  8I  Yb   dPYb     88   88__          
   Y8   8P 88"""   8I  dY  dP__Yb    88   88""          
   `YbodP' 88     8888Y"  dP""""Yb   88   888888 ''')

	message("underline", '''
version 1.0
Created by eLVee & rickdaalhuizen
''')
	argument = sys.argv
	try:
		if argument[1]== "-a":
			filtered_apps()
			message('success', "[+] Checking for OSX preinstalled apps in " + apps_dir + " and removing them from the list")
			message('success', "[+] Here's a list of all the NOT preinstalled apps in " + apps_dir + ":")
			for apps in filtered_list:
				print(apps.rstrip())
		elif argument[1] == "-v":
			filtered_apps()
			message("success", "[+] Checking version numbers of applications in " + apps_dir + " (if any):")
			find_version()
			for versions in version_list:
				print(versions.rstrip())
		elif argument[1] == "-h":
			message("warning", """
usage: python findapp.py [-a] [-v] [-b]
optional arguments:
  -a   Creates a list named 'filtered_apps.txt' in the current dir.
  -v.  Creates a list named 'app_version.txt' in the current dir.
  -h.  Show this help message and exit
""")
			exit()
	except IndexError:
		message("warning", """
usage: python findapp.py [-a] [-v] [-b]
optional arguments:
  -a   Creates a list named 'filtered_apps.txt' in the current dir.
  -v.  Creates a list named 'app_version.txt' in the current dir.
  -h.  Show this help message and exit
""")
		exit()

if __name__ == "__main__":
	Main()
