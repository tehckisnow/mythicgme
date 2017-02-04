import random
import sys

def roll():
    d100 = random.randint(1, 100)
    print(d100)
    if d100 == 11:
        print("Random Event")
    elif d100 == 22:
        print("Random Event")
    elif d100 == 33:
        print("Random Event")
    elif d100 == 44:
        print("Random Event")
    elif d100 == 55:
        print("Random Event")
    elif d100 == 66:
        print("Random Event")
    elif d100 == 77:
        print("Random Event")
    elif d100 == 88:
        print("Random Event")
    elif d100 == 99:
        print("Random Event")
    return

def menu():
    print("""
    What would you like to know?
    1. Oracle
    2. Event
    3. Location
    4. Creature
    5. NPC
    6. Exit
    """)
    usrchoice = input(">")
    print(usrchoice + " selected")
    if usrchoice == "1":
        likely()
        menu()
    elif usrchoice == "2":
        event()
        menu()
    elif usrchoice == "3":
        location()
        menu()
    elif usrchoice == "4":
        creature()
        menu()
    elif usrchoice == "5":
        npc()
        menu()
    elif usrchoice == "6":
        sys.exit(0)
    else:
        print("Shiggity Schwa?")
        menu()
    return

def likely():
    d100 = random.randint (1, 100)
    print("""
    How Likely?
    1. 50/50
    2. Very likely
    3. Very unlikely
    """)
    likely = input(">")
    if likely == "1":
        roll()
        if d100 < 51:
            print("Yes.")
        elif d100 > 50:
            print("No.")
    elif likely == "2":
        roll()
        if d100 < 76:
            print("Yes.")
        elif d100 > 75:
            print("No.")
    elif likely == "3":
        roll()
        if d100 < 26:
            print("Yes.")
        elif d100 > 25:
            print("No.")
    return

def event():
    d100 = random.randint (1, 100)
    eventfocus=["remote event", "remote event", "remote event", "remote event", "remote event", "remote event", "remote event", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "NPC action", "New NPC", "New NPC", "New NPC", "New NPC", "New NPC", "New NPC", "New NPC", "Move toward a thread", "Move toward a thread", "Move toward a thread", "Move toward a thread", "Move toward a thread", "Move toward a thread", "Move toward a thread", "Move toward a thread", "Move toward a thread", "Move toward a thread", "Move away from a thread", "Move away from a thread", "Move away from a thread", "Move away from a thread", "Move away from a thread", "Move away from a thread", "Move away from a thread", "Close a thread", "Close a thread", "Close a thread", "PC negative", "PC negative", "PC negative", "PC negative", "PC negative", "PC negative", "PC negative", "PC negative", "PC negative", "PC negative", "PC negative", "PC negative", "PC Positive", "PC Positive", "PC Positive", "PC Positive", "PC Positive", "PC Positive", "PC Positive", "PC Positive", "Ambiguous event", "Ambiguous event", "Ambiguous event", "Ambiguous event", "Ambiguous event", "Ambiguous event", "Ambiguous event", "Ambiguous event", "NPC negative", "NPC negative", "NPC negative", "NPC negative", "NPC negative", "NPC negative", "NPC negative", "NPC negative", "NPC negative", "NPC positive", "NPC positive", "NPC positive", "NPC positive", "NPC positive", "NPC positive", "NPC positive", "NPC positive"]
    action=["attainment", "starting", "neglect", "fight", "recruit", "triumph", "violate", "oppose", "malice", "communicate", "persecute", "increase", "decrease", "abandon", "gratify", "inquire", "antagonize", "move", "waste", "truce", "release", "befriend", "judge", "desert", "dominate", "procrastinate", "praise", "separate", "take", "break", "heal", "delay", "stop", "lie", "return", "imitate", "struggle", "inform", "bestow", "postpone", "expose", "haggle", "imprison", "release", "celebrate", "develop", "travel", "block", "harm", "debase", "overindulge", "adjourn", "adversity", "kill", "disrupt", "usurp", "create", "betray", "agree", "abuse", "oppress", "inspect", "ambush", "spy", "attach", "carry", "open", "carelessness", "ruin", "extravagance", "trick", "arrive", "propose", "divide", "refuse", "mistrust", "deceive", "cruelty", "intolerance", "trust", "excitement", "activity", "assist", "care", "negligence", "passion", "work hard", "control", "attract", "failure", "pursue", "vengeance", "proceedings", "dispute", "punish", "guide", "transform", "overthrow", "oppress", "change"]
    subject=["goals", "dreams", "environment", "outside", "inside", "reality", "allies", "enemies", "evil", "good", "emotions", "opposition", "war", "peace", "the innocent", "love", "the spiritual", "the intellectual", "new ideas", "joy", "messages", "energy", "balance", "tension", "friendship", "the physical", "a project", "pleasures", "pain", "possessions", "benefits", "plans", "lies", "expectations", "legal matters", "bureaucracy", "business", "a path", "news", "exterior factors", "advice", "a plot", "competition", "prison", "illness", "food", "attention", "success", "failure", "travel", "jealousy", "dispute", "home", "investment", "suffering", "wishes", "tactics", "stalemate", "randomness", "misfortune", "death", "disruption", "power", "a burden", "intrigues", "fears", "ambush", "rumor", "wounds", "extravagance", "a representative", "adversities", "opulence", "liberty", "military", "the mundane", "trials", "masses", "vehicle", "art", "victory", "dispute", "riches", "status quo", "technology", "hope", "magic", "illusions", "portals", "danger", "weapons", "animals", "weather", "elements", "nature", "the public", "leadership", "fame", "anger", "information"]
    ln0 = len(eventfocus)-1  ##these lines check the length of their respective lists so I don't have to
    ln1 = len(action)-1      ##
    ln2 = len(subject)-1     ##

    d10a = random.randint (0, ln0)     #rolling all dice before printing so they can be printed on same line below
    d10b = random.randint (0, ln1)
    d10c = random.randint (0, ln2)
    print(eventfocus[d10a])
    print(action[d10b], subject[d10c])
    return

