'''
This program prints the efficient robots recognised by the paper written by the contributors which satisfy the input specificaiton ranges provide by a user.
The csv files containing data of Fanuc, Kuka, ABB, Yaskawa and Universal Robots should be in the root directory of the
cuurent Python file.
Disclaimer: Under no circumstances, the contributors of this code be liable for any direct or indirect condsequential damages.
'''
import math
import csv
import glob, os
root_directory=os.path.dirname(os.path.abspath(__file__))

def get_variable_name(variable):
   """
   This function take a variable and returns its name in string format
   """
   variable_dicts=globals()
   for name in variable_dicts:
      if id(variable_dicts[name])==id(variable):
         return(name)

def print_selected_robots(max_payload=math.inf, min_payload=-math.inf, max_weight=math.inf, min_weight=-math.inf, max_reach=math.inf, min_reach=-math.inf, max_rep=math.inf, min_rep=-math.inf, max_AMAS=math.inf, min_AMAS=-math.inf, max_dof= 15, min_dof=1, type="not specified") ->None:

    """
    Prints efficient industrial robots or cobots with specifications fall within the input ranges.
 
    Args:
    max_payload (float): maximum payload capacity of the robot in kg with the default value of +infinitive.
    max_payload (float): minimum payload capacity of the robot in kg.
    max_weight (float): maximum weight of the robot in kg with the default value of +infinitive.
    min_weight (float): minimum weight of the robot in kg.
    max_reach (float): maximum weight of the robot in mm with the default value of +infinitive.
    min_reach (float): minimum weight of the robot in mm.
    max_rep (float): maximum repeatability of the robot in mm with the default value of +infinitive.
    min_rep (float): minimum repeatability of the robot in mm.
    max_AMAS (float): maximum average of maximum angular speeds (AMAS) of the robot in mm with the default value of +infinitive.
    min_AMAS (float): minimum average of maximum angular speeds (AMAS) of the robot in mm.
    max_dof (int): maximum DOF of the robot with the default value of 15.
    min_dof (int): minimum DOF of the robot with the default value of 1.
    type (string): The type of the robot can be either "IR" (industril robot), "cobot" (industrial cobot) or "not specified" with the default value of "not specified".
    
    Returns:
        Nothing. It prints the selected robots.
    """
    # Importing data of Kuka.CSV ---------------------------------------------
    Kuka={}
    Kuka_csv_dir= root_directory+"\\Kuka.csv"
    opened_csv_file=open(Kuka_csv_dir, newline="")
    # Getting data from Kuka.csv file
    Object_of_dictionaries=csv.DictReader(opened_csv_file, delimiter=",")
    for row_dict in Object_of_dictionaries: # we should create the dictionary when the file is still open
        Kuka[row_dict["Robot's model"]]={"n": int(row_dict["Number in group"]), "w":float(row_dict["weight"]), "p":float(row_dict["payload"]), "r": float(row_dict["reach"]), "a":float(row_dict["A factor"]), "rep":float(row_dict["Repeatability"]), "b": float(row_dict["B factor"]), "avg":float(row_dict["avg"]), "dof":int(row_dict["DOF"]), "t":row_dict["type"]}
    opened_csv_file.close()

    # Importing data of ABB.CSV ---------------------------------------------
    ABB={}
    ABB_csv_dir= root_directory+"\\ABB.csv"
    opened_csv_file=open(ABB_csv_dir, newline="")
    # Getting data from ABB.csv file
    Object_of_dictionaries=csv.DictReader(opened_csv_file, delimiter=",")
    for row_dict in Object_of_dictionaries: # we should create the dictionary when the file is still open
        ABB[row_dict["Robot's model"]]={"n": int(row_dict["Number in group"]), "w":float(row_dict["weight"]), "p":float(row_dict["payload"]), "r": float(row_dict["reach"]), "a":float(row_dict["A factor"]), "rep":float(row_dict["Repeatability"]), "b": float(row_dict["B factor"]), "avg":float(row_dict["avg"]), "dof":int(row_dict["DOF"]), "t":row_dict["type"]}

    opened_csv_file.close()

    # Importing data of Universal Robotics.CSV ---------------------------------------------
    UR={}
    UR_csv_dir= root_directory+"\\Universal Robots.csv"
    opened_csv_file=open(UR_csv_dir, newline="")
    # Getting data from UR.csv file
    Object_of_dictionaries=csv.DictReader(opened_csv_file, delimiter=",")
    for row_dict in Object_of_dictionaries: # we should create the dictionary when the file is still open
        UR[row_dict["Robot's model"]]={"n": int(row_dict["Number in group"]), "w":float(row_dict["weight"]), "p":float(row_dict["payload"]), "r": float(row_dict["reach"]), "a":float(row_dict["A factor"]), "rep":float(row_dict["Repeatability"]), "b": float(row_dict["B factor"]), "avg":float(row_dict["avg"]), "dof":int(row_dict["DOF"]), "t":row_dict["type"]}

    opened_csv_file.close()


    # Importing data of Fanuc.CSV ---------------------------------------------
    Fanuc={}
    Fanuc_csv_dir= root_directory+ "\\Fanuc.csv"
    opened_csv_file=open(Fanuc_csv_dir, newline="")
    # Getting data from Fanuc.csv file
    Object_of_dictionaries=csv.DictReader(opened_csv_file, delimiter=",")
    for row_dict in Object_of_dictionaries: # we should create the dictionary when the file is still open
        Fanuc[row_dict["Robot's model"]]={"n": int(row_dict["Number in group"]), "w":float(row_dict["weight"]), "p":float(row_dict["payload"]), "r": float(row_dict["reach"]), "a":float(row_dict["A factor"]), "rep":float(row_dict["Repeatability"]), "b": float(row_dict["B factor"]), "avg":float(row_dict["avg"]), "dof":int(row_dict["DOF"]), "t":row_dict["type"]}

    opened_csv_file.close()

    # Importing data of Yaskawa.CSV ---------------------------------------------
    Yaskawa={}
    Fanuc_csv_dir= root_directory+"\\Yaskawa.csv"
    opened_csv_file=open(Fanuc_csv_dir, newline="")
    # Getting data from Fanuc.csv file
    Object_of_dictionaries=csv.DictReader(opened_csv_file, delimiter=",")
    for row_dict in Object_of_dictionaries: # we should create the dictionary when the file is still open
        Yaskawa[row_dict["Robot's model"]]={"n": int(row_dict["Number in group"]), "w":float(row_dict["weight"]), "p":float(row_dict["payload"]), "r": float(row_dict["reach"]), "a":float(row_dict["A factor"]), "rep":float(row_dict["Repeatability"]), "b": float(row_dict["B factor"]), "avg":float(row_dict["avg"]), "dof":int(row_dict["DOF"]), "t":row_dict["type"]}

    opened_csv_file.close()

    manufacturers=[Kuka, ABB, Fanuc, Yaskawa, UR]

    for manufacturer in manufacturers:
        for robot in manufacturer:
            if manufacturer[robot]["avg"]!=0 and manufacturer[robot]["rep"]!=0:
                manufacturer[robot]["c"]=round(manufacturer[robot]["p"]*manufacturer[robot]["r"]* manufacturer[robot]["avg"]/(manufacturer[robot]["rep"]*manufacturer[robot]["w"]*1000), 1)
            else:
                manufacturer[robot]["c"]=0
    list_of_selected_robots=[]
    for manufacturer in manufacturers:
        for robot in manufacturer:
            if (manufacturer[robot]["c"] >= 247.5  and manufacturer[robot]["c"]<=5525.1 and manufacturer[robot]["b"] >= 2355.0  and manufacturer[robot]["b"]<=17040.6 and manufacturer[robot]["a"] >= 105.7 and manufacturer[robot]["a"]<=828.1): # bounds have been calculated in the paper
                if (manufacturer[robot]["p"]>= min_payload and manufacturer[robot]["p"]<=max_payload and manufacturer[robot]["w"]>= min_weight and manufacturer[robot]["w"]<=max_weight and manufacturer[robot]["r"]>= min_reach and manufacturer[robot]["r"]<=max_reach and manufacturer[robot]["rep"]>= min_rep and manufacturer[robot]["rep"]<=max_rep and manufacturer[robot]["avg"]>= min_AMAS and manufacturer[robot]["avg"]<= max_AMAS and manufacturer[robot]["dof"]>= min_dof and manufacturer[robot]["dof"]<=max_dof):
                    if (type=="not specified"):
                        list_of_selected_robots.append((manufacturer[robot]["c"], robot))
                    elif (type=="IR" and manufacturer[robot]["t"]=="IR"):
                        list_of_selected_robots.append((manufacturer[robot]["c"], robot))
                    elif (type=="cobot" and (manufacturer[robot]["t"]=="cobot" or manufacturer[robot]["t"]=="Cobot")):
                        list_of_selected_robots.append((manufacturer[robot]["c"], robot ))

    
    list_of_selected_robots=sorted(list_of_selected_robots, reverse=True) # to sort based on C factor (first element of the tuples) from the highest to the lowest
    
    for elements in list_of_selected_robots:
        print(elements[1], " with C factor: ", elements[0])

# Calling the function
print_selected_robots(max_payload=10,  min_payload=2, type="cobot")