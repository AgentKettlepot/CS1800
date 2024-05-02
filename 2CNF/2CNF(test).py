'''
1. Instantiate a list Var_ID to store all variables and Var_Nodes to store all Nodes
2. Read file line by line
3. For every line:
    A.   Read both variables
    B.   If the variable ID's are NOT in Var_ID (ID: Xi=2i-1 ; !Xi=2i )
        1. Store the variables in Var_ID by their ID
            - ID: Xi=2i-1 ; !Xi=2i 
        2. Create a Node object for every variable with:
            - ID
            - Pointers: array of other IDs
            - Boolean value: (P → Q) ↔ (¬P ∨ Q)
                             Contrapositive: (¬Q→¬P) ↔ (Q ∨ ¬P)
        3. Add the new Node to Var_Nodes
        
    C. If the variable ID's are IN Var_ID:
        1. Don't add them to Var_ID
        2. Access their Node objects and add new Pointers


4. Sort VAR_NODE by IDs

# At this point, we should have a graph with 2N Nodes, where
# N is the number of variables. Start traversing the Var_NODES
# list by element


5. For node in VAR_NODE
    1. Set "counterpart" to opposite
        1. If element.ID=odd, set ID+1 to opposite
        2. If element.ID=even, set ID-1 to opposite
    2. Access Node with ID=ID and its pointers

    3. For each pointer:
        1. If the pointer is True/Null: 
            1. Good, set it to True and its counterpart to False
            2. Recursively call its pointers and check them
        2. If the pointer is False: 
            1. Doesn't work! Break and check ID=ID+1
'''


class Node:
    def __init__(self, ID, pointers, bool_val):
        self.ID=ID
        self.pointers=pointers
        self.bool_val=bool_val
#Step 1
VAR_ID=[] 
VAR_NODE=[] #Stores the nodes 

def VarIDSetup(ID_1, ID_2):
    # OR to Implication:  (P → Q) ↔ (¬P ∨ Q)
    # Not VAR_ONE should point to Var_TWO
    print(VAR_ID)
    for node in VAR_NODE:
        print(node.ID)

    if (ID_1 not in VAR_ID):
        VAR_ID.append(ID_1)
     # We need to check if the NOT VAR_ONE node is in the VAR_ID list
    NOT_VAR_ID = ID_1-1 if ID_1%2==0 else ID_1+1
    # If the NOT_VAR is already in the list, we can add the implication relationship
    if (NOT_VAR_ID in VAR_ID):
        VAR_NODE[NOT_VAR_ID-1].pointers.append(ID_2)
    else:
        # If the NOT_VAR is NOT in the var_id list, we need to create it 
        # and insert the implication relationship
        not_var_id_node = Node(NOT_VAR_ID, ID_2, None)
        VAR_NODE.append(not_var_id_node)
        VAR_NODE = sorted(VAR_NODE, key=lambda x:x.ID)



#Step 2
f = open("test0.txt", "r")
next(f)
for x in f:
    space_pos = x.find(" ")
    #3A
    var_one = x[:space_pos]
    var_two = x[space_pos:]
    #3B
    ID_1 = ID_2 = 0
    if ("-" in var_one):
        ID_1=2*int(var_one[-1])
    else:
        ID_1=2*int(var_one)-1
    if ("-" in var_two):
        ID_2=2*int(var_two[:-1])
    else:
        ID_2=2*int(var_two)-1
    #print(str(ID_1) + " " + str(ID_2))

    #3C
    #VarIDSetup(ID_1, ID_2)
    #VarIDSetup(ID_2)
    #print(x)

