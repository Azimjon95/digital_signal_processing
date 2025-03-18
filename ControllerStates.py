import numpy as np
import matplotlib.pyplot as plt

# === Параметры канала связи ===
delay = 120  # Задержка в мс
throughput = 10  # Пропускная способность в Мбит/с
error_rate = 0.02  # Ошибки передачи (доля)
packet_loss = 0.05  # Потери пакетов (доля)

# === Нормализация параметров ===
# Установка норм диапазонов для каждого параметра
delay_min, delay_max = 0, 100  # Нормальный диапазон для задержки
throughput_min, throughput_max = 1, 20  # Нормальный диапазон для пропускной способности
error_rate_min, error_rate_max = 0, 0.01  # Нормальный диапазон для ошибок передачи
packet_loss_min, packet_loss_max = 0, 0.01  # Нормальный диапазон для потерь пакетов

# Нормализация параметров
x_delay = (delay - delay_min) / (delay_max - delay_min)
x_throughput = (throughput - throughput_min) / (throughput_max - throughput_min)
x_error_rate = (error_rate - error_rate_min) / (error_rate_max - error_rate_min)
x_packet_loss = (packet_loss - packet_loss_min) / (packet_loss_max - packet_loss_min)

# === Весовые коэффициенты ===
w_delay = 0.3  # Вес для задержки
w_throughput = 0.3  # Вес для пропускной способности
w_error_rate = 0.2  # Вес для ошибок передачи
w_packet_loss = 0.2  # Вес для потерь пакетов

# === Расчет интегральной оценки ===
S = (w_delay * (1 - x_delay) +
     w_throughput * (1 - x_throughput) +
     w_error_rate * (1 - x_error_rate) +
     w_packet_loss * (1 - x_packet_loss))

# === Интерпретация результата ===
if S > 0.8:
    status = 'Канал связи работает нормально'
elif 0.5 <= S <= 0.8:
    status = 'Канал перегружен или требует оптимизации'
else:
    status = 'Канал связи неисправен'

# === Вывод результатов ===
print('--- Результаты диагностики канала связи ---')
print(f'Задержка: {delay:.2f} мс (нормализованное значение: {x_delay:.2f})')
print(f'Пропускная способность: {throughput:.2f} Мбит/с (нормализованное значение: {x_throughput:.2f})')
print(f'Ошибки передачи: {error_rate * 100:.2f}% (нормализованное значение: {x_error_rate:.2f})')
print(f'Потери пакетов: {packet_loss * 100:.2f}% (нормализованное значение: {x_packet_loss:.2f})')
print(f'Интегральная оценка: {S:.4f}')
print(f'Решение: {status}')

# === График нормализованных значений ===
params = ['Задержка', 'Пропускная способность', 'Ошибки передачи', 'Потери пакетов']
normalized_values = [x_delay, x_throughput, x_error_rate, x_packet_loss]

plt.figure(figsize=(8, 6))
plt.bar(params, normalized_values, color='b', label='Нормализованные параметры')
plt.plot(params, [1, 1, 1, 1], 'r--', linewidth=2, label='Идеальное состояние')
plt.ylabel('Нормализованное значение')
plt.title('Нормализованные параметры канала связи')
plt.grid(True)
plt.legend()
plt.show()
