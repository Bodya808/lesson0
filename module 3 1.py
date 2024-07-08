calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    lenght = len(string)
    upper = string.upper()
    lower = string.lower()
    count_calls()
    return lenght, upper, lower


def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        if string.lower() == item.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)



