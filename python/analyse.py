import yaml
import os

def filespath():
    return(os.listdir(os.getcwd()+"/../data"))

def batsmanrate():
    matches = filespath()
    for matchfile in matches:
        fp = open("./../data/"+matchfile, "r")
        matchData = yaml.load(fp)
        fp.close()
        
def bowler():
    pass

if(__name__ == "__main__"):
    batsmanrate()
    
