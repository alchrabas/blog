Title: Bestaro is alive! After Facebook verification
Slug: bestaro-is-alive
Date: 2019-08-21 23:05:00
Tags: bestaro, facebook, graph-api
Category: bestaro
Authors: Aleksander Chrabąszcz
Summary: After successful Facebook API Verification there is a new hope for Bestaro

I didn't believe it's possible to get access to Facebook Graph API for a small, non-profit initiative.

That's why I didn't do anything for half a year after writing [the previous sad post](({filename}facebook-api-killed-bestaro.md)), especially because the whole process was not clear until july and then I've heard about many rejections and people waiting weeks for a decision.

But I've tried and succeded and I'll explain how it happened.

# Preparations

Despite all of this, around october I've decided to give it a try. Some day. I've read the requirements imposed by Facebook, but it still wasn't clear to me if it's ok to create a site which collects and processes the data to present it to multiple users. On the other hand, I was sure it is necessary to supply [Privacy Policy](https://mapazwierzat.pl/en/privacy-policy). I had to be very creative to write 'I don't store any user data' in over 800 words.

The next step was translating everything and providing multilanguage support. I didn't plan that, as almost 100% of the users of MapaZwierzat.pl will know Polish, but I had to do it for the sole purpose of passing the review, as it wasn't guaranteed who is going to review the application.

Then I had to feed my app with some sample data and create a screencast, with me as a narrator. I couldn't believe it's so hard to say a few correct sentences without making a mistake :D

# Application and review

Finally, in mid-april I've applied for app review. I did it late in the evening and in the morning... I got approved 🎉

![I am a happy panda](/images/bestaro-is-alive/happy-panda.jpg)

But my initial enthusiasm calmed down, because there was the second phase left. As I am not working for a business, I had to pass the individual verification. It meant sending a scan of valid document like an ID card or passport. So I did it and then waited... a week. There were some holidays, so instead of 5 business days I've waited for two weeks and then reported the issue. After some time I got some not entirely clear message that my uploaded file was somehow lost, so I reapplied and then waited for another two weeks or so. Then tried to restart the process and wait again. Then I've reported the issue again. This time, after a few minutes, my application got accepted. Woohoo!

# Outcome

I've tested the extent of the Graph API access and it allows for less than previously, but still enough for most of my use cases. But getting the access is not enough, I still need to apply to an admin of a specific group to get right to read (public) posts through the API. That's the main challenge I need to overcome right now. Sadly it's now also completely impossible to read the contents of the posts shared to the group (because you need to get approval of the original group), but the rest is working.

Speaking about technicals, in the mean time of the review process, I've rewritten the frontend of application to make it simpler by using Create React App and removed atrocious integration of Play Framework and NPM through SBT. I plan to completely remove Play Framework, which now is used only as a server for REST API. I plan to start storing images in S3 and the processed announcement records in DynamoDB or Aurora, but that might be a long way.

My main goal is to officialy open the site and let people use it, at least in my home city, Kraków.
