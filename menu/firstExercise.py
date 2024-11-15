from logic.firstExercise import save_course

def design():  
    course = input("What is the course name? ")  
    result = save_course(course)
    print(result)