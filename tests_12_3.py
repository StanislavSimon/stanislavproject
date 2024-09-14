from tests_12_1 import Runner
from tests_12_2 import Runner, Tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Test Runner ')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)


    def test_run(self):
        runner = Runner('Test Runner ')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)


    def test_challenge(self):
        runner_1 = Runner('Test Runner 1')
        runner_2 = Runner('Test Runner 2')
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


# if __name__ == "__main__":
#     unittest.main()


class TournamentTest(unittest.TestCase):
    if_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(if_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)


    def test_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['Усэйн, Ник'] = results
        self.assertTrue(results[2] == 'Ник')


    def test_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['Андрей, Ник'] = results
        self.assertTrue(results[2] == 'Ник')


    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        TournamentTest.all_results['Усэйн, Андрей, Ник'] = results
        self.assertTrue(results[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(f'{i + 1}: {elem}')


if __name__ == '__main__':
    unittest.main()