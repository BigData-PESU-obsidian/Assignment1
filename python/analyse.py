import time
import csv
import makeCSV

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
                
    if(printAll == True):
        writeCSV(batsmanDict, "batvul.csv")
        writeCSV(bowlerDict, "ballvul.csv")

    #vulnerable_batsman_bowler( batsmanDict, bowlerDict)
    return([batsmanDict, bowlerDict])
    
def vulnerable_batsman_bowler( batsmen, bowlers):
    batsmenmax={}
    bowlermax={}

    battime = time.time()
    fp = open("BatsmenVulnerability.csv", "w")
    writer = csv.writer(fp)
    for batsman in batsmen:
        batsmenmax[batsman]={}
        try:
            maxwickets=max(batsmen[batsman].values())
        except:
            maxwickets = 0
        for key,value in batsmen[batsman].items():
            if value==maxwickets:
                batsmenmax[batsman][key]=value
        writer.writerow([batsman]+[str(vul)+","+str(batsmenmax[batsman][vul]) for vul in batsmenmax[batsman]])
        #print(" batsman {} is more vulnerable with bowlers {}".format(batsman,batsmenmax[batsman]))
    fp.close()
    battime = time.time() - battime

    bowltime = time.time()
    fp = open("BowlersVulnerability.csv", "w")
    writer = csv.writer(fp)
    for bowler in bowlers.keys():
        bowlermax[bowler]={}
        try:
            maxruns=max(bowlers[bowler].values())
        except:
            maxruns = 0
        for key,value in bowlers[bowler].items():
            if value==maxruns:
                bowlermax[bowler][key]=value
        writer.writerow([bowler]+[str(vul)+","+str(bowlermax[bowler][vul]) for vul in bowlermax[bowler]])
        #print(" bowler {} is more vulnerable with {}".format(bowler,bowlermax[bowler]))
    fp.close()
    bowltime = time.time() - bowltime
    
    return(battime, bowltime)

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

    convtime = 0
    
    start = time.time()
    convtime = makeCSV.makecsv() 
    print("Time taken for conversion from .yaml to .csv : {} seconds".format(convtime))
    retDat = analyseBatBall()
    battime, bowltime = vulnerable_batsman_bowler(retDat[0], retDat[1])
    print("Time taken to get batsmen vulneribility data : {} seconds".format(battime))
    print("Time taken to get bowlers vulneribility data : {} seconds".format(bowltime))
    print("Total take : {} seconds".format(time.time() - start))
    
