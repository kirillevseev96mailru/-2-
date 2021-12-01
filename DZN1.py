import re
email = re.compile(r'[a-zA-Z\.-]+@[\w\.-]+')

def Email_verification_(email_email):
    verification = email.findall(email_email)
    if verification:
        domen, addres = verification[0]
    else:
        raise ValueError(f'wrong email: {email_email}')
    print(domen, addres)

entered_email = input('Введите email на проверку: ')
Email_verification_(entered_email)