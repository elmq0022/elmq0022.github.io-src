 Title: Chipy Mentorship (Part 2 of 3) 
 Date: 2017-05-xx 12:00 
 Category: Chipy, Python, Mentorship


# Updates and Fixes
 Well since my last post, I finihsed up most of the login stuff, but it could use some polish and an email backend.  
 
 bootstrap working working from the CDN and I am trying to make stuff look better.  I found some good advice on fonts and 
 CSS styling for sites with a lot of Chinese [here](URL) 

 I've since added a my models to Django's admin. That's rather painless exercise for the basic stuff, but there is plenty 
 of customization a person can do if he really wants to.  
 
 I showed my project to my wife, and she quickly found a bug the full text search.  
 The english definitions from CC-CEDICT are separated by "/" characters and when a specific key workd like "hello" occured in the 
 defintiona as ".../hello..." the entry was not found.  
 This was an easy fix done with a regex that substitues all the instances of "/" with "\s/\s".


# Next Project - Suggesting Items to Learn
 I really want the site to give the user meaningful characters (a single chinese character) and meaningful words (one or more chinese characters) to learn.
 To do that I either need a table of frequency of occurence of these items in chinese lanaguage.  Since I don't have one, I'm going to have to make one.

 This posses two main difficulties.  First, is the choice of corpus.  The documents I choose to analyze will impact the frequency of the words observed directly. 
 The second issue is that Chinese texts do not delimit words with a space.   
 To suggest characters and words to learn I need to start doing some) frequency analysis on all my entries.  Unfortunately Chinese sentences do not have any spaces in golang to get in the right mindset to learn Chinese...).  

 For now, I'm going to basically ignore the first issue and use Wikipedia because it's there.  This is probably not a great choice 
 dates and times place names etc are going to show up way too often. 

  The second issue needs to be addressed. Enter the good folks form stanford
  who work on the Stanford NLP, and the good folks who maintain python's NLTK
  which interfaces Stanford's NLP kit which happens to be written Java....
  BOOO.... mainly becaue the JVM isr really slow to fire up. 
  Fortunately there seems to be a server option for the program, so I can probably make this a dameon and use it as a service.  

 This will also address another issue I have noticed. My search only works well on a single characters or group of characters.  Entering an entire sentence
 isn't possible with previous implementation.  So if I could segment a Chinese sentence, I could have the program search each term and 
 hopefully return something reasonable.  

 # Implemenation - How to do a SQL Query in a 1,000 Lines of Code or More
 For what seems to be a really simple application this is a ... ton of work.  I mean really....


# Dev Ops Stuff...
Jordan helped me out a lot with AWS on the first go around.  I then spent a couple (frustrating) days getting aws, nginx, gunicorn, and django all playing 
nicely together.  

Jordan looked at my setup and noticed a fair amount of security stuff to address...
Okay, so it was only really two items.  There really should be a user with read only access setup to access and server the application.  
This techincally should prevent a hacker from getting in on the active account and modifing the code directly.  The other issue was getting an 
encryption service up and running so I could server HTTPS instead of HTTP.  This is important since I'm potentially dealing with other users' 
passwords.  

After two hours of messing around we were mostly done with rerouting http request to https as an exercise for me to complete.  