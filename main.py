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
        return (
            f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.;\
             Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч;\
              Потрачено ккал: {self.calories}')


class Training:
    """Базовый класс тренировки."""

    M_IN_KM = 1000
    LEN_STEP = 0.65

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

        action = self.action
        distance = action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self, distance, duration) -> float:
        """Получить среднюю скорость движения."""

        mean_speed = distance / self.duration
        return mean_speed

    def get_spent_calories(self, mean_speed, weight, duration, height) -> \
            float:
        """Получить количество затраченных калорий."""
        # weight = self.weight
        spent_calories = (18 * mean_speed - 20) * self.weight / self.M_IN_KM * self.duration
        return spent_calories

    def show_training_info(self) -> InfoMessage:
        distance = self.get_distance(self.action)
        mean_speed = self.get_mean_speed(self.get_distance(self.action),
                                         self.duration)
        calories = self.get_spent_calories(mean_speed, self.weight,
                                           self.duration)
        duration = self.duration
        workout_type = self.__class__.__name__

        info_mess = InfoMessage(workout_type, duration, distance, mean_speed,
                                calories)

        return info_mess


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38

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
        mean_speed = self.length_pool * self.count_pool / self.M_IN_KM / duration
        return mean_speed

    def get_spent_calories(self, mean_speed, weight, duration) -> float:
        spent_calories = (mean_speed + 1.1) * 2 * self.weight

        return spent_calories

        # print(info_mes)


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self, mean_speed, weight, duration) -> float:
        spent_calories = (18 * mean_speed - 20) * \
                         self.weight / self.M_IN_KM * self.duration * 60
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
                           ) -> float:

        spent_calories = (0.035 * self.weight + (mean_speed ** 2 // self.height) * 0.029 * \
                          self.weight) * self.duration * 60
        return spent_calories

    def show_training_info(self) -> InfoMessage:
        distance = self.get_distance(self.action)
        mean_speed = self.get_mean_speed(self.get_distance(self.action),
                                         self.duration)
        calories = self.get_spent_calories(mean_speed, self.weight,
                                           self.duration, self.height)
        duration = self.duration
        workout_type = self.__class__.__name__

        info_mess = InfoMessage(workout_type, duration, distance, mean_speed,
                                calories)

        return info_mess

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'SWM':
        swm_object_class_training = Swimming(*data)
        return swm_object_class_training

    elif workout_type == 'RUN':
        run_object_class_training = Running(*data)
        return run_object_class_training

    elif workout_type == 'WLK':
        wlk_object_class_training = SportsWalking(*data)
        return wlk_object_class_training

def main(training: Training) -> None:
  """Главная функция."""
  info = training.show_training_info()
  message = info.get_message()
  print(message)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
