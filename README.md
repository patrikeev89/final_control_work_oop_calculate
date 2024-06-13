# final_control_work_oop_calculate

# Калькулятор Комплексных Чисел

## Описание
Этот проект представляет собой калькулятор для выполнения операций сложения, умножения и деления комплексных чисел.

## Установка и Запуск

1. Убедитесь, что у вас установлен Python 3.7 или выше.
2. Склонируйте репозиторий:
    ```
    git clone https://github.com/patrikeev89/final_control_work_oop_calculate.git
    ```
3. Перейдите в директорию проекта:
    ```
    cd complex-calculator
    ```
4. (Необязательно) Создайте виртуальное окружение:
    ```
    python -m venv venv
    source venv/bin/activate   # для Windows используйте `venv\Scripts\activate`
    ```
5. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```
6. Запустите приложение:
    ```
    python calculator/main.py
    ```

## Примеры

### Сложение
num1 = ComplexNumber(3, 2)
num2 = ComplexNumber(1, 7)
result = calculator.add(num1, num2)
print(result) # 4 + 9i

### Умножение
num1 = ComplexNumber(3, 2)
num2 = ComplexNumber(1, 7)
result = calculator.multiply(num1, num2)
print(result) # -11 + 23i

### Деление
num1 = ComplexNumber(3, 2)
num2 = ComplexNumber(1, 7)
result = calculator.divide(num1, num2)
print(result) # 0.2 - 0.4i


SOLID Принципы
Single Responsibility Principle: Каждый класс имеет одну ответственность.
Open/Closed Principle: Классы легко расширять, но не изменять.
Liskov Substitution Principle: Нет наследования, все классы могут использоваться взаимозаменяемо.
Interface Segregation Principle: Интерфейсы не создаются, так как используется Python.
Dependency Inversion Principle: Зависимости инвертированы путем использования абстракций.

Паттерны Проектирования
Singleton: Логгер настраивается один раз и используется по всему проекту.
Factory: Классы Calculator и ComplexNumber создаются напрямую, но можно использовать фабрики для их создания.
