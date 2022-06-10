import os

import zhconv as zhconv
from mutagen.flac import FLAC


def get_meta(x_path):
    for dirpath, directories, files in os.walk(x_path):
        for sound_file in files:
            if sound_file.endswith('.flac') or sound_file.endswith('.FLAC'):
                print('flac:\t\t%s/%s' % (dirpath, sound_file))
                flac_file = os.path.join(dirpath, sound_file)
                metadata = FLAC(flac_file)
                titles = [zhconv.convert(item, "zh-hans") for item in get_metadata(metadata, "TITLE")]
                albums = [zhconv.convert(item, "zh-hans") for item in get_metadata(metadata, "ALBUM")]
                album_artists = [zhconv.convert(item, "zh-hans") for item in get_metadata(metadata, "ALBUMARTIST")]
                artists = [zhconv.convert(item, "zh-hans") for item in get_metadata(metadata, "ARTIST")]

                metadata["TITLE"] = titles
                metadata["ALBUM"] = albums
                metadata["ALBUMARTIST"] = album_artists
                metadata["ARTIST"] = artists
                metadata["COMMENT"] = [""]
                metadata["DESCRIPTION"] = [""]

                metadata.save()
                print("metadata:\ttitles:%s, albums:%s, album_artists:%s, artists:%s" % (
                    titles, albums, album_artists, artists))


def get_metadata(metadata, key):
    datas = []
    if key in metadata:
        for item in metadata.get(key):
            datas.append(item)
    if len(datas) == 0:
        datas.append("")
    return datas


if __name__ == '__main__':
    # XPATH = "/Volumes/music/music/歌手专辑/"
    XPATH = "%s/" % os.path.abspath('..')
    get_meta(XPATH)
