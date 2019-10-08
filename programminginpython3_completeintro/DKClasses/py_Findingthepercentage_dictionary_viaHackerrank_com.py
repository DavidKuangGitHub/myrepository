#py_Findingthepercentage_dictionary_viaHackerrank_com.py You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and CHemistry. The marks can be floating values. The user enters some integer N followed by the names and marks for N students. It is required to save the record in a dictionary data type. THe user enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
#Example Input 
#3
#Krishna 67 68 69
#Arjun 70 98 63
#Malika 52 56 60
#Malika
#Example output
#56.00

print("Enter the number of the students: ")
n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = input()
query_scores = student_marks[query_name]
#print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
print("{0:.2f}".format(sum(query_scores)/3))
