web_dev = ["Rahul", "Sneha", "Asha"]
data_science = ["Vikram", "Neha", "Kiran"]
uiux_design = ["Priya", "Manoj", "Rita"]

all_participants = [web_dev, data_science, uiux_design]

web_dev.append("Arjun")

data_science.insert(1, "Simran")

uiux_design.pop()

copied_ds = data_science.copy()
data_science.clear()

print("First two Web Development participants:", web_dev[:2])

name_lengths = [len(name) for name in copied_ds]
print("Length of each name in copied Data Science list:", name_lengths)

asha_present = ("Asha" in web_dev) or ("Asha" in copied_ds) or ("Asha" in uiux_design)
print("Is Asha in any workshop list?", asha_present)

first_participants = (web_dev[0], copied_ds[0], uiux_design[0])
print("Tuple of first participants from each workshop:", first_participants)
