 ###


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        print(
            f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.; Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; Потрачено ккал: {self.calories}')


class Training:
    """Базовый класс тренировки."""


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

        distance = action * LEN_STEP / M_IN_KM
        return distance

    def get_mean_speed(self, distance, duration) -> float:
        """Получить среднюю скорость движения."""

        mean_speed = distance / duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self,
                           action: int,
                           duration: float,
                           weight: float
                           ) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info_mes = InfoMessage(self.action,
                               self.duration,
                               self.get_distance(self.action),
                               self.get_mean_speed(self.get_distance(action), self.duration),
                               self.get_spent_calories()
                               )
        #print(info_mes)
        return info_mes

        pass


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self, duration, mean_speed, weight):
        spent_calories = (18 * mean_speed - 20) * weight / M_IN_KM * duration
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.height = height

    def get_spent_calories(self,
                           duration,
                           weight,
                           height,
                           mean_speed
                           ):
        spent_calories = 0.035 * self.weight + (self.mean_speed ** 2 //
                                         self.height) * 0.029 * \
                         self.weight) * self.duration
        return spent_calories


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

# READY
def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'SWM':
        object_class_training = Swimming(data[0], data[1], data[2],
                                              data[3], data[4] )
        return object_class_training

    elif workout_type == 'RUN':
        object_class_training = Running(data[0], data[1], data[2])
        return object_class_training

    elif workout_type == 'WLK':
        object_class_training = SportsWalking(data[0], data[1], data[2],
                                              data[3])
        return object_class_training
    # * Функция должна определить тип тренировки и создать объект соответствующего класса,
    # передав ему на вход параметры, полученные во втором аргументе. Этот объект
    pass


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    info.get_message()



# READY
if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
