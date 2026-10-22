"""Демонстрація мінімальної роботи реєстру студентів."""

from .student_accounting import Student, StudentRegistry


def main() -> None:
    registry = StudentRegistry()
    registry.add_student(Student(1, "Олена", "Петренко", "ІПЗ-31"))
    registry.add_student(Student(2, "Іван", "Іваненко", "ІПЗ-32"))
    for student in registry.list_students():
        print(f"{student.student_id}: {student.last_name} {student.first_name} — {student.group}")


if __name__ == "__main__":
    main()
