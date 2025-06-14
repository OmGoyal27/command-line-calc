# How to add the feature to run via powershell

This is required only once.

## Step 1

Configure PowerShell to Allow Script Execution

By default, PowerShell may block script execution. To allow script execution, you need to set the execution policy:

Open PowerShell as an administrator.

Run the following command to set the execution policy:

```bash
Set-ExecutionPolicy RemoteSigned
```

Choose Yes or A to confirm.

## Step 2

Create an Alias in PowerShell Profile

To make the open command always available, add an alias in your PowerShell profile:

Open your PowerShell profile script:

```bash
notepad $PROFILE
```

If the file does not exist, run the following code:

```bash
if (-not (Test-Path -Path $PROFILE)) {
    New-Item -Type File -Path $PROFILE -Force
}
```

Add the following line to create an alias for your script:

```txt
Set-Alias =calc "C:\path\to\your\script\directory\run.ps1"
```

Make sure to replace `"C:\path\to\your\script\directory\run.ps1"` with the actual path to your run.ps1 file.

Save and close the file.

Reload your PowerShell profile to apply the changes:

```bash
. $PROFILE
```

## To remove it, run the following code:

```bash
Remove-Item Alias:=calc -ErrorAction SilentlyContinue
```