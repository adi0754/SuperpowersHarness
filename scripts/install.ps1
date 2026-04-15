param(
  [string[]]$Platforms = @("codex", "claude", "cursor"),
  [string]$RepoPath = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

function Get-SkillNames {
  param(
    [string]$RepoPath
  )

  $skillsDir = Join-Path $RepoPath "skills"
  if (-not (Test-Path $skillsDir)) {
    throw "Skills directory does not exist: $skillsDir"
  }

  $skillFolders = Get-ChildItem -LiteralPath $skillsDir -Directory | Where-Object {
    Test-Path (Join-Path $_.FullName "SKILL.md")
  }

  if (-not $skillFolders -or $skillFolders.Count -eq 0) {
    throw "No skill folders found under: $skillsDir"
  }

  return $skillFolders | ForEach-Object { $_.Name }
}

$skillNames = Get-SkillNames -RepoPath $RepoPath

$platformSkillDirs = @{
  codex = "$env:USERPROFILE\.codex\skills"
  claude = "$env:USERPROFILE\.claude\skills"
  cursor = "$env:USERPROFILE\.cursor\skills"
}

function Ensure-Junction {
  param(
    [string]$LinkPath,
    [string]$TargetPath
  )

  if (-not (Test-Path $TargetPath)) {
    throw "Target path does not exist: $TargetPath"
  }

  $resolvedTarget = (Resolve-Path $TargetPath).Path

  if (Test-Path $LinkPath) {
    $existingItem = Get-Item -LiteralPath $LinkPath
    $existingTarget = $existingItem.Target

    if ($existingTarget) {
      $resolvedLinkTarget = (Resolve-Path $existingTarget).Path
      if ($resolvedLinkTarget -eq $resolvedTarget) {
        Write-Host "Already installed: $LinkPath"
        return
      }
    }

    throw "Path already exists and points elsewhere: $LinkPath"
  }

  New-Item -ItemType Directory -Force -Path (Split-Path $LinkPath -Parent) | Out-Null
  New-Item -ItemType Junction -Path $LinkPath -Target $resolvedTarget | Out-Null
  Write-Host "Installed: $LinkPath -> $resolvedTarget"
}

foreach ($platform in $Platforms) {
  if (-not $platformSkillDirs.ContainsKey($platform)) {
    throw "Unsupported platform: $platform"
  }

  $skillRoot = $platformSkillDirs[$platform]
  New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null

  foreach ($skillName in $skillNames) {
    $targetPath = Join-Path $RepoPath "skills\$skillName"
    $linkPath = Join-Path $skillRoot $skillName
    Ensure-Junction -LinkPath $linkPath -TargetPath $targetPath
  }
}

Write-Host ""
Write-Host "Install complete."
Write-Host "Next step:"
Write-Host "  Restart your AI tool, then use SuperpowersHarness with one of: sh-start, sh-pack, sh-run, sh-recover"
