students = {
    "s1":{ "name":"Abhishek","surname":"Bairagi","address":"Neemuch" },
    "s2":{ "name":"Sharuk","surname":"Khan","address":"Indore" },
    "s3":{ "name":"Rajveer","surname":"Singh","address":"Ratlam" },
    "s4":{ "name":"Ranu","surname":"Patidar","address":"Jeeran" },
}




for student in students:
    print(f'Hello {students[student]["name"]} {students[student]["surname"]} From {students[student]["address"]}')