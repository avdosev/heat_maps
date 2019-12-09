import argparse
import heat_map_plot as hmp
import geojson as geoj

parser = argparse.ArgumentParser(description='Hide info in image.')

args = parser.parse_args()


if __name__ == "__main__":
    filename = "city_grid.geojson"
    cmap = 'YlGnBu'
    print("started")
    data = geoj.read_geojson(filename)
    print("end reading geojson")
    print("features count", len(data["features"]))
    print("start draw")
    # hmp.geopandas(filename, "prestige", cmap=cmap)
    hmp.html_map(filename, "prestige", "../output/map.html", cmap=cmap)
