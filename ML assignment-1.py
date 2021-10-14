# QUESTION-1
s = "Hi There Class!"
x = s.split(" ")
print(x)
print()

# QUESTION-2
txt = "the diameter of {planet} is {diameter} kilometers"
new_txt = txt.format(planet = "Earth",diameter = 12742)
print(new_txt)
print()

# QUESTION-3
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
g = lst[3][1][2][0]
print(g)
print()

# QUESTION-4
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
g = d['k1'][3]['tricky'][3]['target'][3]
print(g)
print()

# QUESTION-5
def domainget(email):
    print(email.split('@')[0])
domainget('user@domain.com')
print()

# QUESTION-6
def findstring(s):
    if(x.find("dog")):
        return True
x = 'The breed of this dog is German Shepherd'
f = findstring(x)
print(f)
print()

# QUESTION-7
def countstring(s):
    count = s.count("dog")
    return count
x = 'The breed of this dog is German Shepherd and it is a very faithful dog'
count = countstring(x)
print(count)
print()

# QUESTION-8
seq = ['soup','dog','salad','cat','great']
print(list(filter(lambda word : word[0] != 's',seq)))