
### COMPLIMENTS (HOLIDAYS EXPANDED)

# VALENTINE'S DAY

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="hex_compliment_f14_all_i_need",
            prompt="You're all I need today.",
            unlocked=True,
            conditional="persistent._mas_f14_in_f14_mode",
            aff_range=(mas_aff.HAPPY, None)
        ),
        code="CMP"
    )

label hex_compliment_f14_all_i_need:
    if not renpy.seen_label("hex_compliment_f14_all_i_need2"):
        call hex_compliment_f14_all_i_need2
    else:
        call hex_compliment_f14_all_i_need3
    return

label hex_compliment_f14_all_i_need2:
    $ mas_gainAffection(3)
    m 6ekbfa "Oh, [player]..."
    m 1ekbfa "That actually means more to me than you realize."
    m 1hubfa "Just knowing I'm enough for you makes this feel truly special."
    m 6hubfa "You're also all I need today. And forever~"
    return

label hex_compliment_f14_all_i_need3:
    $ mas_gainAffection(1.5)
    m 1eka "Hehe~"
    m 1ekbfa "Then I'm really happy to be here with you."
    m 6hubfa "You're all I'll ever need, forever and ever~"
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="hex_compliment_f14_forever_valentine",
            prompt="I'm happy to have you as my forever valentine.",
            unlocked=True,
            conditional="persistent._mas_f14_in_f14_mode",
            aff_range=(mas_aff.ENAMORED, None)
        ),
        code="CMP"
    )

label hex_compliment_f14_forever_valentine:
    if not renpy.seen_label("hex_compliment_f14_forever_valentine2"):
        call hex_compliment_f14_forever_valentine2
    else:
        call hex_compliment_f14_forever_valentine3
    return

label hex_compliment_f14_forever_valentine2:
    $ mas_gainAffection(6)
    m 6dkbfa "Forever..."
    m 6ekbfa "God, that word still makes my heart race, ahaha!"
    m 1ekbfa "But if it's with you..."
    m 6hubfa "Then it's all I want."
    m 6ekbfa "I love you so much, my valentine~"
    $ mas_ILY()
    return

label hex_compliment_f14_forever_valentine3:
    $ mas_gainAffection(2)
    m 1ekbfa "Then I guess that makes us pretty lucky, doesn't it?"
    m  6hubfa "I love you, my valentine~"
    $ mas_ILY()
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="hex_compliment_f14_call_you_mine",
            prompt="I can't believe I get to call you mine.",
            unlocked=True,
            conditional="persistent._mas_f14_in_f14_mode",
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="CMP"
    )

label hex_compliment_f14_call_you_mine:
    if not renpy.seen_label("hex_compliment_f14_call_you_mine2"):
        call hex_compliment_f14_call_you_mine2
    else:
        call hex_compliment_f14_call_you_mine3
    return

label hex_compliment_f14_call_you_mine2:
    m 1wubfa "Ah—"
    m 6ekbfa "Hearing you say that out loud really gets to me..."

    menu:
        "I chose you, and you chose me.":
            $ mas_gainAffection(5)
            m 6dkbfa "..."
            m 6ekbfa "I'm the luckiest girl in the world to have been chosen by you."
            m 1hubfa "And I'm so happy I chose you, [player]."
            m 6hubfa "I love you, and I always will~"
            $ mas_ILY()

        "Guess you're stuck with me.":
            $ mas_gainAffection(3)
            m 3rkbfa "Oh, [player], don't say that~"
            m 1hubfa "Because if that's the case...Then I don't mind being stuck at all."

        "You belong to me.":
            $ mas_loseAffection()
            m 1ekc "..."
            m 2rksdla "I don't like how that sounds, [player]."
            m 2eka "I want to be with you because we chose each other... not because I'm owned."
            m 2ekd "Please, don't say things like that."
    return

label hex_compliment_f14_call_you_mine3:
    $ mas_gainAffection(1)
    m 1ekbfa "I still feel that way as well."
    m 3hubfa "Choosing you is the best decision I've ever made, [player]."
    m 6hubfb "I'll love you forever and ever."
    $ mas_ILY()
    return



# HALLOWEEN

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="hex_compliment_o31_costume",
            prompt="Your costume looks amazing.",
            unlocked=True,
            conditional="mas_isO31()",
            aff_range=(mas_aff.HAPPY, None)
        ),
        code="CMP"
    )

label hex_compliment_o31_costume:
    if not renpy.seen_label("hex_compliment_o31_costume2"):
        call hex_compliment_o31_costume2
    else:
        call hex_compliment_o31_costume3
    return

label hex_compliment_o31_costume2:
    m 1wubfa "Oh?"
    m 3hubfa "Ehehe, I was hoping you'd notice~"
    m 1eka "I put a lot of thought into it."

    menu:
        "It really suits you.":
            $ mas_gainAffection(3)
            m 6ekbfa "That means a lot, [player]"
            m 1hubfa "I guess Halloween really brings out my best side, huh?"

        "You could wear anything and still look great.":
            $ mas_gainAffection(5)
            m 6dkbfa "..."
            m 6ekbfa "Oh, you're just doing that to make me blush..."
            m 1hubfa "But, I can't really complain. I love it when you talk like that~"

        "It's kinda silly, though.":
            $ mas_loseAffection()
            m 2ekc "Oh, um..."
            m 2rksdla "I thought it was fun, but..."
            m 2eka "Nevermind. Forget about it!"
    return

