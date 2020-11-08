from gutscli.services.subprocess_runner import SubprocessRunner


class RemoteService(object):
    def subtree_merge(cls, url, branch, target_dir):
        process = SubprocessRunner()
        output = process.run("remote-merge-subtree", [url, branch, target_dir])
        if output == "":
            return None

        return output
