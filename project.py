import numpy as np
from numpy import random

#K fold cross validaiton code
def leave_one_out_cross_validation (data,current_set,feature_to_add):
    #code to replace irrelevant rows of the data variable with zeroes
    for x in range(1,len(data[0])):
        if (x not in current_set) and (x != feature_to_add):
            for y in range(len(data)):
                data[y][x] = 0
   
    number_correctly_classified = 0
    
    for i in range(len(data)):
        object_to_classify = data[i][1:]
        label_object_to_classify = data[i][0]

        nearest_neighbor_distance = np.inf
        nearest_neighbor_location = np.inf
        for k in range(len(data)):
            if k != i:
                current_row = data[k][1:]
                #print("Ask if ", i + 1,"is nearest neighbor with ", k + 1)
                #distance = np.sqrt(pow(sum(object_to_classify - data[k][1:]),2))
                val = 0
                for d in range(len(data[0])-1):
                    val = val + pow(object_to_classify[d] - current_row[d],2)

                distance = np.sqrt(val)
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data[nearest_neighbor_location][0]
        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified = number_correctly_classified + 1
        
    return number_correctly_classified / len(data)

        #print("Object ", i+1," is class ", label_object_to_classify)
        #print("Its nearest_neighbor is ", nearest_neighbor_location, "which is in class ", nearest_neighbor_label)

        #print("Looping over i, at the ", i + 1,"location")
        #print("The ", i + 1,"th object is in class ", label_object_to_classify)
        

#SEARCH FUNCTION OF THE ALGORITHM
def feature_search(data,num):

    current_set_of_features = []; #intialized an empty set
    best_of_all = 0
    set_of_best = []

    for i in range(1,len(data[0])): 
        print("On the ", i,"th level of the search tree")
        feature_to_add_at_this_level = 0 
        best_so_far_accuracy = 0

        for k in range(1,len(data[0])): 
            if k not in current_set_of_features:
                print("--Considering adding the ", k," feature")
                if num == 1:
                    data = np.loadtxt('CS170_Small_Data__113.txt')

                elif num == 2:
                    data = np.loadtxt('CS170_Large_Data__122.txt')
                
                accuracy = leave_one_out_cross_validation(data,current_set_of_features,k) #k+1
                print("Returned with an Accuracy of ", accuracy)

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = k

        if best_so_far_accuracy > best_of_all:
            best_of_all = best_so_far_accuracy
            set_of_best.append(feature_to_add_at_this_level)


        current_set_of_features.append(feature_to_add_at_this_level)
        print("On level ", i, "I added feature ", feature_to_add_at_this_level, " to current set")

    print("The best accuracy is ", best_of_all, "with features ", set_of_best)


def main():

    print("Welcome to Cruz Ramirez's Forward Feature Selection Algorithm.\nType in a '1' for searching the small dataset 113 or a '2' for searching the large dataset 122:")

    userdata = int(input())

    if userdata == 1:
        data = np.loadtxt('CS170_Small_Data__113.txt')

    elif userdata == 2:
        data = np.loadtxt('CS170_Large_Data__122.txt')

    feature_search(data,userdata)
    

if __name__ == "__main__":
    main()


