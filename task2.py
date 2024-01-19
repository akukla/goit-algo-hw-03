import turtle
import argparse


def koch_snowflake(t, depth, size):
    if depth == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, depth-1, size/3)
            t.left(angle)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Створення фракталу «сніжинка Коха»')
        parser.add_argument('depth', type=int, default=2, help='Глибина рекурсії (integer)')
        
        args = parser.parse_args()
        depth = args.depth

        # Ініціалізуємо turtle
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Koch Snowflake")

        fractal_turtle = turtle.Turtle()
        fractal_turtle.speed(0)  # Задаємо швидкість turtle
    
        fractal_turtle.penup()
        fractal_turtle.goto(-150, 90)
        fractal_turtle.pendown()

        # Запускаємо генерацію фракталу
        koch_snowflake(fractal_turtle, depth, 300)

        # Закриваємо turtle по кліку на вікні
        screen.exitonclick()
    except SystemExit: # Не потрібно нічого робити, argparse вже вивів повідомлення про помилку
        pass
