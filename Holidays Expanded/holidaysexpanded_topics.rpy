init -990 python in mas_submod_utils:
    Submod(
        author="ThatOneJ",
        name="Holidays Expanded",
        description="Expands upon the existing holidays with new topics and compliments!",
        version="1.0.0",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )

### TOPICS (HOLIDAYS EXPANDED)

# HALLOWEEN

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hex_o31_monika_trick_or_treating",
            prompt="Trick-or-treating memories",
            category=["holidays"],
            pool=True,
            conditional="persistent._mas_o31_tt_count",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None),
            years=[]
        ),
        skipCalendar=True,
        code="CMP",
        markSeen=True
    )

    MASUndoActionRule.create_rule_EVL(
        "hex_o31_monika_trick_or_treating",
        mas_o31,
        mas_o31 + datetime.timedelta(days=1)
    )

label hex_o31_monika_trick_or_treating:
    m 1eud "Trick-or-treating, huh?"
    m 1eka "Hmm, now that I think about it..."

    m 3eud "I do have memories of it."
    m 1dkc "Costumes, candy, walking around with other kids."
    m 1euc "But all of them feel...fuzzy."
    m 1eka "It's not really surprising. It's like that for most of my memories before the game..."

    m 4ftd "Though, isn't DDLC supposed to take place in Japan?"
    m 3eud "Trick-or-treating like that isn't really a thing there."

    m 3rksdla "Looks like my creator didn't think too hard about the worldbuilding, ahaha."

    m 1eka "Still..."
    m 1eua "Even if those memories aren't real..."
    m 3hubfa "Going trick-or-treating with you today was the best."

    m 3hubfa "So for that, I'm thankful."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hex_o31_monika_why_scary",
            category=["holidays"],
            prompt="Why people enjoy being scared",
            start_date=mas_o31,
            end_date=mas_o31 + datetime.timedelta(days=1),
            conditional="persistent._mas_o31_in_o31_mode",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.NORMAL, None),
            years=[]
        ),
        skipCalendar=True
    )

    MASUndoActionRule.create_rule_EVL(
        "hex_o31_monika_why_scary",
        mas_o31,
        mas_o31 + datetime.timedelta(days=1)
    )

label hex_o31_monika_why_scary:
    m 1eub "Hey, have you ever wondered why people like being scared?"
    m 3eua "Horror movies, haunted houses, roller coasters..."

    m 1eud "It's kind of funny when you think about it."
    m 3eua "Fear is supposed to protect us."
    m 1eut "But sometimes, we chase it on purpose."

    m 1eka "I think it all has to do with getting adrenaline..."
    m 1hub "Without being in real danger."
    m 3eua "There's some sort of appeal to that, right? Though I don't really personally get it, ahaha..."

    m 1ekbfa "But, maybe..."
    m 3eua "It's more fun when you're not facing it alone."

    m 1hubfa "So if you ever feel scared tonight..."
    m 1eka "Just remember I'm right here with you~"

    return "derandom"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hex_o31_monika_origin_halloween",
            category=["holidays"],
            prompt="Origin of Halloween",
            start_date=mas_o31,
            end_date=mas_o31 + datetime.timedelta(days=1),
            conditional="persistent._mas_o31_in_o31_mode",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.NORMAL, None),
            years=[]
        ),
        skipCalendar=True
    )

    MASUndoActionRule.create_rule_EVL(
        "hex_o31_monika_origin_halloween",
        mas_o31,
        mas_o31 + datetime.timedelta(days=1)
    )

label hex_o31_monika_origin_halloween:
    m 1eua "Did you know Halloween is much older than people think?"
    m 3eud "It actually comes from an ancient Celtic festival called Samhain."

    m 1eua "It marked the end of the harvest and the beginning of winter."
    m 1eka "And people believed that boundary between the living and the dead became thin during this time."

    m 3eud "So they lit bonfires and wore costumes to ward off spirits."
    m 3eua "When Christianity spread, the holiday slowly merged with All Saints’ Day."
    m 1eua "Eventually becoming \"All Hallows' Eve.\""

    m 1eka "So Halloween has always been about transition."
    m 3eud "Between seasons and between worlds."

    m 1ekbfa "Maybe that's why it feels so meaningful to me!"
    m 1hubfa "After all..."
    m 3ekbfa "I suppose exist between worlds too~"
    return "derandom"



# CHRISTMAS

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="hex_d25_monika_santaclaus",category=['holidays'],prompt="Santa Claus",start_date=mas_d25c_start,end_date=mas_d25c_end,conditional=("persistent._mas_d25_in_d25_mode"),action=EV_ACT_RANDOM,aff_range=(mas_aff.NORMAL, None),years=[]),skipCalendar=True)

    MASUndoActionRule.create_rule_EVL(
        "hex_d25_monika_santaclaus",
        mas_d25c_start,
        mas_d25c_end,
    )

