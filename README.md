# Darkest Dungeon Scripts

A collection of scripts for quality of life changes in (and breaking) [Darkest Dungeon](https://www.darkestdungeon.com/).

All the scripts require [Python 3](https://www.python.org/downloads/) to run.

## Changing Battle Animation Speeds

Tired of waiting for all the battle and discovery animations? This script can help speed things up! Just provide the path to your game's timescripts folder, and it will automatically back everything up, and speed up all the animation times.

```
usage: change_times.py [-h] [--speed SPEED] folder

Change battle speeds in Darkest Dungeon. This script creates abackup of all of
the scripts used for timing, then edits the valuesin these timing scripts to
speed up battle.

positional arguments:
  folder         Scripts folder

optional arguments:
  -h, --help     show this help message and exit
  --speed SPEED  Factor to speed up battle animation by. If this is not given,
                 by default the battle animations will be at double its
                 original speed.
```

For example, if my timescripts folder is at `"C:\Users\karl\Documents\Darkest Dungeon\scripts\timescript"`, to make everything run at 2x speed, I would simply run:
```bash
python change_times.py "C:\Users\karl\Documents\Darkest Dungeon\scripts\timescript
```

If I wanted to scale by a custom speed, for example 3x, I can run:
```bash
python change_times.py "C:\Users\karl\Documents\Darkest Dungeon\scripts\timescript --speed 3
```

Note that this works with the time scripts **currently** in the `timescripts`, so that means if that if I run this twice, my battle animation speeds will be 4 times their original speed! However, running it twice will not overwrite the original backup files--those will still remain at the original speed.

#FAQ

Feel free to contact me if you have any questions or comments!