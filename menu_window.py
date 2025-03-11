# menu_window.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import ( 
     QWidget, QVBoxLayout, QHBoxLayout, 
     QPushButton, QLabel, QLineEdit, QFormLayout
)

from question import *

vbox_layout = QVBoxLayout()

menu_win = QWidget()
menu_win.setWindowTitle("Меню управління картками")

form = QFormLayout()
textinput1 = QLineEdit()

form.addRow("Введіть запитання:", textinput1)
textinput2 = QLineEdit()
form.addRow("Введіть вірну відповідь:", textinput2)
textinput3 = QLineEdit()
form.addRow("Введіть першу хибну відповідь:", textinput3)
textinput4 = QLineEdit()
form.addRow("Введіть другу хибну відповідь:", textinput4)
textinput5 = QLineEdit()
form.addRow("Введіть третю хибну відповідь:", textinput5)
vbox_layout.addLayout(form)

hbox = QHBoxLayout()
add_question_btn = QPushButton("Додати запитання")

def add_question():
     question = textinput1.text()
     correctAns = textinput2.text()
     wrongans1 = textinput3.text()
     wrongans2 = textinput4.text()
     wrongans3 = textinput5.text()
     if len(question) > 0 and \
     len(correctAns) > 0 and \
     len(wrongans1) > 0 and \
     len(wrongans2) > 0 and \
     len(wrongans3) > 0:
          new_question = Question(question, 
                                  correctAns, 
                                  wrongans1,
                                  wrongans2,
                                  wrongans3)
          questions.append(new_question)

add_question_btn.clicked.connect(add_question)

clear_btn = QPushButton("Очистити")

def clear_fields():
     for text_input in [textinput1, textinput2, textinput3, textinput4, textinput5]:
          text_input.clear()

clear_btn.clicked.connect(clear_fields)

hbox.addWidget(add_question_btn)
hbox.addWidget(clear_btn)
vbox_layout.addLayout(hbox)

statistic_title_lbl = QLabel("Статистика")

statistic_lbl = QLabel("Разів відповіли: 0\nВірних відповідей: 0\nУспішність: 0%")
vbox_layout.addWidget(statistic_title_lbl)
vbox_layout.addWidget(statistic_lbl)

back_btn = QPushButton("Назад")
vbox_layout.addWidget(back_btn)

menu_win.setLayout(vbox_layout)

def populate_question(question):
     textinput1.setText(question.question)
     textinput2.setText(question.correct_answer)
     textinput3.setText(question.wrong_ans1)
     textinput4.setText(question.wrong_ans2)
     textinput5.setText(question.wrong_ans3)