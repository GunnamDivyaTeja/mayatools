import maya.cmds as mc
import pymel as pm
mc.ls(sl=True)
mc.ConvertSelectionToFaces()
mc.polyExtrudeFacet(ltz = 0.05, offset = 0.005, divisions = 3)
mc.selectType(v=True)