frontend = {"Asha", "Ravi", "Sneha", "Kiran"}
backend = {"Ravi", "Neha", "Kiran"}

backend.add("Arjun")

frontend.remove("Sneha")

both_courses = frontend & backend
print("Students in both courses:", both_courses)

only_backend = backend - frontend
print("Students only in Backend:", only_backend)

unique_students = frontend | backend
print("Total number of unique students:", len(unique_students))

course_counts = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

print("\nCourse enrollment count:")
for course, count in course_counts.items():
    print(f"{course}: {count} students")

fullstack_dict = {**course_counts, "Fullstack": course_counts["Frontend"] + course_counts["Backend"]}
print("\nUpdated course dictionary with Fullstack:")
print(fullstack_dict)
