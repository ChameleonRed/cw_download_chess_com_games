# Description

Download all chess.com games. 
All games PGN file will be stored current or specified directory.

Raw source JSON files with extra information is stored in `output/cache` path. 

# Usage

## Get help
`cw_download_chess_com_games -h`

## Get games

`cw_download_chess_com_games --user_name your_chess_com_name`

## Get games into custom path/directory

`cw_download_chess_com_games --user_name your_chess_com_name --output_path .`

## Update recent games

Delete `output/cache` to allow fresh download.

# License
Copyright 2022 by Cezary K. Wagner. Licensed under [Attribution-NonCommercial-NoDerivatives 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0).