@echo off

echo ==============================
echo  Daily Utility Build
echo ==============================

python -m pip install pyinstaller

python -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name DailyUtility ^
    main.py

echo.
echo ==============================
echo  Build completed
echo ==============================
echo.
echo EXE:
echo dist\DailyUtility.exe
echo.

pause