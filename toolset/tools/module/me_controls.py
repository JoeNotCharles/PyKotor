from __future__ import annotations

import json
import math
from abc import ABC, abstractmethod
from enum import IntEnum
from typing import Set, List, Union, Callable, Any, Optional

from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QKeySequence
from pykotor.common.geometry import Vector2, Vector3
from pykotor.gl.scene import Scene
from pykotor.resource.generics.git import GITInstance

from tools.module.me_widgets import ModuleRenderer

MB_L = QtCore.Qt.LeftButton
MB_M = QtCore.Qt.MiddleButton
MB_R = QtCore.Qt.RightButton


def getMouseCode(string: str):
    MOUSE_MAP = {
        "LEFT": QtCore.Qt.LeftButton,
        "MIDDLE": QtCore.Qt.MiddleButton,
        "RIGHT": QtCore.Qt.RightButton
    }

    return MOUSE_MAP[string]


def getKeyCode(string: str):
    KEY_MAP = {
        "CTRL": QtCore.Qt.Key_Control,
        "ALT": QtCore.Qt.Key_Alt,
        "SHIFT": QtCore.Qt.Key_Shift
    }

    if string in KEY_MAP:
        return KEY_MAP[string]
    else:
        return QKeySequence(string)[0]


KEY_CTRL = QtCore.Qt.Key_Control
KEY_Z = QtCore.Qt.Key_Z
KEY_Q = QtCore.Qt.Key_Q
KEY_W = QtCore.Qt.Key_W
KEY_A = QtCore.Qt.Key_A
KEY_S = QtCore.Qt.Key_S
KEY_D = QtCore.Qt.Key_D
KEY_0 = QtCore.Qt.Key_0
KEY_1 = QtCore.Qt.Key_1
KEY_2 = QtCore.Qt.Key_2
KEY_3 = QtCore.Qt.Key_3
KEY_4 = QtCore.Qt.Key_4
KEY_5 = QtCore.Qt.Key_5
KEY_6 = QtCore.Qt.Key_6
KEY_7 = QtCore.Qt.Key_7
KEY_8 = QtCore.Qt.Key_8
KEY_9 = QtCore.Qt.Key_9


class ModuleEditorControls(ABC):
    def __init__(self, renderer: ModuleRenderer):
        self.renderer: ModuleRenderer = renderer
        self.variables: List[DCVariable] = []

    @abstractmethod
    def onMouseMoved(self, screen: Vector2, delta: Vector2, buttons: Set[int], keys: Set[int]) -> None:
        ...

    @abstractmethod
    def onMouseScrolled(self, delta: Vector2, buttons: Set[int], keys: Set[int]) -> None:
        ...

    @abstractmethod
    def onMousePressed(self, screen: Vector2, buttons: Set[int], keys: Set[int]) -> None:
        ...

    @abstractmethod
    def onMouseReleased(self, screen: Vector2, buttons: Set[int], keys: Set[int]) -> None:
        ...

    @abstractmethod
    def onKeyPressed(self, buttons: Set[int], keys: Set[int]) -> None:
        ...

    @abstractmethod
    def onKeyReleased(self, buttons: Set[int], keys: Set[int]) -> None:
        ...

    def getValue(self, name: str) -> Any:
        for variable in self.variables:
            if variable.name() == name:
                return variable.get()

    def setValue(self, name: str, value: Any) -> Any:
        for variable in self.variables:
            if variable.name() == name:
                return variable.set(value)

    def wz(self, x: float, y: float, z: float) -> float:
        point = self.renderer.walkmeshPoint(x, y, z)
        return z - point.z

    def translateSelectedObjects(self, snap: bool, dx: float, dy: float, dz: float) -> None:
        for obj in self.renderer.scene.selection:
            x = obj.data.position.x + dx
            y = obj.data.position.y + dy
            z = obj.data.position.z

            point = Vector3(obj.data.position.x + dx, obj.data.position.y + dy, obj.data.position.z)
            if snap:
                point = self.renderer.walkmeshPoint(x, y, z)
            point.z += dz

            instance = obj.data
            instance.position = point

    def rotateSelectedObjects(self, yaw: float, pitch: float) -> None:
        for obj in self.renderer.scene.selection:
            instance: GITInstance = obj.data
            instance.rotate(yaw / 80, 0, 0)

    def alterCameraPosition(self, dx: float, dy: float, dz: float) -> None:
        self.renderer.scene.camera.x += dx
        self.renderer.scene.camera.y += dy
        self.renderer.scene.camera.z += dz

    def snapCameraPosition(self, x: float = None, y: float = None, z: float = None) -> None:
        if x is not None:
            self.renderer.scene.camera.x = x
        if y is not None:
            self.renderer.scene.camera.y = y
        if z is not None:
            self.renderer.scene.camera.z = z

    def alterCameraRotation(self, yaw: float, pitch: float) -> None:
        self.renderer.scene.camera.yaw += yaw
        self.renderer.scene.camera.pitch += pitch

    def setCameraRotation(self, yaw: float, pitch: float) -> None:
        self.renderer.scene.camera.yaw = yaw
        self.renderer.scene.camera.pitch = pitch

    def selectObjectAtMouse(self) -> None:
        self.renderer.doSelect = True

    def openContextMenu(self) -> None:
        x, y = self.renderer.cursor().pos().x(), self.renderer.cursor().pos().y()
        self.renderer.customContextMenuRequested.emit(self.renderer.mapFromGlobal(QPoint(x, y)))


