Title: Chipy Mentorship (Part 3 of 3)
Date: 2017-05-24 12:00
Category: Chipy Mentorship
Tags: Chipy, Python, Mentorship
Status: draft

# TLDR
With a little help from JQuery the final bits of my project came together with a multiple choice quiz implemented as a single page application.
Additionally, deployment to EC2 is now just a single shell command thanks to Fabric and some straight forward python scripting. 

# Building the Quiz App
The single page app I had in mind was pretty basic.
Really I just needed to push some JSON data around and excute a few DOM manipulations.
There are probably some benefits to learning one of the many JavaScript frameworks out there.  
But the JSON handling and DOM manipulation I needed were rather minimal, so I just stuck with JQuery.

The changes needed to make a Django view function work with JSON data weren't all that bad.
First, I gave my Quiz Model a "toJSON" method that returns a dictionary representation of a quiz instance.
Second, instead of returning a rendered template the function now returns an HTTP response with JSON as its content type.

    #!python
    return HttpResponse(json.dumps(result), content_type="application/json")

There was some additional boiler plate code needed to select the CSRF token send it with the request.
If you want to read more about how ths is done there's information the [Django documentation](https://docs.djangoproject.com/en/1.11/ref/csrf/).
Also a [RealPython](https://realpython.com/blog/python/django-and-ajax-form-submissions/) has a nice tutorial about this. 

# Deploying with Fabric
[Fabric](http://www.fabfile.org/) is a library that allows python to run shell commands locally or remotely via SSH. 
A really basic fab file could look something like this:

    #!python
    # in fabfile.py

    def caffinate_coder():
        print("Making some coffee.")

Now calling "fab caffinate_coder" from the command line will echo "Making some coffee."
As you can see this is straight python code.
To do meaningful work for a deploy these functions will need to issue shell commands locally and on the remote host.
Fabric makes this dead simple with the "local" and "run" commands.
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

This example sets some environment variable which tell Fabric how to connect to the remote host.
Hopefully their meaning is clear from their name and description.
The first function uses the "local" command and "ls" to list the files on the local machine.
The second function does the same thing, but the command will be executed on each of the remote servers.

Since this is all so simple, I almost had my deploy script working on the first try.
There were a couple issues to debug.
First Fabric was looking form a .ssh/config file, and I don't have one on my Windows machine.
The solutions was simple enough; create an empty .ssh/config file in my user directory.
The other thing was getting virtualenvwrapper to work properly with remote commands.
Fabric provides a couple nice [context manager]() , [prefix](), for things like this, but simply using workon < environment > didn't work.
The solution to this was to specify the full path to the workon command.

As an added bonus for all the python 3 converts, I got some good advice on Chipy's Slack channel to use Fabric3.
This is a fork of Fabric that supports a more minimal, and perhapse more sane, set of python version, python 2.7+ and python 3.4+.
The next release of Fabric will probably have better python 3 support.

# Thanks to my Mentor, Chipy, and All the Fantastic Mentors and Mentees
The python metorship has been a fun and rewarding experience for me.
I didn't anticipate learning as much as I did or covering the large range of topics that Jordan and I discussed.

I have to thank Jordan for taking the time to mentor me these last 3 months.
He has been patient and extremely helpful guiding me through this project.

I also want to say thank you to Ray, Hana, and Patrick for organizing everything.
And thanks to all the other Chipy mentors for dedicating their valuable free time to make this a great experience for everyone invovled. 