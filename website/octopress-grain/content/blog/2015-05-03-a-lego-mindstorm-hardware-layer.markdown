---
layout: post
title: "A Lego Mindstorm hardware layer"
date: "2015-04-18 20:28"
author: bcopy
categories: [lego mindstorm,nxt-python,drivar]
comments: true
published: true
---

The Raspbuggy platform is destined to be an open educational programming platform. It is designed to adapt to a 
large array of hardware layers, so that it can evolve through time.

In order to cope with different hardware platforms, it relies on a hardware abstraction layer called "Drivar".

<!--more-->

Drivar is (currently) a Python library that provides a simple and stable API to give access to :

* Controlling the activity of the car motors (direction of the rotation, speed).
* Obtaining reading from sensors (proximity ultrasonic sensors for instance).
* Acquiring and processing images and videos for image recognition.

Today, I have started writing the "Drivar NXT" classes, that allow the Raspbuggy to run on top of Lego Mindstorm NXT kit.

NXT kits are quite easy to drive from Python via USB thanks to the excellent NXT-Python library.

In order to organise our next Robotics challenge and introduce the Raspbuggy platform at CERN, we will use four NXT kits
that will provide an ideal development target for our contestants.

Stay tuned...


