---
layout: post
title: Computer Networking: A top-down approach
date: 2021-01-05
Author: Jack Zhu
tags: [computer-science, computer-networking]
comments: true
---

It's not easy to write reading notes for a textbook, esp. for a very well-structured and popular one. The essential reason is its completeness and comprehensiveness, which makes a brief outline less interesting or even error-prone. It doesn't make sense to quote *use prefetching for the video streaming* for example without presenting the context.

![internet](../images/internet.png)

But I always like to write something once I finish a book, and this one won't be an exception. *James Kurose*'s *Computer Networking* is one of the textbooks that teach you about computer networking, but it doesn't follow the conventional approach, i.e covering from the bottom layer(physical layer) to the top layer(application layer), and he chose the opposite order, i.e from top to bottom. I think this is brilliant, and very useful for the readers who won't be a network administrator but more likely to be a programmer, which it's more relevant and important to know the higher layers of the computer network for a programmer.

It's also more up-to-date comparing to other textbooks under the same topic. We can gain some insights from the offering about Netflix's streaming, Google's datacenter, 4G technology, wireless protocols(e.g WiFi and bluetooth, etc). We appreciate the service from Netflix, Google, Facebook, etc by paying the subscription fee monthly, and the guys behind the *perfect* user experience(e.g streaming, google search) are pushing the technology to its edge every day.

With understanding each layer and its features and possible drawbacks, we can be more confident and careful to write code about network communication. We know the unavoidable latency and the typical value of the RTT for a request/response cycle, which will help us write more robust and user-friendly code to serve our customers better, by factoring in the highly-variable latency, the tradeoff between reliability and timeliness, etc. Therefore, we think twice about which protocol to use between UDP and TCP, how to keep a long-live HTTP connection, how to cache to reduce the network requests, etc.

And I've learned a lot and refreshed my rusty network knowledge, while it's a pity that I don't have enough time to do the homework in each chapter(or it might be an excuse). Learning computer networking again reminds me the good time in college when I was so busy on playing basketball or computer games, but it was also a very wonderful time when I could easily bury myself in the school library for an entire day without stepping out the building and could easily forget the meals.

Let's zoom out a bit. It's fascinating to look back about how great and sophisticated the computer network has been designed and implemented and deployed. It's a huge amount of work under close collaboration by following the distributed and layered philosophy. It is open and public, so every company could invest money to build what they are good at without worrying about the compatibility issue or negotiating the access to some data. Therefore, the Internet has grown like a wildfire across the world, and everyone benefits from it substantially, until we've got some evils like Tencent, Alibaba, Facebook, Google, Amazon, etc. The intrinsic nature of the Internet, like openness, being distributed has been shattered into pieces by creating an *intranet* of its own, and you have to pay a great amount of money to be able to access the data, or you are not allowed at all, even though most of the data is actually created by the users in the first place not the company.

Therefore, I appreciate the great efforts and achievements from computer scientists to build the *Internet*, which might arguably be the greatest invention in human history, on one hand. On the other hand, I feel really sorry to see how the *Internet giants* have done and what they would do in the future. Such *Intranet* approach will surely kill the innovations and slow down the technology progress, which will slow down poverty alleviation and place negative impact on human welfare as a whole.