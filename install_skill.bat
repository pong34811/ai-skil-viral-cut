@echo off
chcp 65001 >nul
title Install Skill: Viral Cut Detection

set "SKILL_NAME=viral-cut-detection"
set "SRC=%~dp0.opencode\skills\%SKILL_NAME%"
set "DST=%USERPROFILE%\.config\opencode\skills\%SKILL_NAME%"

echo.
echo ============================================
echo  Install Skill: %SKILL_NAME%
echo ============================================
echo.
echo  Source: %SRC%
echo  Dest:   %DST%
echo.

if not exist "%SRC%" (
    echo [ERROR] Source not found: %SRC%
    echo.
    echo Make sure you run this .bat from the project root folder.
    pause
    exit /b 1
)

if not exist "%DST%" (
    mkdir "%DST%"
    echo [OK] Created directory: %DST%
)

copy /Y "%SRC%\SKILL.md" "%DST%\SKILL.md" >nul

if exist "%DST%\SKILL.md" (
    echo [OK] Installed successfully!
    echo.
    echo The skill "%SKILL_NAME%" is now available globally.
    echo You can use it in any opencode project.
) else (
    echo [ERROR] Copy failed.
    pause
    exit /b 1
)

echo.
pause
