dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}


#Оператор слияния(|)
dictionary_3 = (dictionary_1 | dictionary_2)
print(dictionary_3)

dictionary_1.update(dictionary_2)


print(dictionary_1)

dictionary_4 = dictionary_1.copy()
dictionary_4.update(dictionary_2)
print(dictionary_4)