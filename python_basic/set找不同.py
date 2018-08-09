# Author:Patrick
char_list = [' a ', ' b ', ' c ', ' c ', ' d ', ' d ', ' d ']
sentence = "Welcome Back to This Tutorial"

print(set(char_list))
print('\n')

print(set(char_list + list(sentence)))
print('\n')

unique_char = set(char_list)
unique_char.add(' x ')
# unique_char.add（['y'，'z']）这是错的
print(unique_char)
print('\n')

unique_char.remove(' x ')
print(unique_char)
unique_char.discard(' d ')
print(unique_char)
unique_char.clear()
print(unique_char)
print('\n')

unique_char = set(char_list)
print(unique_char.difference({' a ', ' e ', ' i '}))
print(unique_char.intersection({' a ', ' e ', ' i '}))
