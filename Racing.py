class Car:
    def __init__(self, name, model, max_speed):
        self._name = name
        self._model = model
        self._max_speed = max_speed

    def __int__(self):
        return self._max_speed

    def __str__(self):
        return self._name + " " + self._model


class Driver:
    def __init__(self, name, car, skill):
        self._name = name
        self._car = car
        self._skill = skill

    def race_car(self):
        return str(self._car)

    def __int__(self):
        return self._skill

    def __str__(self):
        return self._name

    def get_car_speed(self):
        return int(self._car)

    def get__skill(self):
        return self._skill


class Race:
    def __init__(self, drivers, skill_needed):
        self._drivers = drivers
        self._leaderboard = {}
        for x in self._drivers:
            self._leaderboard[str(x)] = 0
        self._skill_needed = skill_needed
        self._crashed = []
        self._sort_em()

    def show_drivers(self):
        show_em = []
        for x in self._drivers:
            show_em.append(str(x))
        return show_em

    def show_leaderboard(self):
        return self._leaderboard

    def _crashes(self):
        for x in self._drivers:
            if x.get__skill() < self._skill_needed:
                self._crashed.append(x)

    def get_crashed(self):
        return self._crashed

    def _get_standings(self):
        pass

    def _sort_em(self):
        for i in range(1, len(self._drivers)):
            current = self._drivers[i]
            pos = i
            while pos > 0 and self._drivers[pos - 1].get_car_speed() < current.get_car_speed():
                self._drivers[pos] = self._drivers[pos - 1]
                pos = pos - 1
            self._drivers[pos] = current

    def _make_leaderboard(self):
        self._get_standings()
        self._crashes()
        self._sort_em()
        points = [8, 6, 4]
        not_crashed = [x for x in self._drivers if x not in self._crashed]
        for x in range(0, len(not_crashed)):
            self._leaderboard[str(not_crashed[x])] = points[x]

    def race_em(self):
        self._make_leaderboard()
        for x in self._crashed:
            print(str(x) + " crashed")

        return self._leaderboard


class Championship:
    def __init__(self, races):
        self._races = races
        self._final = {}

    def _leaderboard(self):
        self._final = {key: 0 for key in self._races[0].show_leaderboard().keys()}
        for race in self._races:
            for board in race.show_leaderboard().keys():
                self._final[board] += race.show_leaderboard()[board]

    def do_races(self):
        for race in self._races:
            race.race_em()
        self._leaderboard()

    def get_final(self):
        return self._final
