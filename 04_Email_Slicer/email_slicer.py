'''
# collect email from user
# split email using the @, the first part as the username, the second part is gonna be saved as domain
# split domain using .
'''


def main():

    print(" Welcome to email slicer ")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print(f'Username: {username}')
    print(f'Domain: {domain}')
    print(f'Extension: {extension}')


main()
