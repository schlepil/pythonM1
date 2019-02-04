__globString = "notebook_1"

from autograder.utils import writeRes

def q_1(result:int):
    """
    Autograder for
    Store the square of $\pi$ rounded to the next smaller integer in the variable called *res_1_1*
    :param result:
    :return: bool
    """
    from math import pi, floor
    
    isOk = False
    
    try:
        print("Provided result {0}".format(result))

        if not isinstance(result,int):
            print("Is not an integer -> false")
        else:
            isOk = (result == floor(pi**2))
            print("The provided result is {0}".format(isOk))
        
    except:
        print("Automatic string conversion failed, result cannot be correct")
    
    
    writeRes("{0}_1 : {1:d} of 1".format(__globString, isOk))
    
    return isOk

def q_2(result:bool):
    
    from math import pi

    #"Determine wether the fourth root of $2^\\pi$ is confined between the closed interval between one and two, save the answer in *res_1_2*"
    
    isOk = False
    
    try:
        print("Provided result {0}".format(result))
        
        if not isinstance(result,bool):
            print("Is not an boolean -> false")
        else:
            isOk = (result == 1. <= (2^pi)**(1./4.) <= 2. )
            print("The provided result is {0}".format(isOk))

    except:
        print("Automatic string conversion failed, result cannot be correct")

    writeRes("{0}_2 : {1:d} of 1".format(__globString,isOk))

    return isOk
    
    
        
    