class DynamicModuleEditorControls(ModuleEditorControls):

    def __init__(self, renderer: ModuleRenderer):
        super().__init__(renderer)

        self.name: str = ""

        self.mouseMoveEvents: List[DCItem] = []
        self.mousePressEvents: List[DCItem] = []
        self.mouseReleaseEvents: List[DCItem] = []
        self.mouseScrollEvents: List[DCItem] = []
        self.keyPressEvents: List[DCItem] = []
        self.keyReleaseEvents: List[DCItem] = []
        # self.keyHoldEvents: List[DCItem] = []

    def load(self, filepath: str) -> None:
        self.variables: List[DCVariable] = []
        self.mouseMoveEvents = []
        self.mousePressEvents = []
        self.mouseReleaseEvents = []
        self.mouseScrollEvents = []
        self.keyPressEvents = []
        self.keyReleaseEvents = []

        f = open(filepath, )
        rootJSON = json.load(f)

        self.name = rootJSON["name"]

        for name, variableJSON in rootJSON["variables"].items():
            data_type = variableJSON["type"]
            default = variableJSON["default"]

            var = None
            if data_type == "STRING":
                var = DCVariableString(name, default, variableJSON["allowed"])
            elif data_type == "INT":
                var = DCVariableInt(name, default)
            elif data_type == "FLOAT":
                var = DCVariableFloat(name, default)
            elif data_type == "BOOL":
                var = DCVariableBool(name, default)
            else:
                ValueError("Unknown data type '{}'.".format(data_type))

            self.variables.append(var)

        for controlJSON in rootJSON["controls"]:
            if controlJSON["event"] == "MOUSE_MOVE":
                array = self.mouseMoveEvents
            elif controlJSON["event"] == "MOUSE_PRESS":
                array = self.mousePressEvents
            elif controlJSON["event"] == "MOUSE_RELEASE":
                array = self.mouseReleaseEvents
            elif controlJSON["event"] == "MOUSE_SCROLL":
                array = self.mouseScrollEvents
            elif controlJSON["event"] == "KEY_PRESS":
                array = self.keyPressEvents
            elif controlJSON["event"] == "KEY_RELEASE":
                array = self.keyReleaseEvents
            else:
                raise ValueError("Unknown event '{}'.".format(controlJSON["event"]))

            keys = set()
            for keyJSON in controlJSON["keys"]:
                key = keyJSON if isinstance(keyJSON, int) else getKeyCode(keyJSON)
                keys.add(key)

            mouse = set()
            for mouseJSON in controlJSON["mouse"]:
                key = mouseJSON if isinstance(mouseJSON, int) else getMouseCode(mouseJSON)
                mouse.add(key)

            effects = []
            for effectsJSON in controlJSON["effects"]:
                for effectJSON in effectsJSON:
                    args = effectsJSON[effectJSON]

                    if effectJSON == "alterCameraPosition":
                        effect = DCEffectAlterCameraPosition(*args)
                    elif effectJSON == "setCameraPosition":
                        effect = DCEffectSetCameraPosition(*args)
                    elif effectJSON == "alterCameraRotation":
                        effect = DCEffectAlterCameraRotation(*args)
                    elif effectJSON == "setCameraRotation":
                        effect = DCEffectSetCameraRotation(*args)
                    elif effectJSON == "alterObjectPosition":
                        effect = DCEffectAlterObjectPosition(*args)
                    elif effectJSON == "alterObjectRotation":
                        effect = DCEffectAlterObjectRotation(*args)
                    elif effectJSON == "selectObjectAtMouse":
                        effect = DCEffectSelectObjectAtMouse()
                    elif effectJSON == "openContextMenu":
                        effect = DCEffectOpenContextMenu()
                    elif effectJSON == "setVariable":
                        effect = DCEffectSetVariable(*args)
                    else:
                        raise ValueError("Unknown effect '{}'.".format(effectJSON))

                    effects.append(effect)

            array.append(DCItem(keys, mouse, effects))

    def onMouseMoved(self, screen: Vector2, delta: Vector2, buttons: Set[int], keys: Set[int]) -> None:
        for event in self.mouseMoveEvents:
            if event.mouse == buttons and event.keys == keys:
                for effect in event.effects:
                    effect.apply(self, delta.x, delta.y)

    def onMouseScrolled(self, delta: Vector2, buttons: Set[int], keys: Set[int]) -> None:
        for event in self.mouseScrollEvents:
            if event.mouse == buttons and event.keys == keys:
                for effect in event.effects:
                    effect.apply(self, delta.x, delta.y)

    def onMousePressed(self, screen: Vector2, buttons: Set[int], keys: Set[int]) -> None:
        for event in self.mousePressEvents:
            if event.mouse == buttons and event.keys == keys:
                for effect in event.effects:
                    effect.apply(self, 0, 0)

    def onMouseReleased(self, screen: Vector2, buttons: Set[int], keys: Set[int]) -> None:
        for event in self.mouseReleaseEvents:
            if event.mouse == buttons and event.keys == keys:
                for effect in event.effects:
                    effect.apply(self, 0, 0)

    def onKeyPressed(self, buttons: Set[int], keys: Set[int]) -> None:
        for event in self.keyPressEvents:
            if event.mouse == buttons and event.keys == keys:
                for effect in event.effects:
                    effect.apply(self, 0, 0)

    def onKeyReleased(self, buttons: Set[int], keys: Set[int]) -> None:
        for event in self.keyReleaseEvents:
            if event.mouse == buttons and event.keys == keys:
                for effect in event.effects:
                    effect.apply(self, 0, 0)


