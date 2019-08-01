Title: How changes in Facebook API killed Bestaro
Slug: facebook-api-killed-bestaro
Date: 2018-04-06 22:00:00
Tags: bestaro, facebook, graph-api
Category: bestaro
Authors: Aleksander Chrabąszcz
Summary: Changes in Facebook API

You've most likely heard the big news that Facebook has leaked (or given) personal data of 50 (or 87) millions of users to Cambridge Analytica. I'm not going to go into details with that, because I don't find it very interesting.

The thing I'm concerned about is that, as a consequence, Facebook decided to block/limit their official APIs. Right now I find it impossible to collect the data, even for public groups or pages. It happened suddenly and there's almost no technical information regarding that, so I'm not yet sure what needs to be done to regain access to the data. The most concrete things [I found on Facebook's site](https://newsroom.fb.com/news/2018/04/restricting-data-access/) is:

> Going forward, all third-party apps using the Groups API will need approval from Facebook and an admin to ensure they benefit the group. Apps will no longer be able to access the member list of a group.

It means I lost access to vast majority of data I used for [Bestaro service]({filename}bestaro-overview.md) and the site ([MapaZwierzat](https://mapazwierzat.pl)) powered by it. The sad thing is, I was just doing the last improvements for the first official release. Now I'm going to wait for more details, but it doesn't mean I'm going to throw it in the trash can. I'll finish the work on the frontend to be ready to publish it if collecting the data ever becomes possible.

![I am a sad panda](/images/facebook-api/sad-panda.jpg)
