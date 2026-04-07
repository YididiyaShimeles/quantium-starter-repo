from app import app
from dash import dcc


def find_component_by_id(component, target_id):
    if hasattr(component, "id") and component.id == target_id:
        return component

    children = getattr(component, "children", None)

    if children is None:
        return None

    if isinstance(children, (list, tuple)):
        for child in children:
            found = find_component_by_id(child, target_id)
            if found is not None:
                return found
    else:
        found = find_component_by_id(children, target_id)
        if found is not None:
            return found

    return None


def test_header_is_present():
    header = find_component_by_id(app.layout, "dashboard-header")
    assert header is not None
    assert header.children == "Pink Morsel Sales Dashboard"


def test_visualisation_is_present():
    graph = find_component_by_id(app.layout, "sales-graph")
    assert graph is not None
    assert isinstance(graph, dcc.Graph)


def test_region_picker_is_present():
    picker = find_component_by_id(app.layout, "region-picker")
    assert picker is not None
    assert isinstance(picker, dcc.RadioItems)