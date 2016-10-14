def view(table):
    if not table:
        print "No records\n"
    for x in table:
        for key in x:
            print ("%s: %s" % (key.capitalize(), x[key]))
        print ""


def add():
    print "New type (T) or article (A)?"
    ch = ''
    while ch not in ['T', 'A']:
        ch = str(raw_input()).capitalize()
    if ch == 'T':
        new_record = dict.fromkeys(['name', 'manufacturer', 'provider'])
    else:
        new_record = dict.fromkeys(['type', 'name', 'price', 'quantity', 'provision date'])
    for x in new_record.keys():
        print ("%s: " % x.capitalize()),
        new_record[x] = str(raw_input())
    return new_record


def remove(table):
    print "Type (T) or article (A) to remove?\nTypes are deleted with all relative articles!"
    ch = ''
    while ch not in ['T', 'A']:
        ch = str(raw_input()).capitalize()
    print "Name of type/article to remove: ",
    del_name = str(raw_input())
    new_table = []
    remove_flag = 0
    for x in table:
        if x['name'] == del_name or (x.has_key('type') and x['type'] == del_name):
            remove_flag += 1
        else:
            new_table.append(x)
    if not remove_flag:
        print "Nothing to remove\n"
    else:
        print "Record(s) removed\n"
    return new_table


def edit():
    print "Here record is edited\n"


def filter():
    print "Here is record search\n"
