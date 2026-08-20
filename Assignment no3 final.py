assignment=['das assignment','dsu assignment','oop assignment','python assignment']

print(assignment)

# add newm assignment
assignment.append("java assignment")

print(assignment)


# condition ok

completed=input("entert the complated assignment:-")

if completed in assignment:
    assignment.remove(completed)
   
    print("updated assigenment list",assignment)

else:
   
    print("not completed")
