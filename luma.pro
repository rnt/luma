CONFIG += qt debug

RESOURCES = luma/resources.py

SOURCES += luma/resources.py
SOURCES += luma/version.py
SOURCES += luma/runtests.py
SOURCES += luma/luma.py
SOURCES += luma/lumaWithOptions.py
SOURCES += luma/plugins/template/TemplateList.py
SOURCES += luma/plugins/template/TemplateObject.py
SOURCES += luma/plugins/template/gui/TemplateWidget.py
SOURCES += luma/plugins/template/gui/AddAttributeDialogDesign.py
SOURCES += luma/plugins/template/gui/AddObjectclassDialogDesign.py
SOURCES += luma/plugins/template/gui/AddObjectclassDialog.py
SOURCES += luma/plugins/template/gui/AddAttributeDialog.py
SOURCES += luma/plugins/template/gui/TemplateWidgetDesign.py
SOURCES += luma/plugins/template/gui/AddTemplateDialog.py
SOURCES += luma/plugins/template/gui/AddTemplateDialogDesign.py
SOURCES += luma/plugins/template/model/TemplateTableModel.py
SOURCES += luma/plugins/template/model/AttributeTableModel.py
SOURCES += luma/plugins/template/model/ObjectclassTableModel.py
SOURCES += luma/plugins/search/Search.py
SOURCES += luma/plugins/search/FilterBuilder.py
SOURCES += luma/plugins/search/Filter.py
SOURCES += luma/plugins/search/SearchForm.py
SOURCES += luma/plugins/search/SearchResult.py
SOURCES += luma/plugins/search/gui/FilterBuilderDesign.py
SOURCES += luma/plugins/search/gui/SearchPluginSettingsDesign.py
SOURCES += luma/plugins/search/gui/SearchPluginDesign.py
SOURCES += luma/plugins/search/gui/SearchFormDesign.py
SOURCES += luma/plugins/search/gui/FilterWizardDesign.py
SOURCES += luma/plugins/search/model/SearchResultModel.py
SOURCES += luma/plugins/browser_plugin/AdvancedObjectWidget.py
SOURCES += luma/plugins/browser_plugin/BrowserView.py
SOURCES += luma/plugins/browser_plugin/NewEntryDialog.py
SOURCES += luma/plugins/browser_plugin/NewEntryDialogDesign.py
SOURCES += luma/plugins/browser_plugin/HtmlParser.py
SOURCES += luma/plugins/browser_plugin/modeltest.py
SOURCES += luma/plugins/browser_plugin/TemplateFactory.py
SOURCES += luma/plugins/browser_plugin/item/LDAPErrorItem.py
SOURCES += luma/plugins/browser_plugin/item/AbstractLDAPTreeItem.py
SOURCES += luma/plugins/browser_plugin/item/LDAPTreeItem.py
SOURCES += luma/plugins/browser_plugin/item/ServerTreeItem.py
SOURCES += luma/plugins/browser_plugin/item/RootTreeItem.py
SOURCES += luma/plugins/browser_plugin/gui/DeleteDialogDesign.py
SOURCES += luma/plugins/browser_plugin/gui/ExportDialogDesign.py
SOURCES += luma/plugins/browser_plugin/model/LDAPTreeItemModel.py
SOURCES += luma/plugins/browser_plugin/model/EntryModel.py
SOURCES += luma/test/ServerListTest.py
SOURCES += luma/test/ServerObjectTest.py
SOURCES += luma/test/ConnectionTest.py
SOURCES += luma/test/settings.py
SOURCES += luma/base/gui/PluginSettings.py
SOURCES += luma/base/gui/MainWindow.py
SOURCES += luma/base/gui/AbstractLumaPlugin.py
SOURCES += luma/base/gui/WelcomeTab.py
SOURCES += luma/base/gui/ServerDialog.py
SOURCES += luma/base/gui/SplashScreen.py
SOURCES += luma/base/gui/ServerDelegate.py
SOURCES += luma/base/gui/SettingsDialog.py
SOURCES += luma/base/gui/AboutPlugin.py
SOURCES += luma/base/gui/Settings.py
SOURCES += luma/base/gui/Dialog.py
SOURCES += luma/base/gui/AboutDialog.py
SOURCES += luma/base/gui/design/AboutLicenseDesign.py
SOURCES += luma/base/gui/design/MainWindowDesign.py
SOURCES += luma/base/gui/design/WelcomeTabDesign.py
SOURCES += luma/base/gui/design/WidgetPlusOkCancelDialog.py
SOURCES += luma/base/gui/design/LoggerWidgetDesign.py
SOURCES += luma/base/gui/design/SettingsDialogDesign.py
SOURCES += luma/base/gui/design/ServerDialogDesign.py
SOURCES += luma/base/gui/design/NewEntryDialogDesign.py
SOURCES += luma/base/gui/design/AboutCreditsDesign.py
SOURCES += luma/base/gui/design/ExportDialogDesign.py
SOURCES += luma/base/gui/design/AboutPluginDesign.py
SOURCES += luma/base/gui/design/AboutDialogDesign.py
SOURCES += luma/base/gui/rejects/BaseSelector.py
SOURCES += luma/base/gui/rejects/BaseSelectorDesign.py
SOURCES += luma/base/util/Paths.py
SOURCES += luma/base/util/IconTheme.py
SOURCES += luma/base/util/i18n.py
SOURCES += luma/base/util/gui/PluginListWidget.py
SOURCES += luma/base/util/gui/PluginListWidgetDesign.py
SOURCES += luma/base/util/model/PluginListWidgetModel.py
SOURCES += luma/base/backend/Exception.py
SOURCES += luma/base/backend/PluginLoader.py
SOURCES += luma/base/backend/Connection.py
SOURCES += luma/base/backend/Log.py
SOURCES += luma/base/backend/PluginObject.py
SOURCES += luma/base/backend/ObjectClassAttributeInfo.py
SOURCES += luma/base/backend/ServerObject.py
SOURCES += luma/base/backend/LumaConnection.py
SOURCES += luma/base/backend/ServerList.py
SOURCES += luma/base/backend/SmartDataObject.py
SOURCES += luma/base/model/ServerListModel.py
SOURCES += luma/base/model/PluginSettingsListModel.py
SOURCES += luma/base/model/SettingsModel.py

