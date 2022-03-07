from __future__ import annotations

from enum import IntEnum
from typing import List, Optional, Tuple, Set

from pykotor.common.geometry import Vector3, Vector4, Vector2, SurfaceMaterial
from pykotor.common.misc import Color
from pykotor.resource.type import ResourceType


class MDL:
    """
    Represents a MDL/MDX file.

    Attributes:
        root: The root node of the model.
        anims: The animations stored in the model.
        name: The model name.
        fog: If fog affects the model.
        supermodel: Name of another model resource to import extra data from.
    """

    BINARY_TYPE = ResourceType.MDL

    def __init__(
            self
    ):
        self.root: MDLNode = MDLNode()
        self.anims: List[MDLAnimation] = []
        self.name: str = ""
        self.fog: bool = False
        self.supermodel: str = ""

    def get(
            self,
            node_name: str
    ) -> Optional[MDLNode]:
        pick = None

        nodes = [self.root]
        while nodes:
            node = nodes.pop()
            if node.name == node_name:
                pick = node
            else:
                nodes.extend(node.children)

        return pick

    def all_nodes(
            self
    ) -> List[MDLNode]:
        nodes = []
        scan = [self.root]
        while scan:
            node = scan.pop()
            nodes.append(node)
            scan.extend(node.children)
        return nodes

    def find_parent(
            self,
            child: MDLNode
    ) -> Optional[MDLNode]:
        all_nodes = self.all_nodes()
        parent = None
        for node in all_nodes:
            if child in node.children:
                parent = node
        return parent

    def global_position(
            self,
            node: MDLNode
    ) -> Vector3:
        position = node.position
        parent = self.find_parent(node)
        while parent is not None:
            position += parent.position
            parent = self.find_parent(parent)
        return position

    def get_by_node_id(
            self,
            node_id
    ) -> MDLNode:
        for node in self.all_nodes():
            if node.node_id == node_id:
                return node
        raise ValueError

    def all_textures(
            self
    ) -> Set[str]:
        textures = set()
        for node in self.all_nodes():
            if node.mesh and node.mesh.texture_1 != "NULL" and node.mesh.texture_1 != "":
                textures.add(node.mesh.texture_1)
        return textures

    def all_lightmaps(
            self
    ) -> Set[str]:
        lightmaps = set()
        for node in self.all_nodes():
            if node.mesh and node.mesh.texture_2 != "NULL" and node.mesh.texture_2 != "":
                lightmaps.add(node.mesh.texture_2)
        return lightmaps


# region Animation Data
class MDLAnimation:
    def __init__(
            self
    ):
        self.name: str = ""
        self.root_model: str = ""
        self.anim_length: float = 0.0
        self.transition_length: float = 0.0
        self.events: List[MDLEvent] = []
        self.root: MDLNode = MDLNode()

    def all_nodes(
            self
    ) -> List[MDLNode]:
        nodes = []
        scan = [self.root]
        while scan:
            node = scan.pop()
            nodes.append(node)
            scan.extend(node.children)
        return nodes


class MDLEvent:
    def __init__(
            self
    ):
        self.activation_time: float = 0.0
        self.name: str = ""


# endregion


# region Node Headers
class MDLNodeFlags(IntEnum):
    HEADER = 0x00000001
    LIGHT = 0x00000002
    EMITTER = 0x00000004
    CAMERA = 0x00000008
    REFERENCE = 0x00000010
    MESH = 0x00000020
    SKIN = 0x00000040
    DANGLY = 0x00000100
    AABB = 0x00000200
    SABER = 0x00000800


class MDLNode:
    """
    A node in the MDL tree that can store additional nodes or some extra data related to the model such as geometry or
    lighting.

    Attributes:
        children: List of children linked to the node.
        controllers: List of controllers linked to the node.
        name: Name of the node.
        position: The position of the node.
        orientation: The orientation of the node.
        light: Light data associated with the node.
        emitter: Emitter data associated with the node.
        mesh: Trimesh data associated with the node.
        skin: Skin data associated with the node.
        dangly: Danglymesh data associated with the node.
        aabb: Walkmesh data associated with the node
        saber: Sabermesh data associated with the node.
    """

    def __init__(
            self
    ):
        # self.parent: Optional[MDLNode] = None

        self.children: List[MDLNode] = []
        self.controllers: List[MDLController] = []
        self.name: str = ""
        self.node_id: int = -1
        self.position: Vector3 = Vector3.from_null()
        self.orientation: Vector4 = Vector4.from_null()

        self.light: Optional[MDLLight] = None
        self.emitter: Optional[MDLEmitter] = None
        self.reference: Optional[MDLReference] = None
        self.mesh: Optional[MDLMesh] = None
        self.skin: Optional[MDLSkin] = None
        self.dangly: Optional[MDLDangly] = None
        self.aabb: Optional[MDLWalkmesh] = None
        self.saber: Optional[MDLSaber] = None

    def descendants(
            self
    ) -> List[MDLNode]:
        ancestors = []
        for child in self.children:
            ancestors.append(child)
            ancestors.extend(child.descendants())
        return ancestors

    def child(
            self,
            name
    ) -> MDLNode:
        for child in self.children:
            if child.name == name:
                return child
        else:
            raise KeyError


