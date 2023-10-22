class RaceResult:
    def __init__(self, car_one, car_two):
        self.car_one = car_one
        self.car_two = car_two
        self.winner = None
        self.calculate_winner()

    def calculate_winner(self):
        if self.car_one.disqualified and self.car_two.disqualified:
            self.winner = "Draw - Both cars had a false start!"
        elif self.car_one.disqualified:
            self.winner = "Car Two wins - Car One had a false start!"
        elif self.car_two.disqualified:
            self.winner = "Car One wins - Car Two had a false start!"
        else:
            car_one_time = (
                self.car_one.get_race_time() + self.car_one.get_reaction_time()
            )
            car_two_time = (
                self.car_two.get_race_time() + self.car_two.get_reaction_time()
            )
            if car_one_time < car_two_time:
                self.winner = "Car One wins!"
            elif car_one_time > car_two_time:
                self.winner = "Car Two wins!"
            else:
                self.winner = "Draw!"
