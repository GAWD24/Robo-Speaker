# import os 
# while True :
#     x = input("sayu : ")
#     if x == "q":
#         os.system("say 'bye bye friend' ")
#         break
#     command = f"say {x}"
#     os.system(command)
print([x for x in range(2,101) if all(x%i != 0 for i in range(2,int(x**(0.5)+1)))])