
# main_window.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QSpinBox, QLabel, QGroupBox, QButtonGroup, QRadioButton
)

from random import shuffle, randint
from question import *

main_win = QWidget()
main_win.resize(600, 500)
main_win.setWindowTitle("Memory Card - Неділя 16:00")
main_win.move(100, 100)

question = questions[randint(0, len(questions) - 1)]

# top UI
layout_card = QVBoxLayout()
top_layout = QHBoxLayout()
menu_btn = QPushButton("Меню")
top_layout.addWidget(menu_btn, alignment=Qt.AlignLeft, stretch=1)

rest_btn = QPushButton("Відпочити")
top_layout.addWidget(rest_btn, alignment=Qt.AlignRight)

box_minutes = QSpinBox()
box_minutes.setValue(30)
top_layout.addWidget(box_minutes, alignment=Qt.AlignRight)

minutes_lbl = QLabel("хвилин")
top_layout.addWidget(minutes_lbl, alignment=Qt.AlignRight)

layout_card.addLayout(top_layout, stretch=1)

word_label = QLabel("?")
layout_card.addWidget(word_label, stretch=1, alignment=Qt.AlignTop | Qt.AlignCenter)

# main block
group_box = QGroupBox("Варіанти відповідей")

radio_btns_group = QButtonGroup()
radio1 = QRadioButton("2")
radio2 = QRadioButton("1")
radio3 = QRadioButton("3")
radio4 = QRadioButton("4")
radio_btns_group.addButton(radio1)
radio_btns_group.addButton(radio2)
radio_btns_group.addButton(radio3)
radio_btns_group.addButton(radio4)

layout1 = QHBoxLayout()
layout1_1 = QVBoxLayout()
layout1_2 = QVBoxLayout()
layout1_1.addWidget(radio1)
layout1_1.addWidget(radio2)
layout1_2.addWidget(radio3)
layout1_2.addWidget(radio4)
layout1.addLayout(layout1_1)
layout1.addLayout(layout1_2)
group_box.setLayout(layout1)

layout_card.addWidget(group_box, stretch=7)

# answer block
answer_block = QGroupBox("Результат")

is_correct_label = QLabel("Правильно")
correct_answer_lbl = QLabel("СЛОВО ВІДПОВІДЬ")

answer_layout = QVBoxLayout()
answer_layout.addWidget(is_correct_label, alignment=Qt.AlignTop | Qt.AlignLeft)
answer_layout.addWidget(correct_answer_lbl, alignment=Qt.AlignCenter, stretch=2)

answer_block.setLayout(answer_layout)
answer_block.hide()
layout_card.addWidget(answer_block, stretch=7)

# bottom buttom
answer_btn = QPushButton("Відповісти")

def reset_radio_buttons():
    global radio1, radio2, radio3, radio4, radio_btns_group
    radio_btns_group.setExclusive(False)
    for radio in [radio1, radio2, radio3, radio4]:
        radio.setChecked(False)
    radio_btns_group.setExclusive(True)

def show_result():
    # fill answer_block
    global question
    answer = ""
    for radio in [radio1, radio2, radio3, radio4]:
        if radio.isChecked():
            answer = radio.text()

    print(answer)
    if question.check_answer(answer):
        is_correct_label.setText("Правильно!")
    else:
        is_correct_label.setText("Неправильно!")

    correct_answer_lbl.setText(question.correct_answer)

    answer_block.show()
    group_box.hide()
    answer_btn.setText("Наступне запитання")

def show_question():
    global question, questions
    # fill radio buttons from group_box
    # select question question = get_next()
    new_index = randint(0, len(questions) - 1)
    new_question = questions[new_index]
    while question.question == new_question.question:
        new_index = randint(0, len(questions) - 1)
        new_question = questions[new_index]
    question = new_question
    radio_questions = question.variants() # shuffle variants
    shuffle(radio_questions)
    word_label.setText(question.question)

    radio1.setText(radio_questions[0])
    radio2.setText(radio_questions[1])
    radio3.setText(radio_questions[2])
    radio4.setText(radio_questions[3])

    answer_block.hide()
    reset_radio_buttons()
    group_box.show()
    answer_btn.setText("Відповісти")
def button_processing():
    global answer_btn
    if answer_btn.text().lower() == "відповісти":
        if radio1.isChecked() or \
            radio2.isChecked() or \
            radio3.isChecked() or \
            radio4.isChecked():
            show_result()
    else:
        show_question()
     
answer_btn.clicked.connect(button_processing)

layout_card.addWidget(answer_btn, stretch=1, alignment=Qt.AlignBottom | Qt.AlignCenter)
main_win.setLayout(layout_card)

main_win.show()