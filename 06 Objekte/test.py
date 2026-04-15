# Primitive Datentypen (int, float, bool, str): immer Kopie des Wertes
# z. B. wenn ich einen Variable (primitiven Datentyp) in eine Funktion gebe
# x = 5
# y = quadriere(x) --> Hier wird die 5 übergeben und nicht die Referenz von x
# --> Call by Value
my_string1 = "Hi"
my_string2 = my_string1 # Kopiere Wert
my_string1 += " students"
print(my_string1)
print(id(my_string1))
print(id(my_string2))

# Bei ALLEN nicht-primitiven Datentypen (Klassen wie list, dict, eigene Klassen): immer Kopie der Referenz
# z. B. wenn ich einen Variable (nicht primitive Klasse) in eine Funktion gebe
# x = [2, 3, 4]
# y = summiere_liste(x) --> Hier wird die Referenz an die Funktion übergeben
# --> Call by Reference
numbers_list1 = [2, 3, 4]
numbers_list2 = numbers_list1 # Kopiere Referenz
numbers_list1.append(5)
print(numbers_list1)
print(numbers_list2)
print(id(numbers_list1))
print(id(numbers_list2))
