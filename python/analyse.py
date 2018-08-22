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

    
if(__name__=="__main__"):
    
    start = time.time()
    retDat = analyseBatBall()
    print("Time take : {} seconds".format(time.time() - start))
    
