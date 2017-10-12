#!/usr/bin/env python

import glob
import subprocess

# hashes to be used in most print statements to sort te code in the terminal.
singlehash = '''
######################################################################
'''
doublehash = '''
######################################################################
######################################################################
'''

# a list with OSX preinstalled apps. The script needs to skip these
system_apps = [
"/Applications/DVD Player.app",
"/Applications/Siri.app",
"/Applications/QuickTime Player.app",
"/Applications/Chess.app",
"/Applications/Photo Booth.app",
"/Applications/Notes.app"
"/Applications/Image Capture.app",
"/Applications/iBooks.app",
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

print(singlehash)
print("Looking for the directory..")
print("")

def find_all_apps():
	# a list with all the installed apps - the preinstalled OSX app
	corrected_list = []
	print("Found the directory ", directory, " and bound to it.")
	print("Creating a filelist named 'Application_list.txt' in the current dir.")
	print(singlehash)
	# using glob to find all .app files in the dir '/applications' set by the var 'directory'
	for applist in glob.glob(directory+"*.app"):
		# Checking if .app is in the list of OSX preinstalled apps.
		if applist in system_apps:
			pass
		else:
			# Appeding the filelist to the corrected list if it's not in the dont_list
			corrected_list.append(applist)
			# Creating a textfile with all the apps
			with open("Application_list.txt", "a") as textfile:
				textfile.write(applist+"\n")
	print("I stripped the OSX standard applications like safari, mail, siri etc.")
	print("Here's a list of all the applications")
	print("")
	# Looping through all the apps in the corrected list to show a nice list order.
	for applist in corrected_list:
		print(applist)
	print(singlehash)

"""Ideas: """
	## Write code here to find all the system versions. If you have commandline tools installed.
	##Use subprocess.Popen("/usr/libexec/PlistBuddy -c "Print CFBundleShortVersionString" /Applications/TextEdit.app/Contents/Info.plist")
	#version = subprocess.Popen("/usr/libexec/PlistBuddy -c "Print CFBundleShortVersionString" /Applications/TextEdit.app/Contents/Info.plist")
	#import plistlib
	#plistlib.readPlist('/Applications/Firefox.app/Contents/Info.plist')['CFBundleShortVersionString']

try:
	# a list that needs to be callable globally
	directory = ("/Applications/")
	find_all_apps()
	
except OSError:
	# If the directory '/applications' is not found you give it in manually.
	while True:
		print("Couldn't find the " + directory + " folder. Do you want to enter in manually?")
		question = input("(Y)es or (N)o: ")
		print(singlehash)
		if question == "Y":
			new_dir = input("Please enter the place of the Applications folder here: ")
			find_all_apps()
		elif question == "N":
			print("Stopping the script!")
			print(singlehash)
			break
		else:
			print("Wrong input. Try again..")
			print(singlehash)

except FileNotFoundError:
	print("Couldn't find any .app files. Please check the var 'directory' if it's set right.")