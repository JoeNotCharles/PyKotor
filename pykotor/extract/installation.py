from __future__ import annotations

import os
from collections import namedtuple
from contextlib import suppress
from copy import copy
from enum import Enum
from typing import Dict, List, Optional, Tuple, NamedTuple

from pykotor.common.stream import BinaryReader

from pykotor.common.language import Language, Gender
from pykotor.extract.file import FileResource, FileQuery, ResourceResult, LocationResult, ResourceIdentifier
from pykotor.extract.capsule import Capsule
from pykotor.extract.chitin import Chitin
from pykotor.extract.talktable import TalkTable
from pykotor.resource.formats.gff import load_gff
from pykotor.resource.formats.mdl import MDL
from pykotor.resource.formats.tlk import TLK
from pykotor.resource.formats.tpc import TPC, load_tpc
from pykotor.resource.formats.twoda import TwoDA, load_2da
from pykotor.resource.type import ResourceType


class ItemTuple(NamedTuple):
    resname: str
    name: str
    filepath: str


class TextureQuality(Enum):
    HIGH = "a"
    MODERATE = "b"
    LOW = "c"


class Installation:
    """
    Installation provides a centralized location for loading resources stored in the game through its
    various folders and formats.
    """
    TEXTURES_TYPES = [ResourceType.TPC, ResourceType.TGA, ResourceType.DDS]

    def __init__(self, path: str, name: str = "KotOR", tsl: bool = False):
        self._path: str = path.replace('\\', '/')
        if not self._path.endswith('/'): self._path += '/'

        self.name: str = name
        self.tsl: bool = tsl

        self._chitin: List[FileResource] = []
        self._modules: Dict[str, List[FileResource]] = {}
        self._lips: Dict[str, List[FileResource]] = {}
        self._texturepacks: Dict[str, List[FileResource]] = {}
        self._override: Dict[str, Dict[str, FileResource]] = {}
        self._talktable: Optional[TalkTable] = TalkTable(self._path + "dialog.tlk")

        self.load_modules()
        self.load_override()
        self.load_lips()
        self.load_textures()
        self.load_chitin()

    # region Get Paths
    def path(self) -> str:
        return self._path

    def module_path(self) -> str:
        module_path = self._path
        for folder in os.listdir(self._path):
            if os.path.isdir(module_path + folder) and folder.lower() == "modules":
                module_path += folder + "/"
        if module_path == self._path:
            raise ValueError("Could not find modules folder in '{}'.".format(self._path))
        return module_path

    def override_path(self) -> str:
        override_path = self._path
        for folder in os.listdir(self._path):
            if os.path.isdir(override_path + folder) and folder.lower() == "override":
                override_path += folder + "/"
        if override_path == self._path:
            raise ValueError("Could not find override folder in '{}'.".format(self._path))
        return override_path

    def lips_path(self) -> str:
        lips_path = self._path
        for folder in os.listdir(self._path):
            if os.path.isdir(lips_path + folder) and folder.lower() == "lips":
                lips_path += folder + "/"
        if lips_path == self._path:
            raise ValueError("Could not find modules folder in '{}'.".format(self._path))
        return lips_path

    def texturepacks_path(self) -> str:
        texturepacks_path = self._path
        for folder in os.listdir(self._path):
            if os.path.isdir(texturepacks_path + folder) and folder.lower() == "texturepacks":
                texturepacks_path += folder + "/"
        if texturepacks_path == self._path:
            raise ValueError("Could not find modules folder in '{}'.".format(self._path))
        return texturepacks_path
    # endregion

    # region Load Data
    def load_chitin(self) -> None:
        chitin = Chitin(self._path)
        self._chitin = [resource for resource in chitin]

    def load_modules(self) -> None:
        self._modules = {}
        module_files = [file for file in os.listdir(self.module_path()) if file.endswith('.mod') or file.endswith('.rim') or file.endswith('.erf')]
        for module in module_files:
            self._modules[module] = [resource for resource in Capsule(self.module_path() + module)]

    def reload_module(self, module) -> None:
        self._modules[module] = [resource for resource in Capsule(self.module_path() + module)]

    def load_lips(self) -> None:
        self._lips = {}
        lips_path = self.lips_path()
        lip_files = [file for file in os.listdir(lips_path) if file.endswith('.mod')]
        for module in lip_files:
            self._lips[module] = [resource for resource in Capsule(lips_path + module)]

    def load_textures(self) -> None:
        self._texturepacks = {}
        texturepacks_path = self.texturepacks_path()
        texturepacks_files = [file for file in os.listdir(texturepacks_path) if file.endswith('.erf')]
        for module in texturepacks_files:
            self._texturepacks[module] = [resource for resource in Capsule(texturepacks_path + module)]

    def load_override(self) -> None:
        self._override = {}

        for path, subdirs, files in os.walk(self.override_path()):
            directory = path.replace("\\", "/").replace(self.override_path(), "")
            path = (path if path.endswith("/") else path + "/").replace("\\", "/")
            self._override[directory] = {}

            for file in files:
                with suppress(Exception):
                    name, ext = file.split('.', 1)
                    size = os.path.getsize(path + file)
                    resource = FileResource(name, ResourceType.from_extension(ext), size, 0, path + file)
                    self._override[directory][file] = resource

    def reload_override(self, directory):
        self._override[directory] = {}
        files = os.listdir(self.override_path() + directory)
        for file in files:
            with suppress(Exception):
                name, ext = file.split('.', 1)
                size = os.path.getsize(self.override_path() + directory + file)
                resource = FileResource(name, ResourceType.from_extension(ext), size, 0, self.override_path() + directory + file)
                self._override[directory][file] = resource
    # endregion

    # region Get FileResources
    def chitin_resources(self) -> List[FileResource]:
        return self._chitin[:]

    def modules_list(self) -> List[str]:
        return list(self._modules.keys())

    def module_resources(self, filename) -> List[FileResource]:
        return self._modules[filename][:]

    def lips_list(self) -> List[str]:
        return list(self._lips.keys())

    def lip_resources(self, filename) -> List[FileResource]:
        return self._lips[filename][:]

    def texturepacks_list(self) -> List[str]:
        return list(self._texturepacks.keys())

    def texturepack_resources(self, filename) -> List[FileResource]:
        return self._texturepacks[filename][:]

    def override_list(self) -> List[str]:
        return list(self._override.keys())

    def override_resources(self, directory: str) -> List[FileResource]:
        return list(self._override[directory].values())
    # endregion

    def talktable(self) -> TalkTable:
        return self._talktable

    def resource(self, resname: str, restype: ResourceType, *, capsules: List[Capsule] = None, folders: List[str] = None,
                 skip_modules: bool = False, skip_chitin: bool = False, skip_override: bool = False) -> ResourceResult:
        """
        Returns a resource matching the specified resref and restype. If no resource is found then None is returned
        instead.

        Resource is search for in the following order:
            1. "folders" parameter.
            2. Installation override folder.
            3. "capsules" parameter.
            4. Installation module files in modules folder.
            5. Installation Chitin.

        Args:
            resname: The ResRef string.
            restype: The resource type.
            capsules: An extra list of capsules to search in.
            folders: An extra list of folders to search in.
            skip_chitin: If true, skips searching chitin files.
            skip_modules: If true, skips searching through module files.
            skip_override: If true, skips searching through override files.

        Returns:
            The filepath to the resource and resource bytes data or None.
        """
        capsules = [] if capsules is None else capsules
        folders = [] if folders is None else folders

        query = FileQuery(resname, restype)

        # 1 - Check user provided folders
        for folder in folders:
            folder = folder + '/' if not folder.endswith('/') else folder
            for file in [file for file in os.listdir(folder) if os.path.isfile(folder + file)]:
                filepath = folder + file
                with suppress(Exception):
                    f_resref, f_restype = ResourceIdentifier.from_path(file)
                    if query.resname.lower() == f_resref and query.restype == f_restype:
                        return ResourceResult(filepath, resname, BinaryReader.load_file(filepath))

        # 2 - Check installation override
        if not skip_override:
            override_path = self.override_path()
            for subfolder, directory in self._override.items():
                for filename, resource in directory.items():
                    filepath = override_path + subfolder + filename
                    if resource == query:
                        return ResourceResult(filepath, resname, resource.data())

        # 3 - Check user provided modules
        for capsule in capsules:
            if capsule.exists(resname, restype):
                return ResourceResult(capsule.path(), resname, capsule.resource(resname, restype))

        # 4 - Check installation modules
        if not skip_modules:
            module_path = self.module_path()
            for module_name, resources in self._modules.items():
                filepath = module_path + module_name
                for resource in resources:
                    if resource == query:
                        return ResourceResult(filepath, resname, resource.data())

        # 5 - Check installation chitin
        if not skip_chitin:
            filepath = self.path() + "chitin.key"
            for resource in self._chitin:
                if resource == query:
                    return ResourceResult(resource.filepath(), resname, resource.data())

        return ResourceResult("", "", None)

    def resource_batch(self, queries: List[FileQuery], *, capsules: List[Capsule] = None, folders: List[str] = None,
                 skip_modules: bool = False, skip_chitin: bool = False, skip_override: bool = False) -> List[ResourceResult]:
        results: List[ResourceResult] = []

        capsules = [] if capsules is None else capsules
        folders = [] if folders is None else folders

        # 1 - Check user provided folders
        for folder in folders:
            folder = folder + '/' if not folder.endswith('/') else folder
            for file in [file for file in os.listdir(folder) if os.path.isfile(folder + file)]:
                filepath = folder + file
                with suppress(Exception):
                    f_resref, f_restype = ResourceIdentifier.from_path(file)
                    for query in copy(queries):
                        if query.resname.lower() == f_resref and query.restype == f_restype:
                            queries.remove(query)
                            results.append(ResourceResult(filepath, query.resname, BinaryReader.load_file(filepath)))

        # 2 - Check installation override
        if not skip_override:
            override_path = self.override_path()
            for subfolder, directory in self._override.items():
                for filename, resource in directory.items():
                    filepath = override_path + subfolder + filename
                    for query in copy(queries):
                        if resource == query:
                            queries.remove(query)
                            results.append(ResourceResult(filepath, query.resname, resource.data()))

        # 3 - Check user provided modules
        for capsule in capsules:
            for query in copy(queries):
                if capsule.exists(query.resname, query.restype):
                    results.append(ResourceResult(capsule.path(), query.resname, capsule.resource(query.resname, query.restype)))

        # 4 - Check installation modules
        if not skip_modules:
            modules_path = self.module_path()
            for module_name, resources in self._modules.items():
                filepath = modules_path + module_name
                for resource in resources:
                    for query in copy(queries):
                        if resource == query:
                            results.append(ResourceResult(filepath, query.resname, resource.data()))

        # 5 - Check installation chitin
        if not skip_chitin:
            handles = {}
            for resource in self._chitin:
                for query in copy(queries):
                    if resource == query:
                        if resource.filepath() not in handles:
                            handles[resource.filepath()] = BinaryReader.from_file(resource.filepath())
                        handles[resource.filepath()].seek(resource.offset())
                        data = handles[resource.filepath()].read_bytes(resource.size())
                        results.append(ResourceResult(resource.filepath(), query.resname, data))

        return results

    def locate(self, resname: str, restype: ResourceType, *, capsules: List[Capsule] = None, folders: List[str] = None,
               skip_modules: bool = False, skip_chitin: bool = False, skip_override: bool = False,
               skip_textures: bool = False) -> List[LocationResult]:
        """
        Returns a list filepaths for where a particular resource matching the given resref and restype are located.

        Texture is search for in the following order:
            1. "folders" parameter.
            2. Installation override folder.
            3. "capsules" parameter.
            4. Installation module files in modules folder.
            5. Normal texture pack.
            6. Installation Chitin.

        Args:
            resname: The ResRef string.
            restype: The resource type.
            capsules: An extra list of capsules to search in.
            folders: An extra list of folders to search in.
            skip_chitin: If true, skips searching chitin files.
            skip_modules: If true, skips searching through module files.
            skip_override: If true, skips searching through override files.
            skip_textures: If true, skips searching through the texturepack.

        Returns:
            A list of filepaths.
        """
        capsules = [] if capsules is None else capsules
        folders = [] if folders is None else folders

        query = FileQuery(resname, restype)
        locations: List[LocationResult] = []

        # 1 - Check user provided folders
        for folder in folders:
            folder = folder + '/' if not folder.endswith('/') else folder
            for file in [file for file in os.listdir(folder) if os.path.isfile(folder + file)]:
                with suppress(Exception):
                    f_resref, f_restype = ResourceIdentifier.from_path(file)
                    f_filepath = folder + file
                    f_size = os.path.getsize(f_filepath)
                    if resname.lower() == f_resref and restype == f_restype:
                        locations.append(LocationResult(f_filepath, 0, f_size))

        # 2 - Check installation override
        if not skip_override:
            override_path = self.override_path()
            for subfolder, files in self._override.items():
                for filename, resource in files.items():
                    if resource == query:
                        filepath = override_path + subfolder + filename
                        size = os.path.getsize(filepath)
                        locations.append(LocationResult(filepath, 0, size))

        # 3 - Check user provided modules
        for capsule in capsules:
            locations.extend([LocationResult(resource.filepath(), resource.offset(), resource.size())
                              for resource in capsule if resource == query])

        # 4 - Check installation modules
        if not skip_modules:
            for modules in self._modules.values():
                resources = modules
                locations.extend([LocationResult(resource.filepath(), resource.offset(), resource.size())
                                  for resource in resources if resource == query])

        # 5 - Check installation texturepack
        if not skip_textures:
            resources = self.texturepack_resources("swpc_tex_tpa.erf")
            locations.extend([LocationResult(resource.filepath(), resource.offset(), resource.size())
                              for resource in resources if resource == query])

        # 6 - Check installation chitin
        if not skip_chitin:
            resources = self._chitin
            locations.extend([LocationResult(resource.filepath(), resource.offset(), resource.size())
                              for resource in resources if resource == query])

        return locations

    def texture(self, resname: str, *, capsules: List[Capsule] = None, folders: List[str] = None,
                skip_modules: bool = False, skip_chitin: bool = True, skip_gui: bool = True,
                skip_override: bool = False, texture_quality: TextureQuality = TextureQuality.HIGH) -> Optional[TPC]:
        """
        Returns a TPC object loaded from a resource with the specified ResRef.

        Texture is search for in the following order:
            1. "folders" parameter.
            2. "capsules" parameter.
            3. Installation override folder.
            4. Normal texture pack.
            5. GUI texture pack.
            6. Installation Chitin.
            7. Installation module files in modules folder.

        Args:
            resname: The ResRef string.
            capsules: An extra list of capsules to search in.
            folders: An extra list of folders to search in.
            skip_modules: If true, skips searching through module files in the installation modules folder.
            skip_chitin: If true, skips searching through chitin files in the installation.
            skip_gui: If true, skips searching through the gui files in the texturepacks folder.
            skip_override: If true, skips searching through the override files in the installation.
            texture_quality: Which texturepack to search through.

        Returns:
            TPC object or None.
        """
        capsules = [] if capsules is None else capsules
        folders = [] if folders is None else folders

        # 1 - Check user provided folders
        for folder in folders:
            folder = folder + '/' if not folder.endswith('/') else folder
            for file in [file for file in os.listdir(folder) if os.path.isfile(folder + file)]:
                with suppress(Exception):
                    f_resref, f_restype = ResourceIdentifier.from_path(file)
                    if resname.lower() == f_resref and f_restype in [ResourceType.TPC, ResourceType.TGA]:
                        return load_tpc(BinaryReader.load_file(folder + file))

        # 2 - Check user provided modules
        for capsule in capsules:
            if capsule.exists(resname, ResourceType.TGA):
                return capsule.resource(resname, ResourceType.TPC)
            if capsule.exists(resname, ResourceType.TPC):
                return capsule.resource(resname, ResourceType.TGA)

        # 3 - Check installation override folder
        if not skip_override:
            for directory in self._override.values():
                for file_name, resource in directory.items():
                    if resource.resname().lower() == resname.lower() and resource.restype() == ResourceType.TGA:
                        return load_tpc(resource.data())
                    elif resource.resname().lower() == resname.lower() and resource.restype() == ResourceType.TPC:
                        return load_tpc(resource.data())

        # 4 - Check normal texturepack
        for resource in self.texturepack_resources("swpc_tex_tp{}.erf".format(texture_quality.value)):
            if resource.resname().lower() == resname.lower() and resource.restype() == ResourceType.TPC:
                return load_tpc(resource.data())

        # 5 - Check GUI texturepack
        if not skip_gui:
            for resource in self.texturepack_resources("swpc_tex_gui.erf"):
                if resource.resname().lower() == resname.lower() and resource.restype() == ResourceType.TPC:
                    return load_tpc(resource.data())

        # 6 - Check chitin
        if not skip_chitin:
            for resource in self._chitin:
                if resource.resname().lower() == resname.lower() and resource.restype() == ResourceType.TPC:
                    return load_tpc(resource.data())

        # 7 - Check modules files in installation modules folder
        if not skip_modules:
            for module_name, resources in self._modules.items():
                for resource in resources:
                    if resource.resname().lower() == resname.lower() and resource.restype() == ResourceType.TPC:
                        return load_tpc(resource.data())
                    if resource.resname().lower() == resname.lower() and resource.restype() == ResourceType.TGA:
                        return load_tpc(resource.data())

        return None

    def twoda(self, resname: str) -> Optional[TwoDA]:
        return load_2da(self.resource(resname, ResourceType.TwoDA).data)

    def string(self, stringref: int) -> str:
        return self._talktable.string(stringref)

    def module_name(self, module_filename: str) -> str:
        """
        Returns the name of the area for a module from the installations module list. The name is taken from the
        LocalizedString "Name" in the relevant module file's ARE resource.

        Args:
            module_filename: The name of the module file.

        Returns:
            The name of the area for the module.
        """
        root = module_filename.replace(".mod", "").replace(".erf", "").replace(".rim", "")
        root = root[:-len("_s")] if root.endswith("_s") else root
        root = root[:-len("_dlg")] if root.endswith("_dlg") else root

        name = ""

        for module in self.modules_list():
            if root not in module:
                continue

            capsule = Capsule(self.module_path() + module)
            tag = ""

            if capsule.exists("module", ResourceType.IFO):
                ifo = load_gff(capsule.resource("module", ResourceType.IFO))
                tag = ifo.root.get_resref("Mod_Entry_Area").get()
            if capsule.exists(tag, ResourceType.ARE):
                are = load_gff(capsule.resource(tag, ResourceType.ARE))
                locstring = are.root.get_locstring("Name")
                if locstring.stringref > 0:
                    name = self._talktable.string(locstring.stringref)
                elif locstring.exists(Language.ENGLISH, Gender.MALE):
                    name = locstring.get(Language.ENGLISH, Gender.MALE)
                break

        return name

    def module_names(self) -> Dict[str, str]:
        """
        Returns a dictionary mapping module filename to the name of the area. The name is taken from the LocalizedString
        "Name" in the relevant module file's ARE resource.

        Returns:
            A dictionary mapping module filename to in-game module area name.
        """
        module_names = {}
        for module in self.modules_list():
            module_names[module] = self.module_name(module)
        return module_names
