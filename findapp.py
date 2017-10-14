#!/usr/bin/env python

import glob
import subprocess
import os

# Global variables
apps_dir = ("/Applications")
system_apps = os.popen("find " + apps_dir + " -iname *.app")
output = "filterd_apps.txt"

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
"/Applications/DVD Player.app\n",
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
"/Applications/Safari.app",
"/Applications/Dictionary.app",
"/Applications/Contacts.app",
"/Applications/Time Machine.app",
"/Applications/Font Book.app",
"/Applications/FaceTime.app",
"/Applications/Keynote.app",
"/Applications/Mission Control.app",
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
		print(colors.RED + msg + colors.END)
	else:
		print(msg)

# 1. Checking if .app is in the list of OSX preinstalled apps.
# 2. Appeding the filelist to the corrected list if it's not in the blacklist.
# 3. Creating a textfile with the filterd apps.
def filter_apps():
	filterd_list = []
	message('success', "Check for OSX preinstalled apps in " + apps_dir)
	for app in system_apps:
		if app.rstrip() in blacklist:
			print(app.rstrip() + " is blacklisted!")
			pass
		else:
			filterd_list.append(app)
			with open(output, "a") as textfile:
				textfile.write(app)

	message("success", "Applications are filterd and saved in ")

def show_filterd_list():
	message("success","Show filterd list...\n")
	filterd_list = open("./" + output, "r")
	for app in filterd_list:
		print(app)

try:
	filter_apps()
	# show_filterd_list()
	
except OSError:
	message("error", "Error...")
# 	# If the directory '/applications' is not found you give it in manually.
# 	while True:
# 		print("Couldn't find the " + directory + " folder. Do you want to enter in manually?")
# 		question = input("(Y)es or (N)o: ")
# 		print(singlehash)
# 		if question == "Y":
# 			new_dir = input("Please enter the place of the Applications folder here: ")
# 			find_all_apps()
# 		elif question == "N":
# 			print("Stopping the script!")
# 			print(singlehash)
# 			break
# 		else:
# 			print("Wrong input. Try again..")
# 			print(singlehash)

# except FileNotFoundError:
# 	print("Couldn't find any .app files. Please check the var 'directory' if it's set right.")