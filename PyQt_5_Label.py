import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("label.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 시그널 입력부분

        # 라벨(QLabel)

        # 버튼 기능 지정
        self.btn_ChgTxt.clicked.connect(self.changeTextFunction)
        self.btn_PrintTxt.clicked.connect(self.printTextFunction)
        self.btn_ClearLable.clicked.connect(self.clearTextFunction)
        


    def changeTextFunction(self):
        #self.Label이름.setText("String")
        #Label에 글자를 바꾸는 메서드
        self.label1.setText("This is Label - Change Text")

    def printTextFunction(self) :
        #self.Label이름.text()
        #Label에 있는 글자를 가져오는 메서드
        print(self.label1.text())

    def clearTextFunction(self) :
        #self.Label이름.clear()
        #Label에 있는 글자를 지우는 메서드
        self.label1.clear()



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()