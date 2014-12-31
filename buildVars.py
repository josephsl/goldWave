# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "goldwave",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("GoldWave"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("An add-on for enhancing access and usage of the Goldwave audio editor."),
	# version
	"addon_version" : "3.0-dev",
	# Author(s)
	"addon_author" : u"Joseph Lee <joseph.lee22590@gmail.com>, David Parduhn <xkill85@gmx.net>, Mesar Hameed <mhameed@src.gnome.org>",
	# URL for the add-on documentation support
	"addon_url" : 'http://addons.nvda-project.org',
	# File name for the add-on help file.
	"addon_docFileName" : "readme.html"
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "appModules", "*.py"),]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
