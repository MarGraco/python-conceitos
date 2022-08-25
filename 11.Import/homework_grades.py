from grade_average_service import calculate_homework
import grade_average_service as grade_service

homework_assignment_grades = {
    'homework_1': 85,
    'homework_3': 100, 
    'homework_2': 81
}

grade_service.calculate_homework(
    homework_assignment_grades
)

#calculate_homework(homework_assignment_grades)
