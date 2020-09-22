import argparse
import os
import re
import shutil


def regex_scale_time(time_str):
    """
    Scales time value given by regex.

    TODO: SPEED should be given as an arg but it's a global variable (because I pass this function to regex
    TODO: substitute as a callback function, so no args provided there)

    :param time_str: guaranteed to be in ".time [FLOAT]" format, where the float is the original time
    :return: ".time [FLOAT]" format, where the float is the new time, scaled by SPEED
    """
    time_val = time_str.group(1)
    time_val = float(time_val)

    time_val = time_val / SPEED     # scale by 1 / speed
    time_val = round(time_val, 3)   # round to 3 decimal places (milliseconds)

    time_val = str(time_val)
    return ".time " + time_val


def speed_up(folder):
    """
    Speed up all time values found in the "timescript" folder, which includes the timing for scripts that
    control the battle animation speed and event timing. Will save all the original files to a backup folder.

    :param folder: path to "scripts\timescript" folder
    :return: None
    """
    # get all ".times" files in current folder
    files = os.listdir(folder)
    files = filter(lambda x: x.endswith(".times"), files)
    files = list(files)

    # make backup
    backup_folder = os.path.join(folder, "backup")
    if not os.path.exists(backup_folder):
        print("Backup files will be saved to:")
        print(backup_folder)
        os.mkdir(backup_folder)

    for file in files:
        file_path = os.path.join(folder, file)
        backup_file_path = os.path.join(backup_folder, file)

        if not os.path.exists(backup_file_path):
            shutil.copy(src=file_path, dst=backup_file_path)

        # make changes to time
        with open(file_path, "r+") as f:
            text = f.read()

            text = re.sub(r".time (([0-9]*[.])?[0-9]+)", regex_scale_time, text)

            f.seek(0)
            f.write(text)
            f.truncate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change battle speeds in Darkest Dungeon. This script creates a"
                                                 "backup of all of the scripts used for timing, then edits the values"
                                                 "in these timing scripts to speed up battle.")

    parser.add_argument("folder", help="Scripts folder")
    parser.add_argument("--speed", type=int, default=2,
                        help="Factor to speed up battle animation by. If this is not given, by default the battle "
                             "animations will be at double its original speed.")

    args = parser.parse_args()

    global SPEED
    SPEED = args.speed

    print("\nSpeeding up battle animations by a factor of {0}...".format(SPEED))
    speed_up(folder=args.folder)
    print("Done!")

