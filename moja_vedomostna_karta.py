import sys
print(sys.executable)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout, QButtonGroup
from random import shuffle 

class Question():
    '''contains a question, a correct answer and three incorrect ones'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3 
        
app = QApplication([])



main_win = QWidget()
main_win.setWindowTitle("Otázky a odpovede")
main_win.setGeometry(100, 100, 500, 300)

layout = QVBoxLayout()

question_label = QLabel("Ktorá z národností neexistuje?")
layout.addWidget(question_label)

answer_group = QGroupBox("Odpovede")
answer_layout = QVBoxLayout()

radio_button1 = QRadioButton("Slovensko")
radio_button2 = QRadioButton("Československo")
radio_button3 = QRadioButton("Maďarsko")
radio_button4 = QRadioButton("Česká")

RadioGroup = QButtonGroup()
RadioGroup.addButton(radio_button1)
RadioGroup.addButton(radio_button2)
RadioGroup.addButton(radio_button3)
RadioGroup.addButton(radio_button4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

answer_layout.addWidget(radio_button1)
answer_layout.addWidget(radio_button2)
answer_layout.addWidget(radio_button3)
answer_layout.addWidget(radio_button4)

answer_group.setLayout(answer_layout)
layout.addWidget(answer_group)

evaluate_button = QPushButton("Vyhodnotiť")
layout.addWidget(evaluate_button)


result_label = QLabel("Výsledok:")
result_value_label = QLabel("")
correct_answer_label = QLabel("Správna odpoveď: Československo")


answer_group.hide()



result_layout = QVBoxLayout()
result_layout.addWidget(result_label)
result_layout.addWidget(result_value_label)
result_layout.addWidget(correct_answer_label)


layout.addLayout(result_layout)


layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

main_win.setLayout(layout)
main_win.show()


main_win = QWidget()
main_win.setWindowTitle("Otázky a odpovede")
main_win.setGeometry(100, 100, 500, 300)

layout = QVBoxLayout()

question_label = QLabel("Ktorá z národností neexistuje?")
layout.addWidget(question_label)

answer_group = QGroupBox("Odpovede")
answer_layout = QVBoxLayout()




answer_group.setLayout(answer_layout)
layout.addWidget(answer_group)

evaluate_button = QPushButton("Vyhodnotiť")
layout.addWidget(evaluate_button)


result_label = QLabel("Výsledok:")
result_value_label = QLabel("")
correct_answer_label = QLabel("Správna odpoveď: Československo")


answer_group.hide()





result_layout = QVBoxLayout()
result_layout.addWidget(result_label)
result_layout.addWidget(result_value_label)
result_layout.addWidget(correct_answer_label)


layout.addLayout(result_layout)


layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

main_win.setLayout(layout)
main_win.show()


answers = [radio_button1, radio_button2, radio_button3, radio_button4]

def show_question():
    ''' show question panel '''
    answer_layout.show()
    answer_layout.hide()
    evaluate_button.setText('Answer')
    RadioGroup.setExclusive(False)
    radio_button1.setChecked(False)
    radio_button2.setChecked(False)
    radio_button3.setChecked(False)
    radio_button4.setChecked(False)
    RadioGroup.setExclusive(True)


def ask(question, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1) 
    answers[2].setText(wrong2) 
    answers[3].setText(wrong3)
    question_label.setText(question)
    question_label.setText(right_answer)



app.exec()

app.exec()