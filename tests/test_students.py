import unittest

from src.student_accounting import Student, StudentRegistry


class StudentRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = StudentRegistry()
        self.olena = Student(1, "Олена", "Петренко", "ІПЗ-31")
        self.ivan = Student(2, "Іван", "Іваненко", "ІПЗ-32")

    def test_add_and_find_student(self) -> None:
        self.registry.add_student(self.olena)
        self.assertEqual(self.registry.get_student(1), self.olena)

    def test_student_id_is_unique(self) -> None:
        self.registry.add_student(self.olena)
        with self.assertRaises(ValueError):
            self.registry.add_student(Student(1, "Іван", "Іваненко", "ІПЗ-32"))

    def test_empty_name_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.registry.add_student(Student(3, "", "Петренко", "ІПЗ-31"))

    def test_filter_students_by_group(self) -> None:
        self.registry.add_student(self.olena)
        self.registry.add_student(self.ivan)
        self.assertEqual(self.registry.filter_by_group("іпз-31"), [self.olena])


if __name__ == "__main__":
    unittest.main()
