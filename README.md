# music-splicer
A Python command-line script to splice an audio file into smaller chunks with user-specified timestamps

How to use:

1. Have python installed.
2. Put the timestamps in the form "hh\:mm\:ss [name]", each on a separate line.
3. Add an extra line with the end time of the final chunk.
4. Run the command `python main.py [timestamps filename] [audio filename]`.
5. The program outputs each chunk starting at its timestamp and ending at the one in the next line.
6. If you wish to have a chunk end at a different time, you can add a dummy timestamp for the time you wish to use.
