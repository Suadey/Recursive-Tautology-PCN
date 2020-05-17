'''
*****************************************
*                                       *
* Unate Recursive Complement Calculator *
*                                       *
* Python SDK : 3.8.1                    *
* Author : Siddhi Pandare               *
* Version : 1.0.0                       *
*                                       *
*****************************************
'''

# Parses Input Array to a PCN list.
def Input_PCN ( file ):
    array =File_to_list (file) # Get Input Parsed into a List of Numbers.
    vars_in = array[0][0] # Numbers of Total Variables in Function.
    cubes_in = array[1][0] # Numbers of Total Cubes in Function.
    all_cubes = [  [ '11' for y in range(0, vars_in)]  for x in range(0, cubes_in) ]
    for x in range (2,len(array)):
        for y in range (1,len(array[x]) ):
            number = array[x][y]
            ins = '01'
            if number < 0:
                number = abs(number)
                ins = '10'
            all_cubes[x-2][number-1]=ins
    return all_cubes,cubes_in,vars_in

# Parses input File in List seperated by lines.
def File_to_list (file ):
    file=file.read()
    file=file.split("\n")
    list_inputs=[[int(i) for i in x.split(" ")  if i != ""] for x in file if x != '' ]
    return list_inputs

#Returns Shannon's Positive and Negative Cofactor 
def Cofactor_Calculator(function,bin_var,type_c,vars_in):
    ps_c = []
    apped = 0
    bound = '01'
    if type_c == '1': # Positive.
        bound = '10'
    for x in range (len(function)):
        if not function[x][bin_var] == bound:
            ps_c.append([]) # Inster New Cube.
            for y in range (len(function[x])):
                ps_c[apped].append(function[x][y])
            ps_c[apped][bin_var] = '11'
            apped+=1
    n_t_p = 0
    for x in range (len(ps_c)):
        count = 0
        for y in range (vars_in):
            if ps_c[x][y] == '11' :
                 count+=1
        if count == vars_in:
            n_t_p = 1
            lis_t_p = x   
    if n_t_p == 1 :
        rs_c = []
        rs_c.append([]) # Inster New Cube.
        rs_c[0] = ['11'] * vars_in
        return rs_c
    return ps_c

def Binate_Var ( function , vars_c ):
    Tru_Apps = [0] * vars_c
    Com_Apps = [0] * vars_c
    Binate = [0] * vars_c
    Binate_Flag = 0 # Initial flag for Binate Function is false.
    # Check for Binate Variables.
    for y in range ( vars_c ): # Parse all variables. 
        for x in range ( len( function ) ): # On all functions.
            if function[x][y] == '01' :
                Tru_Apps[y]+=1
            elif function[x][y] == '10' :
                Com_Apps[y]+=1
            if Tru_Apps[y] > 0 and Com_Apps[y] > 0 : # Var Is Binate.
                Binate[y] = 1 # Update Binate vars table.
                Binate_Flag = 1 # Function is Binate.
    # If function is Binate, choose the Binate variable which apperas in the most cubes. 
    if Binate_Flag == 1 :
        Binate_Apps = 0 # Threshold.
        Tie_Flag = 0 # Tie flag.
        for y in range ( vars_c ) : 
            if Binate[y] == 1 : # Iff variable is Binate.
                Apps_Temp = Tru_Apps[y] + Com_Apps[y] # Count Binate Variable Xi Appearences.
                if  Binate_Apps < Apps_Temp :
                        Binate_Apps = Apps_Temp # Update Threshold.
                        Tie_Flag = 0 # Reset Tie Flag.
                elif Binate_Apps == Apps_Temp :
                        Tie_Flag = 1 # Invert Tie Flag.
        # Iff there is a tie on the above procedure.
        if  Tie_Flag == 1 :
            # Let T denote the number o cubes where this variable appears in true form.
            # Let C denote the number of cubes where this variable appears in complement form.            
            # Choose the variable that has the smallest value of |T-C|.
            T_minus_C = [-1] * vars_c
            Ratio_Tie_Flag = 0 # Tie flag.
            for y in range ( vars_c ) : 
                if Binate[y] == 1 : 
                    if  Binate_Apps == Tru_Apps[y] + Com_Apps[y]  : # Count Binate Var Xi Appearences.
                        T_minus_C[ y ] = abs( Tru_Apps[y] - Com_Apps[y] ) # Get |T-C|.
                        Min_Ratio = T_minus_C[ y ]  
            # Get Smaller |T-C| Ratio.
            for y in range ( vars_c ) : 
                if  T_minus_C[y] < Min_Ratio and T_minus_C[y] >= 0 :
                    Min_Ratio = T_minus_C[y]
            # Look for Ratio Tie.
            Min_Ratio_Apps = 0
            for y in range ( vars_c ) :
                if ( T_minus_C[y] == Min_Ratio ):
                    Min_Ratio_Apps += 1
                    if Min_Ratio_Apps > 1:
                        Ratio_Tie_Flag = 1
                        break
            if  Ratio_Tie_Flag == 1 : # Again a Tie.
                # Choose the variable with the lowest index.
                for y in range (vars_c) :
                    if  T_minus_C[ y ] == Min_Ratio :
                        return y
            else: # Not a Ratio Tie.
                for y in range (vars_c) :
                    if  T_minus_C[ y ] == Min_Ratio :
                        return y
        else:
            for y in range (vars_c) :
                if Binate[y] == 1 :
                    Apps_Temp = Tru_Apps[y] + Com_Apps[y] # Count Binate Variable Xi Appearences.
                    if ( Binate_Apps == Apps_Temp ) :
                        return y
    else:
        # Choose the unate variable in the most cubes.
        # First Get Unate Table.
        Unate = [0] * vars_c
        for y in range (vars_c) :
            Unate[y] = Com_Apps[y]
            if  Tru_Apps[y] > 0 :
                Unate[y] = Tru_Apps[y]
        # Search for Most Unate Variables. 
        Most_Unate = 0
        for y in range (vars_c) :
            if  Unate[y] > Most_Unate :
                Most_Unate = Unate[y]
        # Search if There are more than One.
        Unate_Apps = 0
        for y in range (vars_c) :
            if Unate[y] == Most_Unate :
                Unate_Apps+=1
        # Get Unate Tie */
        Unate_Tie_Flag = 0
        if  Unate_Apps > 1 :
            Unate_Tie_Flag = 1
        if Unate_Tie_Flag == 1 :
            # Choose the Variable with the lowest index.
            for y in range (vars_c) :
                if  Unate[y] == Most_Unate :
                    return y
        else :
            for y in range (vars_c) :
                if  Unate[y] == Most_Unate :
                    return y

