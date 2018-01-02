import subprocess
from dogebuild.plugin.interfaces import *


class Fpc(Plugin):
    name = 'fpc'
    add_dir_key = '-Fu"{0}"'

    def get_active_tasks(self):
        tasks = [self.create_task(CompileTask)]
        if hasattr(self, 'main_test_file'):
            tasks.extend([
                self.create_task(CompileTestsTask),
                self.create_task(RunTestsTask),
                ])

        return tasks


class CompileTask(Task):
    name = Fpc.name + ':compile'

    def run(self):
        call_string = ['fpc']

        if hasattr(self.plugin, 'unit_dirs'):
            for d in self.plugin.unit_dirs:
                call_string.append(Fpc.add_dir_key.format(d))

        call_string.append(self.plugin.main_file)

        subprocess.call(call_string)


class CompileTestsTask(Task):
    name = Fpc.name + ':compile-tests'

    def run(self):
        call_string = ['fpc']

        if hasattr(self.plugin, 'test_dirs'):
            for d in self.plugin.test_dirs:
                call_string.append(Fpc.add_dir_key.format(d))

        call_string.append(self.plugin.main_test_file)

        subprocess.call(call_string)


class RunTestsTask(Task):
    name = Fpc.name + ':run-tests'

    def run(self):
        target = self.plugin.main_test_file
        subprocess.call([target])


class CleanTask(Task):
    name = Fpc.name + ':clean'

    def run(self):
        pass
