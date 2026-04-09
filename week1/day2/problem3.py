grades = [78, 45, 89, 66, 92, 34, 55, 47, 81, 60]

# print the highest and the lowest score the just passed and the just failed top k students 
passmark=50


k=2
failcount=len([score for score in grades if score<passmark])

sort_grades=sorted(grades)

print({
    'failcount':failcount,
    'pass_count':len(grades)-failcount,
    'Lowest':sort_grades[:k],
     'highest':sort_grades[-k:][::-1]

})


