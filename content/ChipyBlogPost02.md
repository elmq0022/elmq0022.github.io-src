Title: Chipy Mentorship (Part 2 of 3)
Date: 2017-05-24 12:00
Category: Chipy, Python, Mentorship
Tags: Chipy, Python, Mentorship

# TLDR;
Since my last post I've improved a lot of the code, cleaned up the site's look, and added some data analytic capabilities thanks to [jieba](https://github.com/fxsjy/jieba).
My next steps are building a SPA quiz application and automating my AWS deploy using fabric.
To see my progress visit [hanyu.pro](https://www.hanyu.pro) and [github](https://github.com/elmq0022/hanyu).
<br>
<br>

# Recap
In my last post, I discussed my substantial progress on my first Django application, Hanyu.
Prior to that post, I had done everything from getting setup with git and github to loading my database and deploying to AWS.
The pace was pretty fast and left me with a some clean up to do.
Here's just a few of the items I either improved or fixed:

- Reworked the management commands to load and update the database.
- Added all the models to Django's admin.
- Improved the full-text search capabilities of the site.
- Created a search that parses a Chinese sentence and returns all the definitions.
- Cleaned up the site's user authentication.

With those out of the way I was free to add new features.

<br>
# How is Chinese Like an Obfuscated C Contest?
There's a lot of differences between Chinese and English.
Most people are aware that the language uses characters instead of words composed of letters.
Another large difference is syntax for delimiting groups of characters.
There isn't one.
Where English words are space delimited, Chinese skips delimiters all together.
Since I want to do some basic frequency this poses a problem.
Consider this sentence, wodedahuanggou, which can be parsed a couple different ways:

    wode dahuang gou

This roughly means "my rhubarb dog".  Yeah, that's not a sentence you would expect to utter.
Another option is:

    wode da huang gou

This means "my big yellow dog".  Obviously, this is a more sensible choice.

So I don't have the skill or the time to segment all my corpus of text by hand.
So how can I have the computer do this?
Well, first I would need a lot of data that's already been parsed, i.e. a training set.
And then, I could use some kind of mathematical model of conditional expectations based on various n-graphs of the corpus.
This model could then be used as an algorithm for the computer to reasonably segment sentences.
This is a good problem to work on, but my goal is to make a website that helps people (myself included) learn Chinese.
Reinventing this wheel, when there are already good wheels out there, beyond pedagogic reasons, there is much reason for me to roll my own code here.

The first library I tried was the Stanford segmenter.
I figured this might be a solid choice because, well, it's from Stanford.
Plus, python's NLTK package has binding to get this Java package.
After some mild cursing, I got everything working on my dev machine, but there were some issues in production.
Basically, the JVM is slow to start and uses a lot of memory.
I could work around the slow to startup times by running the algorithm as a service and making requests from python.
But, the amount of ram the JVM required was something I couldn't overcome on an EC2 instance on AWS's free tier.

Happily, the second package I found, [jieba](https://github.com/fxsjy/jieba), is pure python.
The interface is dead simple like a python package should be.
Plus for my purposes it's actually pretty performant.
Python +1, Java nada.

By the way, if you're wondering, both jieba and the Stanford segmenter fail the test above.
There options to father tune both packages though.

<br>
# Next Project - Suggesting Items to Learn
Now that I can segment Chinese text, I can do a frequency analysis on a corpus of documents.
This, in turn, will allow me to suggest frequently used characters and words for a user to learn.
I have, in fact, started implementing some of this, but there are still details to work through.

<br>
# Hey Better Looking
I don't know a lot on the frontend and although I've heard the terms javascript, jquery, and bootstrap before, I've never really used them.
So, when I stumbled upon [AdminLTE](https://github.com/fxsjy/jieba), I was pretty stoked.
I wouldn't call this template pretty, but it is pretty reasonable.
After screwing with Django templates for a couple days and making a couple of tags I had everything wired up.

<br>
# Dev, Ops, or Maybe Both?
Jordan, my mentor, helped me a lot with the initial AWS deploy.
I then spent a couple of frustrating but rewarding days getting AWS, nginx, gunicorn, and Django playing together.

Since then deploy Jordan has help harden the AWS security a bit.
First, he had me create a user with read only access to server the application.
This should help prevent a hacker from hijacking the active account and using it modify code on the site directly.
The other issue was getting an encryption service up and running, so the site serves HTTPS instead of HTTP.
This is important because I don't want password sent to my site unencrypted.
We followed the instructions on [Let's Encrypt](https://letsencrypt.org/) and did a few modifications to my AWS config.

<br>
# What's Next
There's a couple big ticket items that I want to finish up before the mentorship is over.
One is to build a quiz application, and I want to do it using a SPA architecture.
The other is to automate my deploy to AWS.

Jordan and I discussed the architecture of the quiz application the other day.
We rather quickly settling on a basic approach for my first attempt.
With out getting into too much detail, I'll use [JQuery](https://jquery.com/) for the frontend.
I know it's not "fashionable", but it works, and I don't have pickup an entire framework.

The backend will be pretty straight forward too.
I'll use Django's class based views and the JSON Response Mixin to serve up JSON data.
Again, I've elected to use what's already there instead of a framework like Django REST Framework or tastypie.
As I start to figure thing out more or when things get more complicated I will learn a framework then.

I've actually really enjoyed learning more about AWS and Linux throughout my project.
The one thing that's been kind of a bummer is not having a one click deploy.
To remedy this, I'm going automate my AWS deploy with fabric.
Ansible, Chef, and Puppet are more first tier choices for larger projects these days.
But, at this stage, my deploy isn't crazy complicated, and I don't probably won't need any additional EC2 instances anytime soon.

<br>
# See My Progress First Hand
You can see the actual site at [www.hanyu.pro](https://www.hanyu.pro).
All the code is on [github](https://github.com/elmq0022/hanyu/).
