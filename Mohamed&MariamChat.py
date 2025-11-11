import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen, QProgressBar
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtGui import QPixmap, QFont, QColor, QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mariam & Mohamed Chat")
        self.setGeometry(100, 100, 1200, 800)

        # 🔗 تحميل الموقع
        self.browser = QWebEngineView()
        self.browser.load(QUrl("https://shhhh111.github.io/Mohamed-And-Mariam/"))
        self.setCentralWidget(self.browser)

        # أيقونة النافذة
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(base_path, "logo_mohamed_and_mariam.ico")
        self.setWindowIcon(QIcon(icon_path))

class SplashScreen(QSplashScreen):
    def __init__(self):
        pixmap = QPixmap(400, 300)
        pixmap.fill(QColor("black"))
        super().__init__(pixmap)
        self.setFont(QFont("Arial", 16))

        # شريط التحميل
        self.progress = QProgressBar(self)
        self.progress.setGeometry(50, 230, 300, 20)
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.showMessage("🚀 جاري تشغيل المحادثة", 0x0094, QColor("white"))
        self.counter = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(30)  # سرعة التحميل

    def update_progress(self):
        self.counter += 1
        self.progress.setValue(self.counter)
        if self.counter >= 100:
            self.timer.stop()
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()

    # بعد التحميل يفتح البرنامج
    window = MainWindow()
    QTimer.singleShot(3200, window.show)

    sys.exit(app.exec_())

