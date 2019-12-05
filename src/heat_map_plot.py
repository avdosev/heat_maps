import matplotlib.pyplot as plt
import geopandas as gpd

def geopandas(filename, column, cmap):
    mo_gdf = gpd.read_file(filename)
    ax = mo_gdf.plot(column=column, cmap=cmap, legend=True, figsize=[15,15])
    plt.show()
