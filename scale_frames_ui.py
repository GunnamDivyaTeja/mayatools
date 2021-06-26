import maya.cmds as mc
from maya import OpenMayaUI as omui

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
import shiboken2

MAYA_WINDOW_POINTER = omui.MQtUtil.mainWindow()
MAYA_MAIN_WINDOW = shiboken2.wrapInstance(int(MAYA_WINDOW_POINTER), QWidget)

WIN_TITLE = "Keyframe Scaler"

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__(MAYA_MAIN_WINDOW)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle(WIN_TITLE)

        grid = QGridLayout(self)
        self.setLayout(grid)

        check_box = QCheckBox("Scale selected only")
        explanation_of_selection = QLabel("If off, will scale the whole curve after or before "
                                          "the first or the last selected keyframe")
        explanation_of_selection.setWordWrap(True)
        first_frame_button = QPushButton("F")
        last_frame_button = QPushButton("L")
        input_value_field = QDoubleSpinBox()
        input_value_field.setSingleStep(0.1)
        input_value_field.setMinimum(float("-inf"))
        scale_button = QPushButton("Scale")

        grid.addWidget(check_box, 0,0,1,4)
        grid.addWidget(explanation_of_selection, 1, 0, 1, 4)
        grid.addWidget(first_frame_button, 2,0,1,1)
        grid.addWidget(input_value_field, 2,1,1,2)
        grid.addWidget(last_frame_button, 2,3,1,1)
        grid.addWidget(scale_button, 3,0,1,4)

        self.show()

def main():
    MainWindow()