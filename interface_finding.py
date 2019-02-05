class Bcform(QWidget):

  def __init__(self):
    super().__init__()

self.initUI()

def initUI(self):

self.lbl1 = QLabel('Найден beacon-маячок:', self)

self.lbl1.move(150, 50)

self.line1 = QLineEdit(self)

self.line1.setText(ibng.key_generation()[0])

self.line1.resize(385,20)

self.line1.move(35,100)

self.btn = QPushButton("Расчитать дистанцию",self)

self.btn.setToolTip('Рассчитать дистанцию до найденного маячка?')

self.btn.resize(self.btn.sizeHint())

self.btn.move(140, 150)

self.btn.clicked.connect(self.buttonClicked)

self.lbl2 = QLabel('Расстояние до маячка:', self)

self.lbl2.move(150, 200)

self.line2 = QLineEdit(self)

self.lbl2.adjustSize()

self.line2.move(150,250)

self.lbl3 = QLabel('метр', self)

self.lbl3.move(280, 250)

self.resize(450, 350)

self.center()

self.setWindowTitle('iBeacon')

self.show()

def center(self):

qr = self.frameGeometry()

cp = QDesktopWidget().availableGeometry().center()

qr.moveCenter(cp)

self.move(qr.topLeft())

def closeEvent(self, event):

reply = QMessageBox.question(self, 'Message',

"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

if reply == QMessageBox.Yes:

event.accept()

else:

event.ignore()

def buttonClicked(self):

key,tx_power = ibng.key_generation()

rssi = ibng.get_rssi(tx_power)

dictance = ibng.get_distance(rssi,tx_power)

self.line2.setText(str(dictance))

if __name__ == '__main__':

app = QApplication(sys.argv)

ex = Bcform()

sys.exit(app.exec_())
