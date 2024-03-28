from string import ascii_lowercase


def is_pangram(text):
    flag = True
    new_string = text.replace(' ', '').lower()
    for i in ascii_lowercase:
        if i in new_string:
            flag = True
        else:
            return False
    if flag:
        return True


print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The jay pig fox zebra and my wolves quack'))
print(is_pangram('Hello world'))