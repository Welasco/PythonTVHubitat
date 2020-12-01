test = "str-1232"
test2 = "str1232"
test = test.split("-")
print(len(test))

if len(test) > 1:
    cmd1 = test[0]
    cmd2 = test[1]

    print(cmd1)
    print(cmd2)    
    if not cmd2 in '1232':
        print('if not')
    elif cmd2 == '1232':
        print('')


else:
    pass

print(test[0])
print(test2[0])