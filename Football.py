import maya.cmds as mc
from PySide2.QtGui  import *
from PySide2.QtCore  import *
from PySide2.QtWidgets  import *

radius = float(input())
def createFootball(radius):
    ball = mc.polyPrimitive( r=radius, l=0.4036, pt=0)
    mc.ls(sl = True)
    mc.polySmooth()
    mc.sculpt(mode='stretch', insideMode='even', maxDisplacement=0.1, dropoffType='linear', dropoffDistance=1, groupWithLocator=0, objectCentered=1)
    mc.selectType(v=True)
createFootball(radius)

def make_football_from_tool():
    print("Radius of Foortabll:",radius.text())
    CreateBall(radius=float(radius.text()))
    ball_tool.hide()
app=QApplication.instance()

ball_tool=QWidget()
ball_tool.setFixedSize(400,200)
ball_tool.setWindowTitle("Football Tool")
lay=QVBoxLayout()
ball_tool.setLayout(lay)
ball_radius=QLineEdit()
ok_btn=QPushButton("Create Football")
radius_lab=QLabel("Radius of Football:")
lay.addWidget(radius_lab)
lay.addWidget(ok_btn)

ok_btn.clicked.connect(make_football_from_tool)
dna_tool.show()
app.exec_()