# Домашнее задание по теме "Простые Юнит-Тесты"
import unittest
from runner import Runner

# Задача "Проверка на выносливость":

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("walker")
        for i in range(0,10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("runner")
        for i in range(0, 10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("walker")
        for i in range(0,10):
            runner1.walk()
        runner2 = Runner("runner")
        for i in range(0, 10):
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()