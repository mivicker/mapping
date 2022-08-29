from typing import List
import numpy as np
import geopandas as gpd
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt
import tilemapbase
from tilemapbase.mapping import Extent
import warnings
import matplotlib.cbook

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)
import seaborn as sns
import shapely.speedups

shapely.speedups.enable()

points = gpd.read_file(
    "./data/noord-hollard-latest-free.shp/gis_osm_pois_free_1.shp"
)
points = points.to_crs("EPSG:3857")

city = gpd.read_file("./data/geojson.json")
city = city.to_crs("EPSG:3857")

points = gpd.sjoin(points, city, how="left")
points = points.dropna(subset=["index_right"])


def create_bounding_box(points: gpd.GeoDataFrame) -> List[np.float64]:
    return [
        points["geometry"].x.min(),
        points["geometry"].x.max(),
        points["geometry"].y.min(),
        points["geometry"].y.max(),
    ]


# This creates the sql3 cache necessary to get tiles
# from OSM


def plot_map(
    display_data: gpd.GeoDataFrame, geography: gpd.GeoDataFrame, filename: str
) -> None:
    """
    Takes municiple boundaries and a point dataset and plots
    them onto open street map tiles then saves plot to given
    filename.
    """

    # create the tilemapbase cache with 'init' and create the extent
    tilemapbase.init(create=True)
    extent = tilemapbase.extent_from_frame(geography, buffer=25)

    fig, ax = plt.subplots(figsize=(10, 10))
    bounding_box = create_bounding_box(points)
    plotter = tilemapbase.Plotter(
        extent, tilemapbase.tiles.build_OSM(), width=1000
    )
    plotter.plot(ax)

    # geography.plot(ax=ax, alpha=0.3, edgecolor="black", facecolor="white")

    display_data.plot(
        ax=ax,
        alpha=0.4,
        color="red",
        marker="$\\bigtriangledown$",
    )

    ax.set_xlim(bounding_box[0] + 2000, bounding_box[1])
    ax.set_ylim(bounding_box[2] + 2000, bounding_box[3])
    ax.figure.savefig(f"./data/{filename}", bbox_inches="tight")


plot_map(points, city, "with_func.png")
