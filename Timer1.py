import sys
import os
from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QStyledItemDelegate, QInputDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtCore import QTimer, QTime, Qt
from PyQt6.QtGui import QIcon, QPixmap

class TimeDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)
        return editor

    def setModelData(self, editor, model, index):
        if index.column() == 1:  # Column 2 (index 1) contains time values
            time_text = editor.text()
            try:
                hours, minutes, seconds = time_text.split(':')
                hours = int(hours)
                minutes = int(minutes)
                seconds = int(seconds)
                if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:  # Check valid time values
                    super().setModelData(editor, model, index)
                else:
                    QMessageBox.warning(
                        editor, 'Invalid Time', 'Invalid time. Please enter a valid time in the format "HH:mm:ss".'
                    )
                    return  # Return without clearing the editor's text
            except ValueError:
                QMessageBox.warning(
                    editor, 'Invalid Format', 'Invalid time format. Please use the format "HH:mm:ss".'
                )
                return  # Return without clearing the editor's text

        super().setModelData(editor, model, index)  # Call the base class method

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TimerQT.ui", self)

        self.second_window = None

        # Initialize variables
        self.timer1 = QTimer()
        self.timer2 = QTimer()
        self.time1 = QTime(0, 0, 0)
        self.time2 = QTime(0, 0, 0)
        self.stop_start_btn = self.findChild(QtWidgets.QPushButton, 'stop_start_btn')  # According to UI file
        self.segment_timer = self.findChild(QtWidgets.QLabel, 'segment_timer')  # According to UI file
        self.total_timer = self.findChild(QtWidgets.QLabel, 'total_timer')  # According to UI file
        self.user_input = self.findChild(QtWidgets.QTableWidget, 'user_input')  # According to UI file
        self.segment_reset_btn = self.findChild(QtWidgets.QPushButton, 'segment_reset_btn')  # According to UI file
        self.all_reset_btn = self.findChild(QtWidgets.QPushButton, 'all_reset_btn')  # According to UI file
        self.table_reset_btn = self.findChild(QtWidgets.QPushButton, 'table_reset_btn')  # According to UI file

        # Connect buttons to functions
        self.stop_start_btn.clicked.connect(self.start_stop)
        self.segment_reset_btn.clicked.connect(self.segment_reset)
        self.all_reset_btn.clicked.connect(self.all_reset)
        self.table_reset_btn.clicked.connect(self.reset_table)

        self.timer1.timeout.connect(self.update_timer1)  # Connect timer1 to update_timer1
        self.timer2.timeout.connect(self.update_timer2)
        self.user_input.setItemDelegate(TimeDelegate())  # Set the custom delegate for the QTableWidget
        self.user_input.setRowCount(0)  # Reset the table
        self.user_input.setColumnCount(3)  # Set the column count
        self.user_input.setHorizontalHeaderLabels(['Segment', 'Time', 'Total Time'])  # Set the header labels

        # Initialise Icons
        self.stop_start_btn.setIcon(QIcon("Icons/Play.png"))
        self.all_reset_btn.setIcon(QIcon("Icons/Reset.png"))
        self.segment_reset_btn.setIcon(QIcon("Icons/Reset.png"))
        self.table_reset_btn.setIcon(QIcon("Icons/Reset3.png"))

        # Add an image to the graphicsView
        scene = QGraphicsScene(self)
        pixmap = QPixmap("Icons\GravityMedia.jpg")  # Replace "path_to_your_image.jpg" with the actual path to your image file
        pixmap = pixmap.scaledToWidth(self.graphicsView.width(), Qt.TransformationMode.SmoothTransformation)
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.graphicsView.setScene(scene)
        self.graphicsView.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Adjust column width of the Table column 1, starts at 0
        self.user_input.setColumnWidth(0, 250)  # Set the width of column 1 to 30
        #self.user_input.resizeColumnToContents(0)  # Adjust column width based on content

        self.second_window = None

        # Connect itemChanged signal to table_cell_changed slot
        self.user_input.itemChanged.connect(self.table_cell_changed)

    def open_second_window(self):
        self.second_window = SecondWindow()

        screen_count = QtWidgets.QApplication.screens()
        if len(screen_count) >= 2:
            # If there is a second screen, move the second window to that screen and maximize it
            screen = screen_count[1]
            second_window_rect = screen.availableGeometry()
            self.second_window.setGeometry(second_window_rect)
        else:
            # If there is no second screen, open the second window in windowed mode
            self.second_window.show()

        self.second_window.show()

    def closeEvent(self, event):
        if self.second_window:
            self.second_window.close()

    def start_stop(self):
        if self.timer1.isActive():
            self.timer1.stop()
            self.timer2.stop()
            self.stop_start_btn.setText('Start')
            self.stop_start_btn.setIcon(QIcon("Icons/Play.png"))
        else:
            self.timer1.start(1000)
            self.timer2.start(1000)
            self.stop_start_btn.setText('Stop')
            self.stop_start_btn.setIcon(QIcon("Icons/PlayStop.png"))

    def get_user_input(self):
        text, ok = QInputDialog.getText(self, 'User Input', 'Enter your text:')
        if ok:
            return text
        else:
            return None

    def segment_reset(self):
        # Store the current value of Timer 1
        current_time = self.time1

        # Reset Timer 1
        self.time1 = QTime(0, 0, 0)
        self.segment_timer.setText(self.time1.toString())
        if self.second_window:
            self.second_window.segment_timer.setText(self.time1.toString())

        # Stop both timers
        self.timer1.stop()
        self.timer2.stop()

        # Update the Stop/Start button text
        self.stop_start_btn.setText('Start')

        # Get user input and update the table
        user_text = self.get_user_input()
        if user_text is not None:
            row_position = self.user_input.rowCount()  # Get the current row count
            self.user_input.insertRow(row_position)
            self.user_input.setItem(row_position, 0, QTableWidgetItem(user_text))
            self.user_input.setItem(row_position, 1, QTableWidgetItem(current_time.toString()))

        # Calculate the total time and update column 3
        self.update_total_time()

    def all_reset(self):
        # Reset Timer 1 and Timer 2
        self.time1 = QTime(0, 0, 0)
        self.time2 = QTime(0, 0, 0)
        self.segment_timer.setText(self.time1.toString())
        self.total_timer.setText(self.time2.toString())
        if self.second_window:
            self.second_window.segment_timer.setText(self.time1.toString())
            self.second_window.total_timer.setText(self.time2.toString())

        # Stop both timers
        self.timer1.stop()
        self.timer2.stop()

        # Update the Stop/Start button text
        self.stop_start_btn.setText('Start')
        self.stop_start_btn.setIcon(QIcon("Icons/Play.png"))
        self.all_reset_btn.setIcon(QIcon("Icons/Reset.png"))
        self.segment_reset_btn.setIcon(QIcon("Icons/Reset.png"))

    def reset_table(self):
        self.user_input.setRowCount(0)
        self.update_total_time()

    def update_total_time(self):
        total_time = QTime(0, 0, 0)  # Initialize the total time

        # Calculate the total time by summing the time values in column 2
        for row in range(self.user_input.rowCount()):
            time_item = self.user_input.item(row, 1)
            if time_item is not None:
                time = QTime.fromString(time_item.text())
                total_time = total_time.addSecs(time.hour() * 3600 + time.minute() * 60 + time.second())

                # Update column 3 with the cumulative total time
                self.user_input.setItem(row, 2, QTableWidgetItem(total_time.toString()))

    def update_timer1(self):
        self.time1 = self.time1.addSecs(1)
        self.segment_timer.setText(self.time1.toString())
        if self.second_window:
            self.second_window.segment_timer.setText(self.time1.toString())

    def update_timer2(self):
        self.time2 = self.time2.addSecs(1)
        self.total_timer.setText(self.time2.toString())
        if self.second_window:
            self.second_window.total_timer.setText(self.time2.toString())

    def table_cell_changed(self, item):
        if item.column() == 1:  # Check if the edited cell is in column 2 (index 1)
            current_text = item.text()
            try:
                QTime.fromString(current_text)
            except ValueError:
                QMessageBox.warning(self, 'Invalid Format', 'Invalid time format. Please use the format "HH:mm:ss".')
                previous_text = item.data(QtCore.Qt.ItemDataRole.DisplayRole)  # Get the previous value
                item.setText(previous_text)  # Restore the previous value

            # Recalculate column 3
            self.update_total_time()

class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TimerQTWin2.ui", self)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
window.open_second_window()
sys.exit(app.exec())
