# Slowloris-Python
Slowloris Python is a very basic slow http attack script written in Python

# How It Works?
This script starts a request for a webpage and doesn't finish its request until connection is timed-out on server side.
So server resources are being held with your requests and make others to connect impossible.

# So can I takedown anyserver do I want?
No. It's not that simple yet this script is not that professional. It requires more than one computer to take down anyserver
you want. But some websites with badly configured Apache can go down easily. Defaut Apache configuration is included. Besides,
remote server will be online again as soon as you Ctrl + C script.

# Then why you created this?
Because it's not for giving damage to websites. It's more like penetration your own system to see if your configuration is
correct or your firewalls and protection kits really protect you. 
