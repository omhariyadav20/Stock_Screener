from lib.auth import verify_user, find_user

print('admin auth:', verify_user('admin', '12121212'))
print('quant auth:', verify_user('quant', '12345678'))
u = find_user('admin')
print('admin record:', u)
