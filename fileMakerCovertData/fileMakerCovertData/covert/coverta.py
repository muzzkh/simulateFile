import os.path
import time

monologue = """Once upon a time there was a lovely 
                         princess. But she had an enchantment 
                         upon her of a fearful sort which could 
                         only be broken by love's first kiss. 
                         She was locked away in a castle guarded 
                         by a terrible fire-breathing dragon. 
                         Many brave knights had attempted to 
                         free her from this dreadful prison, 
                         but non prevailed. She waited in the 
                         dragon's keep in the highest room of 
                         the tallest tower for her true love 
                         and true love's first kiss. (laughs) 
                         Like that's ever gonna happen. What 
                         a load of - (toilet flush)
 
               Allstar - by Smashmouth begins to play. Shrek goes about his 
               day. While in a nearby town, the villagers get together to go 
               after the ogre.
 
               NIGHT - NEAR SHREK'S HOME

                                     MAN1
                         Think it's in there?

                                     MAN2
                         All right. Let's get it!

                                     MAN1
                         Whoa. Hold on. Do you know what that 
                         thing can do to you?
 
                                     MAN3
                         Yeah, it'll grind your bones for it's 
                         bread.
 
               Shrek sneaks up behind them and laughs.

                                     SHREK
                         Yes, well, actually, that would be a 
                         giant. Now, ogres, oh they're much worse. 
                         They'll make a suit from your freshly 
                         peeled skin.
 
                                     MEN"""
message = monologue.split()

for m in message :
    n = open(m, 'x')
    n.close()
    n = open("send", 'x')
    n.close()
    while(os.path.isfile("send")) :
        time.sleep(.5)