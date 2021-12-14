---
layout: post
title: Two Clojure Books
date: 2021-12-04
Author: Jack Zhu
tags: [clojure, programming]
comments: true
---

Reading technical books is always heavy and hard to say fun, but if it's a must(e.g your school, your job), you'd better try to get some fun if possible. Clojure is a new programming language for me, which is also my first serious functional programming language for serious projects, at least I use it for family support and the service it backs supports millions of users.

I am never a Java guy or a functional programming buddy, though I know it and like it, but it's far from serious, since we don't use in in our daily projects. What I did was most about Python, or Objective-C, and Javascript for sure. We usually have different teams to handle different parts of the system, e.g the front-end team, the back-end team, and the Ops team, which could free each other from knowing too much about other teams' work, but it also prevents us from having a high level or insider view about the entire system. It works fine for most projects, because it could make each developer's mind to be able to hold what he needs to and don't need to switch to different context in a daily basis.(Every programmer knows context switching is expensive) It's just like the philosophy of Unix, which allows each module(individual developer here) to do one thing and do it well.

Until I join a new company which embraces the lean development and practices in the entire engineering team. And it means I need to cover from the service layer to have the fundamental logic, to the back-end to expose the RESTful API, to the front-end to consume the APIs, to the Ops to deploy, and also I must know a lot about database, elastic search, CI/CD, etc, not to mention the different languages, e.g Clojure, Java, Python, Javascript, etc.

![programming](../images/programming.png)

Is that a bliss or a misfortune to a developer? In the short run, of course, it's a misfortune and misery, since the developer has to jump out his own comfort-zone and learn new things in a very tight time, and also in the daily development he also has to switch context frequently, which could hurt his productivity, and might introduce bugs more frequently due to the immature understanding of the whole system. And he gets confused and lost very easily, because he cannot find the help he needs, whatever it's a snippet of code, or a doc about business decision. He struggles for a while and then he might adapt well and feel some benefits then, which is the long-term benefits of this approach. Obviously no one in a system like facebook or google knows every piece of detail about the entire monster, esp. when it grows and passes a certain line of company size, it will makes everything more like the pipeline in a manufacturing factory, and each one will be just a bolt or a nut and only knows how to fasten that piece, nothing else. You surely don't know how an iPhone is produced at the end of the pipeline even though you're in between. So we gain more knowledge about the system, and everyone knows anyone else's work, and could review code when needed. The **lead time**(defined as the time between opening a ticket and going production) will be reduced, which is surely a bliss to the company and also the customers.



So far, I haven't talked about *Clojure* yet. And I want to do it now. I've finished reading two books recently, and one is *programming clojure* (I know there's another book with a similar name but just a different order of the words), and the other one is *elements of Clojure* ("elements of" surely will remind you about something not like cookbook which you could follow, but like philosophy you might be inspired or forget).

*programming clojure* is the book recommended by the Clojure author *Rich Hickey*(a pity that he didn't write a clojure book), so it might worth trying. It's not a dense book and easy to follow, in which it covers the essential parts of the language and demonstrates the elegance of Clojure in the implementation. Building over JVM is a huge advantage to be able to deploy and interoperate with Java.

*elements of Clojure* is more philosophical, and just like a philosophy book, it's easy to click and resonate with you, since obviously you know them already but the author puts them in the print. I don't say it's not important, and just like what the author says, the *tacit knowledge* is important and building some useful terms or vocabularies that people in the Clojure community could use is very important and helpful too. The author is very knowledgable and versatile in different areas, which he can give very interesting analogues and comparisons between software engineering and architecture or construction etc. And we will gradually realize software engineering is no new engineering field at all, and what applies to other engineering fields would also apply to software engineering. Therefore due to the short history of software engineering and much longer history of architecture/construction, or art or physics or maths, we could learn a lot from other fields and benefit ourselves greatly.

These two books are good, and if you want some practical suggestions you can follow the first book, and if you like to enjoy some philosophy on software engineering, you surely should read the second, which only has about 100 pages(I guess books from *Kant* or *Hegel* are still on your bookshelf, covered by dust, a lot of dust, just like mine).