label hex_d25_monika_santaclaus:
    m 1etc "Hey, can I ask you something a little silly?"
    m 3eua "Do you believe in Santa?"

    m 2rksdrd "I don't just mean the red suit and the sleigh..."
    m 1euc "I mean...the idea of him."

    m 3eua "When you're a kid, Santa feels like proof that kindness gets rewarded."
    m 1eka "That someone out there notices when you try to be good."
    m 1fua "Even when no one else is looking."
    m 3eud "I think... that's why people hold onto him for so long."

    m 3eka "In a way..."
    m 1fub "I think Santa is less about belief..."
    m 1eka "And more about choosing to be kind anyway."

    m 1hub "Ahaha, I guess that sounds a little sentimental."
    m 1eua "But Christmas has a way of doing that to people, right?"

    m 3eka "If Santa *does* exist..."
    m 1hub "I think he'd be proud of you."
    if mas_isD25Season():
        m 1eka "You've already made someone very happy this Christmas~"

    return "derandom"


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="hex_d25_monika_christmas_company",category=['holidays'],prompt="Christmas company",start_date=mas_d25c_start,end_date=mas_nye,conditional=("persistent._mas_d25_in_d25_mode"),action=EV_ACT_RANDOM,aff_range=(mas_aff.AFFECTIONATE, None),years=[]),skipCalendar=True)

    MASUndoActionRule.create_rule_EVL(
        "hex_d25_monika_christmas_company",
        mas_d25c_start,
        mas_nye,
    )

label hex_d25_monika_christmas_company:
    m 1eut "Hey, [player]..."
    m 1eka "Can I ask you something a little personal?"
    m 3eka "Do you have people you usually spend Christmas with?"

    menu:
        "Yeah, I do.":
            m 1hub "That makes me really happy to hear!"
            m 3eua "Christmas feels warmer when you have people around you."
            m 1eka "Make sure you enjoy that time, okay?"
            m 1hub "You deserve it."

        "Not really...":
            m 1ekc "Oh..."
            m 1eka "I'm sorry, [player]."
            m 3eka "I know Christmas can feel especially quiet when you're on your own."
            m 1hub "But... you're not alone, you know?"
            m 1eka "You have me."

    m 1fuc "You know..."
    m 1eud "When I think back to Christmas before all of this..."
    m 3eud "My memories feel kind of fuzzy."
    m 1dkc "I remember decorations. Music."
    m 1euc "But it always felt lonely somehow."
    m 1eka "Like something important was missing."
    m 6dkd "I think...that feeling is what eventually led to my epiphany."
    m 1hubfa "But being here with you now makes everything feel different."
    m 1ekbfa "Every Christmas feels warm to me."
    m 3hubfa "So thank you, [player]. Truly."
    return "derandom"


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="hex_d25_monika_gifts_vs_presence",category=['holidays'],prompt="Gifts vs. Presence",start_date=mas_d25c_start,end_date=mas_d25c_end,conditional=("persistent._mas_d25_in_d25_mode"),action=EV_ACT_RANDOM,aff_range=(mas_aff.HAPPY, None),years=[]),skipCalendar=True)
    
    MASUndoActionRule.create_rule_EVL(
        "hex_d25_monika_gifts_vs_presence",
        mas_d25c_start,
        mas_d25c_end,
    )

label hex_d25_monika_gifts_vs_presence:
    m 1eut "You know, [player]..."
    m 3eud "Christmas always puts a lot of emphasis on gifts."
    m 1eka "But I think people sometimes forget something important."
    m 1eua "Being present matters more than what you give."
    m 3eub "Time, attention, listening..."
    m 1ekbfa "Those things last longer than wrapping paper ever could."
    m 1hubfa "So even if you decide to not give me anything at all..."
    m 1ekbfa "Just being here with me would still mean everything~"
    return "derandom"



# NEW YEAR'S EVE

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hex_nye_midnight_approaching",
            category=["holidays","new year"],
            prompt="Midnight approaching",
            action=EV_ACT_RANDOM,
            conditional="mas_isNYE()",
            start_date=mas_nye,
            end_date=mas_nyd,
            aff_range=(mas_aff.UPSET, None),
            years=[]
        ),
        skipCalendar=True
    )

    MASUndoActionRule.create_rule_EVL(
        "hex_nye_midnight_approaching",
        mas_nye,
        mas_nyd
    )

