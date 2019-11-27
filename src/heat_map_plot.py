# import src.geojson as geoj
import geopandas as gpd
import matplotlib.pyplot as plt

def draw_test_plot():
    # data = geoj.read_geojson("city_grid.geojson")
    mo_gdf = gpd.read_file("city_grid.geojson")
    ax = mo_gdf.plot()

    plt.show()