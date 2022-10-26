# id 100051034 (Partem : Wawa Falls), field 100051034
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.zoomCamera(0, 1500, 0, 100, -200)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.sendDelay(300)
sm.zoomCamera(4500, 1500, 4500, -280, 45)
sm.createFieldTextEffect("#fnArial##fs18#Wawa Falls", 100, 1000, 6, -50, -50, 1, 4, 0, 0, 0)
sm.sendDelay(4500)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(1013350) # Brie
sm.sendNext("#face0#Hmm... This is weird. We've combed through the Creepy Crawly Copse, but I haven't seen that last compass part anywhere. Where could it be hiding?")
sm.sendSay("#face0#Maybe Gorgonz only thought he saw the third compass piece fall here. But if it's not here, where do you think it could be?")
sm.sendDelay(300)
sm.zoomCamera(1000, 1500, 1000, -150, 45)
sm.forcedMove(False, 190)
sm.sendDelay(2500)
sm.setParam(549)
sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
sm.sendNext("#face0##b(A glint in the water catches your eye, and you approach to take a closer look. Upon gazing in, you can faintly see the final part of the broken compass lying on the bottom of the river.)#k")
sm.sendSay("#face1#Well, this complicates things. The last part's down there.")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(1013350) # Brie
sm.sendSay("#face0#Ugh. Really?")
sm.sendSay("#face0#You're right. From what I can make out, the pattern looks the same as the others we've picked up.")
sm.sendSay("#face0#Sooo... Do you have any good ideas about how to fish it out? The current here is stronger than it looks, so diving in ourselves would be dangerous.")
sm.setParam(549)
sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
sm.sendSay("#face3##b(You dip your hand into the surging waters for a moment, feeling the churn of the current around your fingers. Begrudgingly, you admit it would be risky for you to try to recover it yourself.)#k")
sm.sendDelay(1000)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(1013350) # Brie
sm.sendNext("#face0#If only we could make the waterfall stop, just for a moment.")
sm.forcedMove(True, 1)
sm.sendDelay(300)
sm.setParam(549)
sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
sm.sendNext("#face0#Stop the waterfall? You think it's actually possible?")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(1013350) # Brie
sm.sendSay("#face1#O-oh no... Me and my big mouth. I'm sorry, I just blurted it out. I don't even know how we could manage something like that.")
sm.setParam(549)
sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
sm.sendSay("#face6#(If all I need is a minute or so, I think I might be able to pull it off. I could knock a big boulder into the stream and stop up the flow for a bit...)")
sm.sendSay("#face6#(Of course, I'd need some explosives to make that happen, and wouldn't you know it, I forgot my dynamite in my OTHER pants. Guess I'll just have to compound an explosive using what I can find in the field.)")
sm.sendSay("#face0#Actually...")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(1013350) # Brie
sm.sendSay("#face1#*sniff*... Y-yes?")
sm.setParam(549)
sm.setInnerOverrideSpeakerTemplateID(1013358) # Pathfinder
sm.sendSay("#face0#Is there anything around here I could use to make an explosive?")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(1013350) # Brie
sm.sendSay("#face0#What would you need that for? ...Wait, you figured out a way, didn't you? Let's see. Something explosive...")
sm.sendDelay(1000)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.createQuestWithQRValue(35947, "12=1;16=1;2=1;6=1")