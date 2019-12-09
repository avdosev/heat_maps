import argparse
import heat_map_plot as hmp
import geojson as geoj

parser = argparse.ArgumentParser(description='Hide info in image.')

args = parser.parse_args()


if __name__ == "__main__":
    filename = "city_grid.geojson"
    cmap = 'YlGnBu'
    column = "obj2"
    print("started")
    print("start draw")
    hmp.geopandas(filename, column, cmap=cmap)
    hmp.html_map(filename, column, "../output/map.html", cmap=cmap)
    print("end draw")
