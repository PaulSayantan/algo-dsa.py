"""Design File System Navigator — shell cd / pwd simulator."""


class FileSystemNavigator:
    def __init__(self) -> None:
        # TODO: hold the current directory as a stack of path components
        pass

    def cd(self, path: str) -> None:
        # TODO: reset on an absolute path, then push names / skip '.' / pop on '..'
        pass

    def pwd(self) -> str:
        # TODO: join the component stack with '/', prefixed by root '/'
        pass


if __name__ == "__main__":
    nav = FileSystemNavigator()
    nav.cd("/usr/local/bin")
    print(nav.pwd())  # expected: '/usr/local/bin'
    nav.cd("../../share")
    print(nav.pwd())  # expected: '/usr/share'
    nav.cd("./docs/../lib")
    print(nav.pwd())  # expected: '/usr/share/lib'
    nav.cd("/")
    print(nav.pwd())  # expected: '/'
    nav.cd("../../a/b")
    print(nav.pwd())  # expected: '/a/b'
