grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
sudents={'Johny','Bilbo','Steve','Khendrik','Aaron'}

#Линейный вариант:

average_grades=[(sum(grades[0])/len(grades[0])),(sum(grades[1])/len(grades[1])),
                (sum(grades[2])/len(grades[2])),(sum(grades[3])/len(grades[3])),
                (sum(grades[4])/len(grades[4]))]
alpabet_range_students=sorted(sudents)
journal_sudents=dict(zip(alpabet_range_students,average_grades))
print('Линейный вариант:',journal_sudents)

#Цикловой вариант:

alpabet_range_students=sorted(sudents)
average_gradess=[]
for block in grades:
    average_block_grades=sum(block)/len(block)
    average_grades.append(average_block_grades)
journal_sudents=dict(zip(alpabet_range_students,average_grades))
print('Цикловой вариант:',journal_sudents)