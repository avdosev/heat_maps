import argparse
import heat_map_plot as hmp

parser = argparse.ArgumentParser(description='Hide info in image.')

args = parser.parse_args()


if __name__ == "__main__":
    print("started")
    hmp.draw_test_plot()
