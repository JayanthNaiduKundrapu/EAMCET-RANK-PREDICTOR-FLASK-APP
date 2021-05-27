import sqlite3
rank = 10000
gender = "Male"
caste = "BCD"
branch = 'CSE'
if gender == "Male":
    gc = caste + "_" + "BOYS"
if gender == "Female":
    gc = caste + "_" + "GIRLS"
connection = sqlite3.connect("data.sqlite")
cursor = connection.cursor()
query = "SELECT inst_code,inst_name,REGION,DIST,PLACE,COED,AFFLIATION,branch_code FROM LAST_RANK_DETAILS WHERE {} <= '{}' AND branch_code = '{}' ".format(gc,rank,branch)
cursor.execute(query)
result = cursor.fetchmany(2)
print(type(result))
for i in result:
    print(i[1])
