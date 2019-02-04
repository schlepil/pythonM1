__globString = "notebook_2"

__stringQ2 = ""

__subString1 = "iizu"
__subString2 = "8oz"

from autograder.utils import writeRes

def q_1(result:float):
    """
    Autograder for
    Use string formating and the eval command to determine the rounding error made by rounding ππ to a five digit expression. Store the obtained error in res_2_1
    :param result:
    :return: bool
    """
    from math import pi
    
    isOk = False
    
    try:
        print("Provided result {0}".format(result))

        if not isinstance(result,float):
            print("Is not an float -> false")
        else:
            piround = eval("{0:.5f}".format(pi))
            pierr = pi - piround
            isOk = (result == pierr)
            print("The provided result is {0}".format(isOk))
        
    except:
        print("Automatic string conversion failed, result cannot be correct")
    
    
    writeRes("{0}_1 : {1:d} of 1".format(__globString, isOk))
    
    return isOk

# Utility function
def get_random_string_q2():
    """
    Create a string that corresponds to 
    
    You are given a random string (in length and characters) stored in *s_in* and must extract 
    the shortest possible substring starting after the first appearance of "iizu" and ending before "8oz".
    Store it in *res_2_2*.
    """
    import string
    import random
    global __stringQ2
    
    allChars = string.ascii_letters+string.digits
    
    #Get long string
    while True:
        __stringQ2.join([random.choice(allChars) for _ in range(50000)])
    
        nList = sorted([random.randint(1000,40000), random.randint(1000,40000)])
        nList[1] += 10
    
        __stringQ2 = __stringQ2[:nList[0]]+__subString1+__stringQ2[nList[0]+1:nList[1]]+__subString2+__stringQ2[nList[1]+1:]
        
        if __stringQ2.find("iizu") < __stringQ2.find("8oz"):
            break
    
    return None
    
def q_2(result:str):
    """
    Autograder for
    You are given a random string (in length and characters) stored in *s_in* and must extract 
    the shortest possible substring starting after the first appearance of "iizu" and ending before "8oz".
    Store it in *res_2_2*.
    :param result:
    :return: bool
    """
    
    isOk = False
    
    assert len(__stringQ2), "Not initialized"
    
    try:
        print("Provided result {0}".format(result))

        if not isinstance(result,str):
            print("Is not a string -> false")
        else:
            #Get the substring
            idx0 = __stringQ2.find(__subString1)+len(__subString1)
            idx1 = __stringQ2.find(__subString2)
            subString = __stringQ2[idx0:idx1]
            isOk = (result == subString)
            print("The provided result is {0}".format(isOk))
        
    except:
        print("Automatic string conversion failed, result cannot be correct")
    
    
    writeRes("{0}_2 : {1:d} of 1".format(__globString, isOk))
    
    return isOk
        
    
    
    
    