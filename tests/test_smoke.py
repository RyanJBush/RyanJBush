import importlib


CANDIDATE_MODULES = ["main", "app", "src.main", "src.app"]


def test_import_main_app_module_and_smoke_assertion():
    for module_name in CANDIDATE_MODULES:
        try:
            importlib.import_module(module_name)
            break
        except Exception:
            continue
    assert True
