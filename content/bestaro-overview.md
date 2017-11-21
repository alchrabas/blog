Title: Bestaro - A library to help in finding lost pets
Slug: bestaro-finding-lost-pets
Date: 2017-01-23 22:45:00
Tags: bestaro, animals
Category: haha
Authors: Aleksander Chrabąszcz
Summary: Overview of the library and service that displays information about lost and found animals on a map


I was thinking what should be the first topic to present on this blog and the answer is pretty simple: a library I'm working since June.

Bestaro is a library that tries to make life easier for Polish people who lost or found an animal, especially dogs or cats.

The library consists of two parts:

 *  backend - responsible for collecting data of existing announcements about lost or found pets, extracting the data from the text, geolocating the place where the event happened and storing it with the picture as a standarized record.
 *  frontend - responsible for presenting it as a  handy map, where it's possible to filter the records displayed on the map, for example based on the event date.

It sounds pretty easy, but it's not. The toughest part right now is parsing the announcements from the web and getting important information. The additional concern is that the messages I'm working on are in Polish, which has lots of inflection. That means unspecified word order in the sentence and trouble in finding out which part of the message mentions the location.

To solve this biggest problem I've decided to create a separate specialized library for finding names of streets in towns in Poland, which is called Bestaro-Locator.

> A short note regarding the library name: bestaro is a word in Esperanto. It's made of two morphems: 'best-' and '-ar-' and a suffix '-o' specific for nouns. 'besto' means 'animal', 'ar' is a modifier that means 'group of'. So literally it's something like 'group of animals', but the actual interpretation is 'fauna'.


