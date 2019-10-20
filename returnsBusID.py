import requests
key = 'Bp3C5aECiQ5gqEkyC83LNhqV6'
def getVID(stopID, direction, rteNum, arrivalTime, curTime):
    urlWStop = f'http://www.ctabustracker.com/bustime/api/v2/getpredictions/?key={key}&stpid={stopID}&format=json'
    stopJson = requests.get(urlWStop).json()
    busTimeResponse = (stopJson['bustime-response'])
    prd = (busTimeResponse['prd'])
    sampleVID = ''
    for x in prd:
        sampleVID = (x['vid'])
        break
    urlWVID = f'http://www.ctabustracker.com/bustime/api/v2/getpredictions/?key={key}&vid={sampleVID}&format=json'
    sampleVIDJson = requests.get(urlWVID).json()
    busTimeResponse2 =( sampleVIDJson['bustime-response'])
    prd2 = busTimeResponse2['prd']
    delT = curTime - arrivalTime
    stopT = 0
    previousStopTime = 0
    for x in prd2:
        if delT <= stopT:
            busID = (x['vid'])
            return busID
        break
    stopsPassed = 0
    curStopId = ''
    for stops in prd2:#for each stop in the line
        if stops['prdctdn'] != 'DUE' and stops['prdctdn'] != 'DLY': #valid value
            stopT += int(stops['prdctdn'])-previousStopTime #the stops the bus has traveled increases as des the time passed
            stopsPassed+=1
            curStopId =stops['stpid']
            previousStopTime = int(stops['prdctdn'])#previous time val

    currStop = f'http://www.ctabustracker.com/bustime/api/v2/getpredictions/?key={key}&stpid={curStopId}&format=json'
    currStopJson = requests.get(currStop).json()
    busTimeResponse3 = currStopJson['bustime-response']
    prd3 = busTimeResponse3['prd']
    for s in prd3:
        return s['vid'].json()

with open(f'./busID.txt', 'w') as file:  # 24 hrs clock
    file.write(getVID(stopID=<var1>, direction=<var2>, rteNum=<var3>, arrivalTime=<var4>, curTime=<var5>))  # magicNumber
    file.close()
    print(getVID(386, 'Eastbound', 20, 0, 7))# as of 6:55