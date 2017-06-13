Title: Chipy Mentorship (Part 3 of 3)
Date: 2017-05-24 12:00
Category: Chipy Mentorship
Tags: Chipy, Python, Mentorship
Status: draft


# TLDR
Summarize here...

# Life on the Frontend - Creating My First SPA

# Learning Javascript and JQuery

# Getting JQuery to Read and Send JSON

# Getting Django to Send JSON

# Testing with Pytest-Django
- Why pytest django 
- Add the django app as a user so it can create tables on the database
- telling pytest it needs to use the database
- initializing the database 

# Deploying with Fabric ...?

Fabric is a niffty tool to run bash commands localy or on a remote host via ssh.
A really basic fab file would look something like this:


...python
    # in fabfile.py

    def caffinate_coder():
        print("Making coffee.")


Now from the command line call fab caffinate_coder and it will echo back "Making coffee."
This should be straight forward because it's just python.
To do meaningful work for a deploy these functions will need to issue batch commands locally and on the remote host.
Fortunately Fabric makes this easy with the local and run commands.  Here's a more complicated file to discuss

...python
    # in fabfile.py
    env.hosts = ["list of remote hosts ip address or domain name",]
    env.user = "< user name for remote >"
    env.key_filename = "< absolute path to ssh key file >"
    env.use_ssh_config = True or False
    env.no_agent = True or False

    def list_local_files():
        local("ls")


    def list_remote_files():
        run("ls")

This example sets some environment variable which let Fabric know how to connect to the remote host.
Hopefully their meaning is clear from their name and the description.
The first function use the local command and "ls" to list the files on the local machine.
The second function does the same thing, but on *each* of the listed remote servers.
So yes, you could just write bash scripts and run them on the server side, but Fabric makes deploying to multiple instances much easier.


I did run into a couple gotchas though.
First Fabric was looking form a .ssh/config file and I didn't have one on windows.
The solutions was simple enough; create an empty .ssh/config file in my user directory.
Yes, I googled that answer.
The other thing was getting virtualenvwrapper to work.
Fabric provides a couple nice [context manager]() , [prefix](), for things like this, but simply using workon < environment > didn't work.

As an added bonus for all the python 3 converts, I got some good advice on Chipy's Slack channel to use Fabric3.
This fork of Fabric supports a more minimal, and perhapse more sane, set of python version, python 2.7+ and python 3.4+.


# Closing Thoughts
