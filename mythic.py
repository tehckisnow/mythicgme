import random
import sys

def menu():
    print("""
    What would you like to know?
    1. Oracle
    2. Event
    3. Location
    4. Creature
    5. NPC
    6. NPC(Binary question)
    7. NPC(Conversation)
    8. Dice
    9. Exit
    """)
    usrchoice = input(">")
    #print(usrchoice + " selected")
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
        NPCbin()
        menu()
    elif usrchoice == "7":
        npcdiscussion()
        menu()
    elif usrchoice == "8":
        dice()
    elif usrchoice == "9":
        sys.exit(0)
    else:
        print("Shiggity Schwa?")
        menu()

def likely():
    print("""
    How Likely?
    1. 50/50
    2. Very likely
    3. Very unlikely
    4. Almost certainty
    5. Nearly impossible
    """)
    likely = input(">")
    d100 = random.randint(1, 100)
    print(d100)
    if d100 == 11:
        print("Random Event")
        event()
    elif d100 == 22:
        print("Random Event")
        event()
    elif d100 == 33:
        print("Random Event")
        event()
    elif d100 == 44:
        print("Random Event")
        event()
    elif d100 == 55:
        print("Random Event")
        event()
    elif d100 == 66:
        print("Random Event")
        event()
    elif d100 == 77:
        print("Random Event")
        event()
    elif d100 == 88:
        print("Random Event")
        event()
    elif d100 == 99:
        print("Random Event")
        event()
    if likely == "1":
        if d100 < 51:
            print("Yes.")
        elif d100 > 50:
            print("No.")
    elif likely == "2":
        if d100 < 76:
            print("Yes.")
        elif d100 > 75:
            print("No.")
    elif likely == "3":
        if d100 < 26:
            print("Yes.")
        elif d100 > 25:
            print("No.")
    elif likely == "4":
        if d100 < 91:
            print("Yes.")
        elif d100 > 90:
            print("No.")
    elif likely == "5":
        if d100 < 11:
            print("Yes.")
        elif d100 > 10:
            print("No.")

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

