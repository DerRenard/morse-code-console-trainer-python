#!/usr/bin/python
import assets.codes as code 
import assets.start as start
import assets.quiz as quiz

startOptions = start.startOptons()
stats = quiz.quiz(startOptions["lang"], startOptions["sumb"])

print(f"""
Правильно: {stats["correct"]}
Неравильно: {stats["incorrect"]}
Ошибки в {stats["mistakes"]}
Всего вопросов: {stats["range"]}
""")