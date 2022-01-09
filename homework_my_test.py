M_IN_KM = 1000

class InfoMessage:
        def __init__(self,
                 training_type,
                 duration,
                 distance,
                 speed,
                 calories
                 ) -> None:
        self.training_type = training_type,
        self.duration = duration,
        self.distance = distance,
        self.speed = speed,
        self.calories = calories


class Training:
    """Базовый класс тренировки."""
    #LEN_STEP = 0.65
    #M_IN_KM = 1000
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self, action) -> float:
        """Получить дистанцию в км."""
        LEN_STEP = 0.65
        M_IN_KM = 1000
        distance = action * LEN_STEP / M_IN_KM
        return distance


    def get_mean_speed(self, distance, duration) -> float:
        """Получить среднюю скорость движения."""
        #дистанция / длительность
        mean_speed = distance / duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        pass


class Running(Training):
    """Тренировка: бег."""
    #
    def get_spent_calories(self, duration, mean_speed, weight):
        spent_calories = (18 * mean_speed – 20) * weight / M_IN_KM * duration
        return spent_calories




class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self, distance, duration) -> float:
        mean_speed = self.length_pool * self.count_pool / M_IN_KM / duration
        return mean_speed

    def get_spent_calories(self, mean_speed, weight) -> float:
        spent_calories = (self.mean_speed + 1.1) * 2 * self.weight
        return spent_calories

    # формула расчёта





def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

