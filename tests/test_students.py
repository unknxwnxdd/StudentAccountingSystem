import unittest

from src.student_accounting import Student, StudentRegistry


class StudentRegistryTests(unittest.TestCase):
    def setUp(self):
        self.registry = StudentRegistry()
        self.registry.add(Student("Петренко", "Іван", "КН-21"))
        self.registry.add(Student("Коваль", "Марія", "КН-21"))
        self.registry.add(Student("Петрук", "Олег", "ІП-22"))

    def test_filter_by_group_returns_students_of_group(self):
        result = self.registry.filter_by_group("КН-21")
        self.assertEqual(len(result), 3)

    def test_filter_by_unknown_group_returns_empty_list(self):
        self.assertEqual(self.registry.filter_by_group("XX-00"), [])

    def test_search_by_surname_is_case_insensitive(self):
        result = self.registry.search_by_surname("пЕТ")
        self.assertEqual(len(result), 2)

    def test_add_without_last_name_raises_error(self):
        with self.assertRaises(ValueError):
            self.registry.add(Student("  ", "Іван", "КН-21"))

    def test_search_with_empty_text_raises_error(self):
        with self.assertRaises(ValueError):
            self.registry.search_by_surname("   ")


if __name__ == "__main__":
    unittest.main()
