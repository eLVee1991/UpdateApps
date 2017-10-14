#!/usr/bin/env python

import glob
import subprocess
import os

# Global variables
apps_dir = ("/Applications")
system_apps = os.popen("ls " + apps_dir + " | grep .app")
output = "filtered_apps.txt"

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
		print(colors.WARNING + msg + colors.END)
	else:
		print(msg)

# 1. Checking if .app is in the list of OSX preinstalled apps.
# 2. Appeding the filelist to the corrected list if it's not in the blacklist.
# 3. Creating a textfile with the filtered apps.
def filtered_apps():
	filtered_list = []
	message('success', "[+] Checking for OSX preinstalled apps in: " + apps_dir)
	for app in system_apps:
		if "/Applications/" + app.rstrip() in blacklist:
			print(app.rstrip() + " is blacklisted!")
			pass
		else:
			if app not in filtered_list:
				filtered_list.append(app)
				with open(output, "a") as textfile:
					textfile.write(app)
			else:
				pass

	print("")
	message("success", "[+] Applications are filtered and saved in the current directory. The file is named: 'filtered_apps.txt")
	print("")

def show_filtered_list():
	message("success", "[+] Showing filtered list:")
	filtered_list = open("./" + output, "r")
	for app in filtered_list:
		print(app.rstrip())
	print("")

# 1. Reading the output file.
# 2. Checking the plist for 'CFBundleShortVersionString' aka application version.
# 3. Returning the version number if possible
def find_version():
	message("success", "[+] Checking version numbers (if any):")
	output = "filtered_apps.txt"
	filtered_list = open("./" + output, "r")
	for apps in filtered_list:
		application = subprocess.Popen("plutil -p /Applications/"+apps.rstrip()+"/Contents/Info.plist | awk '/CFBundleShortVersionString/ {print substr($3, 2, length($3)-2)}'", shell=True, stdout=subprocess.PIPE)
		version_number = application.communicate()[0]
		print(version_number.rstrip())

	print("")
	message("success", "[+] Printed all the version numbers above.")

try:
	filtered_apps()
	show_filtered_list()
	find_version()
	
except OSError:
	message("error", "[+] Error...")
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
