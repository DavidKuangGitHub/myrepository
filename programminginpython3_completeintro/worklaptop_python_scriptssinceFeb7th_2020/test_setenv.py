'''test_setenv.py'''
import os, pytest

@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_strats_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile","w") as f:
            f.write("helloDK")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []