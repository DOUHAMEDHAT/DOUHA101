#Importing the base packages:
for package in ('pip', 'sys'):
    try:
        globals()[package] = __import__(package, globals=globals())
    except ImportError:
        !pip install -U package

#Creating the installed-packages:
installed_packages = !pip freeze
keys = []
values = []
for package_version in installed_packages:
    keys.append(package_version.split('==')[0])
    values.append(package_version.split('==')[1])
    
installed_packages = dict(zip(keys, values))

#Checking the installion and loading:
packages = ['os', 'pandas', 'numpy', 'zipfile', 'google', 'google.cloud', 'google.oauth2.service_account', 'gspread', 'IPython', 'matplotlib', 'dplython', 'requests', 'tkinter']

for package in packages:
    if package in installed_packages.keys():
        if package in sys.modules.keys():
            os.close
        else:
            try:
                globals()[package] = __import__(package, globals=globals())
                print("====> Package is imported successfully now: ", package)
            except ImportError as import_erros:
                print("Package not imported: ", package)
    else:
        #pip._internal.main(["install", package])
        globals()[package] = __import__(package)
