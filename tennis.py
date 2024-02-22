class Tennis:
    def __init__(self, first_player_name: str, second_player_name: str):
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name
        self.first_player_score = 0
        self.second_player_score = 0
        self.score_dict = {
            0: "love",
            1: "fifteen",
            2: "thirty",
            3: "forty",
        }

    def add_first_player_score(self):
        self.first_player_score += 1

    def add_second_player_score(self):
        self.second_player_score += 1

    def _is_equal_score(self) -> bool:
        return self.first_player_score == self.second_player_score

    def _is_deuce(self) -> bool:
        return self.first_player_score >= 3 and self.second_player_score >= 3

    def _is_win(self) -> bool:
        return self.first_player_score >= 4 or self.second_player_score >= 4

    def _get_adv_player_name(self) -> str:
        if self.first_player_score > self.second_player_score:
            return self.first_player_name
        return self.second_player_name

    def score(self) -> str:
        if self._is_deuce():
            if abs(self.first_player_score - self.second_player_score) == 1:
                return f"{self._get_adv_player_name()} adv"
            if abs(self.first_player_score - self.second_player_score) == 2:
                return f"{self._get_adv_player_name()} win"
            return "deuce"
        if self._is_equal_score():
            return f"{self.score_dict[self.first_player_score]} all"
        if self._is_win():
            return f"{self._get_adv_player_name()} win"
        return f"{self.score_dict[self.first_player_score]} {self.score_dict[self.second_player_score]}"
