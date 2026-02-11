import pytest
from appmeteo.main_objects.main_process_command import *

@pytest.fixture
def main_process():
    return MainProcessCommand()

def test_main_process(mocker):
    main = MainProcessCommand()
    # Empêche la boucle infinie en forçant la réponse "Nouvelle opération ?" à False
    mock_confirm = mocker.patch(
        "appmeteo.main_objects.main_process_command.inquirer.confirm",
        return_value=mocker.Mock(execute=lambda: False)
    )
    # Patch toutes les méthodes .execute pour compter les appels
    patches = {}
    for code in ["title", "C1", "C2", "C3", "C4"]:
        patches[code] = mocker.patch.object(main.commands[code], 'execute', return_value=None)
    # Patch de la sélection de menu (commande C0)
    c0_execute = mocker.patch.object(main.commands["C0"], "execute")
    # Test 1 avec la sélection de la première option
    c0_execute.return_value = "1"
    main.process()
    assert patches["title"].call_count == 1
    assert patches["C1"].call_count == 1
    for p in patches.values():
        p.reset_mock()
    # Test 2 avec la sélection de la deuxième option
    c0_execute.return_value = "2"
    main.process()
    assert patches["title"].call_count == 1
    assert patches["C2"].call_count == 1
    for p in patches.values():
        p.reset_mock()
    # Test 3 avec la sélection de la troisième option
    c0_execute.return_value = "3"
    main.process()
    assert patches["title"].call_count == 1
    assert patches["C3"].call_count == 1
    for p in patches.values():
        p.reset_mock()
    # Test 4 avec la sélection de la dernière option
    c0_execute.return_value = "4"
    main.process()
    assert patches["title"].call_count == 1
    assert patches["C4"].call_count == 1
    for p in patches.values():
        p.reset_mock()


def test_select_menu(mocker):
    mock_select = mocker.patch(
        "appmeteo.main_objects.main_process_command.inquirer.select"
    )
    # Test 1 avec la sélection de la première option
    mock_select.return_value.execute.return_value = ("Afficher les derniers relevés de toutes les stations", "1")
    cmd = SelectMenuCommand()
    result = cmd.execute()
    assert result == "1"
    # Test 2 avec la sélection de la dernière option
    mock_select.return_value.execute.return_value = ("Afficher les derniers relevés des stations précédentes (par une file).", "4")
    cmd = SelectMenuCommand()
    result = cmd.execute()
    assert result == "4"
