# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['H:\\Placement_Management\\Trails\\Project_Trail_1\\PlacementManagementSystem.py'],
    pathex=[],
    binaries=[],
    datas=[('c:\\users\\ashha\\appdata\\local\\programs\\python\\python310\\lib\\site-packages\\customtkinter', 'customtkinter/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PlacementManagementSystem',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PlacementManagementSystem',
)
