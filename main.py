# main.py
from PyQt5.QtWidgets import (
    QApplication
)
from time import sleep
from PyQt5.QtCore import QTimer

app = QApplication([])

from main_window import *
from menu_window import *

menu_win.hide()

def show_window():
    main_win.show()

def rest():
    main_win.hide()
    timer_seconds = box_minutes.value() * 5 # 60 for minutes, 1 for demonstration
    # wait for 5 seconds
    QTimer.singleShot(timer_seconds * 1000, show_window)

def show_menu():
    global question
    main_win.hide()
    populate_question(question)
    menu_win.show()
    total = question.correct_count + question.wrong_count
    quality = round(question.correct_count / total * 100, 2) if total > 0 else 0
    statistics = f"Разів відповіли: {total}\nВірних відповідей: {question.correct_count}\nУспішність: {quality}%"
    statistic_lbl.setText(statistics)
# "\n" - перенесення рядка \t - tab
menu_btn.clicked.connect(show_menu)

def close_menu():
    main_win.show()
    menu_win.hide()
    show_question()

close_menu()

back_btn.clicked.connect(close_menu)

rest_btn.clicked.connect(rest)

app.exec_()