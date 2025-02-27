from src.main import greet

def test_greet():
    expected = "欢迎使用 My1AI 项目！"
    assert greet() == expected, f"预期输出：{expected}，实际得到：{greet()}"
