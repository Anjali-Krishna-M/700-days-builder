print("Welcome to the project Ascend")

num_task=int(input("How many task did you complete today ?"))

tasks=[]

for i in range(num_task):
    task=input(f"Enter task {i+1}: ")
    tasks.append(task)

print("\nToday's Progress")

for task in tasks:
    print("Done ",task)