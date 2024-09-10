import numpy as np
import matplotlib.pyplot as plt

# Генерация данных
num_records = np.arange(100, 10500, 500)  # От 100 до 10000 с шагом 500

def query_time_base(x):
    if x <= 2000:
        return 10 + np.random.rand() * 2  # Небольшие колебания около 10 мс
    else:
        return 10 + 0.00375 * (x - 2000)**1.5 + np.random.rand() * 5  # Нелинейный рост после 2000

query_time = np.vectorize(query_time_base)

# Моделирование влияния индексов
no_index_times = query_time(num_records)
btree_times = no_index_times * 0.8  # B-Tree обычно ускоряет запросы
hash_times = no_index_times * 0.7  # Hash может быть еще быстрее для точечных запросов

# Создание графика
plt.figure(figsize=(12, 7))
plt.plot(num_records, no_index_times, marker='o', label='Без индекса')
plt.plot(num_records, btree_times, marker='s', label='B-Tree')
plt.plot(num_records, hash_times, marker='^', label='Hash')

plt.xlabel('Количество записей в таблице teachers', fontsize=12)
plt.ylabel('Время выполнения запроса (мс)', fontsize=12)
plt.title('Влияние индексов на время запроса подходящего преподавателя', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.xlim(0, 11000)
plt.ylim(0, max(no_index_times) * 1.1)

# Добавление пояснительного текста
plt.text(0.05, 0.95, 'До 2000 записей:\nразница менее заметна', transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top')
plt.text(0.7, 0.3, 'После 2000 записей:\nзаметное влияние индексов', transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='bottom')

plt.savefig('teacher_query_index_performance.png', dpi=300, bbox_inches='tight')
plt.show()

# Вывод некоторых значений для проверки
print(f"Время при 10000 записях:")
print(f"Без индекса: {no_index_times[-1]:.2f} мс")
print(f"B-Tree: {btree_times[-1]:.2f} мс")
print(f"Hash: {hash_times[-1]:.2f} мс")