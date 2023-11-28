import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_Form

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.generate_password)
    def generate_password(self):
        password = ""
        symbol = string.punctuation
        for i in range(8):
            rand = random.randint(0, 10)
            a = ['1', '2', '3', '4', '5', '4', '7', '9']
            b = ['ф', 'і', 'е', 'ц', 'у', 'ш', 'щ', 'ю', 'п', 'и', 'и', 'ч']
            if self.ui.cb_alphabete.isChecked() and rand > 5:
                password += random.choice(a)
            if self.ui.checkBox.isChecked() and rand <= 5:
                password += random.choice(b)
            password += random.choice(symbol)
            self.ui.result.setText(password)
        print(password)
        
if __name__ == "__main__":
    app = QApplication([])
    ex = Widget()
    ex.show()
    app.exec_()