class MDLLight:
    """
    Light data that can be attached to a node.

    Attributes:
        flare_radius:
        light_priority:
        ambient_only:
        dynamic_type:
        shadow:
        flare:
        fading_light:
    """

    def __init__(
            self
    ):
        # TODO: Make enums, check if bools, docs, merge flare data into class
        self.flare_radius: float = 0.0
        self.light_priority: int = 0
        self.ambient_only: int = 0
        self.dynamic_type: int = 0
        self.shadow: int = 0
        self.flare: int = 0
        self.fading_light: int = 0
        self.flare_sizes: List = []
        self.flare_positions: List = []
        self.flare_color_shifts: List = []
        self.flare_textures: List = []


class MDLEmitter:
    """
    Emitter data that can be attached to a node.

    Attributes:
        dead_space:
        blast_radius:
        blast_length:
        branch_count:
        control_point_smoothing:
        x_grid:
        y_grid:
        spawn_type:
        update:
        render:
        blend:
        texture:
        chunk_name:
        two_sided_texture:
        loop:
        render_order:
        frame_blender:
        depth_texture:
    """

    def __init__(
            self
    ):
        # TODO: Make enums, check if bools, docs, seperate flags into booleans
        self.dead_space: float = 0.0
        self.blast_radius: float = 0.0
        self.blast_length: float = 0.0
        self.branch_count: int = 0
        self.control_point_smoothing: float = 0.0
        self.x_grid: int = 0
        self.y_grid: int = 0
        self.spawn_type: int = 0
        self.update: str = ""
        self.render: str = ""
        self.blend: str = ""
        self.texture: str = ""
        self.chunk_name: str = ""
        self.two_sided_texture: int = 0
        self.loop: int = 0
        self.render_order: int = 0
        self.frame_blender: int = 0
        self.depth_texture: str = ""
        self.flags: int = 0


class MDLReference:
    """
    Reference data that can be attached to a node.

    Attributes:
        model:
        reattachable:
    """

    def __init__(
            self
    ):
        # TODO: docs
        self.model: str = ""
        self.reattachable: bool = False


class MDLMesh:
    """
    Mesh data that can be attached to a node.
    """

    def __init__(
            self
    ):
        # TODO: look at mesh inverted counter array, rename boolean flags
        self.faces: List[MDLFace] = []
        self.diffuse: Color = Color.WHITE
        self.ambient: Color = Color.WHITE
        self.transparency_hint: int = 0
        self.texture_1: str = ""
        self.texture_2: str = ""
        self.saber_unknowns: Tuple[int, int, int, int, int, int, int, int] = (3, 0, 0, 0, 0, 0, 0, 0)
        self.animate_uv: bool = False
        self.uv_direction_x: float = 0.0
        self.uv_direction_y: float = 0.0
        self.uv_jitter: float = 0.0
        self.uv_jitter_speed: float = 0.0

        self.has_lightmap: bool = False
        self.rotate_texture: bool = False
        self.background_geometry: bool = False
        self.shadow: bool = False
        self.beaming: bool = False
        self.render: bool = True

        # Trimesh
        self.vertex_positions: List[Vector3] = []
        self.vertex_normals: Optional[List[Vector3]] = None
        self.vertex_uv1: Optional[List[Vector2]] = None
        self.vertex_uv2: Optional[List[Vector2]] = None

        # KotOR 2 Only
        self.dirt_enabled: bool = False
        self.dirt_texture: int = 0
        self.dirt_coordinate_space: int = 0
        self.hide_in_hologram: bool = False


class MDLSkin:
    """
    Skin data that can be attached to a node.
    """

    def __init__(
            self
    ):
        self.bone_indices: Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int] = (
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.qbones: List[Vector3] = []
        self.tbones: List[Vector3] = []
        self.bonemap: List[int] = []

        self.vertex_bones: List[MDLBoneVertex] = []


class MDLDangly:
    """
    Dangly data that can be attached to a node.
    """


class MDLWalkmesh:
    """
    AABB data that can be attached to a node.
    """


class MDLSaber:
    """
    Saber data that can be attached to a node.
    """


# endregion


# region Geometry Data
class MDLBoneVertex:
    def __init__(
            self
    ):
        self.vertex_weights: Tuple[float, float, float, float] = (0.0, 0.0, 0.0, 0.0)
        self.vertex_indices: Tuple[float, float, float, float] = (-1.0, -1.0, -1.0, -1.0)


class MDLFace:
    def __init__(
            self
    ):
        self.v1: int = 0
        self.v2: int = 0
        self.v3: int = 0
        self.material: SurfaceMaterial = SurfaceMaterial.GRASS
        self.a1: int = 0
        self.a2: int = 0
        self.a3: int = 0
        self.coefficient: int = 0
        self.normal: Vector3 = Vector3.from_null()


# endregion


# region Controller Data
class MDLControllerType(IntEnum):
    INVALID = -1

    POSITION = 8
    ORIENTATION = 20
    SCALE = 36
    ILLUM_COLOR = 100
    ALPHA = 132

    P2P_BEZIER_2 = 132


class MDLController:
    """
    A controller is an object that gets attached to the node and influences some sort of change that is either static
    or animated.
    """

    def __init__(
            self
    ):
        self.controller_type: MDLControllerType = MDLControllerType.INVALID
        self.rows: List[MDLControllerRow] = []


class MDLControllerRow:
    def __init__(
            self,
            time,
            data
    ):
        self.time: float = time
        self.data: List[float] = data

    def __repr__(
            self
    ):
        return "MDLControllerRow({}, {})".format(self.time, self.data)

    def __str__(
            self
    ):
        return "{} {}".format(self.time, self.data).replace(',', '').replace('[', '').replace(']', '')
# endregion
