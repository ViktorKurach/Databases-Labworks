import view
import add
import remove
import edit
import search


def main_menu():
    while 1:
        print "1. View records\n2. Add record\n3. Remove record\n4. Edit record\n5. Search records\n6. Exit"
        ch = ''
        while ch not in ['1', '2', '3', '4', '5', '6']:
            ch = str(raw_input())
        if ch == '1':
            view.main()
        elif ch == '2':
            add.main()
        elif ch == '3':
            remove.main()
        elif ch == '4':
            edit.main()
        elif ch == '5':
            search.main()
        else:
            break

main_menu()
