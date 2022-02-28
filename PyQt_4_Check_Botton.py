import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("check_botton.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 시그널 입력부분

        # 체크박스(QCheckBox) : self.체크박스이름.stateChanged.connect(함수)

        # 그룹박스 밖의 체크박스
        self.chk_1.stateChanged.connect(self.chkFunction)
        self.chk_2.stateChanged.connect(self.chkFunction)
        self.chk_3.stateChanged.connect(self.chkFunction)

        # 그룹박스 안의 체크박스
        self.groupchk_1.stateChanged.connect(self.groupchkFunction)
        self.groupchk_2.stateChanged.connect(self.groupchkFunction)
        self.groupchk_3.stateChanged.connect(self.groupchkFunction)

    def chkFunction(self): # 체크박스는 여러개가 선택가능하기 때문에 elif를 사용하지 않음
        if self.chk_1.isChecked() : print('check_1 is cheked')
        if self.chk_2.isChecked() : print('check_2 is cheked')
        if self.chk_3.isChecked() : print('check_3 is cheked')

    def groupchkFunction(self):
        if self.groupchk_1.isChecked() : print('Group_check_1 is cheked')
        if self.groupchk_2.isChecked() : print('Group_check_2 is cheked')
        if self.groupchk_3.isChecked() : print('Group_check_3 is cheked')
        



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()