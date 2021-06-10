import os
import subprocess


class SubprocessRunner(object):
    def run(cls, script, params):
        params = [cls._get_scripts_dir() + "/" + script + ".sh"] + params
        process = subprocess.run(
            params, stdout=subprocess.PIPE, universal_newlines=True
        )

        return process.stdout.strip()

    def _get_scripts_dir(cls):

        return os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "../../scripts"
        )
