paragraph = """
Python is a powerful programming language used for web development, 
data analysis, artificial intelligence, and more. 
This Python course helps beginners learn programming in an easy and fun way.
"""

length = len(paragraph)
print("Length of paragraph:", length)

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

print("Preview (first 50 characters):", paragraph[:50])

replaced_para = paragraph.replace("Python", "PYTHON")
print("\nAfter replacing 'Python' with 'PYTHON':")
print(replaced_para)

lower_para = paragraph.lower()
print("\nParagraph in lowercase:")
print(lower_para)

trimmed_para = paragraph.strip()
print("\nParagraph after removing extra spaces:")
print(trimmed_para)

words = trimmed_para.split()
print("\nList of words:")
print(words)

if "course" in lower_para:
    print("\nThe word 'course' is present in the paragraph.")
else:
    print("\nThe word 'course' is NOT present in the paragraph.")

message = "The course description is {} characters long and has {} words.".format(length, len(words))
print("\n" + message)
