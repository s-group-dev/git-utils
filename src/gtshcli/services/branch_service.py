from gtshcli.services.subprocess_runner import SubprocessRunner


class BranchService(object):
    def list(cls, branch, params):
        process = SubprocessRunner()
        params = [branch] + params
        output = process.run("branch-list", params)
        if output == "":
            return None

        return output

    def delete(cls, params):
        process = SubprocessRunner()
        return process.run("branch-delete", params)