class HolocronModuleEditorControls(DynamicModuleEditorControls):

    def __init__(self, renderer: ModuleRenderer):
        super().__init__(renderer)

        self.variables: List[DCVariable] = [
            DCVariableFloat("panCamSensitivity", 0.033),
            DCVariableFloat("rotateCamSensitivity", 0.005),
            DCVariableFloat("raiseCamSensitivity", 0.025),
            DCVariableFloat("panObjSensitivity", 0.033),
            DCVariableFloat("rotateObjSensitivity", 0.005)
        ]

        self.mouseMoveEvents: List[DCItem] = [
            DCItem({KEY_CTRL}, {MB_L}, [DCEffectAlterCameraPosition("panCamSensitivity", "cx", "cy", 0)]),
            DCItem({KEY_CTRL}, {MB_M}, [DCEffectAlterCameraRotation("rotateCamSensitivity", "dx", "dy")]),
            DCItem(set(),      {MB_L}, [DCEffectAlterObjectPosition("panObjSensitivity", True, "cx", "cy", 0)]),
            DCItem(set(),      {MB_M}, [DCEffectAlterObjectRotation("rotateObjSensitivity", "dx")])
        ]
        self.mousePressEvents: List[DCItem] = [
            DCItem(set(), {MB_L}, [DCEffectSelectObjectAtMouse()]),
            DCItem(set(), {MB_R}, [DCEffectOpenContextMenu()])
        ]
        self.mouseReleaseEvents: List[DCItem] = []
        self.mouseScrollEvents: List[DCItem] = [
            DCItem({KEY_CTRL}, set(), [DCEffectAlterCameraPosition("raiseCamSensitivity", 0, 0, "dy")])
        ]
        self.keyPressEvents: List[DCItem] = [
            DCItem({getKeyCode("1")}, set(), [DCEffectSetCameraRotation(0, "crp")]),
            DCItem({getKeyCode("3")}, set(), [DCEffectSetCameraRotation(0, "crp"), DCEffectAlterCameraRotation(None, math.pi/2, 0)]),
            DCItem({getKeyCode("7")}, set(), [DCEffectSetCameraRotation("cry", 0)]),
            DCItem({getKeyCode("4")}, set(), [DCEffectAlterCameraRotation(None, math.pi/8, 0)]),
            DCItem({getKeyCode("6")}, set(), [DCEffectAlterCameraRotation(None, -math.pi/8, 0)]),
            DCItem({getKeyCode("8")}, set(), [DCEffectAlterCameraRotation(None, 0, math.pi/8)]),
            DCItem({getKeyCode("2")}, set(), [DCEffectAlterCameraRotation(None, 0, -math.pi/8)]),
            DCItem({getKeyCode("W")}, set(), [DCEffectAlterCameraRotation(None, 0, math.pi/8)]),
            DCItem({getKeyCode("A")}, set(), [DCEffectAlterCameraRotation(None, math.pi/8, 0)]),
            DCItem({getKeyCode("S")}, set(), [DCEffectAlterCameraRotation(None, 0, -math.pi/8)]),
            DCItem({getKeyCode("D")}, set(), [DCEffectAlterCameraRotation(None, -math.pi/8, 0)]),
            DCItem({getKeyCode("Q")}, set(), [DCEffectAlterCameraPosition(None, 0, 0, 1)]),
            DCItem({getKeyCode("Z")}, set(), [DCEffectAlterCameraPosition(None, 0, 0, -1)])
        ]
        self.keyReleaseEvents: List[DCItem] = []


