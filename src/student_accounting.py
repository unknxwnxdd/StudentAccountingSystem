"""Навчальна модель даних і сервіс обліку студентів без зовнішніх залежностей."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Student:
    student_id: int
    first_name: str
    last_name: str
    group: str


class StudentRegistry:
    def __init__(self) -> None:
        self._students: dict[int, Student] = {}

    def add_student(self, student: Student) -> None:
        if student.student_id <= 0:
            raise ValueError("Student ID must be positive")
        if not student.first_name.strip() or not student.last_name.strip():
            raise ValueError("Student name is required")
        if not student.group.strip():
            raise ValueError("Academic group is required")
        if student.student_id in self._students:
            raise ValueError("Student ID already exists")
        self._students[student.student_id] = student

    def get_student(self, student_id: int) -> Student | None:
        return self._students.get(student_id)

    def list_students(self) -> list[Student]:
        return list(self._students.values())