def location():
    typelst=["custom", "expected", "none", "special", "random", "complete"]
    speciallst=["supersize", "barely there", "remove element", "add element", "this is bad", "this is good", "multi-element", "exit here", "return", "going deeper", "common ground", "random element"]
    ln0 = len(typelst)-1  ##these lines check the length of their respective lists so I don't have to
    ln1 = len(speciallst)-1      ##
    print("-")
    d10a = random.randint (0, ln0)     #rolling all dice before printing so they can be printed on same line below
    print("Location: " + typelst[d10a])
    if d10a == 3:
        d10b = random.randint (0, ln1)
        print("*" + speciallst[d10b])
    event()
    print("-")
    d10a = random.randint (0, ln0)
    print("Encounter: " + typelst[d10a])
    if d10a == 3:
        d10b = random.randint (0, ln1)
        print("*" + speciallst[d10b])
    event()
    print("-")
    d10a = random.randint (0, ln0)
    print("objects: " + typelst[d10a])
    if d10a == 3:
        d10b = random.randint (0, ln1)
        print("*" + speciallst[d10b])
    event()
    return

def creature():
    typelst=["alien", "animal", "animated", "elemental", "humanoid", "supernatural beast", "amorphous", "plant", "undead", "insect"]
    potencylst=["minimum(-75%)", "weak(-50%)", "less(-10%)", "baseline average", "more(+10%)", "stronge(+50%)", "maximum(+100)"]
    sizelst=["tiny", "small", "human-sized", "large" "very large", "gigantic"]
    numberoflst=["1", "2", "3", "4", "5", "6 or more"]
    abilitylst=["no special ability", "gaze attack", "resist damage", "burst of speed", "flight", "swim", "enhanced sense", "concealment", "paralysis", "natural weaponry", "climber", "poison", "charge", "distraction", "entangle", "specific vulnerability", "unusual sense", "extra defense", "telepathy", "limited use", "grievous attack", "summon", "immunity", "tunnelling", "targeted attack", "meta power", "ranged attack", "alternate form of travel", "frightening", "life force drain", "fast healing", "attribute damage", "dual classification", "defensive perimeter", "incorporeal", "animate", "multi-enironment", "tranformation"]
    #alienlst=[]
    #animallst=[]
    #animatedlst=[]
    #elementallst=[]
    #humanoid=[]
    #beastlst=[]
    #amorphouslst=[]
    #plantlst=[]
    #undeadlst=[]
    #insectlst=[]

    ln0 = len(typelst)-1
    ln1 = len(potencylst)-1
    ln2 = len(sizelst)-1
    ln3 = len(numberoflst)-1
    ln4 = len(abilitylst)-1

    rndtype = random.randint(0, ln0)
    rndpotency = random.randint(0, ln1)
    rndsize = random.randint(0, ln2)
    rndnumberof = random.randint(0, ln3)
    rndability = random.randint(0, ln4)

    print("-")
    print(typelst[rndtype])
    print(potencylst[rndpotency])
    print(sizelst[rndsize])
    print(numberoflst[rndnumberof])
    print(abilitylst[rndability])
    return

