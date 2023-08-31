from __future__ import annotations

import concurrent.futures
import threading
from typing import TYPE_CHECKING

from pykotor.common.stream import BinaryReader, BinaryWriter
from pykotor.extract.capsule import Capsule
from pykotor.extract.file import ResourceIdentifier
from pykotor.tools.misc import is_capsule_file
from pykotor.tools.path import CustomPath

if TYPE_CHECKING:
    from pykotor.tslpatcher.logger import PatchLogger


print_lock = threading.Lock()


class InstallFile:
    def __init__(self, filename: str, replace_existing: bool) -> None:
        self.filename: str = filename
        self.replace_existing: bool = replace_existing

    def _identifier(self) -> ResourceIdentifier:
        return ResourceIdentifier.from_path(self.filename)

    def apply_encapsulated(
        self,
        log: PatchLogger,
        source_folder: str,
        destination: Capsule,
    ) -> None:
        resname, restype = self._identifier()

        if self.replace_existing or destination.resource(resname, restype) is None:
            if (
                self.replace_existing
                and destination.resource(resname, restype) is not None
            ):
                with print_lock:
                    log.add_note(
                        f"Replacing file {self.filename} in the {destination.filename()} archive...",
                    )
            else:
                with print_lock:
                    log.add_note(
                        f"Adding file {self.filename} in the {destination.filename()} archive...",
                    )

            data = BinaryReader.load_file(CustomPath(source_folder) / self.filename)
            destination.add(resname, restype, data)

    def apply_file(
        self,
        log: PatchLogger,
        source_folder: CustomPath,
        destination: CustomPath,
        local_folder: str,
    ) -> None:
        data = BinaryReader.load_file(source_folder / self.filename)
        save_file_to = destination / self.filename

        if self.replace_existing or not save_file_to.exists():
            if not destination.exists():
                with print_lock:
                    log.add_note(f"Folder {destination} did not exist, creating it...")
                destination.mkdir(parents=True, exist_ok=True)


            if self.replace_existing and not save_file_to.exists():
                with print_lock:
                    log.add_note(
                        f"Replacing file '{self.filename}' to the '{local_folder}' folder...",
                    )
            else:
                with print_lock:
                    log.add_note(
                        f"Copying file '{self.filename}' to the '{local_folder}' folder...",
                    )

            BinaryWriter.dump(save_file_to, data)
        else:
            with print_lock:
                log.add_warning(
                    f"A file named '{self.filename}' already exists in the '{local_folder}' folder. Skipping file...",
                )


class InstallFolder:
    # The `InstallFolder` class represents a folder that can be installed, and it provides a method to
    # apply the installation by copying files from a source path to a destination path.
    def __init__(
        self,
        foldername: str,
        files: list[InstallFile] | None = None,
    ) -> None:
        self.foldername: str = foldername
        self.files: list[InstallFile] = files or []

    def apply(
        self,
        log: PatchLogger,
        source_path: CustomPath,
        destination_path: CustomPath,
    ):
        target: CustomPath = destination_path / self.foldername

        if is_capsule_file(self.foldername):
            destination = Capsule(target, create_nonexisting=True)
            for file in self.files:
                file.apply_encapsulated(log, str(source_path), destination)
        else:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                # Submit each task individually using executor.submit
                futures = [
                    executor.submit(
                        lambda file: file.apply_file(
                            log,
                            source_path,
                            target,
                            self.foldername,
                        ),
                        file,
                    )
                    for file in self.files
                ]

                # Use as_completed to get the results as they complete
                for future in concurrent.futures.as_completed(futures):
                    try:
                        future.result()  # Process the result if needed
                    except Exception as thread_exception:
                        # Handle any exceptions that occurred during execution
                        with print_lock:  # Acquire the lock before printing
                            print("Exception occurred:")
                            print(thread_exception)
