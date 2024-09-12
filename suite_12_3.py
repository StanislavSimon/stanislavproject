import tests_12_3
import unittest


tests_HW_12_3 = unittest.TestSuite()
tests_HW_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tests_HW_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))


tests_R_T = unittest.TextTestRunner(verbosity=2)
tests_R_T.run(tests_HW_12_3)