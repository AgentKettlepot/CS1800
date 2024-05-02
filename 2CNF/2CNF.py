# KEITH YAO
# September 28, 2023
# 2CNF-SAT Parts B and D - CS1800 Accelerated

# PART B
# Converts a list of implications into OR relationships
def makeImplications(clauses):
    bool_imp = [] 
    cont_imp = []
    implications_dict = {}

    for clause in clauses:
        bool_imp.append([(-1)*clause[0], clause[1]])
        cont_imp.append([(-1)*clause[1], clause[0]])
  
    vars = []
    for clause in clauses:
        for num in clause:
            if abs(num) not in vars:
                vars.append(abs(num))

    vars.sort()
    # Value in key-value pair in implications dictionary stores the connected implications
    for i in vars:
        implications_dict[i] = []
        implications_dict[-1*i] = []

    implications = bool_imp + cont_imp
    #print(implications)
    temp = []
    for x in implications:
        if x not in temp:
            temp.append(x)

    implications = temp

    for clause in implications:
        if clause[1] not in implications_dict[clause[0]]:
            implications_dict[clause[0]].append(clause[1])
    #print(implications_dict)
    return implications_dict

def run(file):
   f = open("Tests/"+file, "r")
   clauses = [] # List that stores pairs of variables

   for line in f:
       if line[0:1] != "#" :
            space_pos = line.find(" ")
            var_one = line[:space_pos]
            var_two = line[space_pos:]
            temp = [int(var_one), int(var_two)]
            clauses.append(temp)

   # Turns the list of OR relationships into implications
   graph = makeImplications(clauses) 
   #print(graph)
   need_explore = []
   unassigned = []

    # Adds unconnected nodes to unassigned list
   for clause in clauses:
       for var in clause:
           if abs(var) not in unassigned:
               unassigned.append(abs(var))
   unassigned.sort()
   
   permanent = {}
   temp = {}
   visited = []
   for i in unassigned:
       temp[i] = None
       permanent[i] = None

   start = unassigned[0]
   bool1 = bool2 = None
   var1 = start
   var2 = None

   while True:
       for i in permanent:
           if permanent[i] == None:
               start = i
               break
       need_explore.append(start)
       contradicted = False
       # Explores the implication relationships with first var
       while len(need_explore) > 0:
           var1 = need_explore.pop()
           for i in graph[var1]:
               #print (i)
               if i not in need_explore and i not in visited:
                   need_explore.append(i)
           #print(str(need_explore))

           # Once we finish exploring all the implication relationsips
           if(len(need_explore) == 0):
               if temp[abs(var1)] == None:
                   if var1 < 0:
                       temp[-1 * var1] = False
                   else:
                       temp[var1] = True
               for i in temp:
                   permanent[i] = temp[i]
            # While we are still exploring implications
           else:
               var2 = need_explore.pop()
               if var1 < 0:
                   if temp[-1 * var1] != None:
                       bool1 = not temp[-1 * var1]
                   else:
                       bool1 = True
                       temp[-1 * var1] = False
               else:
                   if temp[var1] != None:
                       bool1 = temp[var1]
                   else:
                       bool1 = True
                       temp[var1] = True

               if var2 < 0:
                   if temp[-1 * var2] != None:
                       bool2 = not temp[-1 * var2]
                   else:
                       bool2 = True
                       temp[-1 * var2] = False
               else:
                   if temp[var2] != None:
                       bool2 = temp[var2]
                   else:
                       bool2 = True
                       temp[var2] = True
               if bool1 and bool2:
                   visited.append(var1)
                   visited.append(var2)
                   need_explore.append(var2)
               else:
                   if contradicted:
                       return False
                   else:
                       contradicted = True
                       visited = []

                       # Sets first branch of permanent values
                       for i in temp:
                           temp[i] = permanent[i]
                       need_explore.clear()
                       need_explore.append(-1*start)
       visited = []
       for i in temp:
           permanent[i] = temp[i]

       assigned = True
       # If there are any unassigned or empty vars, the assignment fails
       #print("perm" + str(permanent))
       for i in permanent:
           if permanent[i] == None:
               assigned = False
       if assigned:
           return permanent

if __name__ == "__main__":
        print("test0: " + str(run("test0.txt")))
        print("test1: " + str(run("test1.txt")))
        print("test2: " + str(run("test2.txt")))
        print("test3: " + str(run("test3.txt")))
        print("test4: " + str(run("test4.txt")))
        print("test5: " + str(run("test5.txt")))
        print("test6: " + str(run("test6.txt")))
        print("test7: " + str(run("test7.txt")))
        print("test8: " + str(run("test8.txt")))
