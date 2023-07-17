import sys
import json
import pickle
import s2sphere
from s2sphere import CellId, LatLng, Cell
from shapely.geometry import Point
sys.setrecursionlimit(10000) 

def load_data_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data["customCoordinates"]

def get_cell_dict(data):
    cell_dict = {}

    for record in data:
        lat, long = record['lat'], record['lng']
        point = s2sphere.LatLng.from_degrees(lat, long).to_point()
        cell = s2sphere.CellId.from_point(point).parent(0)
        cell_dict.setdefault(cell.id(), []).append(point)

    return cell_dict

def divide_cell(cell, cell_dict, max_points=20):
    points = cell_dict.get(cell.id(), [])
    if len(points) <= max_points:
        if points:
            return [cell]
        else:
            return []

    del cell_dict[cell.id()]

    children = cell.children()
    divided_cells = []

    for child in children:
        child_points = []
        for p in points:
            child_cell = s2sphere.Cell(child)
            if child_cell.contains(p):
                child_points.append(p)
        if child_points:
            cell_dict[child.id()] = child_points
            divided_cells.extend(divide_cell(child, cell_dict, max_points))

    return divided_cells

def get_cell_bounds(cell_id):
    cell = s2sphere.Cell(cell_id)

    latitudes = []
    longitudes = []


    points = [cell.get_center(), cell.get_vertex(0), cell.get_vertex(1), cell.get_vertex(2), cell.get_vertex(3)]
    for point in points:
        latlng = s2sphere.LatLng.from_point(point)
        latitudes.append(latlng.lat().degrees)
        longitudes.append(latlng.lng().degrees)

    min_lat = min(latitudes)
    max_lat = max(latitudes)
    min_lon = min(longitudes)
    max_lon = max(longitudes)

    # Handle cells that cross the international date line
    if max_lon - min_lon > 180.0:
        longitudes = [(lng + 360 if lng < 0 else lng) for lng in longitudes]
        min_lon = min(longitudes)
        max_lon = max(longitudes)
        # Wrap back into [-180, 180]
        if max_lon > 180.0:
            max_lon -= 360.0
        if min_lon > 180.0:
            min_lon -= 360.0

    return min_lat, min_lon, max_lat, max_lon

json_file = 'world.json' # CHANGE JSON NAME
max_points = 100

data = load_data_from_json(json_file)
cell_dict = get_cell_dict(data)

cells = []
cell_bounds_dict = {}
cell_keys = list(cell_dict.keys())

for cell_id in cell_keys:
    cell = s2sphere.CellId(cell_id)
    cells.extend(divide_cell(cell, cell_dict, max_points))

for i, cell in enumerate(cells, 0): 
    cell_bounds_dict[i] = get_cell_bounds(cell)

print(cell_bounds_dict)

with open('chile.pkl', 'wb') as f: # CHANGE PKL NAME
    pickle.dump(cell_bounds_dict, f)

