import yaml
import csv
import os
import time

def yaml2csv(fileName):
    no2ing = False
    with open('allBallDetail.csv','a') as csvfile:
        #myrows=["batsman","Bowler","batsman_runs","extras","player_out_name"]
        writer=csv.writer(csvfile)
        #writer.writerow(myrows)
        fp =  open('../data/'+fileName, 'r')   
        data = yaml.load(fp)
        fp.close()
        #data.get("innings") is a list of length 2 
        innings1=(data.get("innings")[0])  #ist innings   
        try:
            innings2=(data.get("innings")[1])  #2nd innings
        except:
            no2ing = True
        #over1_ball1=innings1.get("1st innings").get("deliveries")[0]   #getting over by over details
        #print(over1_ball1.get(0.1).get("batsman"))
        for info in innings1.get("1st innings").get("deliveries"):       
            for balls in info:
                
                #print(type(balls))
                #print(balls)
                
                #print(info.get(balls))
                #print("########################################")
                batsman_name=info.get(balls).get("batsman")
                bowler_name=info.get(balls).get("bowler")
                batsman_runs=(info.get(balls).get("runs").get("batsman"))
                extras=(info.get(balls).get("runs").get("extras"))
                #print(batsman_runs,extras)
                if 'wicket' in info.get(balls).keys():
                    player_out_name=info.get(balls).get('wicket').get("player_out")
                    
                else:
                    player_out_name="NA"
                    
                writer.writerow([batsman_name,bowler_name,batsman_runs,extras,player_out_name])
                
        if(not no2ing):
            for info in innings2.get("2nd innings").get("deliveries"):       
                for balls in info:
                    #print(type(balls))
                    #print(balls)
                    
                    #print(info.get(balls))      gives detail about each ball
                    #print("########################################")
                    batsman_name=info.get(balls).get("batsman")
                    bowler_name=info.get(balls).get("bowler")
                    batsman_runs=(info.get(balls).get("runs").get("batsman"))
                    extras=(info.get(balls).get("runs").get("extras"))
                    #print(batsman_runs,extras)
                    if 'wicket' in info.get(balls).keys():
                        player_out_name=info.get(balls).get('wicket').get("player_out")
                        
                    else:
                        player_out_name="NA"
                        
                    writer.writerow([batsman_name,bowler_name,batsman_runs,extras,player_out_name])
                    

def filespath():
    return(os.listdir(os.getcwd()+"/../data"))

def makecsv():
    fp = open('allBallDetail.csv', "w")
    fp.close()
    listFiles = filespath()
    numOfFiles = len(listFiles) - 1
    i = 0
    start = time.time()
    
    for fileId in listFiles:
        i += 1
        yaml2csv(fileId)

    #print(len(listFiles))
    timestep = time.time() - start
    return(timestep)
    
if(__name__=="__main__"):
    makecsv()
