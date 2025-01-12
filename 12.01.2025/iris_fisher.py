import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import numpy as np

# 1. Загрузка и подготовка данных
iris = load_iris()
X = iris.data
y = iris.target

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Масштабирование данных
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# 2. Определение модели
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(3, activation='softmax')
])

# 3. Компиляция модели
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 4. Обучение модели
history = model.fit(X_train, y_train, epochs=100, validation_split=0.1, verbose=0)

# 5. Оценка модели
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Точность на тестовых данных: {accuracy:.4f}")

# 6. Предсказание на новых данных (с выводом только одного наиболее вероятного класса)
new_data = [[5.1, 3.5, 1.4, 0.2], [6.2, 2.9, 4.3, 1.3], [7.7, 3.0, 6.1, 2.3]]
new_data_scaled = scaler.transform(new_data)

predictions = model.predict(new_data_scaled)
predicted_classes = np.argmax(predictions, axis=1) # Получаем индексы наиболее вероятных классов

for i, predicted_class in enumerate(predicted_classes): # Проходим по всем наборам данных
    predicted_name = iris.target_names[predicted_class]
    print(f"Предсказание для набора данных {i+1}: {predicted_name}")

# Выводим возможные названия видов
print("Возможные названия видов:")
print(iris.target_names)

