import os
import subprocess


class SubProcessRunner(object):

    def run(self, script, params):
        params = [self._get_scripts_dir() + '/' + script + '.sh'] + params
        process = subprocess.run(
            params,
            stdout=subprocess.PIPE,
            universal_newlines=True)

        return process.stdout.strip()

    def _get_scripts_dir(self):
        return os.path.realpath(
            os.path.dirname(
                os.path.realpath(__file__)) + '/../../scripts')
