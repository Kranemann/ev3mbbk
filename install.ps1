# Requires -RunAsAdministrator

function exists {
    param (
        [string]$command
    )
    if (& { $command } 2>&1 -is [System.Management.Automation.ErrorRecord]) { $false } Else { $true }
}


if (!(exists "choco -V")) {
    # install chocolatey
    Invoke-WebRequest "https://chocolatey.org/install.ps1" -UseBasicParsing | Invoke-Expression    
}

# install python
if (!(exists "python -V")) {
    choco install python -y
}

# install project dependencies
pip install -r requirements.txt

# install vs code
if (!(exists 'code -v')) {
    choco install vscode -y
}