def creature():
    typelst=["alien", "animal", "animated", "elemental", "humanoid", "supernatural beast", "amorphous", "plant", "undead", "insect"]
    potencylst=["minimum(-75%)", "weak(-50%)", "less(-10%)", "baseline average", "more(+10%)", "stronge(+50%)", "maximum(+100)"]
    sizelst=["tiny", "small", "human-sized", "large" "very horns/antlers", "gm decisionlarg.e", "gigantic"]
    numberoflst=["1", "2", "3", "4", "5", "6 or more"]
    abilitylst=["no special ability", "gaze attack", "resist damage", "burst of speed", "flight", "swim", "enhanced sense", "concealment", "paralysis", "natural weaponry", "climber", "poison", "charge", "distraction", "entangle", "specific vulnerability", "unusual sense", "extra defense", "telepathy", "limited use", "grievous attack", "summon", "immunity", "tunnelling", "targeted attack", "meta power", "ranged attack", "alternate form of travel", "frightening", "life force drain", "fast healing", "attribute damage", "dual classification", "defensive perimeter", "incorporeal", "animate", "multi-enironment", "tranformation"]
    alienlst=["fishlike", "stinky", "tentacled", "roll on animal table", "extra limbs", "clothed", "nightmarish", "multi-eyed", "dripping", "roll on beast table", "levitating", "insectlike", "roll on insect table", "wormlike", "humanoid looking", "bony", "odd colored", "serpent-like", "aquatic", "gm decision"]
    animallst=["furry", "clawed", "sharp teeth", "tail", "long haired", "ugly", "bird-like", "odd color", "growling", "hopping", "tusks", "hooves", "mammalian", "spotted", "reptilian", "aquatic", "amphibious", "winged", "horns/antlers", "gm decision"]
    animatedlst=["humanoid", "roll on humanoid table", "made of wood", "made of stone", "inscribed with symbols", "exudes steam or smoke", "made of common item(s)", "looks like an animal", "roll on animal table", "roll on insect table", "made of unusual substance", "wields a weapon", "glowing eyes", "noisy", "made of metal", "falling apart, in ill repair", "shape changing", "levitating", "robotic", "gm decision"]
    elementallst=["air-based", "roll on alien table", "roll on human table", "fire based", "roll on amorphous table", "cloud like", "water-based", "levitating/flying", "roll on animated table", "earth-based", "earth-based", "unusual substance", "humanoid", "flowing shape", "olid", "clawed", "water-based", "liquid", "composed of small items", "gm decision"]
    humanoidlst=["very ugly", "roll on animal table", "roll on sup. beast table", "toothy", "primitive", "tusks", "pointed ears", "fine features", "crude clothing", "wielding a weapon", "wearing armor", "horned", "roll on alien table", "odd skin color", "very intelligent", "dumb", "reptillian", "tall", "beautiful", "gm decision"]
    beastlst=["roll on animal table", "roll on alien table", "roll on elemental table", "roll on insect table", "sharp teeth", "glowing eyes", "combo of animals", "winged", "horned", "bird-like", "mammalian", "reptillian", "aquatic", "tall", "multiple eyes", "tentacles", "odd colored", "extra limbs", "furry", "gm decision"]
    amorphouslst=["liquid", "roll on elemental table", "amorphous", "multiple eyes", "clingy/sticky", "tentacles", "bubbling", "cloud-like", "transparent", "floating/levitating", "inky black", "green", "purple", "brown", "blob-like", "shape shifts", "forms a simple shape", "pulsating", "wall-crawling", "gm decision"]
    plantlst=["tree-like", "vines/tentacles", "roll on amorphous table", "mushroom-like", "covered in needles", "colorful", "aquatic", "toothy maw", "flowered", "rooted in the ground", "an fly/float", "humanoid shape", "collection of smaller plants", "covered wth leaves", "stinks", "ambulatory legs", "moving roots", "coated in bark", "fungus", "gm decision"]
    undeadlst=["decayed", "skeletal", "insubstantial", "shadowy", "cold", "roll on humanoid table", "foul smelling", "silent", "filthy", "looks alive", "roll on animal table", "twisted human", "mummified", "glowing eyes", "howling/growling", "claws", "fangs", "ghoulish", "gaunt", "gm decision"]
    insectlst=["insect-like", "roll on alien table", "carapace", "bug-like", "furry", "mandibles", "multiple legs", "worm-like", "humanoid", "pincers/claws", "wall-crawling", "eyes on stalks", "multiple eyes", "aquatic", "spider-like", "agile", "winged", "odd-colored", "has a stinger", "gm decision"]

    ln0 = len(typelst)-1
    ln1 = len(potencylst)-1
    ln2 = len(sizelst)-1
    ln3 = len(numberoflst)-1
    ln4 = len(abilitylst)-1
    ln5 = len(alienlst)-1
    ln6 = len(animallst)-1
    ln7 = len(animatedlst)-1
    ln8 = len(elementallst)-1
    ln9 = len(humanoidlst)-1
    ln10 = len(beastlst)-1
    ln11 = len(amorphouslst)-1
    ln12 = len(plantlst)-1
    ln13 = len(undeadlst)-1
    ln14 = len(insectlst)-1

    rndtype = random.randint(0, ln0)
    rndpotency = random.randint(0, ln1)
    rndsize = random.randint(0, ln2)
    rndnumberof = random.randint(0, ln3)
    rndability = random.randint(0, ln4)
    rndalien = random.randint(0, ln5)
    rndanimal = random.randint(0, ln6)
    rndanimated = random.randint(0, ln7)
    rndelemental = random.randint(0, ln8)
    rndhumanoid = random.randint(0, ln9)
    rndbeast = random.randint(0, ln10)
    rndamorphous = random.randint(0, ln11)
    rndplant = random.randint(0, ln12)
    rndundead = random.randint(0, ln13)
    rndinsect = random.randint(0, ln14)

    print("-")
    print("type: " + typelst[rndtype])
    print("potency: " + potencylst[rndpotency])
    print("size: " + sizelst[rndsize])
    print("numbering: " + numberoflst[rndnumberof])
    print("ability: " + abilitylst[rndability])
    desc = typelst[rndtype]
    if desc == "alien":
        print("description: " + alienlst[rndalien])
        rndalien = random.randint(0, ln5)
        print(alienlst[rndalien])
    elif desc == "animal":
        print("description: " + animallst[rndanimal])
        rndanimal = random.randint(0, ln6)
        print(animallst[rndanimal])
    elif desc == "animated":
        print("description: " + animatedlst[rndanimated])
        rndanimated = random.randint(0, ln7)
        print(animatedlst[rndanimated])
    elif desc == "elemental":
        print("description: " + elementallst[rndelemental])
        rndelemental = random.randint(0, ln8)
        print(elementallst[rndelemental])
    elif desc == "humanoid":
        print("description: " + humanoidlst[rndhumanoid])
        rndhumanoid = random.randint(0, ln9)
        print(humanoidlst[rndhumanoid])
    elif desc == "supernatural beast":
        print("description: " + beastlst[rndbeast])
        rndbeast = random.randint(0, ln10)
        print(beastlst[rndbeast])
    elif desc == "amorphous":
        print("description: " + amorphouslst[rndamorphous])
        rndamorphous = random.randint(0, ln11)
        print(amorphouslst[rndamorphous])
    elif desc == "plant":
        print("description: " + plantlst[rndplant])
        rndplant = random.randint(0, ln12)
        print(plantlst[rndplant])
    elif desc == "undead":
        print("description: " + undeadlst[rndundead])
        rndundead = random.randint(0, ln13)
        print(undeadlst[rndundead])
    elif desc == "insect":
        print("description: " + insectlst[rndinsect])
        rndinsect = random.randint(0, ln14)
        print(insectlst[rndinsect])

