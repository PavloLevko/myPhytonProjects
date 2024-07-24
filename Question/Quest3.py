names = ['Adam', 'Eva', 'Jack', 'Tom']
assignments = [4, 5, 4, 3]
grades = [10, 9, 10, 8]


message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
\nsubmit before you can graduate. You're current grade is {} and can increase \
\nto {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, assignment/grade))
