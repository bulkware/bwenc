; The name of the installer
Name "bwEnc"

; The file to write
OutFile "installers\bwenc_1.1.0_installer_win32.exe"

; The default installation directory
InstallDir "$PROGRAMFILES\bwEnc"

; Registry key to check for directory (so if you install again, it will
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\bwEnc" "Install_Dir"

; Request application privileges for Windows Vista
RequestExecutionLevel admin

;--------------------------------

; Pages
Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

;--------------------------------

; The stuff to install
Section "bwEnc (required)"

    SectionIn RO

    ; Set output path to the installation directory.
    SetOutPath $INSTDIR

    ; Put application files there
    File "build\*.*"

    ; Write the installation path into the registry
    WriteRegStr HKLM "SOFTWARE\bwEnc" "Install_Dir" "$INSTDIR"

    ; Write the uninstall keys for Windows
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\bwEnc" "DisplayName" "bwEnc"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\bwEnc" "UninstallString" '"$INSTDIR\Uninstall.exe"'
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\bwEnc" "NoModify" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\bwEnc" "NoRepair" 1
    WriteUninstaller "Uninstall.exe"

SectionEnd


; Optional section (can be disabled by the user)
Section "Start Menu Shortcuts"

    CreateDirectory "$SMPROGRAMS\bwEnc"
    CreateShortCut "$SMPROGRAMS\bwEnc\bwEnc.lnk" "$INSTDIR\bwEnc.exe" "" "$INSTDIR\bwEnc.exe" 0
    CreateShortCut "$SMPROGRAMS\bwEnc\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" "$INSTDIR\Uninstall.exe" 0

SectionEnd

;--------------------------------

; Uninstaller
Section "Uninstall"

    ; Remove registry keys
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\bwEnc"
    DeleteRegKey HKLM "SOFTWARE\bwEnc"

    ; Remove files
    Delete "$INSTDIR\*.*"

    ; Remove shortcuts, if any
    Delete "$SMPROGRAMS\bwEnc\*.*"

    ; Remove directories used
    RMDir "$SMPROGRAMS\bwEnc"
    RMDir "$INSTDIR"

SectionEnd
