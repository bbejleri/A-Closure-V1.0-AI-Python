############## A-Closure Algorithm V1.0 ############
__author__ = "Bora Bejleri"
__status__ = "Not Finished"

#Composition of base relations lookup table
composition_lookup = {'< c <': '<', '< c =': '<', '< c >': '{<,=,>}', '= c <': '<', '= c =': '=', '= c >': '>',
                      '> c <': '{<,=,>}', '> c =': '>', '> c >': '>' }

constraint_i_j = ['=']

def strIntersection(str1, str2):
  out = ""
  for i in str1:
    if i in str2 and not i in out:
      out += i
  return out

variables = ['i', 'j', 'k'] #not used atm

def aClousure(constraint_i_j):
  new_constraint_table = []
  constraint_i_k = "="
  constraint_k_j = "="
  fixed_point = True

  while(fixed_point):
    fixed_point = False
    for foo in range(len(constraint_i_j)):
        path = str(constraint_i_k) + " " + "c" + " " + str(constraint_k_j)
        new_constraint = strIntersection(constraint_i_j[foo],composition_lookup[path]) #good
        new_constraint_table.append(new_constraint)
    print(new_constraint_table)

    for n in range(len(new_constraint_table)):
        if(new_constraint_table[n] == '' ):
            index = n
            print(index)
            print("Contains empty set i.e not consistent") #empty relation indicates inconsistency
            del constraint_i_j[index] #deletes the relation which is refined into the empty set
            print(constraint_i_j)
            fixed_point = True

def main():
    result = []
    result = aClousure(constraint_i_j)
    print(result)

if __name__== "__main__":
    main()