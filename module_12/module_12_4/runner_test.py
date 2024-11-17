import logging
from rt_with_exceptions import Runner
import unittest

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены.")
    def test_negativ1_walk(self):
        failed = False
        name = "aaa"
        try:
            runner = Runner(name)
            logging.info("Отрицательный тест 1 провален!")
            failed = True
        except TypeError:
            logging.info("Негативный тест(1) на создание Runner выполнен успешно.")
        if (failed):
            raise TypeError(f'Негативный тест должен вызывать исключение!')

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены.")
    def test_negativ2_walk(self):
        with self.assertRaises(ValueError):
            runner = Runner("test", -5)
            logging.info("Негативный тест(2) на создание Runner выполнен успешно.")

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены.")
    def test_walk(self):
        name = "name"
        speed = 3
        try:
            runner = Runner(name,speed)
            for i in range(0,10):
                runner.walk()
            self.assertEqual(runner.distance, 30,"Дисстанция рассчитана неверно")
            logging.info(f"\"test_walk\" выполнен успешно")
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: name={name} speed={speed}", exc_info=True)
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: speed={speed}", exc_info=True)
        except:
            logging.error("Неизвестная ошибка", exc_info=True)


    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены.")
    def test_run(self):
        name = "name"
        speed = 5
        try:
            runner = Runner(name, speed)

            for i in range(0, 10):
                runner.run()
            self.assertEqual(runner.distance, 100,"Ошибка в рассчете расстояния.")
            logging.info("Тест \"test_run\" пройден успешно")
        except TypeError as e:
            logging.error(f"Ошибка типа данных: name={name} speed={speed}", exc_info=True)
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: speed={speed}", exc_info=True)

    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены.")
    def test_challenge(self):
        runner1 = Runner("walker")
        for i in range(0,10):
            runner1.walk()
        runner2 = Runner("runner")
        for i in range(0, 10):
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)
        logging.info("Тест \"test_challenge\" пройден успешно")


