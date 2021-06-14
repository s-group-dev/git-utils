from gtshcli.services.subprocess_runner import SubprocessRunner


class BranchService(SubprocessRunner):
    def list(cls, branch, params):
        params = [branch] + params
        output = cls.run("branch-list", params)
        if output == "":
            return None

        return output

    def delete(cls, params):
        return cls.run("branch-delete", params)
