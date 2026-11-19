import unittest
from main import parse_history, build_report
class HistoryTests(unittest.TestCase):
    def test_timestamp_formats(self):
        rows=parse_history("#1700000000\ngit status\n: 1700003600:0;python main.py\n")
        self.assertEqual([x[0] for x in rows],["git","python"])
        self.assertTrue(all(x[1] for x in rows))
    def test_arguments_are_not_retained(self):
        report=build_report(parse_history("curl --token SECRET\ngit status\n"))
        self.assertNotIn("SECRET",str(report))
    def test_empty(self):
        self.assertEqual(build_report([])["commands_analyzed"],0)
if __name__=="__main__": unittest.main()
