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
	try:
		filtered_list = []
		message('success', "[+] Checking for OSX preinstalled apps in: " + apps_dir)
		message("success", "[+] Applications are filtered and saved in the current directory. The file is named: 'filtered_apps.txt")
		for app in system_apps:
			if "/Applications/" + app.rstrip() in blacklist:
				print(app.rstrip() + " is blacklisted!")
				pass
			else:
				filtered_list.append(app)
				textfile = open(output, "r")
				if app not in textfile:
					textfile = open(output, "a")
					textfile.write(app)
				else:
					pass
	except OSError, FileNotFoundError:
		message("error", "[+] Error...")

	print("")

def show_filtered_list():
	try:
		message("success", "[+] Showing filtered list:")
		filtered_list = open("./" + output, "r")
		for app in filtered_list:
			print(app.rstrip())
		print("")
	except OSError, FileNotFoundError:
		message("error", "[+] Error...")

# 1. Reading the output file.
# 2. Checking the plist for 'CFBundleShortVersionString' aka application version.
# 3. Returning the version number if possible
def find_version():
	message("success", "[+] Checking version numbers (if any):")
	try:
		output = "filtered_apps.txt"
		filtered_list = open("./" + output, "r")
		for apps in filtered_list:
			application = subprocess.Popen("plutil -p /Applications/"+apps.rstrip()+"/Contents/Info.plist | awk '/CFBundleShortVersionString/ {print substr($3, 2, length($3)-2)}'", shell=True, stdout=subprocess.PIPE)
			version_number = application.communicate()[0]
			print(version_number.rstrip())
	except OSError, FileNotFoundError:
		message("error", "[+] Error...")

def Main():
	filtered_apps()
	# (Un)comment the command below if you want the filtered list with applications ouput returned
	show_filtered_list()
	find_version()

if __name__ == "__main__":
	Main()
