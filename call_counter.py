calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    string = (len(string), string.lower(), string.upper())
    return string


print (string_info('Capybara'))
print (string_info('Armageddon'))


def is_contains(string, list_to_search):
    count_calls()
    cnt_ = False
    for i in range(0, len(list_to_search)):
        if list_to_search[i] in string:
            cnt_ = True
            break
    return cnt_

    print (cnt_)


print (is_contains('Urban', ['BaNaN', 'urBAN','ban']))
print (is_contains('cycle', ['recycling', 'cyclic']))
print (calls)
