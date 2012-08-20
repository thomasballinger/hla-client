Prototype client for receiving events from 
the ingrid/heylooka server


Motivation
----------

Clients receive events corresponding only to what the server
thinks they need to know, instead of every single message.

This has applications for reduced load in MMO's where the n
squared communication problem of many clients in a shared world,
or preventing untrusted clients information they should not
reveal to game players (eg, starcraft 1 map hacks)

Protocol
--------

Clients connect to the server on a tcp port, then receive and send
messages about events occuring. These events have the format

   ascii digits representing num bytes message takes up, terminated by a space
   | aforementioned space (doesn't count toward the message length)
   | | Largest radius at which event is perceivable to a client
   | | |  x-position of event
   | | |  |  y-position of event
   | | |  |  |  Display name of event
   | | |  |  |  | 
   18 17 217 23 Big Boom

over a tcp connection. Events are sent to the server using similar format;

    12 /nick thomas
    7 /move N
    16 /event Honk Horn

Install
-------

I used
http://twistedpairdevelopment.wordpress.com/2012/02/21/installing-pyglet-in-mac-os-x/
for installation on OSX Lion.
