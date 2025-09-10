from src.app import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Welcome to the Cafe CLI App!" in captured.out
