from dataclasses import dataclass


@dataclass(frozen=True)
class Student:
    last_name: str
    first_name: str
    group: str


class StudentRegistry:
    def __init__(self):
        self._students = []

    def add(self, student):
        if not student.last_name.strip():
            raise ValueError("Last name is required")
        if not student.group.strip():
            raise ValueError("Group is required")
        self._students.append(student)

    def count(self):
        return len(self._students)

    def filter_by_group(self, group):
        return [s for s in self._students if s.group == group]

    def search_by_surname(self, surname):
        query = surname.strip().lower()
        if not query:
            raise ValueError("Search text is required")
        return [s for s in self._students if s.last_name.lower().startswith(query)]
