CONFIG += qt debug

RESOURCES = luma/resources.py

SOURCES += luma/luma.py
SOURCES += luma/lumaWithOptions.py
SOURCES += luma/resources.py
SOURCES += luma/base/backend/ServerObject.py
SOURCES += luma/base/backend/PluginObject.py
SOURCES += luma/base/backend/ServerList.py
SOURCES += luma/base/backend/SmartDataObject.py
SOURCES += luma/base/backend/PluginLoader.py
SOURCES += luma/base/backend/LumaConnection.py
SOURCES += luma/base/backend/ObjectClassAttributeInfo.py
SOURCES += luma/base/backend/Log.py
SOURCES += luma/base/util/Paths.py
SOURCES += luma/base/util/IconTheme.py
SOURCES += luma/base/util/i18n.py
SOURCES += luma/base/util/model/PluginListWidgetModel.py
SOURCES += luma/base/util/gui/PluginListWidgetDesign.py
SOURCES += luma/base/util/gui/PluginListWidget.py
SOURCES += luma/base/model/ServerListModel.py
SOURCES += luma/base/model/SettingsModel.py
SOURCES += luma/base/model/PluginSettingsListModel.py
SOURCES += luma/base/gui/Settings.py
SOURCES += luma/base/gui/ServerDialog.py
SOURCES += luma/base/gui/MainWindow.py
SOURCES += luma/base/gui/PluginSettings.py
SOURCES += luma/base/gui/SplashScreen.py
SOURCES += luma/base/gui/AboutDialog.py
SOURCES += luma/base/gui/SettingsDialog.py
SOURCES += luma/base/gui/ServerDelegate.py
SOURCES += luma/base/gui/design/MainWindowDesign.py
SOURCES += luma/base/gui/design/AboutCreditsDesign.py
SOURCES += luma/base/gui/design/AboutLicenseDesign.py
SOURCES += luma/base/gui/design/LoggerWidgetDesign.py
SOURCES += luma/base/gui/design/AboutDialogDesign.py
SOURCES += luma/base/gui/design/NewEntryDialogDesign.py
SOURCES += luma/base/gui/design/WidgetPlusOkCancelDialog.py
SOURCES += luma/base/gui/design/ServerDialogDesign.py
SOURCES += luma/base/gui/design/SettingsDialogDesign.py
SOURCES += luma/base/gui/rejects/BaseSelectorDesign.py
SOURCES += luma/base/gui/rejects/BaseSelector.py
SOURCES += luma/test/ServerListTest.py
SOURCES += luma/test/settings.py
SOURCES += luma/test/TestAll.py
SOURCES += luma/test/ServerObjectTest.py
SOURCES += luma/plugins/search/Search.py
SOURCES += luma/plugins/search/model/SearchModel.py
SOURCES += luma/plugins/search/gui/SearchFilterWizardDesign.py
SOURCES += luma/plugins/search/gui/SearchFormDesign.py
SOURCES += luma/plugins/browser_plugin/AdvancedObjectWidget.py
SOURCES += luma/plugins/browser_plugin/modeltest.py
SOURCES += luma/plugins/browser_plugin/BrowserView.py
SOURCES += luma/plugins/browser_plugin/NewEntryDialog.py
SOURCES += luma/plugins/browser_plugin/model/EntryModel.py
SOURCES += luma/plugins/browser_plugin/model/LDAPTreeItemModel.py
SOURCES += luma/plugins/browser_plugin/item/LDAPErrorItem.py
SOURCES += luma/plugins/browser_plugin/item/RootTreeItem.py
SOURCES += luma/plugins/browser_plugin/item/ServerTreeItem.py
SOURCES += luma/plugins/browser_plugin/item/LDAPTreeItem.py
SOURCES += luma/plugins/browser_plugin/item/AbstractLDAPTreeItem.py
SOURCES += luma/plugins/browser_plugin/view/HtmlView.py
SOURCES += luma/plugins/browser_plugin/view/AbstractEntryView.py
SOURCES += luma/plugins/browser_plugin/view/ClassicView.py

FORMS += resources/forms/NewEntryDialogDesign.ui
FORMS += resources/forms/AboutDialogDesign.ui
FORMS += resources/forms/ServerDialogDesign.ui
FORMS += resources/forms/LoggerWidgetDesign.ui
FORMS += resources/forms/SettingsDialogDesign.ui
FORMS += resources/forms/AboutCreditsDesign.ui
FORMS += resources/forms/WidgetPlusOkCancelDialog.ui
FORMS += resources/forms/MainWindowDesign.ui
FORMS += resources/forms/AboutLicenseDesign.ui
FORMS += resources/forms/plugins/search/SearchFilterWizardDesign.ui
FORMS += resources/forms/plugins/search/SearchFormDesign.ui

TRANSLATIONS += resources/i18n/luma_hx.ts
TRANSLATIONS += resources/i18n/luma_en.ts
TRANSLATIONS += resources/i18n/luma_no.ts
