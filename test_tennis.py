from tennis import Tennis


class TestTennis:
    def set_tennis_score(self, tennis: Tennis, i: int = 0, j: int = 0):
        for _ in range(i):
            tennis.add_first_player_score()
        for _ in range(j):
            tennis.add_second_player_score()

    def test_love_all(self):
        tennis = Tennis("Gary", "Ray")
        assert tennis.score() == "love all"

    def test_fifteen_all(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=1, j=1)
        assert tennis.score() == "fifteen all"

    def test_thirty_all(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=2, j=2)
        assert tennis.score() == "thirty all"

    def test_deuce(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=3, j=3)
        assert tennis.score() == "deuce"

    def test_fifteen_love(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=1)
        assert tennis.score() == "fifteen love"

    def test_thirty_love(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=2)
        assert tennis.score() == "thirty love"

    def test_forty_love(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=3)
        assert tennis.score() == "forty love"

    def test_love_fifteen(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=0, j=1)
        assert tennis.score() == "love fifteen"

    def test_love_thirty(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=0, j=2)
        assert tennis.score() == "love thirty"

    def test_love_forty(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=0, j=3)
        assert tennis.score() == "love forty"

    def test_second_player_win(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=0, j=4)
        assert tennis.score() == "Ray win"

    def test_thirty_fifteen(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=2, j=1)
        assert tennis.score() == "thirty fifteen"

    def test_first_player_adv(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=3, j=3)
        tennis.add_first_player_score()
        assert tennis.score() == "Gary adv"

    def test_second_player_adv(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=3, j=3)
        tennis.add_second_player_score()
        assert tennis.score() == "Ray adv"

    def test_first_player_win_after_deuce(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=3, j=3)
        tennis.add_first_player_score()
        tennis.add_first_player_score()
        assert tennis.score() == "Gary win"

    def test_second_player_win_after_deuce(self):
        tennis = Tennis("Gary", "Ray")
        self.set_tennis_score(tennis=tennis, i=3, j=3)
        tennis.add_second_player_score()
        tennis.add_second_player_score()
        assert tennis.score() == "Ray win"
