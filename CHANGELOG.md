# Changelog

All notable changes to bwEnc are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.6.2] - 2026-09-27

### Changed

- Version info.

## [1.6.1] - 2026-09-27

### Changed

- Standardized runtime version handling with the other bulkware applications.

## [1.6.0] - 2026-09-27

### Changed

- GitHub Actions CI package building.
- Packaging system for Debian (.deb) and Red Hat (.rpm) based distros.
- Renewed the Windows packaging system.


## Historical releases

The 1.0.3, 1.1.0, and 1.3.0 dates below are confirmed by version-specific Git
commits. Version 1.2.0 is inferred from its matching source-change commit;
earlier release dates predate retained Git history and are unknown.

### [1.5.0] - 2026-09-23

#### Changed

- Migrated from PyQt6 into PySide6.

### [1.4.0] - 2026-09-23

#### Changed

- Migrated from PyQt4 into PyQt6.

### [1.3.0] - 2019-04-19

#### Changed

- Changed the SourceForge link to a GitHub link.
- Made the toolbar non-movable.
- Moved the Quit button into the toolbar.

#### Fixed

- Fixed a typo in the README.

### [1.2.0] - 2018-02-15

#### Added

- Added documentation for `whitelist.csv` to the README.
- Moved the project to GitHub and added a README.

### [1.1.0] - 2018-01-01

#### Changed

- Processed command-line arguments the same way as other file additions.
- Refreshed the file-list table before showing a message to the user.
- Added a toolbar.
- Changed UTF-8 output to UTF-8 with BOM.
- Made UTF-8 without BOM the default output encoding.

#### Fixed

- Fixed the maximum-size limit.

### [1.0.3] - 2014-01-11

#### Added

- Added action icons and drag-and-drop support.
- Added a dummy column for easier table selections.
- Added row numbers to the table.
- Added more detailed information when adding files.

#### Changed

- Renamed Add directory to Add folder.
- Enabled and disabled widgets based on user actions.
- Adopted the new-style PyQt signals.
- Saved window geometry.

### [1.0.2] - 2013-02-15

#### Changed

- Handled settings with Qt's `QSettings`.

### [1.0.1] - 2013-02-13

#### Added

- Added support for more file types.

### [1.0.0] - 2013-02-02

#### Added

- Initial release.
