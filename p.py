MOT = {
    "mov": "0x001",
    "add": "0x002",
    "sub": "0x003"
}

POT = {
    ".data": "0x01",
    ".code": "0x02",
    "end": "0x03",
    "@data": "0x04"
}

DL = {
    "db": "0x1",
    "dw": "0x2",
    "ds": "0x3"
}

I = {
    "21h": "00x01"
}

DS = 100
CS = 200

REG = {
    "al": "001",
    "bl": "002",
    "ah": "003",
    "ax": "004"
}


ST = {}
LT = {}

currentAdd = 0
flag = 0
sindex = 0
lindex = 10
iflag = 0
ntflag = 0
cflag = 0

wf = open('op.txt','w')
wf.close()

wf = open('op.txt','a')

with open('ass.txt', 'r') as f:
    for line in f:
        ntflag = 0
        cflag = 0
        iflag = 0
        flag = 0
        if currentAdd != 0:
            wf.write(str(currentAdd) + " ")
        x = line.split(" ")
        for i in x:
            if i.endswith("\n"):
                zxc = i.split("\n")
                i = zxc[0]

            if i == "int":
                iflag = 1
                ntflag = 1
                continue

            if iflag == 1:
                if i in I:
                    ntflag = 1
                    wf.write(I.get(i)+ " ")
                    continue

            if i in POT:
                ntflag = 1
                if i == ".data":
                    wf.write(POT.get(i)+ " ")
                    currentAdd = DS
                    continue
                elif i == ".code":
                    wf.write(POT.get(i)+ " ")
                    currentAdd = CS
                    continue
                else:
                    wf.write(POT.get(i)+ " ")
                    continue

            if i in MOT:
                ntflag = 1
                wf.write(MOT.get(i)+ " ")
                flag = 1
                continue

            if flag == 1:
                z = i.split(",")
                ntflag = 1

                for j in z:
                    if j in POT:
                        wf.write(POT.get(j)+ " ")
                        continue

                    if j in DL:
                        wf.write(DL.get(j)+ " ")
                        continue

                    if j in REG:
                        wf.write(REG.get(j)+ " ")
                        continue

                    if j in ST:
                        wf.write(str(ST.get(j))+ " ")
                        continue

                    if j.endswith("h") and j not in REG:
                        LT[j] = lindex
                        wf.write(str(lindex)+ " ")
                        lindex += 1
                        ntflag = 1
                        cflag = 1
                        continue

            if i.endswith(":"):
                ST[i] = sindex
                wf.write(str(sindex)+ " ")
                sindex += 1
                ntflag = 1
                continue
            
            if i.endswith("H"):
                LT[i] = lindex
                wf.write(str(lindex)+ " ")
                ntflag = 1
                continue

            if i == "?":
                ntflag = 1
                continue

            if i.endswith("h") and cflag == 0:
                if i not in REG:
                    LT[i] = lindex
                    wf.write(str(lindex)+ " ")
                    lindex += 1
                    ntflag = 1
                    continue

            if i in DL:
                ntflag = 1
                wf.write(DL.get(i)+ " ")
                continue
            if ntflag == 0:
                if i != '':  
                    ST[i] = sindex
                    wf.write(str(sindex) + " ")
                    sindex += 1
            
        currentAdd += 1
        wf.write("\n")
        
print(ST)
print(LT)
wf.close()
            

            