def npc():
    mod=["superfluous", "addicted", "conformist", "nefarious", "sensible", "untrained", "romantic", "unreasonable", "skilled", "neglectful", "lively", "forthright", "idealistic", "unsupportive", "rational", "course", "foolish", "cunning", "delightful", "miserly", "inept", "banal", "logical", "subtle", "reputable", "wicked", "lazy", "pessemistic", "solemn", "habitual", "meek", "helpful", "unconcerned", "generous", "docile", "cheery", "pragmatic", "serene", "thoughtful", "hopeless", "pleasant", "insensitive", "inexperienced", "prying", "oblivious", "refined", "indispensible", "scholarly", "conservative", "uncouth", "willful", "indifferent", "fickle", "elderly", "sinful", "naive", "privileged", "glum", "likable", "lethargic", "defiant", "obnoxious", "insightful", "tactless", "fanatic", "plebian", "childish", "pious", "uneducated", "inconsiderate", "cultured", "revolting", "curious", "touchy", "needy", "dignified", "pushy", "kind", "corrupt", "jovial", "shrewd", "liberal", "compliant", "destitute", "conniving", "careful", "alluring", "defective", "optimistic", "affluent", "despondent", "mindless", "passionate", "devoted", "established", "unseemly", "dependable", "righteous", "confident"]
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
    print("NPC: " + mod[rndmod] + " " + noun[rndnoun])
    print("power level: " + pwrlvl[rndpwrlvl])
    print("motivation: " + motive[rndmotive] + " " + motivnoun[rndmotivnoun])

