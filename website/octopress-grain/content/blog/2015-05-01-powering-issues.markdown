---
layout: post
title: "Powering issues"
date: "2015-05-01 19:00"
author: bcopy
categories: [power,explorerhat]
comments: true
published: true
---

With all the existing options on the market to control DC motors, collect inputs,
drive outputs, power the whole thing in a standard 5 volts, you would think to controlling a 4WD model car chassis is a no-brainer.
Well, I must be missing something.

<!--more-->

<img src="${r '/images/2015-04-18-raspbuggy-explorer.jpg'}">

Here's what we have so far :

* A 4 wheel drive car chassis, with 4 DC motors that require around 250 mA each.
* A Raspberry Pi B+, requiring a stable 5V 700 mA.
* A dual-USB output battery packing 6600 mAh and a dual 2 A / 1 A power outlet.

... But no convenient way to connect it all.

The Pimoroni Pibrella, although adequately powered independently and able to drive the four motors, can only do so in a single direction (no H-Bridge).
The Pimoroni Explorer Pro (picture above) can certainly power four motors, but only going in the same direction - trying to reverse direction on one set of wheels (essential to change direction with precision) will not work.
We could certainly go ahead with a simpler chassis and only two motors (using a freely moving wheel at the front), which is what the Explorer Pro HAT is really designed for.
But we would lose a lot of precision in the movement, as well as the capacity to evolve on difficult terrain.

Ideally, a simple board that would exhibit :

* Two H-Bridge outputs, powered separately from the Raspberry Pi and capable of driving 2 motors each (2 x 250 mA).
* A ground, 3.3V and 5V individually powered slots. 
* Two digital 5V outputs.
* Two digital protected 5V inputs.

... would be enough to drive the four motors, collect input from two ultrasonic sensors and power a small LED array or an LCD screen.

Any takers ?
