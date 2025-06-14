param (
    [string]$equation
)

if (-not $equation) {
    Write-Output "Usage: =calc <equation>"
    Write-Output "Example: =calc 5 + 3"
    exit 1
}

python "main.py" $equation