###############################################################
def resetRes(fileStr:str = "results.txt"):
    try:
        open(fileStr, 'w').close()
    except FileNotFoundError:
        print("No results stored so far")

###############################################################
def writeRes(str:str, fileStr:str = "results.txt"):
    with open(fileStr,"w+") as f:
        f.write(str)
    return None