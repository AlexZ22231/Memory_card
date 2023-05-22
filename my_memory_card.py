from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize (400, 300)
btn_OK = QPushButton('Ответить')

main_win.total = 0
main_win.score = 0

but1 = QRadioButton()
but2 = QRadioButton()
but3 = QRadioButton()
but4 = QRadioButton()

main_win.cur_question = -1

lb_Question = QLabel()

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
RadioGroupBox.setLayout(layout_ans1) 


layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)




AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
answer = QLabel('Правильный ответ')
layout_correct_answer = QVBoxLayout()
layout_correct_answer.addWidget(result)
layout_correct_answer.addWidget(answer, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
AnsGroupBox.setLayout(layout_correct_answer)

class Question():
    def __init__(
self, question, right_answer, 
wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


layout_line1 = QVBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=Qt.AlignLeft)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line2.setSpacing(10) 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2, alignment= Qt.AlignHCenter) 
layout_line3.addStretch(1)

questions = list()
questions.append(Question('Выбери перевод слова "переменная"', 'variable', 'variation', 'variant', 'changing'))
questions.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Английский'))
questions.append(Question('Какой национальности не существует?', 'Смурфы', 'Чулымцы', 'Энцы', 'Алеуты'))
questions.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))

def next_question():
    main_win.cur_question = randint(0, len(questions)-1)
    ask(questions[main_win.cur_question])



def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    elif btn_OK.text() == 'Следующий вопрос':
        next_question()




def show_question(question):
    lb_Question.setText(question)
    RadioGroup = QButtonGroup()
    RadioGroup.addButton(rbtn_1)
    RadioGroup.addButton(rbtn_2)
    RadioGroup.addButton(rbtn_3)
    RadioGroup.addButton(rbtn_4)
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)    
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 



def ask(obj_question):
    
    rbtn_1.setText(obj_question.right_answer)
    rbtn_2.setText(obj_question.wrong1) 
    rbtn_3.setText(obj_question.wrong2)
    rbtn_4.setText(obj_question.wrong3)
    answer.setText(obj_question.right_answer)
    shuffle(answers)
    answers[0].setText(obj_question.right_answer)
    answers[1].setText(obj_question.wrong1)
    answers[2].setText(obj_question.wrong2)
    answers[3].setText(obj_question.wrong3)
    show_question(obj_question.question)

def show_correct(res):
    result.setText(res)
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
    

def check_answer():
    main_win.total += 1
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        
    else:
        show_correct('Неверно!')
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов:', main_win.score)
    print('Рейтинг:', main_win.score/main_win.total*100, '%')
    

next_question()

btn_OK.clicked.connect(click_ok)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.setSpacing(10) 

main_win.setLayout(layout_card)


main_win.show()
app.exec_()