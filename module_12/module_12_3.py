# Домашнее задание по теме "Систематизация и пропуск тестов".

# Задача "Заморозка кейсов":

# Домашнее задание по теме "Простые Юнит-Тесты"
import unittest
from runner import Runner
from runner2 import Tournament

# Задача "Проверка на выносливость":

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены.")
    def test_walk(self):
        runner = Runner("walker")
        for i in range(0,10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены.")
    def test_run(self):
        runner = Runner("runner")
        for i in range(0, 10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены.")
    def test_challenge(self):
        runner1 = Runner("walker")
        for i in range(0,10):
            runner1.walk()
        runner2 = Runner("runner")
        for i in range(0, 10):
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

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

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены.")
    def test_start1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        all_results = tournament.start()
        self.all_results.append(all_results)
        self.assertEqual(all_results[max(all_results)], 'Ник')

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены.")
    def test_start2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        all_results = tournament.start()
        self.all_results.append(all_results)
        self.assertEqual(all_results[max(all_results)], 'Ник')

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены.")
    def test_start3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        all_results = tournament.start()
        self.all_results.append(all_results)
        self.assertEqual(all_results[max(all_results)], 'Ник')
