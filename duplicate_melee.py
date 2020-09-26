import argparse
import os
import shutil


def duplicate_melee(folder, n):
    """
    I've found experimentally that duplicating the settings in the melee timescript files will cause characters
    to perform the same action multiple times. This can be abused if the player is having a hard time in long
    fights where characters sustain a lot of damage and stress.

    Notes on mechanics:

        - This only works on melee skills. I tried the same thing with ranged and friendly but they do not work.

        - This applies to ALL melee skills, including the enemies'!

        - Because of the previous point, this is actually very bad if the enemies you face have a very high speed
          stat, since they will go first and inflict a LOT of damage on friendly characters.

        - The same attack will repeat a number of times--the RNG rolls before the attack. This means that if a
          character misses or crits, all subsequent hits will also miss or crit respectively.

        - Status effects will not be applied multiple times. For example, if a character bleeds for 3 damage
          per turn, even if the enemy is hit 5 times with this mechanic, they will still only bleed for 3
          per turn. It seems like the status effect is applied after the damage, and something separate from
          these melee timescript files is responsible for that.

        - If an enemy is killed before the number of hits, the remaining hits will be done to the dead body of
          the enemy, thereby also possibly clearing the corpses. However, there is no move update for the
          remaining enemies--no new enemy will fill that slot until the attack is over, even after the corpse
          is cleared.

    :param folder: path to "scripts\timescript" folder
    :param n: total number of hits per melee attack
    :return: None
    """
    # get all melee ".times" files in current folder
    files = ["melee.times", "melee_crit.times"]

    # make backup
    backup_folder = os.path.join(folder, "backup_melee")
    if not os.path.exists(backup_folder):
        print("Backup files will be saved to:")
        print(backup_folder)
        os.mkdir(backup_folder)

    for file in files:
        file_path = os.path.join(folder, file)
        backup_file_path = os.path.join(backup_folder, file)

        if not os.path.exists(backup_file_path):
            shutil.copy(src=file_path, dst=backup_file_path)

        # duplicate file
        with open(file_path, "r+") as f:
            text = f.read()

            for _ in range(n - 1):
                f.write(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change the number of times all characters perform melee attacks "
                                                 "in Darkest Dungeon. This script creates a backup of all of the "
                                                 "scripts used for timing melee attacks, then edits the values "
                                                 "in these timing scripts to make characters attack multiple times.")

    parser.add_argument("folder", help="Timescripts folder. This should can be found in [GAME FOLDER]/scripts")
    parser.add_argument("-n", type=int, default=3, help="Number of times to repeat melee attacks. The default is 3.")

    args = parser.parse_args()

    duplicate_melee(args.folder, args.n)
