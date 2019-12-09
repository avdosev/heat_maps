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
    gdf = gpd.read_file(input_filename)

    x_coord, y_coord = __minmax(gdf["geometry"])

    def avg(min_max):
        return (min_max[1] + min_max[0]) / 2

    m = folium.Map(location=[avg(y_coord), avg(x_coord)])

    # из за корявого интерфейся/документации/моей невнимательности
    # создается соответсвие
    # значение: значени_дата
    # которое по своей сути словарь
    # значение: значение
    # хз как сделать по нормальному возможно никак

    tmp_frame = gpd.GeoDataFrame()
    tmp_frame[column] = gdf[column]
    tmp_frame[column+'_data'] = gdf[column]

    folium.Choropleth(
        geo_data=gdf[[column, 'geometry']].to_json(),
        name='choropleth',
        data=tmp_frame,
        key_on=f'feature.properties.{column}',
        columns=[column, column+'_data'],
        fill_color='YlGnBu',
        line_weight=0,
        fill_opacity=0.7,
        line_opacity=0.2
    ).add_to(m)

    m.save(output)
