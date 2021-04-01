---
layout: post
title: The Pragmatic Programmer
date: 2021-04-01
Author: Jack Zhu
tags: [software-engineering, programming, programmer]
comments: true
---

Each field has its own *bible* books, and computer science is no exception. While those *bible* books might be stacked for years on the shelf, or only are bought as a souvenir, or are proofs that *you buy it and you get it* as most books. I am not that lazy, but not too much better. This book *The Pragmatic Programmer* was read over a decade ago and then till now it's been picked up again.

For a *programming* book, it will become obsolete very quickly unless you touch something *meta* or *philosophy*. That's the main reason why this book just survives after 20+ years and are still been recommendated for new programmers. The 90+ tips in the book mostly still hold like a rock. And it also inspires a lot of subsequent books like [A Philosophy of software design](2020-11-30-a-philosophy-of-software-design.md) as I read last year.

![craft](../images/craft.png)

I want to list some of the tips that resonate with me a lot.

## don't tolerate the broken-window

For a long time, I sway between the *quick and dirty* and *build solid codebase*. After struggling with projects and following either of these doctrines in my developing life, I tilt towards the *solid codebase* approach. *Quick and dirty* might seem to be rational and justifiable if you have a tight delivery schedule. But in reality, it's more of an excuse or laziness, and you justify your decision by saying the requirement(biz logic) will change very soon, while that might be the reason why we should build solid codebase in the first place even under tight schedule.

We all know *broken-window theory*, but we normally underestimate the impact if we don't push hard enough by allowing a small Pull Request to pass which doesn't meet the standard, which will accumulate and finally bite us. Zero to One is a huge leap, while one to a hundred might be trivial until the codebase becomes incurable. 

## Agile is not a noun and it's how you do things

I used to work in a very old-fashioned telecommunication company which advertises themself with adopting the *Agile* approach when I was in the interview. After joining, we did have the *standup meeting*, *planning meeting*, *retro meeting*, etc. But the delivery cycle was still long and tedious and no one complained about it. Therefore, the meetings were more like a social activity or a slack from the busy work. One thing I still remembered vividly is the QA team, who were even in another building, and developers had to spend an afternoon to replicate a trivial bug with the QA collegue.

*Agile* is not just what you declare, but how you do. Each meeting in the practice has its clear purpose, and everyone knows the expected outcome. And at last it's the strive to delight the customers that will make the difference, which requires to involve the end users, a short lead time, a better communication, etc.

## lead time is the key

No matter how you declare and advertise your company, it's crucial to meet the customer's expectation to survive the competitive market, which might boil down to one key metric, i.e *lead time*, which is the time between the start the task and the delivery time to the customer.

In the book [Accelerate](2020-12-07-accelerate.md), it also put a very high weight on *lead time* as something to differentiate a *good* company and a *bad* company. I agree with this argument and the data.

But how to reduce the *lead time* is the key step. It's just like we all know *Standford University* is a perfect choice if you pursue computer science, but knowing that is nothing, you have to know how to get enrolled. And it comes to a very difficult reality that most companies that don't meet the requirement, incl. a good documentation(you can learn what you need quickly and independently, esp. when we are all remote), a trust culture(end-to-end development will require the dependencies in each step, whether it's crendentials or othe needed resource), good mornitoring and falut-tolerance system(you have to know the fault quickly and correct it immediately), etc.

----

After 20+ years, this book is still relevant, and might be a must-read. For me, such books that cover the *meta* and *philosophy* are worthy of reading now and then, which just refresh you with something you know vaguely or ask you to see the whole picture instead of getting lost in some details.