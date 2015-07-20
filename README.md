# Slowloris-Python
Slowloris Python is a very basic slow http attack script written in Python

# How It Works?
This script starts a request for a webpage and doesn't finish its request until connection is timed-out on server side.
So server resources are being held with your requests and make others to connect impossible.

# So can I takedown anyserver do I want?
No. It's not that simple yet this script is not that professional. It requires more than one computer to take down anyserver
you want. But some websites with badly configured Apache can go down easily. Defaut Apache configuration is included. Besides,
remote server will be online again as soon as you Ctrl + C script. This tool it's not for giving damage to websites. It's more like penetration your own system to see if your configuration is correct or your firewalls and protection kits really protect you.

# How do I understand if I'm easily downable?
Simple. Look at the numbers. Slowloris creates number of threads you gave. In a situtation like this means that you've done a good job with configuring your apache.

    Connected: 590 Close: 27014 Error: 0
    Connected: 700 Close: 27374 Error: 0
    Connected: 654 Close: 27710 Error: 0
    Connected: 800 Close: 29100 Error: 0

But this is bad. Can you see how errors are more then connections are closed connections? This is something that you should
deal with and re-configure your stuff. 

    Connected: 400 Close: 10 Error: 754
    Connected: 395 Close: 15 Error: 1024
    Connected: 412 Close: 16 Error: 2148
    Connected: 490 Close: 17 Error: 3012
    Connected: 400 Close: 18 Error: 14020