class DCItem:
    def __init__(self, keys: Set[int], mouse: Set[int], effects: List[DCEffect]):
        self.keys: Set[int] = keys
        self.mouse: Set[int] = mouse
        self.effects: List[DCEffect] = effects


class DCVariable:
    def __init__(self, name: str):
        self._name = name

    def name(self) -> str:
        return self._name

    def get(self) -> Any:
        raise NotImplementedError()

    def set(self, value: Any):
        raise NotImplementedError()


# region Variable Classes
class DCVariableInt(DCVariable):
    def __init__(self, name: str, value: int):
        super().__init__(name)
        self._value: int = value

    def set(self, value: int) -> None:
        self._value = value

    def get(self) -> int:
        return self._value


class DCVariableFloat(DCVariable):
    def __init__(self, name: str, value: float):
        super().__init__(name)
        self._value: float = value

    def name(self) -> str:
        return self._name

    def set(self, value: float) -> None:
        self._value = value

    def get(self) -> float:
        return self._value


class DCVariableBool(DCVariable):
    def __init__(self, name: str, value: bool):
        super().__init__(name)
        self._value: bool = value

    def name(self) -> str:
        return self._name

    def set(self, value: bool) -> None:
        self._value = value

    def get(self) -> bool:
        return self._value


class DCVariableString(DCVariable):
    def __init__(self, name: str, value: str, allowed: List[str]):
        super().__init__(name)
        self._value: str = value
        self._allowed: List[str] = allowed

    def name(self) -> str:
        return self._name

    def set(self, value: str) -> None:
        self._value = value

    def get(self) -> str:
        return self._value


class DCEffect(ABC):
    @abstractmethod
    def apply(self, controls: ModuleEditorControls, dx: float, dy: float) -> None:
        ...

    @staticmethod
    def determineFloat(value: Union[float, str], controls: ModuleEditorControls, dx: float, dy: float) -> float:
        if isinstance(value, str):
            if value == "dx":
                return dx
            elif value == "dy":
                return dy
            elif value == "cx":
                forward = dy * controls.renderer.scene.camera.forward()
                sideward = dx * controls.renderer.scene.camera.sideward()
                return forward.x + sideward.x
            elif value == "cy":
                forward = dy * controls.renderer.scene.camera.forward()
                sideward = dx * controls.renderer.scene.camera.sideward()
                return forward.y + sideward.y
            elif value == "cz":
                ...
            elif value == "cry":
                return controls.renderer.scene.camera.yaw
            elif value == "crp":
                return controls.renderer.scene.camera.pitch
            else:
                return 0
        elif isinstance(value, float) or isinstance(value, int):
            return value
        else:
            return 0
# endregion


# region Effect Classes
# alterCameraPosition
class DCEffectAlterCameraPosition(DCEffect):
    def __init__(self, sensitivityVar: Optional[str], x: Union[float, str], y: Union[float, str], z: Union[float, str]):
        self.sensitivityVar: Optional[str] = sensitivityVar
        self.x: Union[float, str] = x
        self.y: Union[float, str] = y
        self.z: Union[float, str] = z

    def apply(self, controls: ModuleEditorControls, dx: float, dy: float) -> None:
        x = super().determineFloat(self.x, controls, dx, dy)
        y = super().determineFloat(self.y, controls, dx, dy)
        z = super().determineFloat(self.z, controls, dx, dy)
        sensitivity = controls.getValue(self.sensitivityVar) if self.sensitivityVar is not None else 1.0
        controls.alterCameraPosition(x * sensitivity, y * sensitivity, z * sensitivity)


