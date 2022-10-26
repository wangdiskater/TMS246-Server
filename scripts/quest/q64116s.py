# id 64116 ([MONAD: The First Omen] Shabby Armor), field 867202300
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400601) # Elva
sm.sendNext("I was just helping Granny Sanaan make some armor. ")
sm.setInnerOverrideSpeakerTemplateID(9400586) # Sanaan
sm.sendSay("I wouldn't say make, dear. We're more mending. Taking old pieces and putting them together into new armor. ")
sm.setParam(57)
sm.sendSay("#bArmor? ")
sm.setParam(37)
sm.sendSay("Yes, I know someone who's in desperate need of some armor. ")
sm.sendSay("You know who. It's that little nuisance I was telling you about earlier. ")
res = sm.sendNext("While we're on the topic of armor... do you have any extra lying around that you're not using? I need something to cover the arm here...#b\r\n#L0# I don't have anything.#l\r\n#L1# Let me check... #l")
sm.sendNext("Oh, well, that's too bad...")
sm.sendSay("It needs some finishing touches... What do you think? ")
sm.sendSay("Armorsmithing isn't my specialty, but it should work better than it looks. ")
sm.sendSay("He's a lot like me. ")
sm.sendSay("I'm hoping this armor will give the boy the courage to venture outside... But I suppose it's up to him in the end. ")
sm.sendSay("Still, it's always better to do what little you can than do nothing at all. ")
sm.sendSay("Here, take a look at this helmet! I'm rather proud of the horns here. ")
sm.setParam(57)
sm.sendSay("#bImpressive. ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400601) # Elva
sm.sendSay("I can imagine Einar striding out of his house wearing this. Magnificent! ")
sm.setInnerOverrideSpeakerTemplateID(9400586) # Sanaan
sm.sendSay("I hope he's ready for magnificence... ")
sm.setInnerOverrideSpeakerTemplateID(9400601) # Elva
sm.sendSay("I'm sure he'll... Hey, what is that noise? What's going on? ")
sm.setInnerOverrideSpeakerTemplateID(9400586) # Sanaan
sm.sendSay("Sounds to me like someone's getting a bit rowdy. ")
sm.setParam(57)
sm.sendSay("#bWe'd better head over and check it out. ")
sm.setParam(37)
sm.sendSay("Yes, let's go.")
sm.sendSay("Ah, before we go... This is for you. It's nothing compared to what you're wearing, but humor an old woman and take it.")
sm.playExclSoundWithDownBGM("Field.img/masteryBook/EnchantSuccess", 100)
sm.completeQuestNoCheck(parentID)
sm.warp(867202305)