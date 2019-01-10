sss = {'song':None,'rel':None,'Genre':None,'Artists':None,'dur':None }
for key,val in sss.items():
    # print(key)
    val = input('Enter ' + key + ' >>')
    sss[key] = val

print(sss)
for k,v in sss.items():
    print(k,v)

key = None
value = None
def guess(key,value):
    while True:
        print('Enter done to exit')
        key = input('Enter key>>')
        if key ==  'done': break
        value = input('Enter value>>')
        if value == 'done:': break
        if key in sss:
            if sss[key] == value:
                print('Correct')
            else: print('Wrong value')
        else: print('Oh')

guess(key,value)
