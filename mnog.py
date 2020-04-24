unc_users = ['pavel', 'petr', 'semen']
ban_users = set(unc_users)

help_users = {'john', 'semeon', 'ogr'}

all_users = ban_users | help_users
print(all_users)

#bcnjhb
name = input(" Введите ваше имя")
if name in ban_users:
    exit()
else:
    print("ну привет")