# setCameraPosition
class DCEffectSetCameraPosition(DCEffect):
    def __init__(self, x: Union[float, str], y: Union[float, str], z: Union[float, str]):
        self.x: Union[float, str] = x
        self.y: Union[float, str] = y
        self.z: Union[float, str] = z

    def apply(self, controls: ModuleEditorControls, dx: float, dy: float) -> None:
        x = super().determineFloat(self.x, controls, dx, dy)
        y = super().determineFloat(self.y, controls, dx, dy)
        z = super().determineFloat(self.z, controls, dx, dy)
        controls.alterCameraPosition(x, y, z)


# alterCameraRotation
class DCEffectAlterCameraRotation(DCEffect):
    def __init__(self, sensitivityVar: Optional[str], yaw: Union[float, str], pitch: Union[float, str]):
        self.sensitivityVar: Optional[str] = sensitivityVar
        self.yaw: Union[float, str] = yaw
        self.pitch: Union[float, str] = pitch

    def apply(self, controls: ModuleEditorControls, dx: float, dy: float) -> None:
        pitch = super().determineFloat(self.pitch, controls, dx, dy)
        yaw = super().determineFloat(self.yaw, controls, dx, dy)
        sensitivity = controls.getValue(self.sensitivityVar) if self.sensitivityVar is not None else 1.0
        controls.alterCameraRotation(yaw * sensitivity, pitch * sensitivity)


# setCameraRotation
class DCEffectSetCameraRotation(DCEffect):
    def __init__(self, yaw: Union[float, str], pitch: Union[float, str]):
        self.yaw: Union[float, str] = yaw
        self.pitch: Union[float, str] = pitch

    def apply(self, controls: ModuleEditorControls, dx: float, dy: float) -> None:
        yaw = super().determineFloat(self.yaw, controls, dx, dy)
        pitch = super().determineFloat(self.pitch, controls, dx, dy)
        controls.setCameraRotation(yaw, pitch)


# alterObjectPosition
class DCEffectAlterObjectPosition(DCEffect):
    def __init__(self, sensitivityVar: Optional[str], snapToWalkmesh: bool, x: Union[float, str], y: Union[float, str], z: Union[float, str]):
        self.sensitivityVar: Optional[str] = sensitivityVar
        self.snapToWalkmesh: bool = snapToWalkmesh
        self.x: Union[float, str] = x
        self.y: Union[float, str] = y
        self.z: Union[float, str] = z

    def apply(self, controls: ModuleEditorControls, dx: float, dy: float) -> None:
        x = super().determineFloat(self.x, controls, dx, dy)
        y = super().determineFloat(self.y, controls, dx, dy)
        z = super().determineFloat(self.z, controls, dx, dy)
        sensitivity = controls.getValue(self.sensitivityVar) if self.sensitivityVar is not None else 1.0
        controls.translateSelectedObjects(self.snapToWalkmesh, -x * sensitivity, -y * sensitivity, z * sensitivity)


# alterObjectRotation
class DCEffectAlterObjectRotation(DCEffect):
    def __init__(self, sensitivityVar: Optional[str], yaw: Union[float, str]):
        self.sensitivityVar: Optional[str] = sensitivityVar
        self.yaw: Union[float, str] = yaw

    def apply(self, controls: ModuleEditorControls, dx: float, dy: float) -> None:
        yaw = super().determineFloat(self.yaw, controls, dx, dy)
        sensitivity = controls.getValue(self.sensitivityVar) if self.sensitivityVar is not None else 1.0
        controls.rotateSelectedObjects(yaw * sensitivity, 0.0)


# selectObjectAtMouse
class DCEffectSelectObjectAtMouse(DCEffect):
    def __init__(self):
        ...

    def apply(self, controls: ModuleEditorControls, dx: float, dy: float) -> None:
        controls.selectObjectAtMouse()


# openContextMenu
class DCEffectOpenContextMenu(DCEffect):
    def __init__(self):
        ...

    def apply(self, controls: ModuleEditorControls, dx: float, dy: float) -> None:
        controls.openContextMenu()


# setVariable
class DCEffectSetVariable(DCEffect):
    def __init__(self, name: str, value: Any):
        self.name: str = name
        self.value: Any = value

    def apply(self, controls: ModuleEditorControls, dx: float, dy: float) -> None:
        controls.setValue(self.name, self.value)

# endregion
