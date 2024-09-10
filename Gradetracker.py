class StudentGradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        if self.grades==None:
            return 0
        total = sum(self.grades.values())
        count = len(self.grades)
        return total / count

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def get_gpa(self, average):
        if average >= 90:
            return 10.0
        elif average >= 80:
            return 9.0
        elif average >= 70:
            return 8.0
        elif average >= 60:
            return 7.0
        else:
            return 6.0

    def display_grades(self):
        if self.grades==0:
            print("No grades available.")
            return

        print("Grades:")
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")

        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        gpa = self.get_gpa(average)

        print(f"\nAverage Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

def main():
    tracker = StudentGradeTracker()

    while True:
        print("\n1. Add Grade")
        print("2. Display Grades")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            tracker.add_grade(subject, grade)
        elif choice == '2':
            tracker.display_grades()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()