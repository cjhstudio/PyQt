import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("radio.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 시그널 입력부분

        # 버튼(QPushBotton) : self.라디오버튼이름.clicked.connect(함수)
        self.groupBox_rad1.clicked.connect(self.groupRadFunction)
        self.groupBox_rad2.clicked.connect(self.groupRadFunction)
        self.groupBox_rad3.clicked.connect(self.groupRadFunction)

    def groupRadFunction(self):
        if self.groupBox_rad1.isChecked() : print('GroupBox_rad1 Checked')
        elif self.groupBox_rad2.isChecked() : print('GroupBox_rad2 Checked')
        elif self.groupBox_rad3.isChecked() : print('GroupBox_rad3 Checked')



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()