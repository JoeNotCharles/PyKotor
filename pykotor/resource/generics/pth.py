from __future__ import annotations

from contextlib import suppress
from copy import copy

from pykotor.common.geometry import Vector2
from pykotor.common.misc import Game
from pykotor.resource.formats.gff import GFF, GFFContent, GFFList, read_gff, write_gff
from pykotor.resource.formats.gff.gff_auto import bytes_gff
from pykotor.resource.type import SOURCE_TYPES, TARGET_TYPES, ResourceType


class PTH:
    """Stores the path data for a module."""

    BINARY_TYPE = ResourceType.PTH

    def __init__(
        self,
    ):
        self._points: list[Vector2] = []
        self._connections: list[PTHEdge] = []

    def __iter__(
        self,
    ):
        yield from self._points

    def __len__(
        self,
    ):
        return len(self._points)

    def __getitem__(
        self,
        item: int,
    ):
        return self._points[int]

    def add(
        self,
        x: float,
        y: float,
    ) -> int:
        self._points.append(Vector2(x, y))
        return len(self._points) - 1

    def remove(
        self,
        index: int,
    ) -> None:
        self._points.pop(index)

        self._connections = [
            x for x in self._connections if x.source != index and x.target != index
        ]

        for connection in self._connections:
            connection.source = (
                connection.source - 1
                if connection.source > index
                else connection.source
            )
            connection.target = (
                connection.target - 1
                if connection.target > index
                else connection.target
            )

    def get(
        self,
        index: int,
    ) -> Vector2 | None:
        with suppress(Exception):
            return self._points[index]
        return None

    def find(
        self,
        point: Vector2,
    ) -> int | None:
        return self._points.index(point)

    def connect(
        self,
        source: int,
        target: int,
    ) -> None:
        self._connections.append(PTHEdge(source, target))

    def disconnect(
        self,
        source: int,
        target: int,
    ) -> None:
        for edge in copy(self._connections):
            hasSource = edge.source in [source, target]
            hasTarget = edge.target in [source, target]
            if hasSource and hasTarget:
                self._connections.remove(edge)

    def is_connected(
        self,
        source: int,
        target: int,
    ) -> bool:
        return any(x for x in self._connections if x == PTHEdge(source, target))

    def outgoing(
        self,
        source: int,
    ) -> list[PTHEdge]:
        return [
            connection
            for connection in self._connections
            if connection.source == source
        ]

    def incoming(
        self,
        target: int,
    ) -> list[PTHEdge]:
        return [
            connection
            for connection in self._connections
            if connection.target == target
        ]


class PTHEdge:
    def __init__(
        self,
        source: int,
        target: int,
    ):
        self.source = source
        self.target = target

    def __eq__(
        self,
        other: PTHEdge,
    ):
        if not isinstance(other, PTHEdge):
            raise NotImplementedError

        return self.source == other.source and self.target == other.target


def construct_pth(
    gff: GFF,
) -> PTH:
    pth = PTH()

    connections_list = gff.root.acquire("Path_Conections", GFFList())

    for point_struct in gff.root.acquire("Path_Points", GFFList()):
        connections = point_struct.acquire("Conections", 0)
        first_connection = point_struct.acquire("First_Conection", 0)
        x = point_struct.acquire("X", 0.0)
        y = point_struct.acquire("Y", 0.0)

        source = pth.add(x, y)

        for i in range(first_connection, first_connection + connections):
            target = connections_list.at(i).acquire("Destination", 0)
            pth.connect(source, target)

    return pth


def dismantle_pth(
    pth: PTH,
    game: Game = Game.K2,
    *,
    use_deprecated: bool = True,
) -> GFF:
    gff = GFF(GFFContent.PTH)

    connections_list = gff.root.set_list("Path_Conections", GFFList())
    points_list = gff.root.set_list("Path_Points", GFFList())

    for i, point in enumerate(pth):
        outgoings = pth.outgoing(i)

        point_struct = points_list.add(2)
        point_struct.set_uint32("Conections", len(outgoings))
        point_struct.set_uint32("First_Conection", len(connections_list))
        point_struct.set_single("X", point.x)
        point_struct.set_single("Y", point.y)

        for outgoing in outgoings:
            connection_struct = connections_list.add(3)
            connection_struct.set_uint32("Destination", outgoing.target)

    return gff


def read_pth(
    source: SOURCE_TYPES,
    offset: int = 0,
    size: int | None = None,
) -> PTH:
    gff = read_gff(source, offset, size)
    return construct_pth(gff)


def write_pth(
    pth: PTH,
    target: TARGET_TYPES,
    game: Game = Game.K2,
    file_format: ResourceType = ResourceType.GFF,
    *,
    use_deprecated: bool = True,
) -> None:
    gff = dismantle_pth(pth, game, use_deprecated=use_deprecated)
    write_gff(gff, target, file_format)


def bytes_pth(
    pth: PTH,
    game: Game = Game.K2,
    file_format: ResourceType = ResourceType.GFF,
    *,
    use_deprecated: bool = True,
) -> bytes:
    gff = dismantle_pth(pth, game, use_deprecated=use_deprecated)
    return bytes_gff(gff, file_format)