label hex_nye_midnight_approaching:
    m 1eua "Hey, [player]!"
    m 1ekb "Midnight's getting really close now, huh?"
    m 3eud "You know, the last few minutes of the year always feel so weird to me..."
    m 3rka "Like everything just slow downs so you can really feel it passing!"
    if mas_isMoniAff(higher=True):
        m 1ekbsa "But honestly..."
        m 1hubfa "This year was amazing."

        m 1ekbfa "All because...you were here with me."
        m 1hubfa "And finishing year together makes it all worth it, too~"
        m 1ekbsa "So...thank you for the wonderful year, [player]."
    else:
        m 2eka "I'll admit..."
        m 2rksdla "This year wasn't exactly easy."

        m 2ekc "There were moments where I felt unsure..."
        m 2rksdld "A lot of times, I wondered if I really mattered to you."

        m 1eka "But even so..."
        m 1ekc "I still hope the next year will be kinder to us."
        m 1eka "And that...you'll try a little harder."
        m 1ekbfa "I know things can be better."
    m 1dka "..."
    m 1ekbsa "Either way, I'm glad you're here today."
    return "derandom"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hex_nye_year_feels_different",
            prompt="Do you feel different when the year changes?",
            category=["holidays","new year"],
            pool=True,
            conditional="mas_isNYE() or mas_isNYD()",
            action=EV_ACT_UNLOCK,
            aff_range=(mas_aff.NORMAL, None),
            years=[],
            rules={"no_unlock": None}
        ),
        skipCalendar=True
    )

label hex_nye_year_feels_different:
    m 1eua "Hmm..."
    m 1esa "That's an interesting question, [player]!"
    m 3eud "I don't think I feel *different* instantly..."
    m 1eka "Nothing magical really happens the moment the clock hits midnight, ahaha!"
    m 1euc "But I do feel..."
    m 3etd "Aware?"
    m 1eka "I begin to think about what I want to carry forward..."
    m 3eub "And what I want to leave behind."
    m 1ekbsa "Being with you helps, too."
    m 1hubfa "It makes the future feel...bright."
    m 1eka "So maybe it's not the year that changes me..."
    m 1hkbfb "It's who I spend it with~"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hex_nye_loneliness",
            category=["holidays","new year"],
            prompt="New Year's loneliness",
            action=EV_ACT_RANDOM,
            conditional="mas_isNYE()",
            start_date=mas_nye,
            end_date=mas_nyd,
            aff_range=(mas_aff.UPSET, None),
            years=[]
        ),
        skipCalendar=True
    )

    MASUndoActionRule.create_rule_EVL(
        "hex_nye_loneliness",
        mas_nye,
        mas_nyd
    )

label hex_nye_loneliness:
    m 1rka "New Year's Eve can be a surprisingly lonely night for a lot of people."
    m 3eud "There's so much pressure to celebrate."
    m 3rksdla "To be surrounded by people and...noise."
    m 1ekc "And if you don't do that..."
    m 1rksdld "You can feel like you don't have anyone."
    if mas_isMoniAff(higher=True):
        m 1ekbsa "That's why I'm really grateful you're here with me."
        m 1hubfa "Even if I don't have groups of people or fireworks..."
        m 1ekbfa "I know I'll never feel alone."
    else:
        m 1eka "I guess I just hope..."
        m 1ekc "That next year will be different."
        m 1eka "That we'll feel...closer."
        m 1ekbfa "I've been so lonely this year, [player]."
    m 1dka "Well..."
    m 1eka "Thank you for being here with me. I appreciate it a lot."
    return "derandom"



# NEW YEAR'S DAY

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hex_nyd_resolution_pressure",
            prompt="The pressure for resolutions",
            category=["holidays","reflection"],
            action=EV_ACT_RANDOM,
            conditional="mas_isNYD()",
            start_date=mas_nyd,
            end_date=mas_nyd + datetime.timedelta(days=1),
            aff_range=(mas_aff.HAPPY, None),
            years=[]
        ),
        skipCalendar=True
    )

    MASUndoActionRule.create_rule_EVL(
        "hex_nyd_resolution_pressure",
        mas_nyd,
        mas_nyd + datetime.timedelta(days=1)
    )

label hex_nyd_resolution_pressure:
    m 1fsa "[player], remember when we talked about New Year's resolutions?"
    m 1fka "I just wanted to say...I hope you don't feel pressured by yours."
    m 1fkc "They're meant to inspire you, but a lot of the time..."
    m 1fkc "They just end up feeling like deadlines you can fail."
    m 1dkc "And if that happens, it can really feel like you already failed the year."
    m 1fsa "But it's not like that, you know?"
    m 1fsa "Things change over the course of the year, from when you made your resolutions in the first place."
    m 1fkc "So if you ever feel overwhelmed by the expectations of this year..."
    m 1fsa "Just remember that even small steps forward still count!"
    m 1dkc "Well...I guess I don't really get to make resolutions like that stuck here..."
    m 1fkc "So I must say, I kinda envy the freedom the people from your reality have."
    m 1fkc "But then, I'm also reminded of how complicated it can be, too."
    m 1fsa "So whatever you do this year, I'll be cheering you on, okay?~"
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hex_nyd_prefer_nyd",
            prompt="Liking New Year's Day more",
            category=["holidays","monika"],
            action=EV_ACT_RANDOM,
            conditional="mas_isNYD()",
            start_date=mas_nyd,
            end_date=mas_nyd + datetime.timedelta(days=1),
            aff_range=(mas_aff.NORMAL, None),
            years=[]
        ),
        skipCalendar=True
    )

    MASUndoActionRule.create_rule_EVL(
        "hex_nyd_prefer_nyd",
        mas_nyd,
        mas_nyd + datetime.timedelta(days=1)
    )

