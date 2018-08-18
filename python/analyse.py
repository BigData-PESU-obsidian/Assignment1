import time

def analyseBatBall():
    """
    Stores the vulnerability of both batsmen and bowlers w.r.t individual players
    """
    
    batsmanDict = dict()
    bowlerDict = dict()
    
    dataFp = open("output.csv", "r")

    datal = dataFp.readline()

    while(datal):
        
        batsman, bowler, runs, extras, out = datal.strip().split(',')
        datal = dataFp.readline()
        runs = int(runs)
        
        if(out == batsman):
            if(batsman in batsmanDict.keys()):
                if(bowler in batsmanDict[batsman].keys()):
                    batsmanDict[batsman][bowler] += 1
                else:
                    batsmanDict[batsman][bowler] = 1
            else:
                batsmanDict[batsman] = dict()
                batsmanDict[batsman][bowler] = 1

        if(runs != 0):
            if(bowler in bowlerDict.keys()):
                if(batsman in bowlerDict[bowler].keys()):
                    bowlerDict[bowler][batsman] += runs
                else:
                    bowlerDict[bowler][batsman] = runs
            else:
                bowlerDict[bowler] = dict()
                bowlerDict[bowler][batsman] = runs
                
    return([batsmanDict, bowlerDict])

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

    batsmen = retDat[0]
    bowlers = retDat[1]
   
    for batsman in batsmen:
        print(" for {} the data is\n{}".format(batsman, batsmen[batsman]))

    for bowler in bowlers:
        print(" for {} the data is\n{}".format(bowler, bowlers[bowler]))
    
    vulnerabledata=vulnerable_batsman_bowler(batsmen,bowler)
    
