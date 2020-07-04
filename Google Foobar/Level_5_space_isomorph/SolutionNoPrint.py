##############################################################################################################################################################################################
# Overview:
#
# We will use Polya's Enumeration Theorem.
# After discoverying Burnside's Lemma, googling "Burnside's Lemma on a 2d matrix" points us to 
# the mathematical solution. Link below at (1).
# 
###############################################################################################
# Details:
#
# Conviently, when considering the action of just swapping rows (or just swapping columns)
# the possible permutations for the action forms a symmetical group. Meaning the resulting cycle
# index from the symmetrical group of size X will always be the same. 
#
# So for this program we will treat the cycle indicies like 12 known equations, (like the Free-Fall 
# equation from physics, but instead there are 12 different equations)
# So this program has hard coded the cycle indicies for the symmetical groups of size 1 to 12.
#
# The cycle indicies of size 1 to 12 were obtained from Mathematica. See link below at (2) and my work at (3)
# I ran CycleIndexPolynomial[ SymmetricGroup[3], {x1,x2,x3}] from size 1 to 12 and copy & pasted the polynomial.
# This program reads and converts the pasted/hard-coded string into meaningful data to compute the actual solution.
#
# Might sound odd but given the scope of the problem it works perfectly and is very efficent computationally and for development.
#
###############################################################################################
# Links:
#
# (1) Burnside's Lemma applied to grids with interchanging rows and columns - https://math.stackexchange.com/questions/2113657/burnsides-lemma-applied-to-grids-with-interchanging-rows-and-columns
# (2) Symmetic Group - https://mathworld.wolfram.com/SymmetricGroup.html
# (3) a. https://drive.google.com/file/d/1c7EYU2B0BjxE_x335G5gMpGubAyieVWi/view?usp=sharing
#     b. https://drive.google.com/file/d/1YzPLpQbpvt23y8cFvO4xKJLUExv7Dblt/view?usp=sharing
#     c. https://drive.google.com/file/d/1ybWvfgfgFIGhz8B3v2djZwO8cNDZwqag/view?usp=sharing
#
#
###############################################################################################
# Sources:
# 
# Combinatorics 16.12 The Pattern Inventory  Polyas Method of Enumeration - https://www.youtube.com/watch?v=Tkz8QGPHxdA
# Combinatorics 16.10 Counting and Equivalence - Burnsides Theorem - https://www.youtube.com/watch?v=wvofB5tZz3Y
# Visual Group Theory, Lecture 5.2: The orbit-stabilizer theorem - https://www.youtube.com/watch?v=AnJOjE8nVFY
# Polya Theorem (Part 2) - https://www.youtube.com/watch?v=zQZ4kTiaqQI
# Lecture 5: Burnsides Lemma and the Polya Enumeration Theorem - http://web.math.ucsb.edu/~padraic/ucsb_2014_15/math_116_s2015/math_116_s2015_lecture5.pdf
# POLYAS COUNTING THEORY - https://www.whitman.edu/Documents/Academics/Mathematics/Huisinga.pdf
# BURNSIDE-POLYA COUNTING - Graph Enumeration http://www.cs.columbia.edu/~cs4205/files/CM9.pdf
# How many distinct unsolvable Rubik's cubes exist? - https://puzzling.stackexchange.com/questions/525/how-many-distinct-unsolvable-rubiks-cubes-exist
# (crl + f = matrices) List of Generalizations of Common Questions - https://math.meta.stackexchange.com/questions/1868/list-of-generalizations-of-common-questions#13335
#
# https://mathematica.wolframcloud.com/
#
###############################################################################################
import math 
import decimal


