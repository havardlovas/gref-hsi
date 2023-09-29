import configparser
from ..lib import hyperspectral_utils
from ..scripts import visualize, georeference
# Import the configuration file and read it into dictionary
home_path = 'C:/Users/haavasl/PycharmProjects/hyperspectral_toolchain'
data_dir = home_path + '/data/Skogn21012021'
config_file = data_dir + '/configuration.ini'
config = configparser.ConfigParser()
config.read(config_file)



def main():
    # Visualize the data
    visualize.show_mesh_camera(config)

    # Perform some operations
    georeference.main(config_file, mode='georeference', is_calibrated=True)

if __name__ == "__main__":
    main()