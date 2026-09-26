@echo off

echo ==============================
echo  Daily Utility Build
echo ==============================

echo.
echo [1/3] Installing PyInstaller...
python -m pip install pyinstaller

echo.
echo [2/3] Building EXE...
python -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name DailyUtility ^
    main.py

echo.
echo [3/3] Copying plugins...

if exist "dist\plugins" (
    rmdir /s /q "dist\plugins"
)

xcopy "plugins" "dist\plugins" /E /I /Y

echo.
echo ==============================
echo  Build completed!
echo ==============================
echo.
echo Output:
echo dist\DailyUtility.exe
echo dist\plugins\
echo.

pause