def npc():
    mod=["superfluous", "addicted", "conformist", "nefarious", "sensible", "untrained", "romantic", "unreasonable", "skilled", "neglectful", "lively", "forthright", "idealistic", "unsupportive", "rational", "course", "foolish", "cunning", "delightful", "miserly", "inept", "banal", "logical", "subtle", "reputable", "wicked", "lazy", "pessemistic", "solemn", "habitual", "meek", "helpful", "unconcerned", "generous", "docile", "cheery", "pragmatic", "serene", "thoughtful", "hopeless", "pleasant", "insensitive", "inexperienced", "prying", "oblivious", "refined", "indeispensible", "scholarly", "conservative", "uncouth", "willful", "indifferent", "fickle", "elderly", "sinful", "naive", "privileged", "glum", "likable", "lethargic", "defiant", "obnoxious", "insightful", "tactless", "fanatic", "plebian", "childish", "pious", "uneducated", "inconsiderate", "cultured", "revolting", "curious", "touchy", "needy", "dignified", "pushy", "kind", "corrupt", "jovial", "shrewd", "liberal", "compliant", "destitute", "conniving", "careful", "alluring", "defective", "optimistic", "affluent", "despondent", "mindless", "passionate", "devoted", "established", "unseemly", "dependable", "righteous", "confident"]
    noun=["gypsy", "witch", "merchant", "expert", "commoner", "judge", "ranger", "occultist", "reverend", "thug", "drifter", "journeyman", "statesman", "astrologer", "duelist", "jack-of-all-trades", "aristocrat", "preacher", "artisan", "rogue", "missionary", "outcast", "mercenary", "caretaker", "hermit", "orator", "chieftain", "pioneer", "burglar", "vicar", "officer", "explorer", "warden", "outlaw", "adept", "bum", "sorcerer", "laborer", "master", "ascendant", "villager", "magus", "conscript", "worker", "actor", "herald", "highwayman", "fortune-hunter", "governor", "scrapper", "monk", "homemaker", "recluse", "steward", "polymath", "magician", "traveler", "vagrant", "apprentice", "politician", "mediator", "crook", "civilian", "activist", "hero", "champion", "cleric", "slave", "gunman", "clairvoyant", "patriarch", "shopkeeper", "crone", "adventurer", "soldier", "entertainer", "craftsman", "scientist", "ascetic", "superior", "performer", "magister", "serf", "brute", "inquisitor", "lord", "villain", "professor", "servant", "charmer", "globetrotter", "sniper", "courtier", "priest", "tradesman", "hitman", "wizard", "beggar", "tradesman", "warrior"]
    pwrlvl=["much weaker", "slightly weaker", "slightly weaker", "slightly weaker", "comparable", "comparable", "comparable", "comparable", "comparable", "comparable", "comparable", "comparable", "slightly stronger", "slightly stronger", "slightly stronger", "much stronger"]
    motive=["advise", "obtain", "attempt", "spoil", "oppress", "interact", "create", "abduct", "promote", "conceive", "blight", "progress", "distress", "possess", "record", "embrace", "contact", "pursue", "associate", "prepare", "shepherd", "abuse", "indulge", "chronicle", "fulfill", "drive", "review", "aid", "follow", "advance", "guard", "conquer", "hinder", "plunder", "construct", "encourage", "agonize", "comprehend", "administer", "relate", "take", "discover", "deter", "acquire", "damage", "publicize", "burden", "advocate", "implement", "understand", "collaborate", "strive", "complete", "compel", "join", "assist", "defile", "produce", "institute", "account", "work", "accompany", "offend", "guide", "learn", "persecute", "communicate", "process", "report", "develop", "steal", "suggest", "weaken", "achieve", "secure", "inform", "patronize", "depress", "determine", "seek", "manage", "suppress", "proclaim", "operate", "access", "refine", "compose", "undermine", "explain", "discourage", "attend", "detect", "execute", "maintain", "realize", "convey", "rob", "establish", "overthrow", "support"]
    motivnoun=["wealth", "hardship", "affluence", "resources", "prosperity", "poverty", "opulence", "deprivation", "success", "distress", "contraband", "music", "literature", "technology", "alcohol", "medicines", "beauty", "strength", "intelligence", "force", "the wealthy", "the populous", "enemies", "the public", "religion", "the poor", "family", "the elite", "academia", "the forsaken", "the law", "the government", "the downtrodden", "friends", "criminals", "allies", "secret societies", "the world", "military", "the church", "dreams", "discretion", "love", "freedom", "pain", "faith", "slavery", "enlightenment", "racism", "sensuality", "dissonance", "peace", "discrimination", "disbelief", "pleasure", "hate", "happiness", "servitude", "harmony", "justice", "gluttony", "lust", "envy", "greed", "laziness", "wrath", "pride", "purity", "moderation", "vigilance", "zeal", "composure", "charity", "modesty", "atrocities", "cowardice", "narcissism", "compassion", "valor", "patience", "advice", "propaganda", "science", "knowledge", "communications", "lies", "myths", "riddles", "stories", "legends", "industry", "new religions", "progress", "animals", "ghosts", "magic", "nature", "old religions", "expertise", "spirits"]

    ln0 = len(mod)-1
    ln1 = len(noun)-1
    ln2 = len(pwrlvl)-1
    ln3 = len(motive)-1
    ln4 = len(motivnoun)-1

    rndmod = random.randint(0, ln0)
    rndnoun = random.randint(0, ln1)
    rndpwrlvl = random.randint(0, ln2)
    rndmotive = random.randint(0, ln3)
    rndmotivnoun = random.randint(0, ln4)

    print("-")
    print(mod[rndmod])
    print(noun[rndnoun])
    print("power level: " + pwrlvl[rndpwrlvl])
    print(motive[rndmotive])
    print(motivnoun[rndmotivnoun])
    return

menu()

##Things to add
##NPC binary response and bearing
##location charts
##creature charts
##more mythic liklinesses
##alternative mythic templates?
##"yes, and" or automatically generate events
