 Title: Chipy Mentorship (Part 2 of 3) 
 Date: 2017-05-24 12:00 
 Category: Chipy, Python, Mentorship

# Recap 
In my last post I discussed my pretty substantial progress on my first real Django applicaton Hanyu.  
Prior to that post, I had done everything form getting setup with git and github to loading my database and deploying the site to AWS.  
The pace was pretty fast and did leave me with a laundry list of things to cleanup here's just a few of the items I either imporoved or fixed:

- Reworked the managment commands to load and update the database.
- Added all the models to Django's admin.
- Improved the full-text search capabilitties of the site.
- Combined my two separate searches into a single search.
- Cleaned up the authentication application.

The results can be seen at [www.hanyu.pro](https://www.hanyu.pro).  
The full code for the site is on [github](https://github.com/elmq0022/hanyu/).

# How is Chinese Like an Obfuscated C Contest?
There's a lot of differnces between Chinese and English.  
First the writing system isn't phonetic in the way English and the Latin alphabet is.  
But the larger problem for me was the syntax.  In English words are space delimited.  
Chinese doesn't have any delimiter for words.  ba
This wouldn't be problematic except for the fact that how a sentence is segmented can change its meaning. 
For example wodedahuanggou can be parsed a couple ways:

    wode dahuang gou 
 
Which means "my rubarb dog".  Yeah probably not quite right.

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

# Hey Better Looking
I'm not a frontend dev and although I've heard the terms javascript, jquery, and bootstrap before, I've never really used them.  
So when I stumbled upon [AdminLTE](), I was pretty stoked.   
I wouldn't call it pretty, but hey it's pretty reasonable and configuralbe. 
Everything has been wired in, and it even displays your [gravitar]() if that's your thing.  

# Dev, Ops, or Maybe Both?
Jordan helped me out a lot with AWS on the first go around.  I then spent a couple (frustrating) days getting aws, nginx, gunicorn, and django all playing 
nicely together.  

Jordan looked at my setup and noticed a fair amount of security stuff to address...
Okay, so it was only really two items.  There really should be a user with read only access setup to access and server the application.  
This techincally should prevent a hacker from getting in on the active account and modifing the code directly.  The other issue was getting an 
encryption service up and running so I could server HTTPS instead of HTTP.  This is important since I'm potentially dealing with other users' 
passwords.  

After two hours of messing around we were mostly done with rerouting http request to https as an exercise for me to complete.  


Additionally 

# Next Project - Suggesting Items to Learn
 I really want the site to give the user meaningful characters (a single chinese character) and meaninul words (one or more chinese characters) to learn.
 To do that I either need a table of frequency of occurence of these items in chinese lanaguage.  Since I don't have one, I'll will have to make one.

 This has two main difficulties.  First, is the choice of corpus.  The documents I choose to analyze will impact the frequency of the words observed directly. 
 The second issue is that Chinese texts do not delimit words with a space. No significant whitespace?  That's not very ptyhonic.  Maybe golang would be a better
 choice for this project (China's most popluar language).

 I'm going to basically ignore the first issue and use Wikipedia until a fellow mentee mentioned [this](http://www.lancaster.ac.uk/fass/projects/corpus/UCLA/)

  I had a couple of options to deal with item two.  The first and probably standard way is to use 
  Standfords NLP package as a server or from within pythons NLTK package.  I was going to go this route and set it up NLP as service on my AWS instance.  The problem is java is a bit of a resource hog when it comes to memory. Just spinning up the segmenter and the JVM was enough to burn through the memory I had allocated on my EC2 t.nano instance.  Two steps forward, three steps back.  

 I did a brief search on github which lead me to a python package called [jieba](LINK). After a scanning through the README and a `quick pip install jieba`, I was back in business.   
  

 Having a library like this solves another issue I had. The full text search only worked well on an exact dictionary entry.  Entering an entire sentence
 and getting back a resonable result wasn't possible with previous implementation.  Segmenting the Chinese sentence and searching for each segement has yielded pretty reasonable results. 

 # Implemenation - How to do a SQL Query in a 1,000 Lines of Code or More
 So when you look at the [hanyu.pro](https://www.hanyu.pro) the functionality maynot look all that stellar.  This little site is, in fact, hours and hours of work.  I've found deploying a site to AWS and hardening it too be far more work than I had initally imagined.  I can see why services like google appengine and heruko are
 so popular for smaller projects. I have spent at least 4 hours working on AWS deployment with my mentor and several hours more on my own fiddling and reading docs.  
 Django is a "framework for perfections for prefectionists with deadlines" to be sure, but every page you see is composed of a view, a model, and a template.  There's likely more there to get the data in to the database and maintain it.  


#WHAT ELSE????