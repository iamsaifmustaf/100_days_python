from prettytable import PrettyTable
x = PrettyTable()

x.field_names = ["Pokemon Name", "Type"]
x.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)
x.align = 'r'
print(x)