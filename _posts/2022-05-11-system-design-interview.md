---
layout: post
title: System Design Interview
date: 2022-05-11
Author: Jack Zhu
tags: [system design, interview, programming]
comments: true
---

The books I read about my industry normally could be grouped into three: 1) theory heavy, e.g *Introduction to Algorithms*, 2) practice heavy, e.g *C Programming language*, and 3) the books in between, e.g this one. *System Design Interview* is about how to design a specific system, e.g a chat system, a feed service, a youtube like service, etc. And the author tries to show the steps how the interviewee could follow to tackle a *big* difficult problem. The knowledge about the specific projects are wonderful, but what I love more is the method to approach the problem.

In an interview, the interviewer will ask you to design a system X, and then besides the feeling of being nervous and with high pressure, what we can do to impress the interviewer and secure the offer at the end? The author gives the steps we might be able to follow.

![interview](../images/interview.png)

Firstly, we need to clarify the requirements by asking questions, e.g which platforms the system should run on, PC, mobile phones or smart TV? How many DAUs the system should be able to handle? How many API requests a user could make per day? With the knowledge, we are more clear about the requirements and more importantly we have some rough numbers we could use to make some estimation about the system.

Secondly, we can do the back of envelop estimation, i.e some rough estimation. Some important estimation includes: 1) QPS or throughput, so we could estimate the computing resources we might need 2) storage, this is closely related to the cost, which we should show that we care about cost when designing the system.(we are always under the constraints of resources)

Thirdly, we can give a high level design as the first hit. It won't be sophisticated and we just want to invite the interviewers to buy in and communicate early so we could get some feedback and refine the design without wasting too much time. After this step, we have a high level design consented by the interviewers.

Fourthly, dive deep into the design. In this stage, we need to consider the performance, scalability, responsiveness, user experience, etc. And we might need to extend each component to make it more robust and be able to work when the failure occurs. Diagram is useful and intuitive and could be a good media to convey your ideas. Keep talking with the interviewers and ask their suggestions when there're more than one ways to do one thing.

Lastly, after diving into the system, the major part of the interview is done and the interviewers should have an answer about you, but you could still try to impress more, e.g some missing parts which you don't have time to cover in the previous step, e.g failure tolerance, scaling, optimization, etc.

I love these steps to approach an interview, even though it might not be about system design. For any interview, the first important thing you should do is to ask questions to clarify the requirement, not until too late, a big amount of time has been wasted and then you found there's a very important requirement you have to clarify, which might make your effort meaningless. And also in the perspective of an interviewer or in a real-world project, the requirement spec is always not perfect and comprehensive, which you need to ask the product manager to clarify before you dive into the design.