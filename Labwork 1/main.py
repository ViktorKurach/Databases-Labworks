import os
import pickle
import work


filename = 'data.pkl'
if os.path.exists(filename):
    f = open(filename, 'rb')
    table = pickle.load(f)
    f.close()
else:
    table = []
while 1:
    print "1. View records\n2. Add record\n3. Remove record\n4. Edit record\n5. Filter records\n6. Exit"
    ch = ''
    while ch not in ['1', '2', '3', '4', '5', '6']:
        ch = str(raw_input())
    if ch == '1':
        work.view(table)
    elif ch == '2':
        new_record = work.add()
        if new_record in table:
            print "This record already exists\n"
        else:
            table.append(new_record)
            print "New record is written\n"
    elif ch == '3':
        table = work.remove(table)
    elif ch == '4':
        work.edit()
    elif ch == '5':
        work.filter()
    else:
        f = open(filename, 'wb')
        pickle.dump(table, f)
        f.close()
        break
