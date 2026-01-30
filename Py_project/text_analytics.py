txt=open('Py_project/data.txt','r')

lines=list()

for line in txt:
    lines.append(line.strip())

#print(lines)
words=list()
for word in lines:
    words.extend(word.split())
#print(words)
clean_words=list()

for i in words:
    x=str(i)
    x=x.strip()
    if len(x)>0 and (x[-1]=="." or x[-1]==","):
        x=x[0:len(x)-1]
    x=x.lower()
    clean_words.append(x)

#print(clean_words)
def count_words(data):
    counts=dict()
    for c in data:
        if c in counts:
            counts[c]+=1
        else:
            counts[c]=1
    return counts


def topN(count):
    l=list(count.items())
#print(l)
    l.sort(key= lambda x: x[1], reverse=True)
    num=int(input("Enter N for top N words used:"))
    num=min(len(l),num)
    for i in range(num):
        print(l[i])
    
def avgLen(words):
    c=0
    for i in words:
        c+=len(i)
    avg=float(c/(len(words)))
    return avg

count=count_words(clean_words)
#print(count)
total_words=len(clean_words)
#print(total_words)
unique_words=list(count)
#print(unique_words)

sorted_unique=sorted(unique_words,key=len)

print("1. For count of Total words, Unique words")
print("2. For word frequency")
print("3. For top N most frequent word")
print("4. For Longest and shortest word")
print("5. For avg word length")
print("6. To EXIT")
x=0
while x!=6: 
    y=int(input("Enter:"))
    x=y
    if x==1:
        print("Total words",total_words)
        print("Unique words:")
        print(unique_words)
    elif x==2:
        print("Word frequency:")
        print(count)
    elif x==3:
        topN(count)
    elif x==4:
        print("Longest word: ",sorted_unique[-1],", Shortest word: ",sorted_unique[0])
    elif x==5:
        print(avgLen(clean_words))
    elif x==6:
        break
    else:
        print("Invalid number")