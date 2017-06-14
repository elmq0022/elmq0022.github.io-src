Title: Chipy Mentorship (Part 3 of 3)
Date: 2017-05-24 12:00
Category: Chipy Mentorship
Tags: Chipy, Python, Mentorship
Status: draft

# TLDR
With a little help from JQuery the final bits of my project came together with a multiple choice quiz implemented as a single page application.
Additionally, my EC2 deployment is now a single shell command thanks to Fabric and some very straight forward python scripting. 

# Life on the Frontend
The last major feature I wanted to add to hanyu.pro was a multiple choice quiz implemented as a single page application.
There are a lot of JavaScript frameworks these days.
So many that's it could be hard to pick.
But the JSON handling and DOM manipulation I needed were rather minimal, so I just stuck with JQuery.

# Handling JSON with Django and JQuery
The changes needed to make a Django view function work with JSON data aren't all that bad.
First, I gave my Quiz Model a toJSON method that change returns a JSON representation of a quiz instance.
Second, instead of rendering and returning a template the five function now return an HTTP response with JSON content type as seen below.

    #!python
    return HttpResponse(json.dumps(result), content_type="application/json")

# Getting Django and JQuery to Play Together
There was some boiler plate code needed to select the CSRF token off the page and send it with the request.
If you want to read more about there's an overview in the [Django documentation](https://docs.djangoproject.com/en/1.11/ref/csrf/).
There's also a good tutorial on the overall approach from the guys at [RealPython](https://realpython.com/blog/python/django-and-ajax-form-submissions/)

# Deploying with Fabric
[Fabric](http://www.fabfile.org/) is a library that allows python to run shell locally or remotely via SSH. 
A really basic fab file would look something like this:

    #!python
    # in fabfile.py

    def caffinate_coder():
        print("Making some coffee.")

Now calling fab caffinate_coder from the command line will echo "Making some coffee."
As you can see this is really just python code.
To do meaningful work for a deploy these functions will need to issue shell commands locally and on the remote host.
Fabric makes this easy with the "local" and "run" commands.
Here's a more illustrative example to discuss.

    #!python
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

This example sets some environment variable to tell Fabric how to connect to the remote host.
Hopefully their meaning is clear from the name and the description.
The first function uses the local command and "ls" to list the files on the local machine.
The second function does the same thing, but the command will be executed on *each* of the listed remote servers.

This should make my deploys super straight forward, but I did run into a couple gotchas.
First Fabric was looking form a .ssh/config file, and I don't have one on my Windows machine.
The solutions was simple enough; create an empty .ssh/config file in my user directory.
The other thing was getting virtualenvwrapper to work.
Fabric provides a couple nice [context manager]() , [prefix](), for things like this, but simply using workon < environment > didn't work.

As an added bonus for all the python 3 converts, I got some good advice on Chipy's Slack channel to use Fabric3.
This fork of Fabric supports a more minimal, and perhapse more sane, set of python version, python 2.7+ and python 3.4+.

# Thanks to my Mentor, Chipy, and All the Fantastic Mentors and Mentees
The python metorship has bee a fun and rewarding experience for me.
I didn't anticipate learning as much as I did or covering the large range of topics that we discussed.

I have to thank Jordan for taking the time to mentor me these last 3 months.
He has been patient and extremely helpful guiding me through this project.

I also want to say thank you to Ray, Hana, and Patrick for organizing everything.
Thanks to the all the other mentors as well for dedicating their valuable free time to this mentorship session.
