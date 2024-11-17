import unittest
from module_12_3 import TournamentTest, RunnerTest

tournamentST = unittest.TestSuite()

tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournamentST)