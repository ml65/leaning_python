# Домашнее задание по теме "Методы Юнит-тестирования"

import unittest
from runner2 import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = []
        self.ptr = 0
    def setUp(self):
        self.runner1 = Runner("Усэйн",10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(self):
        for res in self.all_results:
            result = {k: v.name for k, v in res.items()}
            print(result)

    def test_start1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        all_results = tournament.start()
        self.all_results.append(all_results)
        self.assertEqual(all_results[max(all_results)], 'Ник')

    def test_start2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        all_results = tournament.start()
        self.all_results.append(all_results)
        self.assertEqual(all_results[max(all_results)], 'Ник')

    def test_start3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        all_results = tournament.start()
        self.all_results.append(all_results)
        self.assertEqual(all_results[max(all_results)], 'Ник')

if __name__ == "__main__":
    unittest.main()
