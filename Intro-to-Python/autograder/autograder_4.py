from typing import List
from copy import copy, deepcopy

from random import randint

__globString = "notebook_4"

__dict = None
__keys = None

from autograder.utils import writeRes

# Utility function
def get_dict_q1():
    global __dict
    
    N = randint(200,400)
    
    __dict = dict([ (randint(-500, 500), randint(-500, 500)) for _ in N ] ) 
    
    return deepcopy(__dict)

def get_keys_q1():
    global __keys
    
    N = randint(100,500)
    
    __keys = [ randint(-550, 550) for _ in N ]
    
    return copy(__keys)

def q_1(result:dict):
    """
    Autograder for
You are given a dictionnary *dIn* (that you should not modify) and a list of key-words *keyIn* that may or may-not be used within *dIn*. Construct a new dictionnary containing only the keys (and the corresponding values in *dIn*) that appear as keywords in *dIn* **and** *keyIn*.
    :param result:
    :return: bool
    """
    
    isOk = False
    
    assert ((__dict is not None) and (__keys is not None)), "Not initialized"
    
    try:
        print("Provided result {0}".format(result))

        if not isinstance(result,dict):
            print("Is not a dict -> false")
        else:
            # Get the dict
            resDict = dict( [(aKey, __dict[aKey]) for aKey in __keys if aKey in __dict.keys()] )
            isOk = (result == resDict)
            print("The provided result is {0}".format(isOk))
        
    except:
        print("Automatic string conversion failed, result cannot be correct")
    
    
    writeRes("{0}_1 : {1:d} of 1".format(__globString, isOk))
    
    return isOk

if __name__ == "__main__":
    from copy import copy
    print("autograder_4")
    print(q_1([]))
    d = copy(__targInt)
    l = copy(__intList)
    print(q_1({}))