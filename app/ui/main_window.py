import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TARS Utility Hub")
        self.resize(400, 200)

        # Create a container widget (central widget) to hold our layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout to position widgets vertically
        layout = QVBoxLayout(central_widget)

        # Add a text label
        self.label = QLabel("Welcome to TARS Utility Hub!", alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        # Add a button
        button = QPushButton("Click Me!")
        layout.addWidget(button)

        # Connect the button click signal to our slot method
        button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText("Hello from PySide6!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
