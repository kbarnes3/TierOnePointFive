# Register helper functions
Set-Item function:global:Invoke-Fabric {
    . $PSScriptRoot\Invoke-Fabric.ps1 @args
} -Force

Set-Item function:global:Update-DevEnvironment {
    param([switch]$Verbose)
    . $PSScriptRoot\Update.ps1 -Verbose:$Verbose
} -Force
