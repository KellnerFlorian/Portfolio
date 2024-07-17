def calculate_needed_points(total_points, pass_rate=0.5, grades=5):
    # Calculate the pass mark in points
    pass_points = total_points * pass_rate

    # Calculate the step between grades
    step = pass_points / (grades - 1)

    # Create a dictionary to store points needed for each grade
    grade_points = {}

    for i in range(1, grades + 1):
        if i == 1:
            grade_points[i] = 0
        else:
            grade_points[i] = round((i - 1) * step, 2)

    return grade_points

# Example usage:
total_points = 100  # Example total points for the exam
grades_needed_points = calculate_needed_points(total_points)

print("Points needed for each grade:")
for grade, points in grades_needed_points.items():
    print(f"Grade {grade}: {points} points")
