grocery_list = ["milk", "bread", "eggs"]

def add_item(item):
    grocery_list.append(item)

def remove_last_item():
    if grocery_list:
        grocery_list.pop()
    else:
        print("Grocery list is empty!")

display_items = lambda items: [print(f"Item: {i}") for i in items]

def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])

print("Initial Grocery List:", grocery_list)

add_item("butter")
add_item("rice")
print("\nAfter adding items:", grocery_list)

remove_last_item()
print("\nAfter removing last item:", grocery_list)

print("\nDisplaying items:")
display_items(grocery_list)

total_chars = count_characters(grocery_list)
print("\nTotal number of characters in all items:", total_chars)
