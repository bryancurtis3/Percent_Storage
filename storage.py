
import sys

data = sys.stdin.readlines()
print(data)

file = "mailexchange.txt"
f = open(file, "r")

line = f.read()
lineMX = line.split("\n")

file = "quota.txt"
f = open(file, "r")

line = f.read()
lineQ = line.split("\n")

lengthMX = len(lineMX)
n = 0
i = 0
q = 0
y = 0
t = 0
qu = 0
it = 0
dom = -1

userID = "user"
newID = "blank"

dl = False
du = False
u = False
e = False


mxList = []

checker = "good"
clean = []
user = []
cleaned = []



for m in range(lengthMX - 1):
    domainMX = []
    mx = []


    if "\t" not in lineMX[m] and ' ' not in lineMX[m] or lineMX[m][0] == ";" :
        m += 1



    # Extracts domain line by line
    while lineMX[m][q] != "\t" and lineMX[m][q] != ' ':
        domainMX += lineMX[m][q]
        q += 1

    # Extracts MX's
    for r in range(len(lineMX[m])):
        t = r + 2

        if lineMX[m][r] == "X":
            while t < len(lineMX[m]):
                mx += lineMX[m][t]
                t += 1


    # Prints domain with matching MX
    domainMX = "".join(domainMX)
    domainMX = domainMX.lower()
    #print(domainMX)

    mx = "".join(mx)
    #print(mx)
    mxList.append(mx)
    q = 0
    """
    if "google" in mx.lower():
        
        if checker != domainMX or checker == "good":
            clean = list(domainMX)
            clean[-1] = ''
            clean = "".join(clean)
            #print(clean)

            cleaned.append(clean)

            checker = domainMX
            #print(checker)
    """


    if checker != domainMX or checker == "good":
        clean = list(domainMX)
        clean[-1] = ''
        clean = "".join(clean)
        #print(clean)

        cleaned.append(clean)

        checker = domainMX
        #print(checker)


    
#___________________PHASE_TWO______________________

duck = sorted(cleaned)

#print(duck)


file = "trueuserdomains.txt"
f = open(file, "r")

line = f.read()
line = line.split("\n")

file = "summary.txt"
f2 = open(file, "r")

line2 = f2.read()
line2 = line2.split("\n")

y = 0
x = 0
z = 0
i = 0
lineNums = []
rested = []
domain = ''

for n in range(len(line)):
    sep = ': '
    rest = line[n].split(sep, 1)[1]
    first = line[n].split(sep, 1)[0]
    rested.append(rest)
    
    for x in range(len(cleaned)):
        
        if first == cleaned[x]:
            lineNums.append(n)
                

            
unrested = []
#print(rested)
for bee in range(len(lineNums)):
    unrested.append(rested[lineNums[bee]])

rerested = sorted(unrested)
recleaned = sorted(cleaned)

#print(rerested)
#print(recleaned)

#print(lineNums)




#print(rerested)

#____________________PHASE_THREE_______________________

ema = 0
for qu in range(len(lineQ)):
    clean = ''
    rest = ''
    
    if "-" in lineQ[qu]:
        dom += 1


    if "user:" in lineQ[qu]:
        newID = lineQ[qu].split(": ", 1)[1]
        u = True
    

    if "email:" in lineQ[qu]:
        email = lineQ[qu].split(": ", 1)[1]
        e = True
        
        
    

    if "disklimit:" in lineQ[qu]:
        limit = lineQ[qu].split(": ", 1)[1]
        limit = limit.replace("M", '')
        if limit == "unlimited":
            limit = 303
        limit = float(limit)
        #print(limit)
        newQuota = limit
        dl = True


    if "diskused:" in lineQ[qu]:
        sep = ': '
        rest = lineQ[qu].split(sep, 1)[1]
        rest = rest.replace("M", '')
        rest = float(rest)


        if limit != 0:
            percent = rest/limit
            percent *= 100

        else:
            percent = "N/A"
            
        if percent != "N/A" and percent >= 95.0 and newID != "blank":
            # All other new code will probably go here (for raising limit)
            du = True
            
            """
            for em in range(len(line2)):
                
                
                if "---" in line2[em]:
                    ema += 1
                    

                if "email:" in line2[em]:
                    email = line2[em].split(": ", 1)[1]
                    #email = email.strip("'")

                    #print(email)
            """

            
            
            newQuota = limit + (limit * .02)

            #print("whmapi1 editquota user=%s quota=%d" % (rerested[dom], newQuota))

            #print(rerested[dom], "\t", rest, "\t", round(percent, 3), end = "% used\n")

            
            newID = "blank"
            userID = newID
            
        #if rest >= 3000:
            #print(rerested[dom], "\t", rest, "\t", round(percent, 3), end = "% used\n")

    if dl == True and du == True and e == True and u == True and "user:" in lineQ[qu]:
        #print(email)

        print("whmapi1 editquota user=%s quota=%d" % (userID, newQuota))
        dl = False
        du = False
        user = False
        email = False       