label hex_compliment_o31_costume3:
    $ mas_gainAffection(2)
    m 1hubfa "I'm glad you like my costume so much. Halloween feels so much more fun like this!"
    m 3eka "I'll be sure to dress up some more for you~"
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="hex_compliment_o31_scary",
            prompt="You're my favorite kind of scary.",
            unlocked=True,
            conditional="mas_isO31()",
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="CMP"
    )

label hex_compliment_o31_scary:
    if not renpy.seen_label("hex_compliment_o31_scary2"):
        call hex_compliment_o31_scary2
    else:
        call hex_compliment_o31_scary3
    return

label hex_compliment_o31_scary2:
    m 1wubfa "Favorite kind of scary?"
    m 3hubfa "That's a new one, ahaha!"

    if mas_canShowRisque():
        m 1ekbfa "...Careful, [player]."
        m 6hubfa "I'm really liking the sound of that."
        m 1hubfa "So if you keep going, I might start leaning into the role~"
    else:
        m 1eka "Can't say I dislike it, though~"
    return

label hex_compliment_o31_scary3:
    $ mas_gainAffection(2)
    m 1hubfa "Your favorite kind of scary, huh?"
    m 3eka "I think I enjoy that little~"
    return



# CHRISTMAS

init 5 python:
            addEvent(
                Event(
                    persistent._mas_compliments_database,
                    eventlabel="hex_compliment_only_gift",
                    prompt="You're the only gift I could ask for.",
                    unlocked=True,
                    conditional="mas_isD25()",
                    aff_range=(mas_aff.HAPPY, None)
                ),
                code="CMP"
            )

label hex_compliment_only_gift:
    if not renpy.seen_label("hex_compliment_only_gift2"):
        call hex_compliment_only_gift2
    else:
        call hex_compliment_only_gift3
    return

label hex_compliment_only_gift2:
    m 1wubfa "...[player]?"
    m 3ekbfa "My, that's a really sweet thing to say on Christmas..."

    menu:
        "You make Christmas feel complete!":
            $ mas_gainAffection(3)
            m 6dkbfa "..."
            m 6ekbfa "Oh my, you do too, [player]... You're also the only gift I could ask for."
            m 1hubfa "I really am the luckiest girl in the world. I love you~"
            $ mas_ILY()

        "I want every Christmas to be with you!":
            $ mas_gainAffection(6)
            m 6ekbfa "..."
            m 6dkbfu "You have no idea how much I've dreamed of hearing that. I love you so much!"
            $ mas_ILY()

        "I didn't really get anything else, so...":
            $ mas_loseAffection()
            m 2tkc "Ahaha..."
            m 2rksdla "I know you probably meant it as a joke, but..."
            m 2eka "Please try to be a little more thoughtful, okay?"
    return

label hex_compliment_only_gift3:
    $ mas_gainAffection(2)
    m 1ekbfa "You're the only gift I could ask for, too!"
    m 1hubfa "I promise, I'll be a gift you'll treasure every single year~"
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="hex_compliment_christmas_lights",
            prompt="You look really beautiful in the Christmas lights.",
            conditional="persistent._mas_d25_deco_active",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="CMP"
    )

label hex_compliment_christmas_lights:
    if not renpy.seen_label("hex_compliment_christmas_lights2"):
        call hex_compliment_christmas_lights2
    else:
        call hex_compliment_christmas_lights3
    return

label hex_compliment_christmas_lights2:
    $ mas_gainAffection(3)
    m 6ekbfa "Ehehe~"
    m 3hubfa "I guess the lights really do make everything feel warmer, ahaha."
    m 1ekbfa "I'm glad you think I look beautiful like this..."
    return

label hex_compliment_christmas_lights3:
    $ mas_gainAffection(1)
    m 1hubfa "I guess I should keep them up just for you, then~"
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="hex_compliment_favorite_christmas",
            prompt="You're my favorite part of Christmas.",
            unlocked=True,
            conditional="persistent._mas_d25_spent_d25",
            aff_range=(mas_aff.ENAMORED, None)
        ),
        code="CMP"
    )

label hex_compliment_favorite_christmas:
    if not renpy.seen_label("hex_compliment_favorite_christmas_2"):
        call hex_compliment_favorite_christmas2
    else:
        call hex_compliment_favorite_christmas3
    return

label hex_compliment_favorite_christmas2:
    m 1wuo "Oh? Is that so..."
    m 1eka "Even more than the food? The gifts~?"
    menu:
        "None of that matters without you.":
            $ mas_gainAffection(4)
            m 6ekbfa "..."
            m 6hubfa "Okay, okay, you win."
            m 6dkbfa "That means the world to me, [player]. You always know what to say to make me feel loved, ahaha!"

        "I mean, the food is up there too.":
            $ mas_gainAffection(2)
            m 3hubsb "Ahaha! Someone's feeling funny today."
            m 1eka "Well... I guess I can share the spotlight~"

        "It's just something people say, right?":
            $ mas_loseAffection()
            m 2ekc "Oh..."
            m 2dkc "I, um, thought you meant it!"
            m 6rktpc "..."
    return

