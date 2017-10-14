import subprocess

class find_version:
	output = "filtered_apps.txt"
	filterd_list = open("./" + output, "r")
	for apps in filterd_list:
		application = subprocess.Popen("plutil -p /Applications/"+apps.rstrip()+"/Contents/Info.plist | awk '/CFBundleShortVersionString/ {print substr($3, 2, length($3)-2)}'", shell=True, stdout=subprocess.PIPE)
		output = application.communicate()[0]
		print(output.rstrip())
