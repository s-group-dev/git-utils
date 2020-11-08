from gutscli.services.subprocess_runner import SubprocessRunner


class RepositoryService(object):
    def clean_up(cls):
        process = SubprocessRunner()
        return process.run("repository-clean-up", [])