FORMS += resources/forms/SettingsDialogDesign.ui
FORMS += resources/forms/AboutDialogDesign.ui
FORMS += resources/forms/AboutPluginDesign.ui
FORMS += resources/forms/ServerDialogDesign.ui
FORMS += resources/forms/LoggerWidgetDesign.ui
FORMS += resources/forms/NewEntryDialogDesign.ui
FORMS += resources/forms/WelcomeTabDesign.ui
FORMS += resources/forms/WidgetPlusOkCancelDialog.ui
FORMS += resources/forms/MainWindowDesign.ui
FORMS += resources/forms/AboutLicenseDesign.ui
FORMS += resources/forms/AboutCreditsDesign.ui
FORMS += resources/forms/plugins/template/AddObjectclassDialogDesign.ui
FORMS += resources/forms/plugins/template/AddAttributeDialogDesign.ui
FORMS += resources/forms/plugins/template/AddTemplateDialogDesign.ui
FORMS += resources/forms/plugins/template/TemplateWidgetDesign.ui
FORMS += resources/forms/plugins/search/SearchFormDesign.ui
FORMS += resources/forms/plugins/search/SearchPluginSettingsDesign.ui
FORMS += resources/forms/plugins/search/SearchPluginDesign.ui
FORMS += resources/forms/plugins/search/FilterBuilderDesign.ui
FORMS += resources/forms/plugins/browser_plugin/DeleteDialogDesign.ui
FORMS += resources/forms/plugins/browser_plugin/ExportDialogDesign.ui

TRANSLATIONS += resources/i18n/luma_no.ts
TRANSLATIONS += resources/i18n/luma_en.ts
TRANSLATIONS += resources/i18n/luma_hx.ts
