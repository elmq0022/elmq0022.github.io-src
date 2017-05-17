Title: Chipy Mentorship (Part 2 of 3) 
Date: 2017-05-24 12:00 
Category: Chipy, Python, Mentorship

# TLDR;
Since I last posted I've fixed a lot of stuff, cleaned up the look, and some data analytic capabilities thanks to jieba.
My next steps are building a SPA quiz application and automating my AWS deploy via fabric. 
Vist [hanyu.pro](https://www.hanyu.pro) and [github](https://github.com/elmq0022/hanyu) to see my progress.  

# Recap 
In my last post I discussed my pretty substantial progress on my first real Django applicaton Hanyu.  
Prior to that post, I had done everything form getting setup with git and github to loading my database and deploying the site to AWS.  
The pace was pretty fast and did leave me with a laundry list of things to cleanup here's just a few of the items I either imporoved or fixed:

- Reworked the managment commands to load and update the database.
- Added all the models to Django's admin.
- Improved the full-text search capabilitties of the site.
- Combined my two separate searches into a single search.
- Cleaned up the authentication application.

# How is Chinese Like an Obfuscated C Contest?
There's a lot of differnces between Chinese and English.  
First the writing system isn't phonetic in the way English and the Latin alphabet is.  
But the larger problem for me was the syntax.  In English words are space delimited.  
Chinese doesn't have any delimiter for words.  ba
This wouldn't be problematic except for the fact that how a sentence is segmented can change its meaning. 
For example wodedahuanggou can be parsed a couple ways:

    wode dahuang gou 
 
Which means "my rubarb dog".  Yeah, probably not quite right.

    wode da huang gou 
    
Which means "my big yellow dog".  Obviously, this a lot more sensible.  

How to teach the computer know that?  
Well, to teach a computer who to do this you need a lot of data that's already been parsed, a training set if you will.  
And then, you have to tune a model of conditional expectations based on various n-graphs of the sentence.  
This is a good problem, but my goal is to make a website that helps people (myself included) learn Chinese.  
Reinventing this wheel, when there are already good ones, isn't going to help much.  

The first library I tried was the Stanford segmenter.  
The work is probably really solid because, well, Standford. 
And python's NLTK package has binding to get this Java package. 
I got everything working on my dev machine, but there were some issues.  
The JVM is slow to start and uses a lot of memory.
I could get around the slow to start part by running the algorithm as a service making requests from python.  
But, the amount of ram the JVM required was something I couldn't overcome on a AWS free tier. 


Happily, the second package I found was [jieba]() and it pure python. 
The interfacte is dead simple like a python package should be. Plus for my purposes it's pretty performat.  
Plus it didn't blow all the ram on the AWS free tier.  
Python +1, Java nada.

By the way, if you're wondering, both jieba and the Stanford segmenter fail the test above.


# Next Project - Suggesting Items to Learn
Now that I can segment Chinese text, I can do a frequency analysis on a corpus of documents.  
This, in turn, will allow me to suggest frequently used characters and words for a user to learn.  
I have, in fact, started implementing some of this, but there are still details to work through.  


# Hey Better Looking
I'm not a frontend dev and although I've heard the terms javascript, jquery, and bootstrap before, I've never really used them.  
So when I stumbled upon [AdminLTE](), I was pretty stoked.   
I wouldn't call it pretty, but hey it's pretty reasonable and configuralbe. 
Everything has been wired in, and it even displays the user's [gravitar]().


# Dev, Ops, or Maybe Both?
Jordan, my mentor, helped me a lot with the initial AWS deploy.  
I then spent a couple of frustrating but rewarding days getting AWS, nginx, gunicorn, and Django to all play together.  

Since the inital deploy Jordan has help harden the AWS security a bit.  
First, he had me create a user with read only access to server the application.  
This should help prevent a hacker from hijacking the active account and using it modify code on the site directly.  
The other issue was getting an encryption service up and running, so the site serves HTTPS instead of HTTP.  
This is important because I don't want password sent to my site unencrypted. 

# What's Next 
There's a couple big ticket items that I want to finish up before the mentorship is over.  
One is to build a quiz application and do it using a SPA architecture.  
The other is to automate my deploy to AWS.  

Jordan and I discussed the architecture of the quiz applicaton the other day. 
After a brief discussion we decided the most basic approach would good enough for my first attempt. 
Basically I'll use [JQuery]() for the frontend piece because it works and I won't have pickup an entire framework right away. 
Really the javascript landscape has way too many frameworks for my taste.  Besides who know which one is going to be popular next week. 

The backend will be pretty straight forward to. 
I'll use Django's class based views and the JSON Response Mixin to serve up my JSON data.  
Again, I've elected to use what's already there instead of a framework like Django REST Framework or tastypie.  
If things get more involved I can pick a framework then. 

I've actually really liked learning more AWS and the linux (specifically ubuntun) throughout my project.  
The one thing that's been kind of a bummer is not having a one click deploy.  
To remedy this I'm going automate my AWS deploy with fabric.  
Ansible, Chef, and Puppet are more first tier choices these days. 
But at this stage, my deploy isn't crazy complicated, and it's unlikely I will need any additional instances anytime soon.

# See My Progress First Hand
You can see the actual site at [www.hanyu.pro](https://www.hanyu.pro).  
All the code is on [github](https://github.com/elmq0022/hanyu/).
