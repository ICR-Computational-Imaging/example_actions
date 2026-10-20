"""Simple tests for the hello-world example."""

from examples import helloworld


def test_get_current_time_str():
    """The time should contain valid hours, minutes, and seconds."""
    current_time = helloworld.get_current_time_str()

    # For example, "09:05:03" has eight characters and three parts.
    assert len(current_time) == 8
    parts = current_time.split(":")
    assert len(parts) == 3

    for part in parts:
        assert len(part) == 2
        assert part.isdigit()

    hours, minutes, seconds = parts
    assert 0 <= int(hours) <= 23
    assert 0 <= int(minutes) <= 59
    assert 0 <= int(seconds) <= 59


def test_main_prints_ten_numbered_lines(capsys):
    """The script should print ten lines, numbered from 1 to 10."""
    helloworld.main()

    # capsys is provided by pytest. It collects text printed during the test.
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert len(lines) == 10

    for number, line in enumerate(lines, start=1):
        assert line.startswith(f"Line {number}.  Time is now ")

    assert captured.err == ""
