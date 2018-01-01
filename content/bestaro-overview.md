Title: Bestaro - Service to help in finding lost pets
Slug: bestaro-finding-lost-pets
Date: 2018-01-23 22:45:00
Tags: bestaro, animals
Category: haha
Authors: Aleksander Chrabąszcz
Summary: Overview of the library and service that displays information about lost and found animals on a map


That's my first post on blog and I'm going to start big, as I'll present Bestaro - the library I'm working on since June.

**Bestaro** is an attempt to make life easier for Polish people who lost or found an animal, especially a dog or cat. It should collect announcements from various sources and present them on a map.

> A short note regarding the library name: bestaro is a word in Esperanto. It's made of two morphems: 'best-' and '-ar-' and a suffix '-o' specific for nouns.  
> 'besto' means 'an animal' and 'ar' is a modifier that means 'a group of'. So literally it's something like 'group of animals', but its actual interpretation is 'fauna'.

The library consists of two parts:

 *  **Backend** - responsible for collecting data of existing announcements about lost or found pets, extracting the data from the text, finding the place where the event happened and storing it with the picture as a standarized record.
 *  **Frontend** - responsible for presenting it as a  handy map, where it's possible to filter the records displayed on the map, for example based on the event date.

As I felt very motivated to work on this project and finish it as quickly as possible, I've decided to use technologies I had really no idea about: Scala with Slick for database layer and Play Framework + Nginx (with HTTP2) for frontend. The first attempt for frontend was ScalaJS, but it found a very painful way to say "No", so I gave up.

![A post from a social network gets the location data extracted and then presented on a map](/images/bestaro-overview/piesel-do-mapy.png)
<p style="text-align:center">So advanced. So much processing</p>

# Backend
It sounds pretty easy, but it's not. The toughest part right now is parsing the announcements from the web and getting important information. The additional concern is that the messages I'm working on are in Polish, which has lots of inflection. That means unspecified word order in the sentence and trouble in finding out which part of the message mentions the location. Especially that every town name can potentially exist in seven different forms, each representing a different case.

## Collecting data
This one is pretty easy. The main data source are public groups on Facebook which are specifically devoted to posting announcements about lost and found pets. Other sources are websites for public announcements, but they have much less records and it's often the same as on Facebook. I've never used Facebook API before, but it was pretty easy so I got it working after a few days.

## Extracting the information from data
I've decided to start with extracting the information from the announcement's text, for now ignoring the picture. Extracting the event date was pretty easy, it was just looking for a few specific date patterns which are most common in Poland. Add a few special keywords like "today" or "yesterday" and that's it.

But then goes the largest challenge in extracting the data: finding out which parts of the message are specifying some location (a street, a district or a town). To solve this biggest problem I've decided to create a separate library specialized in finding names of streets and towns in Poland, which is called **Bestaro-Locator**.

![Learning which words are most likely to represent locations](/images/bestaro-overview/szukanie-miejscowosci.png)

In short: each word is being evaluated and gets a score meaning how likely it's going to represent a location. The best group of adjacent words is being searched in external Geocoding (geolocation) service that returns the coordinates. I'm not going into details, because it's going to be explained thoroughly in the next post.

# Frontend

Frontend is responsible for displaying the records produced by the Backend.
My brief research has suggested, that there are two main actors and use-cases that need to be supported by the application:

 - a person walking around and noticing a probably lost pet. They should be able to quickly check the list of lost pets in the neighbourhood using their mobile phone
 - a person who lost a pet. Most likely checking the large area around the home on the desktop

It means the application must be **extremely** easy to use on mobile devices and should make it possible to see large amounts of data on the desktop. I've quickly crafted a solution and presented it to Joanna, a UX designer.

I got feedback that there is a lot to improve.

So I've started the process of making it correctly. About the technicals, first I wanted to make it all in the bare native ES6 without any frontend libraries, but I ended with React + Redux + Webpack.

So, after the improvement, the user interface of Bestaro looks like this:

![Map and list of animals on desktop](/images/bestaro-overview/frontend-desktop.png)
<p style="text-align:center">On desktop</p>

On the right you can see the map of the area. The center of the map is considered the observer's location, from which all distances are calculated.

On the left you can see the list of all the records. The ones that are closest to the center of the map are on top. To filter the events by date you can use the dropdown on top.

When you click on the picture or the pin on the map, then you can see the record's details: exact date, full-size picture and a link to the original announcement.

![Two views on mobile: 1. map with pins, 2. list of animals](/images/bestaro-overview/frontend-mobile.png)
<p style="text-align:center">On mobile</p>

On mobile you need to click on the big button on the landing page to show the map. Then you need to click another big button to enter the animals list. But the general idea is the same.
