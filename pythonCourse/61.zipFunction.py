# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for eah element

usernames = ["Marko", "Tijana", "Jelena"]
passwords = ["p@ssword", "abc123", "guest"]

users = dict(zip(usernames, passwords))

print(type(users))

for key, value in users.items():
    print(key + " : " + value)
# --------------------------------------------------
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)
