N = int(raw_input())
result = []
scores = []
names = []

for i in range(N):
    #creates dictionary with names as keys and scores as values
    name = raw_input()
    score = float(raw_input())

    result.append(name)
    result.append(score)
    
    #add score to list of scores
    scores.append(score)
    
scores2 = sorted(scores)

i = 0
while scores2[0] == scores2[1]:
    scores2 = scores2[1:]
    i += 1   
  
if len(scores2) > 2 and scores2[1] == scores2[2]:
    in1 = scores.index(scores2[1])
    names.append(result[(in1)*2])
    scores.pop(in1)
    
    in2 = scores.index(scores2[2]) 
    names.append(result[(in2)*2 + 2])
    
    names.sort()
    
    print names[0]
    print names[1]
    
elif len(scores2) > 1:
    in1 = scores.index(scores2[1])
    print result[(in1)*2]

else:
    in1 = scores.index(scores2[0])
    print result[(in1)*2]
    
