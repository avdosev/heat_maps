import matplotlib.pyplot as plt
import geopandas as gpd
import geojson
from shapely.geometry import Polygon


def geopandas(input_filename, column, cmap):
    mo_gdf = gpd.read_file(input_filename)
    mo_gdf.to_json()
    ax = mo_gdf.plot(column=column, cmap=cmap, legend=True, figsize=[15, 15])
    plt.show()


import folium


def __minmax(polygons):
    """return (min_x, max_x), (min_y, max_y)"""
    # TODO optimization
    min_x = min(min(polygons, key=lambda polygon: min(polygon.exterior.coords.xy[0])).exterior.coords.xy[0])
    min_y = min(min(polygons, key=lambda polygon: min(polygon.exterior.coords.xy[1])).exterior.coords.xy[1])

    max_x = max(max(polygons, key=lambda polygon: max(polygon.exterior.coords.xy[0])).exterior.coords.xy[0])
    max_y = max(max(polygons, key=lambda polygon: max(polygon.exterior.coords.xy[1])).exterior.coords.xy[1])

    return (min_x, max_x), (min_y, max_y)


def html_map(input_filename, column, output, cmap):
    mo_gdf = gpd.read_file(input_filename)

    x_coord, y_coord = __minmax(mo_gdf["geometry"])

    def avg(min_max):
        return (min_max[1] + min_max[0]) / 2
    print(f'feature.properties.{column}')
    m = folium.Map(location=[avg(y_coord), avg(x_coord)])
    folium.Choropleth(

    ).add_to(m)

    m.save(output)
