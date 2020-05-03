user = input('Welcome: ')
office = input('Enter office: ')
text = input('Enter text: ')
with open(office, 'r+') as f:
    f.write(text)

# with open('google_kazakstan.txt', 'r+') as f:
#     f.write('')
# with open('google_paris.txt', 'r+') as f:
#     f.write('')
# with open('google_uar.txt', 'r+') as f:
#     f.write('')
# with open('google_kyrgyzstan.txt', 'r+') as f:
#     f.write('')
# with open('google_san_francisco.txt', 'r+') as f:
#     f.write('')
# with open('google_germany.txt', 'r+') as f:
#     f.write('')
# with open('google_moscow.txt', 'r+') as f:
#     f.write('')
# with open('google_sweden.txt', 'r+') as f:
#     f.write('')
