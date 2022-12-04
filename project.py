import numpy as np
from numpy import random

#STUB FUNCTION USED FOR TESTING ONLY, MUST IMPLEMENT LATER FIXME
def leave_one_out_cross_validation (data,current_set,feature_to_add):
    return random.randint(100)
    pass

#SEARCH FUNCTION OF THE ALGORITHM
def feature_search(data):

    current_set_of_features = []; #intialized an empty set

    for i in range(1,len(data[0] - 1)):
        print("On the ", i,"th level of the search tree")
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0

        for k in range(1,len(data[0] - 1)):
            if k not in current_set_of_features:
                print("--Considering adding the ", k," feature")
                accuracy = leave_one_out_cross_validation(data,current_set_of_features,k+1)

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = k

        current_set_of_features.append(feature_to_add_at_this_level)
        print("On level ", i, "I added feature ", feature_to_add_at_this_level, " to current set")



def main():
    #print("Wednesday")
    data = np.loadtxt('CS170_Small_Data__113.txt')

    

    #accuracy = leave_one_out_cross_validation(data,y,z)
    feature_search(data)
    

if __name__ == "__main__":
    main()


