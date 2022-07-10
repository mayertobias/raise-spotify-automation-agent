import json

filenames_global = ["37i9dQZF1DX186v583rmzp.json"]


def get_track_ids_from_playlist_json(filenames):
    for filename in filenames:
        file = open(filename, 'r')
        parsed_json = json.load(file)
        y = []
        for index in range(0, len(parsed_json['items'])):
            y.append(parsed_json['items'][index]['track']['id'])
        print(y)


def reformat_spotify_response_to_axis_input():
    file = open("jmAudioFeatures.json", 'r')
    json_data = json.load(file)
    print(type(json_data))

    audio_features = json_data["audio_features"]

    print(type(audio_features))
    songs = {}
    jsondata = {}
    for items in audio_features:
        # print(f"\nKey: {key}")
        # print(f"Value: {value}\n")
        sub_json = json.dumps(items, indent=4, sort_keys=True)
        json_sub_data = json.loads(sub_json)

        song = {}
        content = {}
        axis = {}
        # print(json.dumps(jsondata))
        axislist = []
        for key, value in json_sub_data.items():
            # print(f"\nKey: {key}")
            # print(f"Value: {value}\n")
            if key == 'id':
                song['id'] = value
            axislist.append({'axis': key, 'value': value})
            # print(axislist)
            # axislist.append({'axis': key})
            # axis['axis'] = key
            # axis['value'] = value
        content = axislist
        # content['othervar'] = "new"

        jsondata['song'] = song
        jsondata['content'] = content
        songs.append(jsondata)
    print("***************")
    print(json.dumps(songs))
    # Close the opened sample JSON file
    # Using close() function
    file.close()