#Complements a simple function straight away
def get_complement(function,vars_in):
    lst_complement=[["11" for i in range (0,vars_in)] for j in range(0,vars_in)]
    k=0 
    counter=0
    for x in range(0,vars_in):
        if function[0][x]=="11":
            k+1
            continue
        elif function[0][x]=="01":
            lst_complement[k][x]="10"
            k=k+1
        elif function[0][x]=="10":
            lst_complement[k][x]="01"
            k=k+1

    val=["11"]*vars_in
    lst_complement=[x for x in lst_complement if x != val]
    return lst_complement

#ANDing of two functions
def PCN_AND ( function , bin_var , var_type ) :
    val = '01'
    if var_type == '0':
        val = '10'
    for x in range(len( function )):
        function[x][bin_var]  = val
    return function

#ORing of functions
def PCN_OR ( function_p , function_n  ) :
    function_ret = []
    function_ret.extend(function_p)
    function_ret.extend(function_n)
    return function_ret

#Function to write output into file
def printer(Out,vars_in,file):
    fh=open("Output"+file,"w")
    fh.write(str(vars_in)+"\n")
    fh.write(str(len(Out))+"\n")
    for x in Out:
        y=[i for i in x if i != "11"]
        fh.write(str(len(y))+" ")
        for i in range(0,len(y)):
            if y[i] == "01":
                fh.write(str(i+1))
            elif y[i] == "10":
                fh.write(str(-(i+1)))
            if i != len(y)-1:
                fh.write(" ")
        fh.write("\n")  
    fh.close()
               

# # Calculation of complement by shannon's expression.
def Complement( function , vars_in ) :
    if  len( function ) == 0 :  # F has no cubes.
        return [[ '11' for y in range(0, vars_in)]]
    elif len( function ) == 1 : # F has Just 1 cube.
        return get_complement ( function , vars_in )
    else :  # Must Do recursion
        binate_var = Binate_Var ( function , vars_in )
        P_C = Cofactor_Calculator ( function , binate_var , '1' , vars_in )
        N_C = Cofactor_Calculator ( function , binate_var , '0' , vars_in ) 
        P_C = Complement( P_C , vars_in )
        N_C = Complement( N_C , vars_in )
        P_C = PCN_AND( P_C , binate_var , '1' )
        N_C = PCN_AND( N_C , binate_var , '0' )
    return PCN_OR( P_C, N_C )

#Main function
def main():
    print("-----------------------------------------")
    print("--UNATE RECURSIVE COMPLEMENT CALCULATOR--")
    print("-----------------------------------------")
    file= input("Enter File: ") #"part5.pcn"
    f_in=open(file,"r")
    # Parse Input Table
    Input_F,cubes_in,vars_in = Input_PCN ( f_in )
    Out = Complement(Input_F,vars_in)
    printer(Out,vars_in,file)
    print("--COMPLEMENTED BOOLEAN FUNCTION PCN IS ---")
    for x in Out:
        print(x)
    f_in.close()
    

main()
