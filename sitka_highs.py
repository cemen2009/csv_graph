import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'data1\\sitka_weather_2018_simple.csv'  # назва файлу з датой
with open(filename) as file_object:  # юзаєм with, щоб корректно відкривався файл та закривався
    reader = csv.reader(file_object)  # створюємо рідер csv файлу
    header_row = next(reader)  # зчитуємо рядок заголовку

    # зчитування максимальних температур
    highs, days = [], []
    # чЕкаєм кожен рядок
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # читай в документації datetime шо це, бо я не їбу
        days.append(current_date)  # сподіваюсь тобі не треба пояснювати, шо робить метод append
        high = int(row[5])  # елемент з індексом 5 - максимальна темрпература
        highs.append(high)

# нанесення даних на діаграму
plt.style.use('seaborn')  # використовуємо стиль seaborn
fig, ax = plt.subplots()  # створюємо графічне зображення, де fig - вся повехня, а ax - конкретна таблиця на поверхні
ax.plot(days, highs, c='red')  # створюємо графік х=дні, у=найвищі_температури, колір_лінії=червоний

# форматування діаграми
plt.title('Daily high temperatures, July 2018', fontsize=20)  # здогадайся шо це означає
plt.xlabel('Days', fontsize=14)  # також сам спробуй
plt.ylabel('Temperature (F)', fontsize=14)  # сам

fig.autofmt_xdate()  # тепер усі значення на осях координат розміщені по діагоналі

# налаштування осей координат(якшо чесно, то я не їбу шо робить параметр which. можливо це пов'язано з ВІЧом)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()  # комп(кріпак) запускає всю цю шляпу і відображає її
