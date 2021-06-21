from gtshcli.services.subprocess_runner import SubprocessRunner


class RemoteService(SubprocessRunner):
    def subtree_merge(cls, url, branch, target_dir):
        output = cls.run("remote-merge-subtree", [url, branch, target_dir])
        if output == "":
            return None

        return output
