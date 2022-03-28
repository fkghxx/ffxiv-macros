# todo 适配常用命令
import math
import  os

MACRO_LINE_MAX = 15


class Macro:
    def __init__(self, name) -> None:
        self.name = name
        self.lines = []

    def add(self, cmd: str):
        self.lines.append(cmd)

    def toFile(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        with open(f"{path}/{self.name}", "w", encoding="utf-8") as f:
            flag = len(self.lines) > MACRO_LINE_MAX
            for i in range(len(self.lines)):
                if flag and i % MACRO_LINE_MAX == 0:
                    f.write(f"## macro {math.ceil(i / MACRO_LINE_MAX) + 1}")
                f.write(self.lines[i])
                f.write("\n")

class hobar:
    cmd = "/hotbar"

    @classmethod
    def copy(cls, source_job, source_id, target_job, target_id) -> str:
        return f"{cls.cmd} copy {source_job} {source_id} {target_job} {target_id}"

class micon:
    cmd = "/micon"
    # todo 类型
    @classmethod
    def icon(cls, name, typ) -> str:
        return f"{cls.cmd} {name} {typ}"

class gs:
    cmd = "/gs"
    @classmethod
    def change(cls, id) -> str:
        return f"{cls.cmd} change {id}"