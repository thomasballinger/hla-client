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

    {
        x:10, (arbitrarily large integers representing origin
        y:-34, of event)
        name:'horn',
        distance: 7 (how close client has to be to receive event),
        url: 'http://www.northernsun.com/images/thumb/2241Spaceship.jpg'
        (url for media to display/play if client is interactive)
        duration: 200 (number of milliseconds it is suggested for the
          client to maintain this event, if transient)
    }


