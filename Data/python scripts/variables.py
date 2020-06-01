filename = "..\Test_data.csv" #the file you want to modify
field_names= ['semester', 'gender', 'friends_time', 'faculty_time', 'attendance', 'attentiveness', 'co_extra_curricular', 'study_time', 'social_time', 'previous_score', 'extra_courses', 'health', 'sleep_time','library_time', 'group_name', 'decision']

high_medium_low = ['High','Moderate','Low']
time_4_1 = ['>4', '1 to 4','<1']
time_8_6 = ['>8','6 to 8','<6']
often_sometimes_never = ['often', 'sometimes', 'never']
cgpa_9_7_5 = ['>9', '7 to 9', '5 to 7', '<5']

values = {
    "semester":[1,2,3,4,5,6,7,8],
    "gender" : ["male", "female"],
    "friends_time": often_sometimes_never,
    "faculty_time" : often_sometimes_never,
    "attendance" : ['<75', '75 to 85', '>85'],
    "attentiveness" : high_medium_low,
    "co_extra_curricular" : often_sometimes_never,
    "study_time" : time_4_1,
    "social_time" : time_4_1,
    "previous_score" : cgpa_9_7_5,
    "extra_courses" : often_sometimes_never,
    "health" : [1, 2, 3, 4, 5],
    "sleep_time" : time_8_6,
    "library_time" : time_4_1,
    "group_name" : [],
    "decision" : cgpa_9_7_5
}