import numpy as np
import matplotlib.pyplot as plt


def ballistic_trajectory(initial_velocity, launch_angle_deg):
    # Преобразование угла из градусов в радианы
    launch_angle_rad = np.radians(launch_angle_deg)

    # Гравитационная постоянная
    g = 10
    # Проверка на крайние случаи
    if launch_angle_deg == 90:  # Вертикальный бросок
        flight_time = 2 * initial_velocity / g
        x_coords = np.zeros(100)  # Траектория горизонтально
        y_coords = initial_velocity * np.linspace(0, flight_time, num=100) - 0.5 * g * np.linspace(0, flight_time,
                                                                                                   num=100) ** 2
    elif launch_angle_deg == 0 or launch_angle_deg == 180:  # Горизонтальный бросок
        flight_time = 0
        x_coords = np.array([0, 0])  # Начальная и конечная точки на земле
        y_coords = np.array([0, 0])
    else:
        # Время полета
        flight_time = (2 * initial_velocity * np.sin(launch_angle_rad)) / g

        # Временные интервалы для моделирования траектории
        time_intervals = np.linspace(0, flight_time, num=100)

        # Расчет координат x и y
        x_coords = initial_velocity * np.cos(launch_angle_rad) * time_intervals
        y_coords = initial_velocity * np.sin(launch_angle_rad) * time_intervals - 0.5 * g * time_intervals ** 2
    print(f'\nВремя полёта: {round(flight_time, 5)} c')
    print(f'Дальность полёта {round(max(x_coords), 5)} м')
    print(f'Высота полёта: {round(max(y_coords), 5)} м')
    return x_coords, y_coords


def plot_trajectory(x_coords, y_coords):
    plt.figure()
    plt.plot(x_coords, y_coords)
    plt.title('Баллистическая траектория')
    plt.xlabel('Расстояние, м')
    plt.ylabel('Высота, м')
    plt.grid(True) # Видимость сетки
    plt.show()


if __name__ == "__main__":
    initial_velocity = float(input("Введите начальную скорость (м/с): "))
    launch_angle_deg = float(input("Введите угол полёта относительно горизонта (градусы): "))

    x_coords, y_coords = ballistic_trajectory(initial_velocity, launch_angle_deg)
    plot_trajectory(x_coords, y_coords)