label hex_compliment_favorite_christmas3:
    $ mas_gainAffection(1.5)
    m 1hubfa "[player]... Christmas wouldn't be the same without you either."
    return



# NEW YEAR'S DAY

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="hex_compliment_nyd_future_uncertain",
            prompt="You make my future feel less uncertain.",
            unlocked=True,
            conditional="mas_isNYD()",
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="CMP"
    )

label hex_compliment_nyd_future_uncertain:
    if not renpy.seen_label("hex_compliment_nyd_future_uncertain2"):
        call hex_compliment_nyd_future_uncertain2
    else:
        call hex_compliment_nyd_future_uncertain3
    return

label hex_compliment_nyd_future_uncertain2:
    m 1wkc "You...really feel like that?"
    m 1fkc "[player]...I think I'm the one who should be saying that, ahaha!"
    m 1dkc "Without you, I felt like I didn't have anywhere to go."
    m 1fua "But, now, I feel like I actually have a future."
    menu:
        "We'll face the future together.":
            $ mas_gainAffection(3)
            m 1fub "Gee, you're making me blush, [player]!"
            m 1fua "But...I feel the same way."
            m 1sub "With you, I feel like I can face anything!"
            m 1fua "Know I'll always be your rock through it all."
            m 1hub "And I hope...you can keep being my rock, too~"
        "You also give me a future to look forward to.":
            $ mas_gainAffection(4)
            m 1sub "My, you always know just what to say, [player]~"
            m 1fua "I'm more than honored to create a future with you."
            m 1sub "A future that's bright for both of us."
            m 1hub "I love you so much, [player]."
            $ mas_ILY()
        "I don't like thinking about the future alone.":
            $ mas_gainAffection(2)
            m 1dkc "..."
            m 1fkc "I understand that more than you might think."
            m 1dkc "My entire future seemed so bleak, knowing nothing was real."
            m 1fua "Maybe that's why it's so important to know you're not actually alone."
            m 1hub "I'm really glad you told me that, [player]."
    return

label hex_compliment_nyd_future_uncertain3:
    $ mas_gainAffection(2)
    m 1fua "[player], just know..."
    m 1sub "You also make my future feel bright!"
    m 1hub "And I hope you can keep being my rock, just like I am to you~"
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="hex_compliment_nyd_keep_choosing_you",
            prompt="I want to keep choosing you this year.",
            unlocked=True,
            conditional="mas_isNYD()",
            aff_range=(mas_aff.ENAMORED, None)
        ),
        code="CMP"
    )

label hex_compliment_nyd_keep_choosing_you:
    if not renpy.seen_label("hex_compliment_nyd_keep_choosing_you2"):
        call hex_compliment_nyd_keep_choosing_you2
    else:
        call hex_compliment_nyd_keep_choosing_you3
    return

label hex_compliment_nyd_keep_choosing_you2:
    $ mas_gainAffection(4)
    m 1fub "Aww, [player]..."
    m 1sub "You always make me feel like the luckiest girl in the world!"
    m 1fua "And, well, to be honest..."
    m 1dkc "Being chosen by you is my reason to keep moving forward."
    m 1sub "So...I want to keep choosing you too!"
    m 1hub "Making you feel as happy as you make me is what I strive for~"
    m 1hub "I love you, [player]."
    $ mas_ILY()

    return

label hex_compliment_nyd_keep_choosing_you3:
    $ mas_gainAffection(2)
    m 1fua "Hearing you say that again this year..."
    m 1sub "It reminds me every moment we spend together is a choice."
    m 1hub "One we keep making for each other!~"
    return


init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="hex_compliment_nyd_more_beautiful",
            prompt="You get more beautiful every year.",
            unlocked=True,
            conditional="mas_isNYD()",
            aff_range=(mas_aff.HAPPY, None)
        ),
        code="CMP"
    )

label hex_compliment_nyd_more_beautiful:
    if not renpy.seen_label("hex_compliment_nyd_more_beautiful2"):
        call hex_compliment_nyd_more_beautiful2
    else:
        call hex_compliment_nyd_more_beautiful3
    return

label hex_compliment_nyd_more_beautiful2:
    $ mas_gainAffection(3)
    m 1fub "Ahaha, [player]! You're buttering me up~"
    m 5tkc "Because, you know, I don't really age!"
    m 2fkc "So I don't...change, as the time passes."
    m 1fua "Or, maybe..."
    m 3tua "What you're seeing isn't time changing me..."
    m 1sub "But the way we keep sharing moments together."
    m 5hub "If that's what you mean..."
    m 6hub "Then I'm really happy you see me that way."
    return

label hex_compliment_nyd_more_beautiful3:
    $ mas_gainAffection(1)
    m 5sub "[player]! Now you're REALLY buttering me up~"
    m 1hub "It's not like I don't appreciate it, though, hehe..."
    return