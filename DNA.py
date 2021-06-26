import maya.cmds as mc
from PySide2.QtGui  import *
from PySide2.QtCore  import *
from PySide2.QtWidgets  import *

def CreateDNA(bonds=50,cylinderrad=0.2, sphererad=0.5):
    result1_objects = []
    for i in range(bonds):
        result1 = mc.polySphere(r = sphererad, sx = 15, sy = 15)
        mc.xform(result1[0], translation = (0, 1 * i, 3.5))
        mc.xform(result1[0], ws = True, rp = (0, 0.25 * i, 0), sp = (0, 0.25 * i, 0))
        mc.xform(result1[0], ro = (0, 12 * i, 0))
        result1_objects.append(result1[0])
    mc.group(result1_objects, name = "Spiral 1")

    result2_objects = []
    for i in range(bonds):
        result2 = mc.polySphere(r = sphererad, sx = 15, sy = 15)
        mc.xform(result2[0], translation = (0, 1 * i, -3.5))
        mc.xform(result2[0], ws = True, rp = (0, -0.25 * i, 0), sp = (0, 0.25 * i, 0))
        mc.xform(result2[0], ro = (0, 12 * i, 0))
        result2_objects.append(result2[0])
    mc.group(result2_objects, name = "Spiral 2")

    result3_objects = []
    for i in range(bonds):
        result3 = mc.polyCylinder(r = cylinderrad, h = 7, sx = 15, sy = 15)
        mc.xform(result3[0], translation = (0, 1 * i, 0))
        mc.xform(result3[0], ro = (0, 12 * i, 0))
        mc.rotate(90, 0, 0, relative = True, componentSpace = True)
        result3_objects.append(result3[0])
    mc.group(result3_objects, name = "Cylinder 1")

def make_dna_from_tool():
    print("Number of Bonds",dna_bonds.text())
    print("Sphere Radius",sph_radius.text())
    print("Cylinder Radius",cy_radius.text())
    CreateDNA(sphererad=float(sph_radius.text()),cylinderrad=float(cy_radius.text()),bonds=int(dna_bonds.text()))
    dna_tool.hide()


app=QApplication.instance()

dna_tool=QWidget()
dna_tool.setFixedSize(400,200)
dna_tool.setWindowTitle("DNA Tool")
lay=QVBoxLayout()
dna_tool.setLayout(lay)
dna_bonds=QLineEdit()
sph_radius=QLineEdit()
cy_radius=QLineEdit()
ok_btn=QPushButton("Create DNA")
height_lab=QLabel("Number of Bonds:")
lay.addWidget(height_lab)
lay.addWidget(dna_bonds)
lay.addWidget(QLabel("Sphere Radius:"))
lay.addWidget(sph_radius)
lay.addWidget(QLabel("Cylinder Radius:"))
lay.addWidget(cy_radius)
lay.addWidget(ok_btn)

ok_btn.clicked.connect(make_dna_from_tool)
dna_tool.show()
app.exec_()