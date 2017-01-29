import random
print("Mythic GME")
d10 = random.randint (1, 100)
print("Oracle:",d10)
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

#d10 = random.randint (0, ln0)     #this is how I originally coded the lines above, resetting a single rng each time
#print(eventfocus[d10])
#d10 = random.randint (0, ln1)
#print(action[d10])
#d10 = random.randint (0, ln2)
#print(subject[d10])
#this is an arbitrary change to test branching
