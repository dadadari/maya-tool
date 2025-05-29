# 파일명: rename_selected.py

import maya.cmds as cmds

def rename_selected_objects(prefix="OBJ_"):
    selection = cmds.ls(selection=True)
    for i, obj in enumerate(selection):
        new_name = f"{prefix}{i+1}"
        cmds.rename(obj, new_name)

# 사용 예시:
# 선택한 오브젝트들을 OBJ_1, OBJ_2, ... 로 이름 변경
rename_selected_objects()
