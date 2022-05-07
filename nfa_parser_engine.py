from sys import argv
f = open(argv[1], "r")
letters = []
states = []
transitions = []
existaS = 0
ok = 1
for s in f:
    # print(s)
    if s[0] == "#":
        pass
    elif s == "Sigma:\n":
        for letter in f:
            if letter[0]=="#":
                pass
            else:
                if letter == "End\n":
                    break
                letter.strip()
                letters.append(letter[0])
    elif s == "States:\n":
        for line in f:
            if line[0]=="#":
                pass
            else:
                if line == "End\n":
                    break
                state = [x for x in line.strip().split(",")]
                if len(state[len(state)-1])>1:
                    state[len(state) - 1]=state[len(state)-1][0]
                if len(state)==2:
                    if state[1]=='S':
                        if existaS==0:
                            existaS=1
                        else:
                            ok=0
                            break
                if len(state)==3:
                    if state[1]=='S' or state[2]=='S':
                        if existaS==0:
                            existaS=1
                        else:
                            ok=0
                            break
                states.append(state)
    elif s == "Transitions:\n":
        for line in f:
            if line[0]=="#":
                pass
            else:
                if line == "End":
                    break
                transition = [x for x in line.strip().split(",")]
                if len(transition[len(transition) - 1]) > 1:
                    transition[len(transition) - 1] = transition[len(transition) - 1][0:2]
                transitions.append(transition)

f.close()
"""
print(letters)
print(states)
print(transitions)
"""
if ok==1:
    for transition in transitions:
        verif = 0
        if transition[1] in letters:
            for cv in states:
                if transition[0] == cv[0]:
                    verif += 1
                if transition[2] == cv[0]:
                    verif += 1
            if verif != 2:
                ok = 0
                break
        else:
            ok = 0
            break

    def cheie(v):
        return v[0], v[1]
    transitions.sort(key=cheie)
    #print(transitions)

if ok == 1:
    print("NFA valid")
else:
    print("NFA invalid")