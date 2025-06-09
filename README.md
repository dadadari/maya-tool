# Rename Tool

선택한 오브젝트들의 이름을 일괄적으로 변경할 수 있는 Maya 툴입니다.
PySide2 기반으로 제작되었으며, prefix/suffix 기반 이름 지정이 가능합니다.

## 📂 설치 방법

1. 이 저장소를 다운로드하거나 클론합니다.
2. `rename_gui.py` 파일을 Maya의 `scripts/` 폴더에 넣습니다.
3. 마야에서 다음 코드를 실행합니다:

```python
import rename_gui
rename_gui.launch_rename_tool()
