single_quotes_string = 'Vio'
multi_line_string = """ 
This is a 
multiline
string
"""
print(multi_line_string)

string_length = "My name is Vio"
print(len(string_length))

escape_sequence = "Python \\\"Programming"
print(escape_sequence)

# formatting strings
first = "Vio"
last = "Slaniceanu"
full = first + " " + last
print(full)

full = f"{first} {last}"
print(full)

# checks if a specific sequence is in a string
print("Vio" in full)
print("Test" not in full)