# Using the vocab from http://www.cs.columbia.edu/~cs4205/files/CM9.pdf (Section 9.1, page 13)
# If a cycle Index = (x_1 x_2)/2 + x_3/3 ----> (x_1*x_2 / 2) is one of the two Cycle Structures
class CycleStructure: 
    # ex) my_cycle_struct = (1/6) * [(t_2)^5 + (t_3)]  ---> cycles = [(t_2)^3 , t_3], coefficient = 1/6
    def __init__(self, coefficient=1):
        self.coefficient = coefficient 
        self.cycles = []

    class Cycle:
        # ex) (t_2)^5 --> subscript = 2, power = 5
        def __init__(self, subscript, power):  
            if power == "":
                power = 1
            self.subscript = int(subscript) # cycle length
            self.power = int(power)         # is the number of cycles with length x in the permutation.
        def __repr__(self):
            return "(X{0})^{1}".format(self.subscript, self.power)



class StarGrid:
    def __init__(self):
        self.num_states = None
        self.cycle_indecies = [[] for x in range(12)] # for clarity (b/c we dont use 12)
        
        # All equation copied from Mathematica 
        self.raw_cycle_indecies = []
        self.raw_cycle_indecies.append("x1")
        self.raw_cycle_indecies.append("x1^2/2 + x2/2")
        self.raw_cycle_indecies.append("x1^3/6 + (x1*x2)/2 + x3/3")
        self.raw_cycle_indecies.append("x1^4/24 + (x1^2*x2)/4 + x2^2/8 + (x1*x3)/3 + x4/4")
        self.raw_cycle_indecies.append("x1^5/120 + (x1^3*x2)/12 + (x1*x2^2)/8 + (x1^2*x3)/6 + (x2*x3)/6 + (x1*x4)/4 + x5/5")
        self.raw_cycle_indecies.append("x1^6/720 + (x1^4*x2)/48 + (x1^2*x2^2)/16 + x2^3/48 + (x1^3*x3)/18 + (*x1*x2*x3)/6 + x3^2/18 + (x1^2*x4)/8 + (x2*x4)/8 + (x1*x5)/5 + x6/6")
        self.raw_cycle_indecies.append("x1^7/5040 + (x1^5*x2)/240 + (x1^3*x2^2)/48 + (x1*x2^3)/48 + (x1^4*x3)/72 + 1/12*x1^2*x2*x3 + (x2^2*x3)/24 + (x1*x3^2)/18 + (x1^3*x4)/24 + (x1*x2*x4)/8 + (x3*x4)/12 + (x1^2*x5)/10 + (x2*x5)/10 + (x1*x6)/6 + x7/7")
        self.raw_cycle_indecies.append("x1^8/40320 + (x1^6*x2)/1440 + (x1^4*x2^2)/192 + (x1^2*x2^3)/96 + x2^4/384 + (x1^5*x3)/360 + 1/36*x1^3*x2*x3 + 1/24*x1*x2^2*x3 + (x1^2*x3^2)/36 + (x2*x3^2)/36 + (x1^4*x4)/96 + 1/16*x1^2*x2*x4 + (x2^2*x4)/32 + (x1*x3*x4)/12 + x4^2/32 + (*x1^3*x5)/30 + (x1*x2*x5)/10 + (x3*x5)/15 + (x1^2*x6)/12 + (x2*x6)/12 + (x1*x7)/7 + x8/8")
        self.raw_cycle_indecies.append("x1^9/362880 + (x1^7*x2)/10080 + (x1^5*x2^2)/960 + (x1^3*x2^3)/288 + (*x1*x2^4)/384 + (x1^6*x3)/2160 + 1/144*x1^4*x2*x3 + 1/48*x1^2*x2^2*x3 + (x2^3*x3)/144 + (x1^3*x3^2)/108 + 1/36*x1*x2*x3^2 + x3^3/162 + (x1^5*x4)/480 + 1/48*x1^3*x2*x4 + 1/32*x1*x2^2*x4 + 1/24*x1^2*x3*x4 + (x2*x3*x4)/24 + (x1*x4^2)/32 + (x1^4*x5)/120 + 1/20*x1^2*x2*x5 + (x2^2*x5)/40 + (x1*x3*x5)/15 + (x4*x5)/20 + (x1^3*x6)/36 + (x1*x2*x6)/12 + (x3*x6)/18 + (x1^2*x7)/14 + (x2*x7)/14 + (x1*x8)/8 + x9/9")
        self.raw_cycle_indecies.append("x1^10/3628800 + x10/10 + (x1^8*x2)/80640 + (x1^6*x2^2)/5760 + (x1^4*x2^3)/1152 + (x1^2*x2^4)/768 + x2^5/3840 + (x1^7*x3)/15120 + 1/720*x1^5*x2*x3 + 1/144*x1^3*x2^2*x3 + 1/144*x1*x2^3*x3 + (x1^4*x3^2)/432 + 1/72*x1^2*x2*x3^2 + (x2^2*x3^2)/144 + (x1*x3^3)/162 + (x1^6*x4)/2880 + 1/192*x1^4*x2*x4 + 1/64*x1^2*x2^2*x4 + (x2^3*x4)/192 + 1/72*x1^3*x3*x4 + 1/24*x1*x2*x3*x4 + (x3^2*x4)/72 + (x1^2*x4^2)/64 + (x2*x4^2)/64 + (x1^5*x5)/600 + 1/60*x1^3*x2*x5 + 1/40*x1*x2^2*x5 + 1/30*x1^2*x3*x5 + (x2*x3*x5)/30 + (x1*x4*x5)/20 + x5^2/50 + (x1^4*x6)/144 + 1/24*x1^2*x2*x6 + (x2^2*x6)/48 + (x1*x3*x6)/18 + (x4*x6)/24 + (x1^3*x7)/42 + (x1*x2*x7)/14 + (x3*x7)/21 + (x1^2*x8)/16 + (x2*x8)/16 + (x1*x9)/9")
        self.raw_cycle_indecies.append("x1^11/39916800 + (x1*x10)/10 + x11/11 + (x1^9*x2)/725760 + (x1^7*x2^2)/40320 + (x1^5*x2^3)/5760 + (x1^3*x2^4)/2304 + (x1*x2^5)/3840 + (x1^8*x3)/120960 + (x1^6*x2*x3)/4320 + 1/576*x1^4*x2^2*x3 + 1/288*x1^2*x2^3*x3 + (x2^4*x3)/1152 + (x1^5*x3^2)/2160 + 1/216*x1^3*x2*x3^2 + 1/144*x1*x2^2*x3^2 + (x1^2*x3^3)/324 + (x2*x3^3)/324 + (x1^7*x4)/20160 + 1/960*x1^5*x2*x4 + 1/192*x1^3*x2^2*x4 + 1/192*x1*x2^3*x4 + 1/288*x1^4*x3*x4 + 1/48*x1^2*x2*x3*x4 + 1/96*x2^2*x3*x4 + 1/72*x1*x3^2*x4 + (x1^3*x4^2)/192 + 1/64*x1*x2*x4^2 + (x3*x4^2)/96 + (x1^6*x5)/3600 + 1/240*x1^4*x2*x5 + 1/80*x1^2*x2^2*x5 + (x2^3*x5)/240 + 1/90*x1^3*x3*x5 + 1/30*x1*x2*x3*x5 + (x3^2*x5)/90 + 1/40*x1^2*x4*x5 + (x2*x4*x5)/40 + (x1*x5^2)/50 + (x1^5*x6)/720 + 1/72*x1^3*x2*x6 + 1/48*x1*x2^2*x6 + 1/36*x1^2*x3*x6 + (x2*x3*x6)/36 + (x1*x4*x6)/24 + (x5*x6)/30 + (x1^4*x7)/168 + 1/28*x1^2*x2*x7 + (x2^2*x7)/56 + (x1*x3*x7)/21 + (x4*x7)/28 + (x1^3*x8)/48 + (x1*x2*x8)/16 + (x3*x8)/24 + (x1^2*x9)/18 + (x2*x9)/18")
        self.raw_cycle_indecies.append("x1^12/479001600 + (x1^2*x10)/20 + (x1*x11)/11 + x12/12 + (x1^10*x2)/7257600 + (x10*x2)/20 + (x1^8*x2^2)/322560 + (x1^6*x2^3)/34560 + (x1^4*x2^4)/9216 + (x1^2*x2^5)/7680 + x2^6/46080 + (x1^9*x3)/1088640 + (x1^7*x2*x3)/30240 + (x1^5*x2^2*x3)/2880 + 1/864*x1^3*x2^3*x3 + (x1*x2^4*x3)/1152 + (x1^6*x3^2)/12960 + 1/864*x1^4*x2*x3^2 + 1/288*x1^2*x2^2*x3^2 + (x2^3*x3^2)/864 + (x1^3*x3^3)/972 + 1/324*x1*x2*x3^3 + x3^4/1944 + (x1^8*x4)/161280 + (x1^6*x2*x4)/5760 + 1/768*x1^4*x2^2*x4 + 1/384*x1^2*x2^3*x4 + (x2^4*x4)/1536 + (x1^5*x3*x4)/1440 + 1/144*x1^3*x2*x3*x4 + 1/96*x1*x2^2*x3*x4 + 1/144*x1^2*x3^2*x4 + 1/144*x2*x3^2*x4 + (x1^4*x4^2)/768 + 1/128*x1^2*x2*x4^2 + (x2^2*x4^2)/256 + 1/96*x1*x3*x4^2 + x4^3/384 + (x1^7*x5)/25200 + (x1^5*x2*x5)/1200 + 1/240*x1^3*x2^2*x5 + 1/240*x1*x2^3*x5 + 1/360*x1^4*x3*x5 + 1/60*x1^2*x2*x3*x5 + 1/120*x2^2*x3*x5 + 1/90*x1*x3^2*x5 + 1/120*x1^3*x4*x5 + 1/40*x1*x2*x4*x5 + (x3*x4*x5)/60 + (x1^2*x5^2)/100 + (x2*x5^2)/100 + (x1^6*x6)/4320 + 1/288*x1^4*x2*x6 + 1/96*x1^2*x2^2*x6 + (x2^3*x6)/288 + 1/108*x1^3*x3*x6 + 1/36*x1*x2*x3*x6 + (x3^2*x6)/108 + 1/48*x1^2*x4*x6 + (x2*x4*x6)/48 + (x1*x5*x6)/30 + x6^2/72 + (x1^5*x7)/840 + 1/84*x1^3*x2*x7 + 1/56*x1*x2^2*x7 + 1/42*x1^2*x3*x7 + (x2*x3*x7)/42 + (x1*x4*x7)/28 + (x5*x7)/35 + (x1^4*x8)/192 + 1/32*x1^2*x2*x8 + (x2^2*x8)/64 + (x1*x3*x8)/24 + (x4*x8)/32 + (x1^3*x9)/54 + (x1*x2*x9)/18 + (x3*x9)/27")

    # Essentially it's plug and chug math
    def calculate_orbits(self, cycle_index): 
        total_orbits = long(0)
        sum_remainder = 0

        for cyc_struct in cycle_index:
            # Numerator
            orbits = long(1)
            for cyc in cyc_struct.cycles:
                num = self.num_states ** cyc.power
                orbits = orbits * num
                
            # Denominator
            quotient, remainder = divmod(orbits, cyc_struct.coefficient)
            fraction = remainder / decimal.Decimal(cyc_struct.coefficient)
            sum_remainder = sum_remainder + fraction

            # Sumation    
            total_orbits = total_orbits + quotient
            
        # Final Sumation
        total_orbits = total_orbits + long(round(sum_remainder))
        return total_orbits

    # https://math.stackexchange.com/questions/2056708/number-of-equivalence-classes-of-w-times-h-matrices-under-switching-rows-and
    # Returns the cycle permutations across two cycles, ie the cycles between the row and column. ... All permutations
    # We return: X_lcm(q1,q2) ^(gcd(q1,q2)*power1*power2)
    def computePair(self, cyc_struct_1, cyc_struct_2):
        coefficient = cyc_struct_1.coefficient * cyc_struct_2.coefficient
        cyc_struct = CycleStructure(coefficient)

        for cyc1 in cyc_struct_1.cycles:
            for cyc2  in cyc_struct_2.cycles:
                subscript = lcm(cyc1.subscript, cyc2.subscript)
                power = gcd(cyc1.subscript, cyc2.subscript) * cyc1.power * cyc2.power
                cycle = cyc_struct.Cycle(subscript, power)
                cyc_struct.cycles.append(cycle)
        return cyc_struct

    # Returns the cycle index for our HxW matrix. Product is of two permutations
    def create_cartesian_product(self, cycle_index_1, cycle_index_2):
        product = [] # I represent "a + b + c" as [a,b,c]
        for cyc_struct_1 in cycle_index_1:
            for cyc_struct_2 in cycle_index_2:
                newcycleStuct = self.computePair(cyc_struct_1, cyc_struct_2)
                product.append(newcycleStuct)
        return product

    # String --> data types
    def convert_raw_cycle_index_to_objects(self, p):
        if self.cycle_indecies[p]:
            return
        raw_indecies = self.raw_cycle_indecies[p].split('+')
        for x in raw_indecies:
            cyc_struct = self.run_lexer(x.strip())
            self.cycle_indecies[p].append(cyc_struct)

    def getNext(self, cyc_string, i):
        i = i + 1
        data = ""
        while i < len(cyc_string) and  cyc_string[i].isdigit() :
            data = data + cyc_string[i]
            i = i + 1
        return data, i
        
    def run_lexer(self, cyc_string): #Pretend it's a lexer
        i = 0
        cyc_struct = CycleStructure()

        subscript = ""
        power = ""        
        while i < len(cyc_string) :
            data = ""
            if cyc_string[i].upper() == "X":
                data,i = self.getNext(cyc_string, i)    
                subscript = data
                if i == len(cyc_string):
                    cycleVar = CycleStructure.Cycle(subscript, power)
                    cyc_struct.cycles.append(cycleVar)
                continue

            if cyc_string[i].upper() == "^":
                data,i = self.getNext(cyc_string, i)                
                power = data if data != "" else 1

                cycleVar = CycleStructure.Cycle(subscript, power)
                cyc_struct.cycles.append(cycleVar)
                subscript = ""
                power = ""
                continue

            if subscript != "" and power == "":
                #power = 1
                cycleVar = CycleStructure.Cycle(subscript, power)
                cyc_struct.cycles.append(cycleVar)
                subscript = ""
                power = ""
                
            if cyc_string[i].upper() == "/":
                data,i = self.getNext(cyc_string, i)
                cyc_struct.coefficient = int(data)
                continue

            i = i + 1
        return cyc_struct

def gcd(a, b):
    while( a % b > 0):
        remainder = a % b
        a = b
        b = remainder
    return b

def lcm(a, b):
    return a*b/gcd(a,b)

def solution(h,w,s):
    
    starGrid = StarGrid()
    starGrid.num_states = s

    starGrid.convert_raw_cycle_index_to_objects(h-1)
    starGrid.convert_raw_cycle_index_to_objects(w-1)

    cycle_index_1 = starGrid.cycle_indecies[h-1] 
    cycle_index_2 = starGrid.cycle_indecies[w-1] 
    product_cycle_index = starGrid.create_cartesian_product(cycle_index_1, cycle_index_2)

    total_orbits = starGrid.calculate_orbits(product_cycle_index)

    return str(total_orbits)

if __name__ == '__main__':
    # good precsion example.  20021086[0] @  h = 7,  w = 3, s = 4 is 0
    # 12, 12, 20 => 97195340925396730736950973830781340249131679073592360856141700148734207997877978005419735822878768821088343977969209139721682171487959967012286474628978470487193051591840
    h = 12
    w = 12
    s = 20

    x = solution(h,w,s)
    print x

