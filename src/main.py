import argparse
import heat_map_plot as hmp


name_to_column = {
    "personal_transport": "tr1",
    "public_transport": "tr2",
    "health_care_facilities": "obj1",
    "educational_institutions": "obj2",
    "social_and_commercial": "obj3",
    "prestige": "prestige"
}

output = "../output/map.html"
filename = "city_grid.geojson"

parser = argparse.ArgumentParser(description='creator heat map')
parser.add_argument('--html', action="store_true")
parser.add_argument('--geopandas', action="store_true")
parser.add_argument('-o', '--outPath', default=output)
parser.add_argument('-i', '--inPath', default=filename)
parser.add_argument('-c', '--cmap', default='YlGnBu', type=str, help="Input color map")
parser.add_argument('--column', type=str, default="educational_institutions", choices=name_to_column.keys())

args = parser.parse_args()

if __name__ == "__main__":
    output = args.outPath
    filename = args.inPath
    cmap = args.cmap
    column = name_to_column[args.column]
    print("started")
    print("start draw")
    if args.html:
        hmp.html_map(filename, column, output, cmap=cmap)
    if args.geopandas:
        hmp.geopandas(filename, column, cmap=cmap)
    print("end draw")
