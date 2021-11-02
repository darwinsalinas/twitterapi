from schemas.user import LoginUser


def print_hi(name):
    user = LoginUser(username='admin', password='12345678', email='asdasd@sdfs.com')
    print(user)
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
