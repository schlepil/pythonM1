from typing import List, Callable, Tuple
from copy import copy, deepcopy

from random import randint

import sys

__globString = "notebook_6"

from autograder.utils import writeRes

def q_1(func:Callable):
    """
    Autograder for
Code a recursive function that computes and returns the factorial of a number, that is the function has to accept integers and return (as first output) the corresponding factorial (also as integer). It should moreover raise a TypeError if anything other then an integer is given as input.
    :param result:
    :return: bool
    TBD check for a better solution to check recursion
    """
    
    from random import randint
    from math import factorial
    
    isOk = False
    
    if not callable(func):
        print("No function or callable provided -> False")
        writeRes("{0}_1 : {1:d} of 1".format(__globString, isOk))
        return isOk
    
    listTest = [randint(-200, -100) for _ in range(20)]+[-2,-1,0,1,2]+[randint(100, 200) for _ in range(20)]
    
    isOk = True
    
    #Build the decorator
    callCounter = 0
    
    isDone = False
    
    for aInt in listTest:
        if isDone:
            break
        if aInt < 0:
            try:
                func(aInt)
            except ValueError:
                pass
            except ... as me:
                print("Failed on func({0}) without ValueError with {1}".format(aInt, me))
                isOk=False; isDone = True
                continue
            else:
                isOk = False; isDone = True
                continue
            
        else:
            if aInt > 100:
                try:
                    sys.setrecursionlimit(aInt-2)
                    func(aInt)
                    print("Succeeded to compute {0}! with a recursion limit of {1} -> not an recursive algorithm".format(aInt, aInt-2))
                    isOk = False;
                    isDone = True
                    continue
                except RecursionError:
                    pass
                except ... as me:
                    print("Failed on func({0}) with {1}".format(aInt,me))
                    isOk = False;
                    isDone = True
                    continue
                
            try:
                if aInt>100:
                    sys.setrecursionlimit(aInt+4) # I do not know why plus 4 is necessary
                res = func(aInt)
            except RecursionError:
                print("Failed on func({0}) as it took too many recursions".format(aInt))
                isOk = False;
                isDone = True
                continue
            except ... as me:
                print("Failed on func({0}) with {1}".format(aInt,me))
                isOk = False;
                isDone = True
                continue
            else:
                pass
                
            isOk = isOk and (res == factorial(aInt))
    
    writeRes("{0}_1 : {1:d} of 1".format(__globString, isOk))
    
    return isOk


if __name__ == "__main__":
    print("Autograder_6")
    
    # Define one possible solution
    def recFrac(initVal:int)->Tuple[int,int]:
        """
        Compute factorial recursively
        :param initVal:
        :param resVal:
        :return:
        """
        
        if initVal<0:
            raise ValueError
        
        if initVal in (0,1):
            # Stop condition
            return 1
        else:
            return initVal*recFrac(initVal-1)
    
    q_1(recFrac)
        
        