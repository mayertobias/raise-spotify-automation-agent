import pandas as pd

df = pd.read_json('//37i9dQZF1DX186v583rmzp.json')
#print(df)
audio_features = df.T
print(audio_features)


# get relevant audio features
#feature_subset = audio_features.drop["uri" "track_href" "analysis_url" "duration_ms" "time_signature"]
#print(feature_subset)