#Class roster For a class roster I would use a list because a roster is subjet to changes
students=["Andres","Felipe","Jonas","Ruth"]

#Visitor IDs For this case since the ID number should be unique for each visitor. I would use a set
visitor_ids={2026,2027,2028,2029}

#Student Ids Since we should have the student information for the creation of an ID, I would use a dictionary to contain each student name and ID #
student_ids={
    2026: "Andres",
    2027: "Felipe",
    2028: "Jonas",
    2029: "Ruth"
}

#Weekday labels. Since the weekdays are information we don't really need to update neither change I would use a tuple
weekdays=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

print(students)
print(visitor_ids)
print(student_ids)
print(weekdays)
print(student_ids[2026]) #For student look up
