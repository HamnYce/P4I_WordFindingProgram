name = input('/Users/hamadbouabbas/Desktop/Git/Python_Projects/P4I_Word_Finding_Program_P11/Harry_Potter_And_The_Sorcerer.txt')
handle = open('/Users/hamadbouabbas/Desktop/Git/Python_Projects/P4I_Word_Finding_Program_P11/Harry_Potter_And_The_Sorcerer.txt', 'r')
text = handle.read()
words = text.split()
counts = dict()

for word in words:
    counts[word] = counts.get(word,0) + 1

    bigcount = None
    bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword, bigcount)