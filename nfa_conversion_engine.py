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
                state = [[x] for x in line.strip().split(",")]
                if len(state[len(state)-1])>1:
                    state[len(state) - 1]=state[len(state)-1][0]
                if len(state) == 2:
                    if state[1][0] == 'S':
                        s_curent = state[0]
                if len(state) == 3:
                    if state[1][0] == 'S' or state[2][0] == 'S':
                        s_curent = state[0]
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

finalstates=[s_curent]
finaltransitions=[]
i=0
while i<len(finalstates):
    for letter in letters:
        create=[]
        lista=[]
        final=0
        for j in finalstates[i]:
            k=0
            while k<len(transitions):
                while k < len(transitions) and transitions[k][0] == j[0] and transitions[k][1] == letter:
                    if transitions[k][2] not in create:
                        create.extend(transitions[k][2])
                    for chestie in states:
                        if chestie[0][0] == transitions[k][2]:
                            if len(chestie) == 2:
                                if chestie[1][0] == 'F':
                                    final = 1
                            if len(chestie) == 3:
                                if chestie[1][0] == 'F' or chestie[2][0] == 'F':
                                    final = 1
                    k+=1
                k+=1
        if final==0:
            if create not in finalstates:
                finalstates.append(create)
            finaltransitions.append(create)
        else:
            lista.append(create)
            lista.append(['F'])
            if lista not in finalstates:
                finalstates.append(lista)
            finaltransitions.append(lista)
    i+=1
"""
print("-----")
print(finalstates)
print(finaltransitions)
print("-----")
"""

print("Sigma:")
for letter in letters:
    print(letter)
print("States:")
for i in range(len(finalstates)):
    if len(finalstates[i])==1 or finalstates[i][1][0].isdigit():
        if finalstates[i]==s_curent:
            print(i, ",S", sep="")
        else:
            print(i)
    else:
        print(i,",F",sep="")
print("Transitions:")
for j in range(len(finalstates)):
    for i in range(len(letters)):
        print(j,",",letters[i],",",end="",sep="")
        for k in range(len(finalstates)):
            if finalstates[k]==finaltransitions[i+2*j]:
                print(k)