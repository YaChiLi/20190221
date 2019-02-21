mathScores = [10, 4, 56, 44, 89, 66, 53, 97]
print(mathScores[1])
print(mathScores[3:6])
print(mathScores[-1])
print(mathScores[-3])
print(mathScores[:5])
print(mathScores[5:])
print(mathScores[-6:])
print(len(mathScores))
print(max(mathScores))
print(min(mathScores))
s = sum(mathScores)
l = len(mathScores)
print(s / l)
x = '8'
y = int(x)

# --------------------------------
ls = []
ls.append(4)
print(ls)
ls.insert(1, 10)
print(ls)
mathScores = [10, 4, 56, 44, 89, 66, 53, 97]
del mathScores[1:3]
print(mathScores)
mathScores.remove(66)
print(mathScores)
mathScores[2]=1
print(mathScores)
print(2 in mathScores)
print(10 in mathScores)
print(mathScores.count(60))
print(mathScores.count(10))
mathScores= [10, 10, 10, 4, 56, 44, 89, 66, 53, 97]
mathScores.remove(10)
print(mathScores)

ls = ['a', 'b', 'c']
print(mathScores + ls)

# ----------------------------------------------------

ls = [[1, 3], [6, 5]]
print(ls[1] [0])

print(sorted(mathScores))

grades = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
print(grades[2])
print(sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]) )
print(sum(grades[1]) / len(grades[1]))
print(sum(grades[2]) / len(grades[2]))
grades.append([94, 90, 96])
# g = grades + [94, 90, 96]
print(grades)