import db
import view


database = db.Database()
menu = view.Menu()
while 1:
    menu.show()
    task = ''
    while task not in ['1', '2', '3', '4', '5', '6']:
        task = str(raw_input())
    if task == '1':
        database.show_albums()
    elif task == '2':
        database.add_album()
    elif task == '3':
        database.edit_album()
    elif task == '4':
        database.delete_album()
    elif task == '5':
        database.search()
    else:
        del database
        del menu
        break
