"""
This module handles classes relating to editing VIS files.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Dict, Set


class VIS:
    """
    Represents a VIS file.
    """

    def __init__(self):
        self._rooms: Set[str] = set()
        self._visibility: Dict[str, Set[str]] = {}

    def __iter__(self):
        for observer, observed in self._visibility.items():
            yield observer, deepcopy(observed)

    def all_rooms(self) -> Set[str]:
        return self._rooms

    def add_room(self, model: str) -> None:
        """
        Adds a room. If an room already exists, it is ignored; no error is thrown.

        Args:
            model: The name or model of the room.
        """
        if model not in self._rooms:
            self._visibility[model] = set()

        self._rooms.add(model)

    def remove_room(self, model: str) -> None:
        """
        Removes a room. If a room does not exist, it is ignored; no error is thrown.

        Args:
            model: The name or model of the room.
        """

        for room in self._rooms:
            if model in self._visibility[room]:
                self._visibility[room].remove(model)

        self._rooms.remove(model)

    def room_exists(self, model: str) -> bool:
        """
        Returns true if the specified room exists.

        Returns:
            True if the room exists.
        """
        return model in self._rooms

    def set_visible(self, when_inside: str, show: str, visible: bool) -> None:
        """
        Sets the visibility of a specified room based off when viewing from another specified room.

        Args:
            when_inside: The room the of the observer.
            show: The observed room.
            visible: If the observed room is visible.
        """
        if when_inside not in self._rooms or show not in self._rooms:
            raise ValueError("One of the specified rooms does not exist.")

        if visible:
            self._visibility[when_inside].add(show)
        elif show in self._visibility[when_inside]:
            self._visibility[when_inside].remove(show)

    def get_visible(self, when_inside: str, show: str) -> bool:
        """
        Returns true if the observed room is visible from the observing room.

        Args:
            when_inside: The room the of the observer.
            show: The observed room.

        Returns:
            True if the room is visible.
        """
        if when_inside not in self._rooms or show not in self._rooms:
            raise ValueError("One of the specified rooms does not exist.")

        return show in self._visibility[when_inside]
