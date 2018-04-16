# dbloader.py
import json

# file names for artist, venue, and show
artist_file_name = 'artist'
venue_file_name = 'venue'
show_file_name = 'show'

# function to read in a json file with specified name passed through
def read_json_file(file_name):

    # create file_name by appending name to known location of file
    file_name = 'fixtures/' + file_name + '.json'

    # try except for opening file
    try:

        # open file as json data
        with open(file_name) as json_data:
            json_obj = json.load(json_data)
            return json_obj

    except Exception as e:
        print("file error loading in JSON file: % e" % e)
        exit(-10)


def main():

    # get json objects for artist, venue, and show respectively
    artist_json = read_json_file(artist_file_name)
    venue_json = read_json_file(venue_file_name)
    show_json = read_json_file(show_file_name)

    print('Artist:')
    print(artist_json)
    print('Venue:')
    print(venue_json)
    print('Show:')
    print(show_json)

main()
