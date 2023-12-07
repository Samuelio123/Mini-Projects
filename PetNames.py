print("    Enter the Names of all your Pets.")
petNames = []
while True:
    print("Number " + str(len(petNames) + 1) + ' pet is?, ' '(Or enter nothing to stop):')
    name = input('--> ')
    if name == '':
        break
    petNames = petNames + [name]
print("The pet names are:")
for name in petNames:
     print('  ' + name)

print("\nCrosscheck if you've forgotten any Name")
print("Enter the name of the Pet")
secname = input('--> ')

if secname not in petNames:
    print("You don't have a pet named", secname)
else:
    print(secname + " is my pet.")
