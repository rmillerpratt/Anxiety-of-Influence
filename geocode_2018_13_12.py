import geopy
import pandas
from geopy.geocoders import Nominatim

def main():
  io = pandas.read_csv('2018_13_12_AoI_1_textonly.csv', index_col=0, header=0, sep=",")

  def get_latitude(x):
    return x.latitude

  def get_longitude(x):
    return x.longitude

  geolocator = Nominatim()

  geolocate_column = io['pub_location'].apply(geolocator.geocode)
  io['latitude'] = geolocate_column.apply(get_latitude)
  io['longitude'] = geolocate_column.apply(get_longitude)
  io.to_csv('geocoding_output_2018_13_12.csv')

if __name__ == '__main__':
 main()
