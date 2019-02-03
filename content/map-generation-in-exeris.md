Title: Map Generator for the Exeris game
Slug: map-generator-for-exeris
Date: 2019-01-31 22:45:00
Tags: bestaro, animals
Category: bestaro
Status: draft
Authors: Aleksander Chrabąszcz
Summary: Generating and displaying a world map for Exeris

I'm working on a game called Exeris for a few years already, but I've never posted about it here. That's because the game progress was featured (not very regularily, though) on a decicated blog available at https://blog.exeris.org. The posts there were usually explaining general ideas, not the implementation details. This time I've decided this post will be focused on programming the technical aspects, so it's going to be harder to grasp for people without mathematical/programming background.

# What is Exeris?
This question is much better to be answered on the [game's blog](https://blog.exeris.org) I've mentioned earlier. In short: it's a browser-based crafting and exploration game, where players can control their characters to travel, gather materials and organize with each other to build structures and tools which can make the further work more efficient. The world is going to consist of two main continents - one of these being periodically removed and randomly generated, so there's always some *terra incognita* waiting for explorators.

# The goal
First of all, I'd like to mention that most of my work about map generation is based on concepts and solutions already tested by Azgarr (the author of [Fantasy Map Generator](https://azgaar.github.io/Fantasy-Map-Generator/)) which are explained on his wonderful blog - https://azgaar.wordpress.com/. Most of the stuff is already done better by him ;) but there are small reasons which forced me to start from scratch.

My goal is to have a nice-looking colorful world map which can be displayed to players and used for navigation, when the game characters are travelling both on land and sea. It should contain areas of different terrains, coastlines, resources and rivers, also with an ability to terraform (e.g. build roads and bridges). It already suggests that there are two completely separate phases:

 - Procedural map generation, which happens in the beginning of the world and creates a geometrical representation of land masses and all the other objects in the game world
 - Map visualization, which takes the geometrical representation and turns it into a picture representing a section of the game world

They are going to be described separately.

One of things is I want the map to look like that:

![A section of the map from The Witcher 3](/images/map-generator/witcher3-map.png)

And that's because I like the style of [map from The Witcher 3](https://witcher3map.com/s/#6/2.888/4.384) ;) This map was most likely skillfully created by a talented artist, but I lack such skills, so I've decided to delegate drawing it to my computer. To get a similar result, I need to use a certain structure of generated landscapes:

 - I need to store the information about the peaks of the mountain chains
 - I'd also like to be able to draw dynamically generated parts of the map (roads, water canals, bridges) and be able to intertwine it into existing game world
 - It's also necessary to not reveal the fact what are the map directions when you look at it (there should be no obvious "UP" on the map)

In this post I'll explain how I worked on map generation, and in the next one you'll be able to read about drawing a map picture.

# Creo-exeris for Map Generation

Creo-exeris (from latin __creo__ - 'I create') is the library I've created for generating the game world, including the heightmap, (simplified) biomes and precipitation which are then used for creation of rivers and different terrain types. It's open source and can be used freely for any project.

The 10k ft overview of this script is:

1. Generate heightmap making the generated mountain chains the centers of the island
2. Generate precipitation map based on (hard-coded) wind
3. Generate terrain types based on precipitation and some randomness
4. Generate rivers
5. Generate resources

When writing about every section I'll link to specific posts on Azgarr's blog, because I've used them as a reference during my work.

## 1. Generate heightmaps

