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
        print "Record(s) has been removed\n"
    return new_table


def edit(table):
    print "Type (T) or article (A) to edit?\nTypes are edited with all relative articles!"
    ch = ''
    while ch not in ['T', 'A']:
        ch = str(raw_input()).capitalize()
    print "Name of type/article to edit: ",
    edit_name = str(raw_input())
    old_name = new_name = ""
    for x in table:
        if x['name'] == edit_name:
            old_name = x['name']
            for key in x.keys():
                print("%s: " % key.capitalize()),
                x[key] = str(raw_input())
            new_name = x['name']
            break
    if old_name == new_name == "":
        print "Nothing to edit\n"
        return table
    if ch == 'T':
        for x in table:
            if x.has_key('type') and x['type'] == old_name:
                x['type'] = new_name
    print "Record(s) has been edited\n"
    return table


def filtrate(table):
    if not table:
        print "Nothing to filter\n"
        return table
    res_list = []
    for x in table:
        if x.has_key('type') and float(x['price']) > 10.0 and x['type'] not in res_list:
            res_list.append(x['type'])
    if res_list:
        print "Article types where minimal price is more than 10.00:"
        for x in res_list:
            print("* %s" % x)
        print ""
    else:
        print "No appropriate article types\n"
    return table
