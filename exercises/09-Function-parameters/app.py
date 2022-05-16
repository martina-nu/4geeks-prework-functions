# Your code goes here:
def render_person(name, bday, eye_color, age, gender):
    string = name + " is a " + str(age) + " years old " + gender + " born in " + bday + " with " + eye_color + " eyes"
    return string


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))