calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    string_1 = len(string)
    string_2 = string.upper()
    string_3 = string.lower()
    return (string_1, string_2, string_3)
def is_contains(string, list_to_search):
    count_calls()
    count = 0
    for i in range(len(list_to_search)):
        if string.upper() in list_to_search[i].upper():
            count +=  1
        else:
            continue
    if count > 0:
        return True
    else:
        return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
