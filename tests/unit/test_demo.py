import pytest

pytestmark = pytest.mark.unit

# @pytest.mark.xfail(reason="已知bug")
def test_add():
    assert 1 + 1 == 2

def test_write(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("HiCli")
    assert p.read_text() == "HiCli"

def test_print(capsys):
    print("hello")
    out, err = capsys.readouterr()
    assert out == "hello\n"