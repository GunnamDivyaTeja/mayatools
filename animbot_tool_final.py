import maya.cmds as mc
from PySide2.QtGui  import *
from PySide2.QtCore  import *
from PySide2.QtWidgets  import *

object = cmds.ls(sl = True)
keys_list = cmds.keyframe(object, sl = True, q=True)
keys_list_2 = []

for i in range(0, len(keys_list)-1):
    if keys_list[i] in keys_list_2:
        pass
    else:
        keys_list_2.append(keys_list[i])
        
def anim_slider_tool(frame_default, frame_num):
    flag = 1
    if len(keys_list_2) >1:
        flag = 1
    else:
        flag = 0
        not_enough = "Select more than one keyframe to make a wave"
        print(not_enough)
    for i in range(0, len(keys_list_2)):
        num = i+1
        if num%2 == 0:
            cmds.keyframe(object, iub = True, relative = False, vc = frame_default, t = (keys_list_2[i],)) 
        else:
            cmds.keyframe(object, iub = True, relative = False, vc = frame_num, t = (keys_list_2[i],)) 
            
app=QApplication.instance()

def toolValueChanged(value):
    x = value*.01
    frame_default = -x
    frame_num = x
    print(frame_num)
    slider.valueChanged.connect(anim_slider_tool(frame_default, frame_num))
    mc.keyTangent(itt = 'spline', ott = 'spline')
    
    
slider_tool=QWidget()
slider_tool.setFixedSize(500,100)
slider_tool.setWindowTitle("Keyframe Tool")
lay=QHBoxLayout()
slider_tool.setLayout(lay)
slider=QSlider() 
slider.setOrientation(Qt.Horizontal)
slider.setMinimum(-100)
slider.setMaximum(100)
label_minimum = QLabel(alignment = Qt.AlignLeft)
label_maximum = QLabel(alignment = Qt.AlignRight)
lay.addWidget(slider)
lay.addWidget(QLabel("Keyframe Wave"))
slider.valueChanged.connect(toolValueChanged)
app.exec_()
slider_tool.show()