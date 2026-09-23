# Changelog

All notable changes to bwEnc will be documented in this file.

## [1.5.0]

### Changed

- Migrated from PyQt6 into PySide6.

## [1.4.0]

### Changed

- Migrated from PyQt4 into PyQt6.

## [1.3.0]

### Changed

- Changed the SourceForge link to a GitHub link.
- Made the toolbar non-movable.
- Moved the Quit button into the toolbar.

### Fixed

- Fixed a typo in the README.

## [1.2.0]

### Added

- Added documentation for `whitelist.csv` to the README.
- Moved the project to GitHub and added a README.

## [1.1.0]

### Changed

- Processed command-line arguments the same way as other file additions.
- Refreshed the file-list table before showing a message to the user.
- Added a toolbar.
- Changed UTF-8 output to UTF-8 with BOM.
- Made UTF-8 without BOM the default output encoding.
- Changed version numbering.

### Fixed

- Fixed the maximum-size limit.

## [1.03]

### Added

- Added action icons and drag-and-drop support.
- Added a dummy column for easier table selections.
- Added row numbers to the table.
- Added more detailed information when adding files.

### Changed

- Renamed Add directory to Add folder.
- Enabled and disabled widgets based on user actions.
- Adopted the new-style PyQt signals.
- Saved window geometry.

## [1.02]

### Changed

- Handled settings with Qt's `QSettings`.

## [1.01]

### Added

- Added support for more file types.

## [1.00]

### Added

- Initial release.