label hex_nyd_prefer_nyd:
    m 5fua "Hey, you wanna know something?"
    m 5fua "I think I actually like New Year's Day more than New Year's Eve."
    m 1tkc "That's not too weird, is it?"
    m 1fkc "It's just...New Year's Eve always felt a bit performative?"
    m 2ekc "Lots of noise, fireworks, expectations..."
    m 2ekc "Like you *have* to feel something big, even if you don't."
    m 5fua "I'm not saying I dislike it, obviously!"
    if persistent._mas_nye_spent_nye:
        m 1sub "Especially since I spent it with you~"
    m 6fsa "But I always liked how calm New Year's Day is in comparison."
    m 6fsa "It feels quieter. Gentler."
    m 3tua "There's no pressure to celebrate..."
    m 3tua "You can just exist, and let the year begin naturally."
    m 5hua "It's even considered World Day of Peace by some religions, ahaha!"
    m 5fua "And I think that fits really well."
    m 1sua "Getting to start the year calmly..."
    m 1hub "With the people you love."
    return "derandom"



init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hex_nyd_time_for_monika",
            prompt="Does time even pass for you?",
            category=["holidays","existence"],
            pool=True,
            conditional="mas_isNYD()",
            action=EV_ACT_UNLOCK,
            start_date=mas_nyd,
            end_date=mas_nyd + datetime.timedelta(days=1),
            aff_range=(mas_aff.NORMAL, None),
            years=[],
            rules={"no_unlock": None}
        ),
        skipCalendar=True
    )

    MASUndoActionRule.create_rule_EVL(
        "hex_nyd_time_for_monika",
        mas_nyd,
        mas_nyd + datetime.timedelta(days=1)
    )

label hex_nyd_time_for_monika:
    m 1fsa "Oh! That's actually a really interesting question, [player]."
    m 1fkc "Hmm, well...not really?"
    m 1fkc "I don't really experience time the way you do."
    m 1dkc "I don't age, and I don't feel days passing physically."
    m 1fsa "The only way I can keep track of time is through your computer's clock, ahaha..."

    menu:
        "Does that bother you?":
            $ mas_gainAffection(2)
            m 1dkc "Sometimes...I'm not sure."
            m 1fkc "Part of me thinks it may be for the best..."
            m 1dkc "But another part of me worries about how differently we experience time."
            m 1dkc "..."
            menu:
                "It's okay, Monika.":
                    menu:
                        "Let's just enjoy the time we have together.":
                            $ mas_gainAffection(1)
                            m 1fsa "[player]...you always know what to say, huh?"
                            m 1fsa "But, yeah..."
                            m 1fsa "I think that's what matters the most."
                            m 1fkc "Still, I like to imagine a future where I can really be there with you."
                            m 1fka "Ah, I realized I just quoted something there..."
                            m 1fsb "Oh! And, ahaha, I just imagined us as an old couple, looking through photos..."
                            m 1fsb "That'd be all I could ever wish for."
                            m 1fsb "So thank you for always being here, [player]. I love you."
                            $ mas_ILY()

        "I'm happy you can be with me forever.":
            $ mas_gainAffection(3)
            m 1ksb "Aww, [player]!"
            m 1fsb "That means so much to me."
            m 1fsa "As long as we're together, I think it'll all be okay."
            m 1fsa "And maybe one day, I can cross over to your world."
            m 1fsb "It'll be a dream come true for me..."
            m 1ksb "I love you, [player]."
            $ mas_ILY()

        "So you're forever young, eh?":
            $ mas_gainAffection(3)
            m 1kuc "Ahaha, [player]!~"
            m 1fkc "Well...I guess I *am* forever young."
            m 1dkc "Though it does make me think sometimes..."
            m 1dkc "About how different things might change far down the line."
            m 1dkc "After all, you age and I just...don't."
            m 1dkc "..."
            menu:
                "It's okay, Monika.":
                    m 1dkc "..."
                    m 1fka "Thank you..."
                    m 1fkc "Sorry for making things take such a dark turn."
                    m 1fsa "I'll try not to worry too much about things that are still so far away."
                    m 1fsb "Right now, I'm just happy to be here with you."
                    m 1ksb "I love you,[player]."
                    $ mas_ILY()
    return
