def get_ll(toponym) -> str:
    # Координаты центра топонима:
    coords = toponym["Point"]["pos"]
    # Долгота и широта:
    longitude, lattitude = coords.split(" ")
    return ",".join([longitude, lattitude])


def get_spn(toponym) -> str:
    values = list(toponym["boundedBy"]["Envelope"].values())
    x1, y1 = map(float, values[0].split())
    x2, y2 = map(float, values[1].split())
    return f"{x2-x1},{y2-y1}"
