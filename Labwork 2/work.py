import db
import view


menu = view.Menu()
while 1:
    menu.show_menu()
    task = ''
    while task not in ['1', '2', '3', '4', '5', '6']:
        task = str(raw_input())
    if task == '1':
        menu.show_albums()
    elif task == '2':
        menu.add_album()
    elif task == '3':
        menu.edit_album()
    elif task == '4':
        menu.delete_album()
    elif task == '5':
        menu.search()
    else:
        del menu
        break
