#!/usr/bin/bash
# from https://stackoverflow.com/questions/25152995/linux-shell-renaming-files-to-creation-time
for f in *.jpeg
do
    mv -n "$f" "$(exiftool -d "%Y%m%d_%H%M%S" -CreateDate "$f" | awk '{print $4".jpg"}')"
done