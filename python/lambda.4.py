passwords = ["abc123", "securePass123","helloWorld", "Qwerty123!",]

valid_passwords = filter(lambda p: any(c.isdigit() for c in p) and any(c.isupper() for c in p), passwords)

print(list(valid_passwords))
