def new_password(oldpassword, newpassword):
    if oldpassword  != newpassword and len(newpassword) >6:
        return True
    else:
        return False

oldpassw = (input('Enter your old password: '))
newpassw = (input('Enter your new password: '))

if new_password(oldpassw, newpassw) == True:
    print('Succes')
else:
    print('Probeert nog een keer')