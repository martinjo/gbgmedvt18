# -*- coding: utf-8 -*-

"""
Copyright: Martin Johansson
License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
Select any number of cards in the card browser, enter a field name and it will be made lowercase and all "." will be removed.
This helps on the mobile client which cannot run the javascript to color .- and case errors as if they were correctly entered (annoying)

To use:

1) Open the card browser
2) Select the desired cards
3) Go to Edit > Cleanup
4) In the pop-up window, enter the field name that you want to "clean"
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from anki.hooks import addHook
from aqt import mw
from aqt.utils import getOnlyText
from anki.utils import timestampID


def cleanFields(nids):
    mw.checkpoint("Clean")
    mw.progress.start()
    
    # Get desired deck name from input box
    fieldName = getOnlyText(_("Field name to modify:"), default="Baksida")
    if not fieldName:
        return
    fieldName = fieldName.replace('"', "")
    
    # Edit notes
    for nid in nids:
        print "Found note: %s" % (nid)
        note = mw.col.getNote(nid)
        # Make lower case and remove "."
        note[fieldName] = note[fieldName].lower().replace(".","")
        note.flush()

    
    
def setupMenu(browser):
    a = QAction("Cleanup", browser)
    browser.connect(a, SIGNAL("triggered()"), lambda e=browser: onCleanFields(e))
    browser.form.menuEdit.addSeparator()
    browser.form.menuEdit.addAction(a)

def onCleanFields(browser):
    cleanFields(browser.selectedNotes())

addHook("browser.setupMenus", setupMenu)
