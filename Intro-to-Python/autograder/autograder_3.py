from typing import List
from copy import copy, deepcopy

__globString = "notebook_3"

__targInt = None
__intList = None

from autograder.utils import writeRes

def q_1(result:List[int]):
    """
    Autograder for
    Generate a list containing all integers which are the square of some other integer in the range [10, 10000[ using list comprehension in its **for** - **if** form and save it to *res_3_1*
    :param result:
    :return: bool
    """
    
    isOk = False
    
    try:
        print("Provided result {0}".format(result))

        if not isinstance(result,List):
            print("Is not a list -> false")
        else:
            if not all([isinstance(aInt,int) for aInt in result]):
                print("All elements must be integer -> false")
            else:
                trueList = [i for i in range(10,10000) if int( (int(i**.5))**2 ) == i]
                isOk = (result == trueList)
                print("The provided result is {0}".format(isOk))
        
    except:
        print("Automatic string conversion failed, result cannot be correct")
    
    
    writeRes("{0}_1 : {1:d} of 1".format(__globString, isOk))
    
    return isOk

# Utility function
def q_2_getTarg():
    import random
    global __targInt
    __targInt = random.randint(-1000, 1000)
    return copy(__targInt)

def q_2_getList():
    import random
    global __intList
    if __targInt is None:
        print("must call q_3_getTarg() first")
        return []
    
    N = random.randint(200, 10000)
    idxTarg = random.randint(10,N-10)
    
    allInt = list(range(-10000, 10000))
    valTarg = random.randint(-1000,+1000)
    
    thisList = []
    
    for _ in range(N):
        thisIdx = random.randint(0,len(allInt)-1)
        thisList.append( allInt.pop(thisIdx) )
    
    thisList[idxTarg] = valTarg
    
    __intList = copy(thisList)
    
    return copy(thisList)


def q_2(refTarg:int, refList:List[int], result:List[int]):
    """
    Autograder for
    You are given a random string (in length and characters) stored in *s_in* and must extract 
    the shortest possible substring starting after the first appearance of "iizu" and ending before "8oz".
    Store it in *res_2_2*.
    :param result:
    :return: bool
    """
    
    from math import fabs
    
    assert ((__targInt is not None) and (__intList is not None)), "Not initialized"
    
    isOk = False
    
    try:
        print("Provided result {0}".format(result))

        if not isinstance(result,list):
            print("Is not a list -> false")
        else:
            if not ( (refTarg == __targInt) and (refList == __intList)):
                print("Modified target or list -> false")
            else:
                if not all([isinstance(aInt,int) for aInt in result]):
                    print("All elements must be integer -> false")
                else:
                    #Get the correct list
                    newList = [ fabs(aInt-__targInt) for aInt in __intList if not aInt==__targInt]
                    isOk = (result == newList)
                    print("The provided result is {0}".format(isOk))
            
    except:
        print("Automatic string conversion failed, result cannot be correct")
    
    
    writeRes("{0}_2 : {1:d} of 1".format(__globString, isOk))
    
    return isOk

if __name__ == "__main__":
    from copy import copy
    print("autograder_3")
    print(q_1([]))
    q_2_getTarg()
    q_2_getList()
    t = copy(__targInt)
    l = copy(__intList)
    print(q_2(t,l,[]))