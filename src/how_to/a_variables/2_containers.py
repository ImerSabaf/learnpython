"""
Advanced types : containers
"""

# 1/ list
THINGS = ["things_a", "things_b", "things_c"]
FOO = [True, 3.14, THINGS]  # this is a list in a list !
CONCATENATE = THINGS + FOO

print(FOO[1])
print(CONCATENATE)

# 2/ tuple : immutable list
MY_TUPLE = ("Othello", "Iago")
print(MY_TUPLE)

# 3/ dictionaries
CHARACTERS = {
    "villain": "Roderigo",
    "hero": "Othello",
    "friend": "Cassio",
    "beauty": "Desdemona",
}

print(CHARACTERS.get("friend"))
