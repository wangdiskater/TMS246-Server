# id 34656 (First Fighting Tactic, 1st job cadena advancement), field 402000001
sm.setSpeakerID(3001200)
if chr.getJob() == 6002:
    sm.sendNext("The treatment worked well for you, which means you're ready to learn Shadowdealer skills and techniques. Welcome to the branch.")
    sm.sendSay("You've done well as my apprentice. You're strong, and you have incredible talent for combat. Keep practicing the techniques I've shown you, and you'll get even stronger.")
    sm.setJob(6400)
    sm.setSTR(4)
    sm.setINT(4)
    sm.setDEX(4)
    sm.setLUK(4)
    sm.setAP(4 + chr.getLevel() * 5)
    sm.addSP(3)
    sm.addMaxHP(350)
    sm.addMaxMP(200)
    sm.giveAndEquip(1353300)
    sm.completeQuestNoCheck(parentID)