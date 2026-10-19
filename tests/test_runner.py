import unittest

import runner


class ExecutePythonTests(unittest.TestCase):
    def test_returns_stdout_on_success(self):
        result = runner.execute_python("print(2 + 2)")
        self.assertEqual(result["stdout"].strip(), "4")
        self.assertEqual(result["returncode"], 0)
        self.assertFalse(result["timed_out"])

    def test_reports_syntax_errors(self):
        result = runner.execute_python("if True print('broken')")
        self.assertNotEqual(result["returncode"], 0)
        self.assertIn("SyntaxError", result["stderr"])

    def test_times_out_long_running_program(self):
        result = runner.execute_python("while True: pass", timeout=0.2)
        self.assertTrue(result["timed_out"])
        self.assertIsNone(result["returncode"])

    def test_rejects_empty_and_non_string_source(self):
        with self.assertRaises(ValueError):
            runner.execute_python("")
        with self.assertRaises(ValueError):
            runner.execute_python(None)  # type: ignore[arg-type]

    def test_rejects_oversized_source(self):
        with self.assertRaises(ValueError):
            runner.execute_python("x = 1\n" * 20_000)

    def test_caps_output(self):
        result = runner.execute_python("print('x' * 70000)")
        self.assertTrue(result["truncated"])
        self.assertLessEqual(len(result["stdout"]), runner.MAX_OUTPUT_CHARS)


if __name__ == "__main__":
    unittest.main()
