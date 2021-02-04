from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

build_options = {'packages': [], 'excludes': [], 'include_files': ['settings_sample.json', 'input_sample.csv']}

executables = [
    Executable('main.py', base = 'Console', target_name = 'GuruStock Automator')
]

setup(name = 'GuruStock Automator',
      version = '1.0.0',
      description = 'GuruStock Automator is a program to automate the extraction of market data from Guru app.',
      options = {'build_exe': build_options},
      executables = executables)
