# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/cale/Desktop/M1-IEI/Project/lithophanes'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='3D Lithophanes',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir='/tmp',
          console=False , icon='resources/icons/app.icns')
app = BUNDLE(exe,
             name='3D Lithophanes.app',
             icon='./resources/icons/app.icns',
             bundle_identifier=None,
             runtime_tmpdir="/tmp",
             info_plist={
                'NSHighResolutionCapable': 'True'
                },
)
