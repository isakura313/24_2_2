unc_users = ['pavel', 'petr', 'semen']
con_users = []

while unc_users:
    con_user = unc_users.pop()
    print(con_user)
    con_users.append(con_user)
print(unc_users)
print(con_users)