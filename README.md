# Python-random-dictionnary-list-generator
Class to generate random list or dictionnary in python


-  This object is used to automatically generate a list or a dictionary according to the size you specify.
    -   This size is defined at the instantiation of the object.
    -   By default, it generates a list or a dictionary of 5 elements.
    -   You can also specify the size of the list or dictionary when calling the method.
    -   You can also specify the size of keys/values when instantiating or calling the object
        

    -   examples : 
            #Instantiation with default parameters
            rd_ld = RandomListOrDictionnary(size=5, key_length=3, values_length=5)
            #We can specify the size
            my_list = rd_ld.createRandomDictionnary(3)
            my_dict = rd_ld.createRandomList(3)