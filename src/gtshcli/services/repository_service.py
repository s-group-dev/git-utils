from gtshcli.services.subprocess_runner import SubprocessRunner


class RepositoryService(SubprocessRunner):
    def clean_up(cls):
        return cls.run("repository-clean-up", [])
