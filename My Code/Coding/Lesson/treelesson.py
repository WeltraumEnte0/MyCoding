def generate_christmas_tree(tree_size):

    tree = []
    for i in range(tree_size):
        spaces = ' ' * (tree_size - i - 1)
        letters = 'X' * (2 * i + 1)
        tree.append(spaces + letters)
 
    trunk_width = tree_size // 3
    trunk_height = tree_size // 2
    trunk_spaces = ' ' * (tree_size - trunk_width)
    trunk = [trunk_spaces + 'X' * trunk_width for _ in range(trunk_height)]
 
    return tree + trunk
 
def print_christmas_tree(christmas_tree):
    for row in christmas_tree:
        print(row)
 
if __name__ == "__main__":
    tree_size = int(input("Enter the size of the Christmas tree: "))
   
    christmas_tree = generate_christmas_tree(tree_size)
    print_christmas_tree(christmas_tree)