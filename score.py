import json
# --------------------------------------------------------------                
#          ----------- PARSE SCORE FILE -----------------  
# -------------------------------------------------------------- 
def getScores():
    data = []

    with open("saves.json", 'r') as f:
        json_object = json.load(f)

    for scores in json_object["save"]:
        data.append(scores)

    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            if(data[i]["lastscore"] < data[j]["lastscore"]):
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data

# --------------------------------------------------------------                
#          ----------- SAVE SCORE----------------  
# -------------------------------------------------------------- 
def saveScore(playerPseudo, score):
    data = getScores()
    updated = False

    for save in data:
        if save["pseudo"] == playerPseudo:
            save["lastscore"] = score
            if score > save["highscore"]:
                save["highscore"] = score
            updated = True

    if not updated:
        data.append({"pseudo": playerPseudo,"lastscore": score, "highscore": score})

    with open("saves.json", "w") as f:
        json.dump({"save": data}, f)



