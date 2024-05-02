import copy
import math

# PART A - BRUTE FORCE
def genBros (n):
    l = []
    for i in range(1, n+1):
        l.append(["a"+str(i), "b"+str(i)])
    return l

def genSis (n):
    l = []
    for i in range (1, n+1):
        l.append(["x"+str(i)])
        l.append(["y" + str(i)])
    return l

def getSis(str):
    if str[0:1] == "x":
        return "y" + str[1:]
    else:
        return "x" + str[1:]

def getDates(b, s, no_pair):
    perms = []
    temp_sisters = copy.deepcopy(s)
    while len(temp_sisters) != 0 and not(len(temp_sisters) == 1 and temp_sisters[0][0] == no_pair):
        datepair = []
        pivot_sis = ""
        for i in temp_sisters:
            if len(i)==1 and i[0] != no_pair:
                pivot_sis = i[0]
                datepair = [pivot_sis, b[0][0]]
                temp_sisters.remove(i)
                break
        sub_perm = []
        temp_brothers = copy.deepcopy(b)
        temp_brothers[0].remove(temp_brothers[0][0])
        new_sisters = []
        for i in s:
            if i != [pivot_sis]:
                new_sisters.append(i)
        if len(new_sisters) == 0:
            perms.append(datepair)
        else:
            if len(temp_brothers[0]) == 0:
                sub_perm = getDates(temp_brothers[1:], new_sisters, "")
            else:
                sub_perm = getDates(temp_brothers, new_sisters, getSis(pivot_sis))

            for i in sub_perm:
                if len(sub_perm) != 1:
                    i.append([pivot_sis, b[0][0]])
                    perms.append(i)
                else:
                    perms.append([i, [pivot_sis, b[0][0]]])
    return perms

print("1 pair of each: " + str(len(getDates(genBros(1), genSis(1), ""))))
print("2 pair of each: " + str(len(getDates(genBros(2), genSis(2), ""))))
print("3 pair of each: " + str(len(getDates(genBros(3), genSis(3), ""))))
print("4 pair of each: " + str(len(getDates(genBros(4), genSis(4), ""))))


# PART B - T(N) with recurrence
def cycle(n):
    return (2 ** (2 * n - 1)) * math.factorial(n) * math.factorial(n - 1)
print("CYCLES - 1 pair: " + str(cycle(1)))
print("CYCLES - 2 pair: " + str(cycle(2)))
print("CYCLES - 3 pair: " + str(cycle(3)))
print("CYCLES - 4 pair: " + str(cycle(4)))

def count_dates(n):
    total = cycle(n)
    for k in range (2, n - 1):
        total += count_dates(n - k)* cycle(k) *  math.comb(n - 1, k - 1) * math.comb(n, k)
    return total
print("1 pair: " + str(count_dates(1)))
print("2 pair: " + str(count_dates(2)))
print("3 pair: " + str(count_dates(3)))
print("4 pair: " + str(count_dates(4)))

# Part C
total = [0, 16]
def calc_n(n):
    for i in range (3, n+1):
        tot = math.comb(i, 2)*math.comb(i-1, 1) * total[i-3] * 16 + total[i-2] * i * (i-1) * 4
        total.append(tot)
    return total
print(calc_n(5))