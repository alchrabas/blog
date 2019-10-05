Title: My review of Latin course on Duolingo
Date: 2019-10-05 22:26:00
Tags: languages, latin
Category: duolingo
Authors: Aleksander Chrabąszcz
Summary: My opinion on recently released Latin course on Duolingo

Great news! Latin (from English) is now available on Duolingo! I was waiting for years to see it coming. It's the subject I was interested in for years and I was wondering if it's going to be a good solution to facilitate learning, especially considering the fact there are not so many sources of original material produced by the language users. It's worth noting that this course is still in the beta phase, so I was prepared to find some bugs or inconsistencies.

I have basic experience with Latin, as I am already learning it for a few years from two main sources: a book "Łacina bez pomocy Orbiliusza" (pretty old and thus pretty funny) and the internet courses, especially [lacina.globalnie.com.pl](http://lacina.globalnie.com.pl/). Both are meant for students who are natively Polish. It helps a lot, because inflection in Latin is very similar to the one in Polish (for example Polish nouns have 7 cases, while Classical Latin ones have 6, but more about it later), so sometimes there can be comments like: 'look, you just need to do it similarily as you do in Polish'.

When I've started learning, my side goal was to see the difference between learning using 'the school way', going a lesson after lesson, e.g. memorizing all the suffixes, instead of reading 'everyday' texts and listening to the sentences (which I consider to be a far superior method). Learning English and German in school made me still unable to speak freely in German and I became comfortable with English only after graduating, so I wanted to check if it's mostly the way it's taught, the pressure of getting good marks or maybe I was just too stupid right then.

To summarize the experiment, I've also started studying Italian (Duolingo + sport news + podcasts + a bit of TV series) and I think I've learned a lot more even though I've started with Italian just one and half a year ago. But still the progress in Latin was noticeable, I think it was much better than with English/German in the same timeframe.

# Why learning Latin?

My main goal was to be able to read classical texts, especially inscriptions on ancient buildings. I'm also interested in the history and evolution of the languages, so it's useful to know the basics of Latin to understand the articles about the processes that occurred in the Romance languages.

![Book with speeched of Vladimir Putin in Latin](/images/latin-course-on-duolingo/vladimirus-putinus.png)

<p style="text-align:center">It's also possible to read some modern authors (photos by <a href="https://twitter.com/maxseddon/status/1049995764313874432">Max Seddon</a>)</p>

# First impression

So I've just started the course and begun the hard work. The beginning was pretty easy, as it always was on Duolingo with languages I've already learned before. Still, I've learned something new and a few things even surprised me. There were my first observations:

### 1. Restored classical pronunciation

The first good thing was the fact the restored classical pronunciation was used for speech. It's great news, because when thinking about it when I was waiting for the course's release, I was sure it's not going to be Polish-Latin pronunciation (which would be ok for me), so I hoped it's not going to be the English one (which is in my opinion very strange). So it couldn't have been better.

### 2. Starting with 'hard' declensions

Both the book and the web course presented a different way of teaching new declensions (groups in which nouns are inflected in the same way) than the books I've used before. There I've started with the first conjugation and the first declension (a pretty easy one) and worked on sentences crafted to use only things I already know, then gradually adding more conjugations and declensions. Duolingo hit me with "hard" nouns, like `mater` and `pater`, which are a part of the most irregular third declension. If you are curious, you can [take a look on the possible endings on wiktionary](https://en.wiktionary.org/wiki/Appendix:Latin_third_declension). That's daunting, but fortunately Duolingo doesn't push that much information at once and words for parents are pretty important, aren't they? So the good thing is, I wasn't warned that these words may be hard, so they were easy.

In general, during the initial lessons I've learned just (the most important) nominativus and accusativus form of some words, while some other words, especially places, were only presented in nominativus and...

### 3. Locativus

Wait, is there a case like that? Earlier I've mentioned the similarities between Polish and Latin. Both languages have the following cases: nominativus, genetivus ("of", posession), dativus ("to sb", indirect object), accusativus (direct object) and vocativus (addressing somebody directly). The difference is existence of instrumentalis and locativus in Polish, which in Latin is more-or-less represented by ablativus. Of course there is no one-to-one relationship between "the same" cases in different languages. The same names are used because their functions are similar, but you can't assume that you always translate Polish genetivus to the Latin one.

So we have 6 cases in Latin, but in the beginning of the Duolingo course, we learn the seventh - Latin locativus. It is presented as almost as prominent as nominativus and accusativus, while it's the case which almost disappeared in pre-classical times and words which do have it are pretty rare exceptions.

In my prior Latin education I've learned just a single word with a locativus case: domus (house). Using Duolingo, in the first day I've already learned a few more. For example some cities have a locativus case, namely [Roma](https://en.wiktionary.org/wiki/Roma#Declension) and the course didn't like me using `in + ablativus`, which I hoped to be an acceptable solution. Maybe when there is locativus, then I should use one, or maybe it's something that will get changed in the future.

### 4. Common speech

Earlier I was generally learning more formal things, on Duolingo there are some sentences that could've been useful if I ever wanted to have a chat in Latin with somebody. Also, some sentences are pretty insane, but it's a common thing on Duolingo.

![Translating the sentence 'The drunk parrot writes a song'](/images/latin-course-on-duolingo/strange-sentence.png)

<p style="text-align:center">Thanks, that may be useful!</p>

### 5. Latin names of American cities

It's also pretty funny, but there is a thing like that. And not just adding a latin-style suffix to create Bostonia. New York, for example, is named by a Roman military camp that existed next to present York on British Isles, so the New York is Novum Eboracum. I hope I will ever make use of this knowledge...

# My use of Latin casual system in programming

A few years ago I was looking for a good library for internationalization of texts in Python. It was meant for [Exeris](https://blog.exeris.org), the game I've started to develop five years ago and still without hopes of finishing it in my lifetime. I wanted to be able to write texts in English and then be able to translate them correctly into Polish, with regard to declension, conjugation and pluralization. For example, in a sentence  `You hit a bear with a steel sword`, where the `steel sword` and `bear` parts can be set dynamically, it should take into account the fact that `bear` should be in accusative and `sword` in instrumentalis. This library, called Pyslate, is publicly available on [GitHub](https://github.com/alchrabas/pyslate) and [PyPI](https://pypi.org/project/pyslate/). Maybe I'll write a separate post about it in the future. But, in general, my acceptance criteria for this library was to be able to internationalize texts from English to both Polish and Latin, in order to cover at least majority of European languages.

# It's Classical Latin

An important thing to note, this course teaches Classical Latin, which is a version of the language from the late republic (I century BC) promoted by the people like Cicero and Caesar. It's a kind of semi-artificial language, in which some words or structures were favored, while others were consciously removed. It was used mostly by educated people, while the common folk spoke differently even in Rome itself, not to mention other people for which Latin wasn't a native language. Such people spoke Vulgar Latin, which, after a series of transformations, gave birth to romance languages: Italian, French, Spanish and others. One of many reasons of the word transformations was mistakes in declension made by less educated people, so it's hard not only for us ;)

# Conclusion

After just 2 or 3 weeks I've finished more than half of the course, so it's obvious the course is very short, but I'm absolutely impressed by the ability to learn Latin by listening. For the time being, it's going to be the main way of studying Latin until I learn everything that's provided. I hope it'll be enough to get a feel of it and then continue with harder courses and easy texts ('Commentarii de Bello Gallico'?). The best thing about Duolingo is it's so easy to spend just a few minutes a day, so it doesn't require any prior planning. Duolingo will never be enough to become proficient with any language, but it always helped me in making a big step forward. And the course is only going to get better, because it's still in Beta and I'm sure it will grow larger. I hope that a newly emerging community of learner (the course already has almost 300 thousand participants) will encourage latinists to contribute to this course.
