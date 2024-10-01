from runner_and_tournament import Runner
from runner_and_tournament import Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(f'{k}: {v}')

    def test_first_tournament(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results['1'] = result
        self.assertTrue(result[2] == 'Ник')

    def test_second_tournament(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results['2'] = result
        self.assertTrue(result[2] == 'Ник')

    def test_third_tournament(self):
        tournament = Tournament(90, self.andrey, self.usain, self.nick)
        result = tournament.start()
        self.all_results['3'] = result
        self.assertTrue(result[3] == 'Ник')


if __name__ == '__main__':
    unittest.main()
