from PySide6.QtWidgets import QApplication 
from controllers.main_interface import DownloadYoutube
import sys

if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    window = DownloadYoutube() 
    window.show()
    sys.exit(app.exec())
