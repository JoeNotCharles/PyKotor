from typing import List


class PatchLogger:
    def __init__(self):
        self.notes: List[PatchLog] = []
        self.warnings: List[PatchLog] = []
        self.errors: List[PatchLog] = []

        self.patches_completed: int = 0

    def complete_patch(self) -> None:
        self.patches_completed += 1

    def add_note(self, message: str) -> None:
        self.notes.append(PatchLog(message))

    def add_warning(self, message: str) -> None:
        self.warnings.append(PatchLog(message))

    def add_error(self, message: str) -> None:
        self.errors.append(PatchLog(message))


class PatchLog:
    def __init__(self, message: str):
        self.message: str = message
