# Task 1: Given the two lists, Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? And how can you check to see if Alice is in both submitted and attended in one if statement?

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted the assignment and attended class!")
elif "Alice" in submitted and "Alice" not in attended:
    print("Alice submitted her assignment but did not attend the class")
else:
    print("Alice attended the class but did not submit the assignemnt.")