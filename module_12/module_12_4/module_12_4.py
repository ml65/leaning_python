# Домашнее задание по теме "Логирование"
import logging
import unittest
from runner_test import RunnerTest

logging.basicConfig(level=logging.INFO, filemode="w", filename="module_12_4.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")

tournamentST = unittest.TestSuite()

tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournamentST)