def NPCbin():
    ##              withdrawn   guarded     cautious     neutral        sociable    helpful     forthcoming
    reactions = [[[5, 30, 87], [9, 45, 90], [12, 60, 93], [15, 75,95], [18, 81, 96], [21, 88, 97], [25, 95, 99]],   #loved
                 [[4, 25, 85], [8, 38, 88], [10, 51, 91], [13, 64, 93], [16, 73, 94], [19, 82, 96], [23, 91, 98]],  #friendly
                 [[4, 21, 83], [7, 33, 86], [9, 45, 89], [11, 56, 91], [14, 65, 93], [17, 76, 95], [21, 87, 98]],   #peaceful
                 [[3, 17, 81], [6, 28, 84], [8, 39, 87], [10, 50, 90], [13, 61, 92], [16, 72, 94], [19, 83, 97]],   #neutral
                 [[2, 13, 79], [5, 24, 83], [7, 35, 86], [9, 44, 89], [11, 55, 91], [14, 67, 93], [17, 79, 96]],    #distrustful
                 [[2, 9, 77], [4, 18, 81], [6, 27, 84], [7, 36, 87], [9, 49, 90], [12, 62, 92], [15, 75, 96]],      #hostile
                 [[1, 5, 75], [3, 12, 79], [4, 19, 82], [5, 25, 85], [7,40,88], [10, 55, 91], [13, 70, 95]]]        #hated
    print("Relationship to NPC?")
    print("""
    1. loved
    2. friendly
    3. peaceful
    4. neutral
    5. distrustful
    6. hostile
    7. hated
    """)
    try:
        rel=int(input(">"))-1
        print("Mood of NPC?")
        print("""
    1. withdrawn
    2. guarded
    3. cautious
    4. neutral
    5. sociable
    6. helpful
    7. forthcoming
        """)
        mood=int(input(">"))-1
        odds=reactions[rel][mood]
        low, med, high = 0,1,2
        d100 = random.randint (1, 100)
        print("d100: ", d100)
        if d100 <= odds[low]:
            print("Strong yes!")
        elif d100 <= odds[med]:
            print("Yes.")
        elif d100 >= odds[high]:
            print("Strong no!")
        elif d100 > odds[med]:
            print("No.")
    except(ValueError):
        print("Please enter a value between 1 and 7")
        NPCbin()

def npcdiscussion():
    bearing=["scheming", "intent", "bargain", "means", "proposition", "plan", "compromise", "agenda", "arrangement", "negotiation", "plot", "inquisitive", "questions", "investigation", "interest", "demand", "suspicion", "request", "curiosity", "skepticism", "command", "petition", "insane", "madness", "fear", "accident", "chaos", "idiocy", "illusion", "turmoil", "confusion", "façade", "bewilderment", "knowing", "report", "effects", "examination", "records", "account", "news", "history", "telling", "discourse", "speech", "friendly", "alliance", "comfort", "gratitude", "shelter", "happiness", "support", "promise", "delight", "aid", "celebration", "mysterious", "rumor", "uncertainty", "secrets", "misdirection", "whispers", "lies", "shadows", "enigma", "obscurity", "conundrum", "hostile", "death", "capture", "judgment", "combat", "surrender", "rage", "resentment", "submission", "injury", "destruction", "prejudiced", "reputation", "doubt", "bias", "dislike", "partiality", "belief", "view", "discrimination", "assessment", "difference"]
    focus=["current scene", "parents", "wealth", "skills", "campaign", "allies", "flaws", "experience", "community", "current story", "weapons", "last story", "history", "relics", "superiors", "future action", "last scene", "antagonist", "knowledge", "treasure", "family", "previous scene", "equipment", "retainers", "last action", "fame", "friends", "contacts", "rewards", "recent scene", "the character", "power", "enemy"]

    ln0 = len(bearing)-1
    ln1 = len(focus)-1

    rndbearing = random.randint(0, ln0)
    rndfocus = random.randint(0, ln1)
    print(bearing[rndbearing] + " " + focus[rndfocus])

def dice():
    d10 = random.randint(1, 10)
    d10a = random.randint(1, 10)
    d10b = random.randint(1, 10)
    d20 = random.randint(1, 20)
    d100 = random.randint(1, 100)
    print("1D10:",d10," 2D10:",d10a+d10b," D20:",d20," 1D100:",d100)
    menu()

menu()

##Things to add
##location charts
