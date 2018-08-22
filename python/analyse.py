import time
import csv

def analyseBatBall(printAll = False):
    """
    Stores the vulnerability of both batsmen and bowlers w.r.t individual players
    """
    batsmanDict = dict()
    bowlerDict = dict()
    dataFp = open("allBallDetail.csv", "r")
    datal = dataFp.readline()
    while(datal):
        
        batsman, bowler, runs, extras, out = datal.strip().split(',')
        datal = dataFp.readline()
        runs = int(runs)
        
        if(batsman not in batsmanDict):
            batsmanDict[batsman] = dict()
            
        if(bowler not in bowlerDict):
            bowlerDict[bowler] = dict()
            
        if(out == batsman):
            if(bowler in batsmanDict[batsman].keys()):
                batsmanDict[batsman][bowler] += 1
            else:
                batsmanDict[batsman][bowler] = 1
                
        if(runs != 0):
            if(batsman in bowlerDict[bowler].keys()):
                bowlerDict[bowler][batsman] += runs
            else:
                bowlerDict[bowler][batsman] = runs
                
    if(printAll = True):
        writeCSV(batsmanDict, "batvul.csv")
        writeCSV(bowlerDict, "ballvul.csv")
    return([batsmanDict, bowlerDict])


def writeCSV( playerDict, fileName):
    fp = open( fileName, "w")
    writer = csv.writer(fp)

    allOpp = set()
    for player in playerDict:
        for opp in playerDict[player]:
            allOpp.add(opp)
    allOpp = list(allOpp)

    for player in playerDict.keys():
        for op in allOpp:
            if( op not in playerDict[player]):
                playerDict[player][op] = 0

    writer.writerow(["Batsman"]+["Total"]+allOpp)
    for player in playerDict.keys():
        total = sum(playerDict[player].values())
        writer.writerow([player] + [total] + [playerDict[player][allOpp[i]] for i in range(len(allOpp))])
    fp.close()

def vulnerable_batsman_bowler(batsmen,bowler):
    batsmenmax={}
    bowlermax={}
    
    for batsman in batsmen:
        batsmenmax[batsman]={}
        maxwickets=max(batsmen[batsman].values())
        for key,value in batsmen[batsman].items():
            if value==maxwickets:
                batsmenmax[batsman][key]=value
        print(" batsman {} is more vulnerable with bowlers \n{}".format(batsman,batsmenmax[batsman]))


    for bowler in bowlers:
        bowlermax[bowler]={}
        maxruns=max(bowlers[bowler].values())
        for key,value in bowlers[bowler].items():
            if value==maxruns:
                bowlermax[bowler][key]=value
        print(" bowler {} is more vulnerable with  \n{}".format(bowler,bowlermax[bowler]))
        
        
    return([batsmenmax,bowlermax])
    
if(__name__=="__main__"):
    
    start = time.time()
    retDat = analyseBatBall()
    print("Time take : {} seconds".format(time.time() - start))
    
