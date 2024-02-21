import pathlib
import time

#  get the preferred root-directory
rootdir = pathlib.Path().resolve().parent.joinpath('cmdlog')

#  cmdlog/settings
settings_dir = rootdir.joinpath('settings').as_posix()

#  cmdlog/logs/
settingslog_path = rootdir.joinpath('logs')

#  cmdlog/py_dir
bin_path = rootdir.joinpath('py_dir')

# .py files

#  cmdlog/settings/
settings_path = rootdir.joinpath(settings_dir).joinpath('config.py')

#  cmdlog/
cmdlog_path = rootdir.joinpath('cmdlog.py')

#  cmdlog/logs/history/
history_path = settingslog_path.joinpath('history').joinpath('history.py')

#  cmdlog/py_dir/*.py

cmdmenu_path = bin_path.joinpath('cmdmenu.py').as_posix()      # <-- The main menu
logger_path = bin_path.joinpath('logger.py').as_posix()        # <-- Creates and writes into a (new) <filename>.log
                                                                 #  Look at "timestring" below for timestring settings.
listfiles_path = bin_path.joinpath('listfiles.py').as_posix()  # <-- List the files in "cmdlog/logs"
readfile_path = bin_path.joinpath('readfile.py').as_posix()    # <-- Print out a chosen log-file to the screen.
delfile_path = bin_path.joinpath('delfile.py').as_posix()      # <-- Remove a chosen log-file
searchlog_path = bin_path.joinpath('searchlog.py').as_posix()  # <-- Search for a keyword in a log-file
loginlog_path = bin_path.joinpath('loginlog.py')               # <-- Check the latest login-attempts

#  making sure that search_path is a string
search_path = str(settingslog_path)

#  Set the timeformat for the filenames
# %Y = Year , %m = month , %d = day , %H = Hour , %M = Minutes , %S = Seconds
timestring = time.strftime("%Y%m%d-%H.%M.%S")
