# Set operators
from pyscript import display 


grade7 = {
    "Chesca Irinco",
    "Johanna Mae Guarin",
    "Harriе Martija",
    "Clarize Galang"
}

grade8 = {
    "Kirche Segura",
    "Rhoann Capili",
    "Liahona Lee",
    "Alexandria Guico"
}

grade9 = {
    "Sophia Ridon",
    "Mia Marajas",
    "Kiesha Granados",
    "Sofia Riofrio"
}

grade10 = {
    "Niqa Agasi",
    "Amanda Bower",
    "Charlize Galang",
    "Julianne Canuday"
}
display('All members:', target='output')
for name in grade7.union(grade8, grade9, grade10):
    display(name, target='output')

display('Total members:', target='output')
display(len(grade7.union(grade8, grade9, grade10)), target='output')